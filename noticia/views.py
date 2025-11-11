from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from .serializer import NoteSerializer, CategorySerializer, LabelSerializer, UserSerializer, ImageSerializer
from .models import Note, Category, Label, Image
# from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.models import User
from rest_framework.views import APIView

# Create your views here.

@api_view(['POST'])
def loginView(request):
    user= get_object_or_404(User, username=request.data.get('username'))
    if not user.check_password(request.data.get('password')):
        return Response({"error": "contraseña invalida"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        token, _ = Token.objects.get_or_create(user=user)
        serializer=UserSerializer(instance=user)
        return Response({'token': token.key,"user": serializer.data},status=status.HTTP_200_OK)

@api_view(['POST'])
def registerView(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            email=serializer.validated_data.get('email', '')
        )
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profileView(request):
    print(request.user.id)
    serializer = UserSerializer(instance=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


class NoteView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    def get_permissions(self):
        if self.action == 'retrieve':  # solo para obtener una nota
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

class categoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class LabelView(viewsets.ModelViewSet):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()

#imagenes EditorJS
class UploadImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image')

        if not image_file:
            return Response({'success': 0, 'error': 'No se envió ninguna imagen'}, status=status.HTTP_400_BAD_REQUEST)

        image = Image.objects.create(autor=request.user, image=image_file)
        serializer = ImageSerializer(image)

        # ⚠️ EditorJS requiere este formato exacto:
        return Response({
            'success': 1,
            'file': {
                'url': request.build_absolute_uri(serializer.data['image'])
            }
        }, status=status.HTTP_201_CREATED)