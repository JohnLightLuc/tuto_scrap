from django.db import models

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=255)
    categorie = models.CharField(max_length=255)
    url_article = models.CharField(max_length=255)
    image_min = models.CharField(max_length=255)
    image_max = models.CharField(max_length=255)
    description = models.TextField()
    contenu = models.TextField()


    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    statut= models.BooleanField(default=True)

#class Detail(models.Model):


