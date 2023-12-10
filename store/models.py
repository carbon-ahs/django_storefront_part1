from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Promotion(models.Model):
    """A model class for discount"""

    description = models.CharField(_("Description"), max_length=255)
    discount = models.FloatField(_("Discount"))

    class Meta:
        verbose_name = _("Promotion")
        verbose_name_plural = _("Promotions")

    def __str__(self):
        return str(self.description)

    def get_absolute_url(self):
        return reverse("Promotion_detail", kwargs={"pk": self.pk})


class Collection(models.Model):
    """A collection of products."""

    title = models.CharField(_("Title"), max_length=255)
    featured_product = models.ForeignKey(
        "store.Product",
        verbose_name=_("Featured Product"),
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
    )

    def __str__(self):
        return str(self.title)


class Product(models.Model):
    """Products of our store."""

    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(default="-")
    description = models.TextField(_("Description"))
    unit_price = models.DecimalField(_("Price"), max_digits=6, decimal_places=2)
    inventory = models.IntegerField(_("Inventory"))
    last_update = models.DateTimeField(
        _("Last Update"), auto_now=False, auto_now_add=False
    )
    collection = models.ForeignKey(
        "store.Collection", verbose_name=_(""), on_delete=models.PROTECT
    )
    promotions = models.ManyToManyField("store.Promotion", verbose_name=_("Promotions"))

    def __str__(self) -> str:
        return str(self.title)


class Customer(models.Model):
    """Customer is king."""

    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"
    MEMBERSHIP_VALUES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold"),
    ]
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    phone = models.CharField(_("Phone Number"), max_length=50)
    birth_date = models.DateField(_("Birth Date"), null=True, blank=True)
    membership = models.CharField(
        _("Membership"),
        max_length=1,
        choices=MEMBERSHIP_VALUES,
        default=MEMBERSHIP_BRONZE,
    )

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Order(models.Model):
    """Order stats."""

    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETE = "C"
    PAYMENT_STATUS_FAILED = "F"

    PAYMENT_STATUS = [
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed"),
    ]
    placed_at = models.DateTimeField(_("Placed At"), auto_now_add=True)
    payment_status = models.CharField(
        _("Payment Status"),
        max_length=1,
        choices=PAYMENT_STATUS,
        default=PAYMENT_STATUS_PENDING,
    )
    customer = models.ForeignKey(
        "store.Customer", verbose_name=_("Customer"), on_delete=models.PROTECT
    )


class OrderItem(models.Model):
    """Items inside every order."""

    order = models.ForeignKey(
        "store.Order", verbose_name=_("Order"), on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "store.Product", verbose_name=_(""), on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField(_("Qty."))
    unit_price = models.DecimalField(_("Price"), max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _("OrderItem")
        verbose_name_plural = _("OrderItems")

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse("OrderItem_detail", kwargs={"pk": self.pk})


class Address(models.Model):
    """Customer order adresses."""

    street = models.CharField(_("Street"), max_length=255)
    city = models.CharField(_("City"), max_length=255)
    customer = models.ForeignKey(
        "store.Customer", verbose_name=_("Customer"), on_delete=models.CASCADE
    )


class Cart(models.Model):
    """Cart of store"""

    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return str(self.created_at)

    def get_absolute_url(self):
        return reverse("Cart_detail", kwargs={"pk": self.pk})


class CartItem(models.Model):
    """Indevisual items of a cart."""

    cart = models.ForeignKey(
        "store.Cart", verbose_name=_("Cart"), on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "store.Product", verbose_name=_("Product"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("CartItem")
        verbose_name_plural = _("CartItems")

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse("CartItem_detail", kwargs={"pk": self.pk})
