from django.shortcuts import render

# Create your views here.
def base_layout(request):
    return render(request,'app/base_layout.html')

def about(request):
    return render(request,'app/about.html')
