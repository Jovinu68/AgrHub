from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        role = request.user.role

        # GET - kila role anaweza kuona
        if request.method == "GET":
            return role in [
                "ADMIN",
                "OFFICER",
                "INSPECTOR",
                "FARMER",
            ]

        # POST - ADMIN na OFFICER
        if request.method == "POST":
            return role in [
                "ADMIN",
                "OFFICER",
            ]

        # PUT/PATCH - ADMIN, OFFICER na INSPECTOR
        if request.method in ["PUT", "PATCH"]:
            return role in [
                "ADMIN",
                "OFFICER",
                "INSPECTOR",
            ]

        # DELETE - ADMIN na OFFICER
        if request.method == "DELETE":
            return role in [
                "ADMIN",
                "OFFICER",
            ]

        return False