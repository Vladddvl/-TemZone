from django.shortcuts import render
from django.db.models import Q
from .models import Topic
from django.shortcuts import render

def index(request):
    return render(request, 'temzone/index.html')

def instruments(request):
    return render(request, 'temzone/instruments.html')

def news(request):
    return render(request, 'temzone/news.html')

# Поиск
def search(request):
    query = request.GET.get('query', '')  # получаем запрос из параметра 'query'
    results = Topic.objects.all()  # начальный queryset

    if query:
        # Ищем по заголовку, содержанию и категории
        results = results.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__icontains=query)
        )

    context = {
        'results': results,
        'query': query,
        'topics': results  # если используете то же имя в шаблоне
    }

    return render(request, 'temzone/search.html', context)
