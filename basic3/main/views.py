from django.shortcuts import render,HttpResponse,redirect
from main.models import ProductModel
from .models import Post
from .forms import product_create_Form
# Create your views here.
def greet(request):
    return render(request,'index.html')
def product(request,id):
    p=ProductModel.objects.get(id=id)
    return HttpResponse(p.name)
def table(request):
    p=ProductModel.objects.all()
    context={
        'p':p
    }
    return render(request,'table.html',context)
def create(request):
    if request.method=='POST':
        form = product_create_Form(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            price=form.cleaned_data['price']
            description=form.cleaned_data['description']
            product=ProductModel(
                name=name,
                price=price,
                description=description
            )
            product.save()
            return redirect('hai/')
        else:
            return render(request,'create_product.html',{'form':form})


    
    return render(request,'create_product.html')

def hai(request):
    return render(request,'front.html')



