from django import forms

class BlogPostForm(forms.Form):
    titulo = forms.CharField(label="Título", max_length=50)
    texto = forms.CharField(label='Texto', widget=forms.Textarea)
    tags = forms.CharField(label='Tags', max_length=100)