from __future__ import unicode_literals
from django import forms
from django.db import models

class user(models.Model):
	#auto_increment_id = models.AutoField(primary_key=True)
	full_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)
	Password = models.CharField(max_length=100)
	
	
'''class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    first_choice = models.CharField(max_length=200)
    second_choice = models.CharField(max_length=200)
    third_choice = models.CharField(max_length=200)
    
class Results(models.Model):
	
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	user = models.ForeignKey(Applicants, on_delete=models.CASCADE)
	choice = models.ForeignKey(Choice, on_delete=models.CASCADE'''
