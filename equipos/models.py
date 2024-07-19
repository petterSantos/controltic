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

class ModelOficina(ExternalModel):
    idOficina = models.TextField(db_column='ofi_codigo', blank=True, primary_key= True)
    nameOficina = models.TextField(db_column='ofi_Oficina', blank=True)

    def __str__(self):
        return self.idOficina+' - oficina: '+self.nameOficina
    
    class Meta(ExternalModel.Meta):
        db_table = 'Tb_Oficinas'

class ModelPersona(ExternalModel):
    idPersona = models.TextField(db_column='per_codigo', blank=True, primary_key=True)
    nombres = models.TextField(db_column='per_nombres', blank=True)
    apellidos = models.TextField(db_column='per_apellidos',blank=True)

    def __str__(self):
        return self.idPersona+' - Persona: '+self.nombres+' '+self.apellidos
    
    class Meta(ExternalModel.Meta):
        db_table ='Tb_Personal'

class ModelInventario(ExternalModel):
    idInventario = models.TextField(db_column='indl_id', blank=True, primary_key= True)
    codOficina = models.TextField(db_column=' indl_codOficina',blank=True)
    codPersona = models.TextField(db_column='indl_codPersonal', blank=True)
    codBien = models.TextField(db_column='indl_codBien', blank=True)
    oficina = models.ForeignKey(ModelOficina,on_delete=models.CASCADE)
    persona = models.ForeignKey(ModelPersona,on_delete=models.CASCADE)
    bien = models.ForeignKey(ModelEquipo,on_delete=models.CASCADE)

    def __str__(self):
        return self.idInventario+' - Persona: '+self.codPersona+' '+self.codBien
    class Meta(ExternalModel.Meta):
        db_table = 'Tb_InvDll'