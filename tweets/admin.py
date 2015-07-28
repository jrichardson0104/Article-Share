from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['id', '__str__', 'get_category','posted']

	class Meta:
		model = Article
	def get_category(self, obj):
		return "\n".join([share.category for share in obj.category.all()])


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', '__str__']
	


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)