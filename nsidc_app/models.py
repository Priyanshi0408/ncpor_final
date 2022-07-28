from tkinter import CASCADE
from django.db import models
# Create your models here.
class about(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class research(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.title
class informationResearch(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.title
class researchScientist(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.title
class researchGrant(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.title
class scientificPublication(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.title
class scientificExpedition(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class research_example_down_scientists(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class research_example_down_resgran(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class research_example_down_sp(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.title

# class research_drop(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     slug = models.ForeignKey(research,on_delete=models.CASCADE)
#     slug_drop = models.CharField(max_length=300,null=True)

#     def __str__(self):
#         return self.title
#     (drop-dowm-->dropdowm through cms / made by priyanshi)

###########tendor page ###############

