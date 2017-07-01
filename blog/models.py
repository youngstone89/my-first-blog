from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)
	
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)


	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey('blog.Post',related_name='comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)


	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text


# class IPAddress(models.Model):
# 	ipaddress=models.TextField()
# 	user_group=models.TextField()
# 	user_name=models.TextField()
# 	user_position=model.TextField()
# 	ip_status=models.CharField(max_length=200)
# 	project=models.TextField()
# 	date_of_start=models.DateTimeField(black=True,null=True)


# 	def __str__(self):
# 		return self.ip_status