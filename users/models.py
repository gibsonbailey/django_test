from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageOps

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path) 
        
        size = 300
        if(img.width > size and img.height > size):
            dimensions = (size, size)
        else:
            size = min(img.width, img.height)
            dimensions = (size, size)
        img = ImageOps.fit(img, dimensions)
        img.save(self.image.path)

