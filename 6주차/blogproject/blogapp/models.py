from django.db import models

# Create your models here.
class Blog(models.Model): 
    title=models.CharField(max_length=200) #제한O
    writer=models.CharField(max_length=100)
    pub_date=models.DateTimeField() #제한X
    body=models.TextField()
    image=models.ImageField(upload_to="blog/", blank=True,null=True)
    #upload_to는 업로드할 공간을 지정하는 것
    #setting.py에 MEDIA_URL로 지정해둔 media폴더에 blog폴더를 만들어서 저장하겠다는 뜻
    #blank=True,null=True : 사진을 업로드 안해도 된다는것!
    #데이터베이스는 테이블이 비는걸 싫어해,,


    def __str__(self):
        return self.title #글이 제목이 보이도록함
    
    def summary(self):
        return self.body[:100]
