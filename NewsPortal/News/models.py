from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    article = 'a'
    news = 'n'

    POSTS = [
        (article, "Статья"),
        (news, "Новость")
    ]

    time = models.DateTimeField(auto_now_add=True)
    news_text = models.TextField()
    news_rate = models.IntegerField(default=1)
    news_title = models.CharField(max_length=255)
    p_chose = models.CharField(max_length=1, choices=POSTS, default=article)
    rate = models.IntegerField(default=0)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through = 'PostCategory')

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()

    def preview(self):
        size = 124 if len(self.news_text) > 124 else len(self.news_text)
        return self.news_text[:size] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=0)

    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
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
