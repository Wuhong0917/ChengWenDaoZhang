from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse

class TK_Category(models.Model):
	name = models.CharField(max_length = 250)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'TK_Categories'

class TK_Video(models.Model):
	title = models.CharField(max_length = 250)
	category = models.ForeignKey(TK_Category, on_delete = models.CASCADE, default = 1)
	link =  models.URLField(blank=True, null=True)
	video_id = models.CharField(max_length = 250, blank=True, null=True	)
	created_at = models.DateTimeField(default=datetime.datetime.now)

	class Meta:
		ordering = ['-created_at']
		verbose_name_plural = 'TK_Videos'

	def __str__(self):
		return f'{self.title}'

		

class Blog_Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Blog_Categories'

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	excerpt = models.TextField(max_length=300, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Blog_Category, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=datetime.datetime.now)
	updated_at = models.DateTimeField(default=datetime.datetime.now)
	is_published = models.BooleanField(default=True)
	views = models.PositiveIntegerField(default=0)
    
	class Meta:
		ordering = ['-created_at']
    
	def __str__(self):
		return self.title
    
	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'pk': self.pk})
    
	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])