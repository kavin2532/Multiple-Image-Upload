from django.shortcuts import render
from .models import  MultipleImageUpLoad

def uploadeMultipleView(request):
    
    if request.method == "POST":
        img = request.FILES.getlist('image')
        
        for image in img:
            MultipleImageUpLoad.objects.create(
                                            images = image)
            
    all_images = MultipleImageUpLoad.objects.all()
    return render(request,'image.html',
                                  {'all_images':all_images})