from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
# Create your models here.

class InteractivLocation(models.Model):
    name        = models.CharField(max_length=120)
    location    = models.CharField(max_length=120, null=True, blank=True)
    categorie   = models.CharField(max_length=120, null=True, blank=False)
    timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug        = models.SlugField(null=True, blank=True)                             #donner un identifiant clair qui se retrouvera dans l'url

    def __str__(self):
        return self.name  #permet d'avoir le nom qui s'affiche dans le DB et non pas InteractivLocation Object

    @property
    def title(self):
        return self.name

def il_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()

#
# def il_post_save_receiver(sender, instance, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)


pre_save.connect(il_pre_save_receiver, sender=InteractivLocation)

# post_save.connect(il_post_save_receiver, sender=InteractivLocation)