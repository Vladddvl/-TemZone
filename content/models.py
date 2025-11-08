from django.db import models
from django.contrib.postgres.fields import JSONField


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=500, blank=True)
    page_content = models.TextField(
        blank=True,
        verbose_name='HTML контент'
    )
    image = models.ImageField(upload_to='topics/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='topics')

    # Гибкие данные для каждой страницы
    page_data = models.JSONField(
        default=dict,
        blank=True,
        verbose_name='Данные страницы',
        help_text='JSON с уникальными данными для этой страницы'
    )
    # Кол-во просмотров
    view_count = models.IntegerField(default=0)
    # Счетчик лайков
    like_count = models.IntegerField(default=0)
    #Дата создания
    created_at = models.DateTimeField(auto_now_add=True)

    # Параметры для фильтрации
    time_required = models.CharField(max_length=20, blank=True)
    initial_investment = models.CharField(max_length=20, blank=True)
    relevance = models.CharField(max_length=20, blank=True)
    complexity = models.CharField(max_length=20, blank=True)
    earning_opportunity = models.CharField(max_length=20, blank=True)
    online = models.CharField(max_length=20, blank=True)
    risks = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title