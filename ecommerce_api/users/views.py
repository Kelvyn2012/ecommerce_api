from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer, UserReadSerializer


class IsSelfOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.id == request.user.id


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return UserSerializer
        return UserReadSerializer

    def get_permissions(self):
        if self.action in ["list", "destroy"]:
            return [permissions.IsAdminUser()]
        if self.action in ["retrieve", "update", "partial_update"]:
            return [permissions.IsAuthenticated(), IsSelfOrAdmin()]
        return super().get_permissions()
