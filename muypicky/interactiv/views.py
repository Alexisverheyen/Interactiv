from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from .models import InteractivLocation
from .forms import InteractivCreateForm, InteractivLocationCreateForm

# def interactiv_listview(request):
#     template_name='interactiv/interactiv_list.html'
#     queryset = InteractivLocation.objects.all()
#     context={
#         "object_list": queryset
#     }
#     return render(request, template_name, context)

def interactiv_createview(request):
    form = InteractivLocationCreateForm(request.POST or None)
    print("etape 1")
    errors = None
    if form.is_valid():
        form.save()
        print("on va vous rediriger")
        return HttpResponseRedirect("/interactiv/")
    else:
        print("le form n'est pas valide")
    print("Etape 2")
    if form.errors:
        errors = form.errors

    template_name = 'interactiv/form.html'
    context ={
        'form':form,
        'errors': errors,
    }
    print("Etape 3")

    return render(request, template_name, context)


class interactivListview(ListView):
    template_name = 'interactiv/interactiv_list.html'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = InteractivLocation.objects.filter(
                Q(categorie__iexact=slug) |
                Q(categorie__icontains=slug)
            )
        else:
            queryset = InteractivLocation.objects.all()

        return queryset


class interactivDetailView(DetailView):
    template_name = 'interactiv/interactiv_detail.html'
    queryset = InteractivLocation.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(interactivDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context
    #
    # def get_object(self,*args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(InteractivLocation, id= rest_id)
    #     return obj
