from django.db import models


class Sector(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True, help_text='Full name of the sector')
    slug = models.SlugField(max_length=50, null=False, blank=False, unique=True)
    vision = models.TextField(null=False, blank=True, default='', help_text='Full vision (HTML allowed)')
    goals = models.TextField(null=False, blank=True, default='', help_text='List of goals, one per line.')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def image_filename(self):
        return 'img/sectors/%s.png' % self.slug
