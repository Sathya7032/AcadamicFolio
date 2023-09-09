from django.contrib import admin
from .models import Contact, Category, Post


#for cnfiguration category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','discription','url', 'add_date',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id','title','image_tag','content',)
    search_fields = ('title',)
    list_filter = ('cate',)

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','assets/js/scipt.js',)


admin.site.register(Contact)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

