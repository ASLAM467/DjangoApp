from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,View
from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

import json

class Index(TemplateView):
    def get(self,request):
        return render(request,'index.html')

