from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,View
from django.views.decorators.csrf import csrf_exempt
from demo_app.demo_class.class_a import A

from django.utils.decorators import method_decorator

import json

class Index(TemplateView):
    def get(self,request):
        return render(request,'index.html')

