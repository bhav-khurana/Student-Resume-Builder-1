from django.shortcuts import render

# Create your views here.

def resume_form(request):
    return render(request, 'resumeGenerator/input.html')
