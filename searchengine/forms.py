from django import forms


class SearchForm(forms.Form):
    search_text = forms.CharField(label="", required=False)
    search_text.widget.attrs.update({'autofocus': 'true'})
