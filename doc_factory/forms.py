from django import forms

class AddEntryForm(forms.Form):
    file = forms.FileField(max_length=100, widget=forms.ClearableFileInput(attrs={'multiple':True}))
