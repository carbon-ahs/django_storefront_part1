from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    price = models.DecimalField(_("Price"), max_digits=6, decimal_places=2)
    inventory = models.IntegerField(_("Inventory"))
    last_update = models.DateTimeField(
        _("Last Update"), auto_now=False, auto_now_add=False
    )

    def __str__(self) -> str:
        return str(self.title)


class Customer(models.Model):
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
        PAYMENT_STATUS_PENDING = "P"
        PAYMENT_STATUS_COMPLETE = "C"
        PAYMENT_STATUS_FAILED = "F"

        PAYMENT_STATUS = [
            (PAYMENT_STATUS_PENDING, "Pending"),
            (PAYMENT_STATUS_COMPLETE, "Complete"),
            (PAYMENT_STATUS_FAILED, "Failed"),
        ]
        placed_at = models.DateTimeField(
            _("Placed At"),
            auto_now_add=True,
        )
        payment_status = models.CharField(
            _("Payment Status"),
            max_length=1,
            choices=PAYMENT_STATUS,
            default=PAYMENT_STATUS_FAILED,
        )


class Address(models.Model):
    street = models.CharField(_("Street"), max_length=255)
    city = models.CharField(_("City"), max_length=255)
    customer = models.OneToOneField(
        "store.Customer",
        verbose_name=_("Customer"),
        on_delete=models.CASCADE,
    )
