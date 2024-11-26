from django.shortcuts import render

# Create your views here.

def indexInstructor(request):
    return render(request, 'instructorAPP\templates\pages\indexInstructor.html')