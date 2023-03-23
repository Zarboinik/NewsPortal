from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += post_rating.get('postRating')

        comment_rating = self.user.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += comment_rating.get('commentRating')

        self.rating = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_type = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, blank=True, through='PostCategory', related_name='posts')
    title = models.CharField(max_length=255)
    text = models.TextField(default='Здесь могла быть статья')
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        s = str(self.text)
        if len(s) <= 124:
            return s
        else:
            return "%s..." % (s[:124])

    def __str__(self):
        return f'{self.title.title()}: {self.author}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='Комментарий')
    time_create = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.user.title()}: {self.post}'
