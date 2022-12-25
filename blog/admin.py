from django.contrib import admin

from blog.models import Post, Category, Tag, Comment

# 데이터모델을 admin에 등록함.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'tag_list', 'title', 'description', 'image', 'create_dt', 'update_dt', 'like')

    # tags를 모두 가져와서 ,로 구분하여 리스트로 리턴
    def tag_list(self, obj):  # obj : post model 객체
        return ','.join([t.name for t in obj.tags.all()])

    # post record를 가져올 때 관련된 tags 정보도 모두 가져오라는 의미
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    prepolulated_fields = {'slug': ('name', )}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepolulated_fields = {'slug': ('name', )}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'short_content', 'create_dt', 'update_dt')
