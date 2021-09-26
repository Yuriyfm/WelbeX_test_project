from django import forms

columns =    (
    ("", ""),
    ("Название", 'Название'),
    ("Количество", "Количество"),
    ("Расстояние", "Расстояние"),
)

filter_methods =    (
    ("", ""),
    ("Больше", "Больше"),
    ("Меньше", "Меньше"),
    ("Равно", "Равно"),
    ("Содержит", "Содержит"),
)

class FilterForm(forms.Form):
    column_name = forms.ChoiceField(choices=columns, required=True)
    filter_method = forms.ChoiceField(choices=filter_methods, required=True)
    value = forms.CharField(max_length=20, required=True)

    column_name.widget.attrs.update({'class': 'form-control', 'required': 'required'})
    filter_method.widget.attrs.update({'class': 'form-control', 'required': 'required'})
    value.widget.attrs.update({'class': 'form-control', 'required': 'required'})
