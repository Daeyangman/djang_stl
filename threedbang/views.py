from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm , UploadForm
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

class TestTemplateView(TemplateView):
    template_name = 'test2.html'


class ServiceTemplateView(TemplateView):
    template_name = 'service.html'
# class MypageTemplateView(TemplateView):
#     template_name = 'mypage.html'
#
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
            stlfile.save()
        return redirect('mypagelist')
    form = UploadForm()
    return render(request, 'mypage.html', {'form': form})

class MypageListView(ListView):
    context_object_name = 'user_stlfile_list'
    paginate_by = 2
    def get_queryset(self):
        user = self.request.user
        return user.stlfile_set.all().order_by('-pub_date')

