from django.forms import ModelForm
from .models import Produit
from django import forms
from .models import Commande
from .models import Fournisseur
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
 first_name = forms.CharField(label='Prénom')
 last_name = forms.CharField(label='Nom')
 email = forms.EmailField(label='Adresse e-mail')
 
class Meta(UserCreationForm.Meta):
 model = User
 fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')
class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'adresse', 'telephone', 'email']

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['libelle', 'description', 'prix', 'type', 'img', 'fournisseur', 'categorie']

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['dateCde', 'totalCde', 'produits']