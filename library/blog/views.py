from django.shortcuts import render, HttpResponse, redirect
from blog.models import CreateLibrary
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def createLibrary(request):
    if request.method=='POST':
        category = request.POST['category']
        sub_category = request.POST['sub_category']
        personal_library = request.POST['personal_library']
        user = request.user
    
        if len(category) < 2 or len(sub_category)< 2 or len(personal_library)<2:
            messages.error(
                request, 'Please Fill Velid Cradentials .')
            return redirect ('createLibrary')
        else:
            messages.success(
                request, 'Your Library Is Successfully Created .')
        

        library = Create_Library(category=category, sub_category=sub_category, personal_library=personal_library, user=user)
        library.save()
    

    return render(request, 'blog/create_library.html')

def Library(request):
    showLibrary = Create_Library.objects.all()
    context = {'showLibrary': showLibrary}
    return render(request, 'blog/library.html', context)
