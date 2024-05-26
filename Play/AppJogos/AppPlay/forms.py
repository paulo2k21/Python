from django import forms
from .models import Jogos




class JogosForm(forms.ModelForm):
    class Meta: 
        model = Jogos
        fields = "__all__"
        labels = {
            'nome': 'Nome',
            'valor': 'Valor',
            'descricao': 'Descricao',
            'imagem': 'Imagem',
            'categoria': 'Categoria',           
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['valor'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Valor*', 'required': 'required'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descricao*', 'required': 'required'})
        self.fields['imagem'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Imagem*', 'required': 'required'})
        self.fields['categoria'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Categoria*', 'required': 'required'})
    