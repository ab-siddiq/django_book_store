from django.contrib import admin
from book.models import BookStoreModel
# Register your models here.
class BookStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id','author','book_name','edition','category','publication_date','last_published')
admin.site.register(BookStoreModel,BookStoreModelAdmin)
