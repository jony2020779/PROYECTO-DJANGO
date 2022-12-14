from django.views.generic import View
from django.shortcuts import render

class Home(View):
    Titulo="BLISS"
    Integrantes=[]

    def get(self,request,*args, **kwargs):
        contexto={
        }
        return render(request,"index.html",contexto)