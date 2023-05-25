#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    
    
"""
medias = []

for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input(f'Digite a nota {j+1} do aluno {i+1}: '))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)

alunos_aprovados = sum(1 for media in medias if media > 7)

print(f'{alunos_aprovados} aluno(s) com médias maiores que 7.')

"""
