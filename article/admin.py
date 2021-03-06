from django.contrib import admin
from .models import Article, Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]
    list_display_links = ["title", "created_date"]
    search_fields = ["title"]
    list_filter= ["author"]
    class Meta:
        model = Article
