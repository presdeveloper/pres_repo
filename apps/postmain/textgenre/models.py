from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.

class TextGenre(models.Model):
	name = models.CharField(max_length=16)
	creation = models.DateField(default=datetime.now)


class TextGenreFollowed(models.Model):
	textgenre = models.ForeignKey(TextGenre, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	creation = models.DateField(default=datetime.now)


