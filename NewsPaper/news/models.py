from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


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


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    news = 'NW'
    paper = 'PA'
    TYPES_OF_CATEGORIES = [
        (news, 'Новости'),
        (paper, 'Статья'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_type = models.CharField(max_length=2,
                                     choices=TYPES_OF_CATEGORIES,
                                     default=news)
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
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
