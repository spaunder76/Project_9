from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.tokens import RefreshToken


# class CustomUserCreate(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         reg_serializer = RegisterUserSerializer(data=request.data)
#         if reg_serializer.is_valid():
#             newuser = reg_serializer.save()
#             if newuser:
#                 return Response({
#                     "message": "Account created successfully",
#                     "user": {
#                         "email": newuser.email,
#                         "user_name": newuser.user_name,
#                     }
#                 }, status=status.HTTP_201_CREATED)
#         return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            # Check age and consent rules
            age = reg_serializer.validated_data.get("age")
            consent = reg_serializer.validated_data.get("consent")

            if int(age) < 18 or consent not in ["compactable", "shareable"]:
                return Response(
                    {"error": "Invalid age or consent rules."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            newuser = reg_serializer.save()
            if newuser:
                return Response(
                    {
                        "message": "Account created successfully",
                        "user": {
                            "email": newuser.email,
                            "user_name": newuser.user_name,
                        },
                    },
                    status=status.HTTP_201_CREATED,
                )
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
