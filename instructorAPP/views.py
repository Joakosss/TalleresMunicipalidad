from django.shortcuts import render

# Create your views here.

def indexInstructor(request):
    return render(request, 'pages/indexInstructor.html')