import os

from django.db import models


def image_filename(instance, filename):
    """ Make S3 image filenames
    """
    return 'images/%s/%s' % (instance.id, os.path.basename(filename))


class Sector(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True, help_text='Full name of the sector')
    slug = models.SlugField(max_length=50, null=False, blank=False, unique=True)
    vision = models.TextField(null=False, blank=True, default='', help_text='Full vision (HTML allowed)')
    goals = models.TextField(null=False, blank=True, default='', help_text='List of goals, one per line.')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def organisations(self):
        org_ids = set(p.organisation.id for p in self.projects.select_related('organisation').all())
        return Organisation.objects.filter(id__in=org_ids).order_by('name').all()

    @property
    def image_filename(self):
        return 'img/sectors/%s.png' % self.slug


class Organisation(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    tel = models.CharField(max_length=100, null=False, blank=True)
    email = models.EmailField(null=False, blank=True, help_text='Contact email address')
    website = models.URLField(null=False, blank=True, help_text='Website')
    description = models.TextField(null=False, blank=True, default='')
    logo = models.ImageField(upload_to=image_filename, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_logo_path(self):
        return self.logo.storage.url(self.logo.name)


class Project(models.Model):
    organisation = models.ForeignKey(Organisation, null=False, on_delete=models.CASCADE, related_name='projects')
    sectors = models.ManyToManyField(Sector, related_name='projects')
    name = models.CharField(max_length=100, null=False, blank=False)
    website = models.URLField(null=False, blank=True, help_text='Website')
    description = models.TextField(null=False, blank=True, default='')
    email = models.EmailField(null=False, blank=True, help_text='Contact email address')

    def __str__(self):
        return self.name
