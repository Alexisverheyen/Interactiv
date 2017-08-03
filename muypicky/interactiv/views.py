import random
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.

#fonction based view
#
# def home(request):
#     num = random.randint(0, 100000000)
#     some_list = [num, random.randint(0, 1000000000), random.randint(0, 100000000)]
#     context = {
#         "bool_item" : True,
#         "num" : num,
#         "some_list" : some_list
#     }
#     #return HttpResponse("hello")
#     return render(request, "home.html", context)   # {} = context in terms of dictionnary
#
# def about(request):
#     context ={
#
#     }
#     return render(request, "about.html", context)
#
# def contact(request):
#     context = {
#
#     }
#     return render(request, "contact.html", context)
#
class ContactView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)  #arguments passés dans l'url, qui ici vont se print dans la console
        context = {}
        return render(request, "contact.html", context)

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_contetc_data(self, *args,**kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'
