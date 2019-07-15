from django.db import models
from postgres_copy import CopyManager


class Fenotipos(models.Model):
    hpo_id = models.CharField(max_length=100)
    hpo_name = models.CharField(max_length=100)
    gene_id = models.CharField(max_length=100)
    gene_name = models.CharField(max_length=100)
    datas = CopyManager()
    objects = models.Manager()

    def __str__(self):
        return self.gene_name
        # self.gene_id, self.hpo_id, self.hpo_name

