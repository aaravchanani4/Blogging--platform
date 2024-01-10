from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
        #You can hence view the object as say 'Vidyasagar profile'
        #You can also run shell and just run user.image to get the imagefield. 
        #user.profile.image.url -> returns the url of the image, duplicate values get hashed

    def save(self, *args, **kwargs):
        #parent class' save method
        super().save(*args, **kwargs)
        
        #              resizing image

        # img = Image.open(self.image.path)
        # if img.height >300 and img.width >300:
        #     output_size = (300,300)
        #     img1 = img.resize(output_size)
        #     img1.save(self.image.path)
