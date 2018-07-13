from django.db import models
#from datetime import datetime

class Video (models.Model):
    class Meta():
        db_table = "Video"
    Video_Url = models.URLField()
    Video_title = models.CharField(max_length=200)
    Video_o = models.TextField(default = " ")
    Video_like = models.IntegerField(default=0)
    #Video_date = models.DateTimeField(default=datetime.now(), blank = True)

    def __str__(self):
        return self.Video_title

class Comment(models.Model):
    class Meta():
        db_table = "Comment"
    comment_text = models.TextField(verbose_name="Комментарий")
    comment_video = models.ForeignKey(Video, True)

    def __str__(self):
        return self.comment_text


