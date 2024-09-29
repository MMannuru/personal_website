from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')  # New view for about page

def research(request):
    return render(request, 'portfolio/research.html')  # Render the research page

def projects(request):
    return render(request, 'portfolio/projects.html')

