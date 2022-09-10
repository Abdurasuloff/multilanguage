from django.shortcuts import render
from .models import New
from django.views.generic import CreateView
from django.utils.translation import gettext as _

# Create your views here.


def index(request):
      text = _("So'ngi yangiliklar")
      news = New.objects.all().order_by('-id')
      return render(request, 'index.html', {'news':news, 'text':text})



class CreateNew(CreateView):
      model = New
      fields = "__all__"  
      template_name = 'new.html'
      
