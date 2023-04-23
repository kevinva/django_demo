from django.db import models

class Article(models.Model):

    title = models.CharField('标题', max_length = 200, unique = True)
    body = models.TextField(default = '')
    pub_date = models.DateTimeField('发布日期', auto_now_add = True)

    def __str__(self):
        return self.title
