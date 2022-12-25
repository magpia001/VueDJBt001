from django.db import models



class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    title = models.CharField('TITLE', max_length=50)
    # description = models.CharField('별칭', max_length=100, blank=True, help_text='설명') # null=True를 하지 않으면 '' 값이 들어감
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.') 
    image = models.ImageField('IMAGE', upload_to='blog/%Y/%m/', blank=True, null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)
    like = models.PositiveSmallIntegerField('LIKE', default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/post/{self.pk}/'


# N테이블에 field를 정의함.
# post와의 관계 N:1  / post가 N이므로 post에 category ForeignKey 정의
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'        

# post와의 관계 N:N  / post와 tag는 N:N 이기 때문에 아무곳에나 해도됨, ManyToManyField() 사용
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}'

# post와의 관계 1:N / Comment가 N이기 때문에 Comment에 post 필드를 ForeginKey로 정의함
class Comment(models.Model):
    # post = models.ForeignKey('크래스가 아래쪽에 정의된 경우', on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, blank=True, null=True)
    # post = models.ForeignKey(클래스가 윗쪽에 정의된 경우, on_delete=models.CASCADE, blank=True, null=True)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)

    @property  # method를 field로 정의한 pytho 문법
    def short_content(self):
        # 댓글에서 10개의 글자만 리턴함
        return self.content[:10]

    def __str__(self):
        return self.short_content