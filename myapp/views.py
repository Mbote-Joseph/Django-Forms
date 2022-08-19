from django.shortcuts import render
from .models import Details
from .forms import DetailsForm
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

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
        "detailform":DetailsForm(),
        
    }
    return render(request, 'index.html', context)


class DetailsListView(ListView):
    model = Details
    template_name = 'detail_list.html'
    context_object_name = 'details'
    ordering = ['-created_at']
    paginate_by = 5
    queryset = Details.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Django Forms'
        return context


class DetailsUpdateView(UpdateView):
    model = Details
    template_name = 'detail_update.html'
    form_class = DetailsForm
    context_object_name = 'detail'
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Django Forms'
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            form = DetailsForm()
        return super().form_valid(form)

    
        
        

