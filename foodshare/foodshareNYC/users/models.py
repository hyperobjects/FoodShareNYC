from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import User

from PIL import Image

# Create your models here.



class CustomUser(AbstractUser):
	location = models.CharField(max_length=100)
	class Meta:
		db_table = 'auth_user'


class Profile(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	#location = 
	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

			
