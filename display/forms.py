from django import forms

from .models import BlogPost
from .models import BlogLogin
from .models import BlogRegister


class BlogPostForm(forms.ModelForm):  # Définition d'une nouvelle classe BlogPostForm qui hérite de forms.ModelForm.
    class Meta:  # Définition de la classe Meta à l'intérieur de BlogPostForm.
        model = BlogPost  # Spécifie que ce formulaire est basé sur le modèle BlogPost.
        fields = ['title', 'content', 'author', 'pub_date']  # Liste des champs du modèle qui seront inclus dans le formulaire.
        widgets = {  # Widgets permet de personnaliser l'apparence des champs de formulaire.
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # Utilise un TextInput pour le champ 'title' avec la classe CSS 'form-control'.
            'content': forms.Textarea(attrs={'class': 'form-control'}),  # Utilise un Textarea pour le champ 'content' avec la classe CSS 'form-control'.
            'author': forms.TextInput(attrs={'class': 'form-control'}),  # Utilise un TextInput pour le champ 'author' avec la classe CSS 'form-control'.
            'pub_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),  # Utilise un DateTimeInput pour le champ 'pub_date' avec la classe CSS 'form-control'.
        }


class BlogLoginForm(forms.ModelForm):
    class Meta:
        model = BlogLogin
        fields = ['email', 'password']
        widgets = \
            {
                'email': forms.TextInput(attrs={'class': 'form-control', 'aria-required': 'true', 'placeholder': 'Enter user Email here'}),
                'password': forms.PasswordInput(attrs={'class': 'form-control', 'aria-required': 'true', 'placeholder': 'Enter password here'}),
            }


class BlogRegisterForm(forms.ModelForm):
    class Meta:
        model = BlogRegister
        fields = ['username', 'email', 'password', 'password2']
        widgets = \
            {
                'username': forms.TextInput(attrs={'class': 'form-control'}),
            }
