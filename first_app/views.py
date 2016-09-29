from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Apartment
from .forms import AptForm

# Create your views here.
def index(request):
  apartments = Apartment.objects.all()
  form = AptForm()
  return render(request, 'index.html', {
    'apartments': apartments,
    'form': form
  })

def detail(request, apt_id):
  apartment = Apartment.objects.get(id=apt_id)
  return render(request, 'detail.html', {'apartment': apartment})

def post_apt(request):
  form = AptForm(request.POST, request.FILES)
  if form.is_valid():
    form.save(commit = True)
  return HttpResponseRedirect('/')
