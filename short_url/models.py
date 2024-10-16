from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.


class ShortUrl(models.Model):

    longUrl = models.URLField(_("Long Url"), max_length=200)
    shortUrl = models.CharField(_("Short Url"), max_length=15)
    created = models.DateTimeField(_("Created Time"), auto_now_add=True)

    class Meta:

        verbose_name = _("ShortUrl")
        verbose_name_plural = _("ShortUrls")

    def __str__(self):
        return str(self.longUrl)

    def get_absolute_url(self):
        return reverse("short_url:detail_url", kwargs={"pk": self.pk})
