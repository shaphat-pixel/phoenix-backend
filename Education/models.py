from django.db import models

# Create your models here.

class Inst_Categories(models.Model):
    cat_name = models.CharField(null=True, default="", max_length=300)


    def __str__(self):
        return f'{self.cat_name}'


class Institution(models.Model):
    inst_cat = models.ForeignKey(Inst_Categories, on_delete=models.CASCADE)
    inst_name = models.CharField(null=True, default="", max_length=300)


    def __str__(self):
        return f'{self.inst_name}'




