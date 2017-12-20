from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import StlFile

import numpy as np
from stl import mesh
#
# @login_required()
# def uploadaddress(request):
#     if request.method == 'POST':
#         form = UploadForm2(request.POST)
#         # from IPython import embed; embed()
#         if form.is_valid():
#             custom = form.save(commit=False)
#             custom.owner = request.user
#             custom.save()
#         return redirect('address')
#     form = UploadForm2()
#     return render(request, 'customaddess.html', {'form': form})
#
#
