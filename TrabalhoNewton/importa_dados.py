import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()

from livros.models import Autor, Livro

# Importa autores
with open('autores.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        Autor.objects.get_or_create(nome=row['nome'], nascimento=row['nascimento'])

# Importa livros
with open('livros.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        autor = Autor.objects.get(nome=row['autor_nome'])
        Livro.objects.get_or_create(titulo=row['titulo'], ano=row['ano'], autor=autor)

print("Importação concluída!")