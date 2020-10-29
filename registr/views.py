from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


class MyRegistrForms(FormView):
    # Указажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
    # это UserCreationForm - стандартный класс Django унаследованный
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    success_url = "/admin"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = 'registr.html'

    def form_valid(self, form):
        form.save()
        # Функция super( тип [ , объект или тип ] )
        # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
        return super(MyRegistrForms, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegistrForms, self).form_invalid(form)
