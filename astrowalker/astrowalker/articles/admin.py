from django.contrib import admin
from .models import Post,Tag

admin.site.register(Post)
admin.site.register(Tag)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id','title','tag_list')
#     list_display_links = ('id','title')

#     def get_queryset(self,reqest):
#         return super().get_queryset(reqest).prefetch_related('tags')

#     def tag_list(self,obj):
#         return u",".join(o.name for o in obj.tags.all())