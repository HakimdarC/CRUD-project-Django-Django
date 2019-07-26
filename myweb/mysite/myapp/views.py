from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.urls import reverse
from .models import Webpage, Topic
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
                                  UpdateView, DeleteView)

# Create your views here
def index(request):
    return render(request, 'index.html')

class DetailList(DetailView):
    model = Webpage
    template_name = 'myapp/webpage_detail.html'
    context_object_name = 'webdetail'

class Cap(CreateView):
    template_name = 'myapp/cap.html'
    model = Webpage

class ListV(ListView):
    model = Webpage
    context_object_name = 'webname'
    template_name = 'myapp/webpage_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class Base(TemplateView):
    template_name = 'base.html'

class CreateWebpage(CreateView):
    fields =('name','url','topic')
    model = Webpage

    def get_absolute_url(self):
        return reverse("cwp", kwargs={'pk':self.pk})

class Update(UpdateView):
    fields = ('name', 'url')
    model = Webpage

class DeleteV(DeleteView):
    model = Webpage
    success_url = reverse_lazy('myapp:list')
    # context_object_name = 'delview'
#mpclass CoffeePro(TemplateView):
    #model = Topic
   #template_name = 'myapp/coffeepro.html'
    #return render(request,'myapp/coffeepro.html')






