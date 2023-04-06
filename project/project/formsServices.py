from django import forms


class NewServices(forms.Form):
    name = forms.CharField(label="Название курса:", max_length=250)
    duration = forms.IntegerField(label='Длительность (в мин.):')
    price = forms.IntegerField(label='Стоимость (в руб.):')
    description = forms.CharField(label="Описание:", required=False, max_length=250)


class UpdateServices(forms.Form):
    duration = forms.IntegerField(label='Длительность (в мин.):')
    price = forms.IntegerField(label='Стоимость (в руб.):')
    description = forms.CharField(label="Описание:", required=False, max_length=250)


class SearchServices(forms.Form):
    name = forms.CharField(label="Название курса:", max_length=250)