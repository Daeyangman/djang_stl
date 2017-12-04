from django.shortcuts import render,redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm , UploadForm,UploadForm2
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import StlFile
import numpy as np
from stl import mesh



# class IndexView(TemplateView):
#     template_name = 'threedbang/index.html'
class BootTemplateView(TemplateView):
    template_name = 'index-smooth-scroll.html'
class AboutUsTemplateView(TemplateView):
    template_name = 'aboutus.html'
class RegualtionTemplateView1(TemplateView):
    template_name = 'regulation_1.html'

class RegualtionTemplateView2(TemplateView):
    template_name = 'regulation_2.html'


class RegualtionTemplateView3(TemplateView):
    template_name = 'regulation_3.html'

class ServiceTemplateView(TemplateView):
    template_name = 'service.html'



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
        # from IPython import embed; embed()
        if form.is_valid():
            stlfile = form.save(commit=False)
            # stl_file = form.save(file=request.FILES['file'], owner=request.user)
            # stl_file.owner = request.user
            stlfile.owner = request.user
            stlfile.meshMake()
            stlfile.filenameMake()
            stlfile.save()
        return redirect('mypagelist')
    form = UploadForm()
    return render(request, 'mypage.html', {'form': form})

def estimate(request, filekey):
    stlfile = StlFile.objects.get(pk = filekey)
    return render(request , 'estimate.html' , {'stlfile' : stlfile})


class MypageListView(ListView):
    context_object_name = 'user_stlfile_list'
    paginate_by = 3
    def get_queryset(self):
        user = self.request.user
        return user.stlfile_set.all().order_by('-pub_date')


#
# @login_required()
# def uploadaddress(request):
#     if request.method == 'POST':
#         form = UploadForm2(request.POST)
#         # from IPython import embed; embed()
#         if form.is_valid():
#             custom_address = form.save(commit=False)
#             custom_address.owner = request.user
#             custom_address.save()
#         return redirect('mypagelist')
#     form = UploadForm2()
#     return render(request, 'customaddress.html', {'form': form})