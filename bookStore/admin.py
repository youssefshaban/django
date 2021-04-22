from django.contrib import admin

from .form import BookForm, CatForm
from .models import bookStore, Isbn, Category

class StoreAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ("title", "author")
    list_filter = ("category",)
    search_fields = ("title",)
    # readonly_fields = ("author",)

class StoreInline(admin.StackedInline):
    model = bookStore
    max_num = 3
    extra = 1

class IsbnAdmin(admin.ModelAdmin):
    inlines = [StoreInline]

class CategoryAdmin (admin.ModelAdmin):
    form = CatForm

admin.site.register(bookStore,StoreAdmin)
admin.site.register(Isbn, IsbnAdmin)
admin.site.register(Category, CategoryAdmin)
