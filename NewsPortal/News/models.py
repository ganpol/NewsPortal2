from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)


class Post(models.Model):





    time = models.DateTimeField(auto_now_add=True)
    news_text = models.CharField()
    news_rate = models.IntegerField(default=1)
    news_title = models.CharField()
    p_chose = models.CharField(max_length = 1, choices = POSTS, default = article)
    rate = models.IntegerField(default=0)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, through='PostCategory')

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=0)

    posts = models.ForeignKey(Post, through='PostCategory')
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()

    # position = models.CharField(max_length=255)
    # labor_contract = models.IntegerField()

    # time_out = models.DateTimeField(null=True)
    # cost = models.FloatField(default=0.0)
    # take_away = models.BooleanField(default=False)
    # complete = models.BooleanField(default=False)

    # price = models.FloatField(default=0.0)
    # composition = models.TextField(default="Состав не указан")

    # amount = models.IntegerField(default=1)
