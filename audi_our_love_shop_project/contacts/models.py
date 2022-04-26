from django.db import models


class ContactsModel(models.Model):
    EMAIL_MAX_LENGTH = 30
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    DEFAULT_CHOICE = '--Select Your Issue--'
    REQUEST_INVOICE_FOR_ORDER = 'Request Invoice for order'
    REQUEST_ORDER_STATUS = 'Request order status'
    HAVE_NOT_RECEIVED_CASHBACK = "Haven't received cashback yet"
    OTHER = 'Other'

    CONTACT_CHOICES = (
        (DEFAULT_CHOICE, DEFAULT_CHOICE),
        (REQUEST_INVOICE_FOR_ORDER, REQUEST_INVOICE_FOR_ORDER),
        (REQUEST_ORDER_STATUS, REQUEST_ORDER_STATUS),
        (HAVE_NOT_RECEIVED_CASHBACK, HAVE_NOT_RECEIVED_CASHBACK),
        (OTHER, OTHER),
    )
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, null=True, blank=True)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, null=True, blank=True)
    email = models.EmailField(max_length=EMAIL_MAX_LENGTH)
    content = models.TextField()
    reason = models.CharField(max_length=100, choices=CONTACT_CHOICES, default='--Select Your Issue--')

    def __str__(self):
        return self.subject
