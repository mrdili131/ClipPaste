from django.shortcuts import render, redirect
from django.views import View
from .models import Data
from .forms import  DataCreationForm
from django.contrib import messages

class IndexView(View):
    def get(self,request):
        form = DataCreationForm()
        return render(request,'index.html',{'form':form})
    def post(self,request):
        form = DataCreationForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            new_data = Data(
                title = title,
                text = text
            )
            new_data.save()
            messages.success(request, "created")
            return redirect('data', id=new_data.id)
        else:
            messages.error(request,"Error data")
        return render(request,'index.html',{'form':form})
    

def dataView(request,id):
    data = Data.objects.get(id=id)
    if data.is_expired:
        data.delete()
    return render(request,'dataview.html',{"data":data})