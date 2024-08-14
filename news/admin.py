from django.contrib import admin
from .models import Category, News,  Contact #Logo,


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','category','status','created_at')
    prepopulated_fields = {'slug':['title']}
    list_filter = ('category','status')
    search_fields = ('title','created_at')

# class CategoryAdmin(admin.ModelAdmin):
#     list_filter = ('M')


admin.site.register(Category)
admin.site.register(News,NewsAdmin)
# admin.site.register(Logo)
admin.site.register(Contact)