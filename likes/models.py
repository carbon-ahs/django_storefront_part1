from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = _("LikedItem")
        verbose_name_plural = _("LikedItems")

    def get_absolute_url(self):
        return reverse("LikedItem_detail", kwargs={"pk": self.pk})
