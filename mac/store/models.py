from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0)
    img = models.ImageField(upload_to="store/images", default="")
    sub_category = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.product_name


