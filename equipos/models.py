from django.db import models

class ExternalModel(models.Model):
    class Meta:
        managed = False
        abstract = True
        app_label = 'support'


class ModelC(ExternalModel):
    some_field = models.TextField(db_column='some_field')

    class Meta(ExternalModel.Meta):
        db_table = 'some_table_c'


class ModelD(ExternalModel):
    some_other_field = models.TextField(db_column='some_other_field')

    class Meta(ExternalModel.Meta):
        db_table = 'some_table_d'
