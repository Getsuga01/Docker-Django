from rest_framework import serializers
from .models import Livro, Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    autor_id = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all(), source='autor', write_only=True
    )

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'ano', 'autor', 'autor_id']