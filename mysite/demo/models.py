from django.db import models

class Article(models.Model):
    title = models.CharField('标题', max_length = 200, unique = True)
    body = models.TextField('正文')
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
