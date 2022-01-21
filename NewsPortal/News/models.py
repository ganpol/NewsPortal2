from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    labor_contract = models.IntegerField()
    user = models.OneToOneField()

class Users(models.Model)
    pass

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    # price = models.FloatField(default=0.0)
    # composition = models.TextField(default="Состав не указан")


class Post(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    news_text = models.CharField()
    news_rate = models.IntegerField(default=1)
    news_title = models.CharField()
    p_chose = models.

    # time_out = models.DateTimeField(null=True)
    # cost = models.FloatField(default=0.0)
    # take_away = models.BooleanField(default=False)
    # complete = models.BooleanField(default=False)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    posts = models.ForeignKey(Category, through='PostCategory')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

class Comment(models.Model)
    pass