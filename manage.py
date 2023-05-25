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
questions = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Já trabalhou com a vítima?",
    "Devia para a vítima?"
]

answers = []

for question in questions:
    response = input(question + " (sim ou não) ")
    while response.lower() != "sim" and response.lower() != "não":
        response = input("Por favor, responda com sim ou não: ")
    answers.append(response.lower() == "sim")

def classify_person(answers):
    num_positive = sum(answers)
    if num_positive == 2:
        return "Suspeito"
    elif 3 <= num_positive <= 4:
        return "Cúmplice"
    elif num_positive == 5:
        return "Assassino"
    else:
        return "Inocente"

result = classify_person(answers)
print("Esta pessoa é classificada como:", result)


"""
