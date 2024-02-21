from django.urls import path
from galeria.views import index, imagem, form, casa_do_leo

urlpatterns = [
    path('',index, name='index'),
    path('imagem/',imagem, name='imagem'),
    path('form/',form, name='form'),
    path('casa_do_leo/',casa_do_leo, name='casa_do_leo'),
]