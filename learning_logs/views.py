from django.shortcuts import render


# Create your views here.
def index(request):
    """Главная страница приложения Learning Log."""
    return render(request, 'learning_logs/index.html')
