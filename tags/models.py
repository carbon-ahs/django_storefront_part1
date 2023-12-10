from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    """Tags for items"""

    label = models.CharField(_("Label"), max_length=255)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return str(self.label)

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})


class TaggedItem(models.Model):
    """All taged items."""

    tag = models.ForeignKey("tags.Tag", verbose_name=_(""), on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = _("TaggedItem")
        verbose_name_plural = _("TaggedItems")

    def get_absolute_url(self):
        return reverse("TaggedItem_detail", kwargs={"pk": self.pk})
