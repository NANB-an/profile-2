from django.shortcuts import render

def profile_view(request):
    return render(request, 'myprofileApp/home.html')
