from django.db import models

# Create your models here.

class tododata(models.Model):
    """
    todoの内容
    todo: 内容
    complate_flag: 済んだか否か
    id: todoの管理番号(主キー)
    """
    id = models.IntegerField(primary_key=True)
    todo = models.CharField(max_length=50)
    is_finished = models.BooleanField(default=False)

