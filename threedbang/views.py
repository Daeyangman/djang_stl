from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm , UploadForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import StlFile
import numpy as np
from stl import mesh

# Create your views here.
# class IndexView(TemplateView):
#     template_name = 'threedbang/index.html'
class BootTemplateView(TemplateView):
    template_name = 'index-smooth-scroll.html'

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'
@login_required()
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST , request.FILES)
        from IPython import embed; embed()
        if form.is_valid():
            # stl_file = form.save(commit=False)
            stl_file = StlFile(file=request.FILES['file'], owner=request.user)
            # stl_file.owner = request.user
            stl_file.meshMake()
            stl_file.save()
        return redirect('threedbang:index')
    form = UploadForm()
    return render(request, 'main/index.html', {'form': form})