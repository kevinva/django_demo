from django.db import models

class Status(models.TextChoices):
    UNSTARTED = 'u', '未开始'
    ONGOING = 'o', '进行中'
    FINISHED = 'f', '已完成'

class Task(models.Model):
    name = models.CharField(verbose_name = 'Task name', max_length = 65, unique = True)
    status = models.CharField(verbose_name = 'Task status', max_length = 1, choices = Status.choices, default = Status.UNSTARTED)

    def __str__(self):
        return self.name