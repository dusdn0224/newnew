from django.db import models
from django.contrib.auth.models import Permission

# Create your models here.
class Medicine(models.Model):
    entpName = models.TextField(null=True)
    itemName = models.TextField(null=True, unique=True)
    itemSeq = models.IntegerField(null=True)
    efcyQesitm = models.TextField(null=True)
    useMethodQesitm = models.TextField(null=True)
    atpnWarnQesitm = models.TextField(null=True)
    atpnQesitm = models.TextField(null=True)
    intrcQesitm = models.TextField(null=True)
    seQesitm = models.TextField(null=True)
    depositMethodQesitm = models.TextField(null=True)
    openDe = models.DateTimeField(null=True)
    updateDe = models.DateField(null=True)
    itemImage = models.TextField(null=True)
    bizrno = models.IntegerField(null=True)