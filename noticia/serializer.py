from rest_framework import serializers
from .models import Note, Category, Label
from django.contrib.auth.models import User
from .models import Image

class NoteSerializer(serializers.ModelSerializer):
    autor_info = serializers.SerializerMethodField()
    autor = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['autor']

    def get_autor_info(self, obj):
        return {
            "id": obj.autor.id,
            "username": obj.autor.username,
            "email": obj.autor.email
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'autor', 'image', 'created_at']
        read_only_fields = ['autor', 'created_at']