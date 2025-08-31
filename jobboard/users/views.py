from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import RegisterSerializer, UserSerializer
from .models import User


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class MeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# --- NEW: Minimal Reset Password endpoint (placeholder) ---
@api_view(["POST"])
@permission_classes([AllowAny])
def reset_password(request):
    """
    Placeholder reset password endpoint.
    For now, just echoes back the provided email.
    Later you can integrate Django's password reset flow.
    """
    email = request.data.get("email")
    if not email:
        return Response({"error": "Email is required."}, status=400)

    return Response(
        {"message": f"If {email} exists, a reset link will be sent."}
    )
