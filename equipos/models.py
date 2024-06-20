from django.db import models

class ExternalModel(models.Model):
    class Meta:
        managed = False
        abstract = True
        app_label = 'support'

class ModelEquipo(ExternalModel):
    idEquipo = models.TextField(db_column='bns_id', blank=True, primary_key=True)
    codInterno = models.TextField(db_column='bns_Interno', blank=True)
    marca = models.TextField(db_column='bns_marca', blank=True)
    modelo = models.TextField(db_column='bns_modelo', blank=True)
    nroSerie = models.TextField(db_column='bns_serie', blank=True)
    color = models.TextField(db_column='bns_color', blank=True)
    fechaPecosa = models.DateField(db_column='bns_fecPecosa')
    estado = models.TextField(db_column='bns_estBien', blank=True)
    descOtros = models.TextField(db_column='bns_dscOtros', blank=True)
    codTipoBien = models.TextField(db_column='bns_codTipoBien', blank=True)
    tipoDocAdq = models.TextField(db_column='bns_codDocAdq', blank=True)
    docAdq = models.TextField(db_column='bns_docAdq', blank=True)
    siaf = models.TextField(db_column='bns_siaf', blank=True)

    def __str__(self):
        return self.codInterno +' - marca: '+self.marca+' - nroSerie: '+self.nroSerie
    class Meta(ExternalModel.Meta):
        db_table = 'Tb_Bienes'

class ModelTipoEquipo(ExternalModel):
    idTipoEquipo = models.TextField(db_column='tip_codigo', blank=True, primary_key=True)
    tipoEquipoExt = models.TextField(db_column='tip_descripcio', blank=True)

    def __str__(self):
        return self.idTipoEquipo +' - tipo: '+self.tipoEquipoExt
    class Meta(ExternalModel.Meta):
        db_table = 'Tb_TipoBien'

