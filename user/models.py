from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    SEX = (
        ('男性', '女性'),
        ('女性', '女性'),
    )
    nickname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=16, unique=True)
    gendle = models.CharField(max_length=8, choices=SEX)

    birth_year = models.IntegerField(verbose_name='出生年', default=1976)
    birth_month = models.IntegerField(verbose_name='出生月', default=1)
    birth_day = models.IntegerField(verbose_name='出生日', default=1)

    avatar = models.CharField(max_length=256, verbose_name='头像')
    location = models.CharField(max_length=32, verbose_name='常居地')

    @property
    def age(self):
        today = datetime.date.today()
        birthday = datetime.date(self.birth_year, self.birth_month,self.birth_day)
        return  (today - birthday).days//365



    def to_dict(self):
        return {
            'nickname': self.nickname,
            'phonenum': self.phonenum,
            'age': self.age,
            'sex': self.gendle,
            'avatar': self.avatar,
            'location': self.location,
        }


class Profile(models.Model):
    SEX = (
        ('男性', '女性'),
        ('女性', '女性'),
    )
    dating_sex = models.CharField(max_length=8, choices=SEX, verbose_name='匹配的性别')
    location = models.CharField(max_length=32, verbose_name='目标地点')

    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')

    min_dating_age = models.IntegerField(default=18, verbose_name='最小匹配年龄')
    max_dating_age = models.IntegerField(default=50,verbose_name='最大匹配年龄')

    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')
    only_matche = models.BooleanField(default=True,verbose_name='不让匹配的人看我相册')
    auto_play = models.BooleanField(default=True,verbose_name='是否自动播放视频')