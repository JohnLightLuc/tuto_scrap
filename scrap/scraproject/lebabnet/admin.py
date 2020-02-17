from django.contrib import admin
from . import models
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'categorie',
        'image_min',
        'image_max',
        'description',
        'contenu',
        'date_add',
        'date_upd',
        'statut',
    )
    



def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Article, ArticleAdmin)
