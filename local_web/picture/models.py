from django.db import models
import hashlib
from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class FileInfo(models.Model):

    """上传的文件信息"""
    id=models.AutoField(primary_key=True,verbose_name="序号")
    filename = models.CharField('文件名', max_length=128)
    md5_name = models.CharField('加密名称', max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags=models.CharField(verbose_name="标识",max_length=255,null=True,blank=True)
    upload_date = models.DateTimeField('上传时间', default=timezone.now)
    removed = models.IntegerField('已删除', default=0)

    # @classmethod
    # def create(cls, filename, user):
    #     file = cls(filename=filename, user=user)
    #     file.md5_name = cls._generate_md5_name(filename)
    #     return file
    #
    # @staticmethod
    # def _generate_md5_name(filename):
    #     """生成md5加密后的名称，加入当前时间字符串，避免文件名重复带来的问题"""
    #     md5_str = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S") + filename
    #     return hashlib.md5(md5_str.encode('utf-8')).hexdigest() + '.' + filename.split('.')[-1]