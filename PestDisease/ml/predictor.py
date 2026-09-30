from transformers import AutoModelForImageClassification
from PIL import Image
import torch
from torchvision import transforms


MODEL_NAME = "mesabo/agri-plant-disease-resnet50"


# Load model
model = AutoModelForImageClassification.from_pretrained(
    MODEL_NAME
)

model.eval()


# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


def predict_disease(image_path):

    # Open image
    image = Image.open(image_path).convert("RGB")

    # Prepare image
    image_tensor = transform(image)

    # Add batch dimension
    image_tensor = image_tensor.unsqueeze(0)

    # Prediction
    with torch.no_grad():

        outputs = model(
            pixel_values=image_tensor
        )

        probabilities = torch.nn.functional.softmax(
            outputs.logits,
            dim=-1
        )

        predicted_index = probabilities.argmax(
            dim=-1
        ).item()

        confidence = probabilities[
            0
        ][predicted_index].item()

    # Get disease name
    disease_name = model.config.id2label[
        predicted_index
    ]

    return {
        "disease": disease_name,
        "confidence": round(
            confidence * 100,
            2
        )
    }