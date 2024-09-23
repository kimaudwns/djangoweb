from django.db import models

# Create your models here.
class Notice(models.Model):
    #id = models.AutoField(primary_key=True)
    #제목
    title = models.CharField(max_length=200)
    #내용
    contents = models.TextField()
    #조회수
    views = models.IntegerField()
    #생성일
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Program(models.Model):
    #id = models.AutoField(primary_key=True)
    # 이름
    title = models.CharField(max_length=200)
    # 설명
    text = models.TextField()
    # 위치 
    subtext = models.TextField()
    #작품 공개 날짜 
    schedule =  models.TextField()
    # 이미지
    img = models.ImageField(blank=True, upload_to="img")

    def __str__(self):
        return self.title 