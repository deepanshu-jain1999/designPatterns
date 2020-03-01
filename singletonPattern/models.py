from django.db import models
from django.core.cache import cache


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def set_cache(self):
        # self.__class__ = <class 'singletonPattern.models.SiteSettings'>
        # self.__class__.__name__  =    SiteSettings
        # self =   SiteSettings object (1)
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class SiteSettings(SingletonModel):
    email = models.EmailField(default='support@example.com')
    work_email = models.EmailField(blank=True)
    name = models.CharField(max_length=255, default='only_user')
    city = models.CharField(max_length=255, default='jewar')
