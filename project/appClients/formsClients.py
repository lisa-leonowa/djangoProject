from django import forms


class NewClients(forms.Form):
    first_name = forms.CharField(label="Имя:", min_length=5, max_length=70)
    last_name = forms.CharField(label="Фамилия:", min_length=5, max_length=70)
    full_name = forms.CharField(label="Отчество:", min_length=5, max_length=70)
    gender = forms.CharField(label="Пол:", max_length=3)
    phone = forms.CharField(label="Номер телефона:", max_length=12, min_length=10)
    remark = forms.CharField(label="Примечание:", required=False, max_length=250)


    def form_values(self):  # метод возвращающий поля формы
        return ['first_name', 'last_name', 'full_name', 'gender', 'phone', 'remark']


class UpdateClients(forms.Form):
    phone = forms.CharField(label="Номер телефона:", max_length=12, min_length=10)
    remark = forms.CharField(label="Примечание:", required=False, max_length=250)
    def form_values(self):  # метод возвращающий поля формы
        return ['phone', 'remark']


class SearchClients(forms.Form):
    first_name = forms.CharField(label="Имя:", min_length=5, max_length=70)
    last_name = forms.CharField(label="Фамилия:", min_length=5, max_length=70)
    full_name = forms.CharField(label="Отчество:", min_length=5, max_length=70)
    def form_values(self):  # метод возвращающий поля формы
        return ['first_name', 'last_name', 'full_name']

