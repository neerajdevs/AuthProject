from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255 ,blank=True , null=True)
    bio = models.TextField(blank=True)
    age = models.IntegerField(blank=True , null=True)
    role = models.CharField(choices=[('Python Developer' , 'Python developer') , ('AI/ML Engineer' , 'AI/ML Engineer'),
                                     ('MERN Stack' , 'MERN Stack'), ('Project Manager' , 'Project Manager'), ('Perparaing','Perparaing')] ,default='Perparaing' )
    
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    linkedin = models.URLField(max_length=200 , blank= True)
    instagram = models.URLField(max_length=200, blank= True)
    protfolio = models.URLField(max_length=200, blank= True)
    leetcode = models.URLField(max_length=200 , blank= True)
    gfg = models.URLField(max_length=200 , blank= True)
    Project_1 = models.URLField(max_length=200 , blank= True)
    Project_2 = models.URLField(max_length=200 , blank= True)
    Project_3 = models.URLField(max_length=200 , blank= True)
    

    def __str__(self):
        return self.user.username