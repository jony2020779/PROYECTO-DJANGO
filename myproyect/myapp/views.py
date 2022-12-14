from django.shortcuts import render , HttpResponse
from django.views.generic import View

# Create your views here.
class Blog(View):
    Titulo="Pasaje Turistico"
    Representante=[]
    Cargos=[]

    def get(self,request,*args, **kwargs):
        contex={

        }
        return render(request,"blog.html",contex)
