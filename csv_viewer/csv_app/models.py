from django.db import models


class CSVRecord(models.Model):

    code = models.TextField()
    name = models.TextField()
    level_one = models.TextField()
    level_two = models.TextField()
    level_three = models.TextField()
    price = models.TextField()
    bid_price = models.TextField()
    number = models.TextField()
    property_fields = models.TextField()
    joint_purchase = models.TextField()
    unit = models.TextField()
    picture = models.TextField()
    display_onscreen = models.TextField()
    description = models.TextField()


