from django.shortcuts import render
from .models import Details
from .forms import DetailsForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            form = DetailsForm()
    else:
        form = DetailsForm()
    

    context={
        'title':'Django Forms',
        'form': form,
        "detailform":DetailsForm()
    }
    return render(request, 'index.html', context)