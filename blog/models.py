from django.db import models
from django.utils import timezone



class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)


	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title
# Create your models here.



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