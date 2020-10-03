from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        """Django模型实例实际上并不将字段公开为字段类：一旦从数据库加载，它们就只是相关数据类型的实例。
        因此，CharField和TextField都可以作为简单字符串访问。"""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."
