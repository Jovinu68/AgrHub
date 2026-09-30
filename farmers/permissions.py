from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        role = request.user.role

        # GET - kila role inaweza kuona
        if request.method == "GET":
            return role in [
                "ADMIN",
                "OFFICER",
                "INSPECTOR",
                "FARMER"
            ]

        # POST - Admin na Officer
        if request.method == "POST":
            return role in [
                "ADMIN",
                "OFFICER"
            ]

        # PUT/PATCH - Admin, Officer, Inspector, Farmer
        if request.method in ["PUT", "PATCH"]:
            return role in [
                "ADMIN",
                "OFFICER",
                "INSPECTOR",
                "FARMER"
            ]

        # DELETE - Admin na Officer
        if request.method == "DELETE":
            return role in [
                "ADMIN",
                "OFFICER"
            ]

        return False

    def has_object_permission(self, request, view, obj):

        role = request.user.role

        # Admin na Officer wanaweza kuona/kufanyia kazi
        # farmer yoyote
        if role in [
            "ADMIN",
            "OFFICER"
        ]:
            return True

        # Inspector anaweza kuona/kubadilisha,
        # lakini sio delete
        if role == "INSPECTOR":
            return request.method in [
                "GET",
                "PUT",
                "PATCH"
            ]

        # Farmer anaweza kuona/kubadilisha
        # profile yake mwenyewe
        if role == "FARMER":
            return obj.user == request.user

        return False