from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageForm

# Create your views here.

def image_list(request):
    images = Image.objects.all()
    return render(request, 'multimedia/image_list.html', {'images': images})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'multimedia/upload_image.html', {'form': form})


def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'multimedia/image_detail.html', {'image': image})


def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('image_list')
    return render(request, 'multimedia/delete_image.html', {'image': image})

