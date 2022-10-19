from django.db import models

class Personas(models.Model):
    
    id_persona = models.AutoField(db_column='id_persona', primary_key=True) 
    tipo_id_pers = models.CharField(db_column='tipo_id_pers', blank=True, null=True,max_length=50,)
    identificacion_pers = models.CharField(db_column='identificacion_pers', unique=True,max_length=50, blank=False, null=False) 
    nombre = models.CharField(db_column='nombre', max_length=50, blank=False, null=False)  
    apellido = models.CharField(db_column='apellido', max_length=50, blank=False, null=False) 
    email = models.CharField(db_column='email',unique=True, max_length=50, blank=False, null=False)  
    fecha_nacimiento= models.DateTimeField(blank=False, null=False)
    celular = models.CharField(db_column='celular', max_length=50, blank=False, null=False)  
    telefono = models.CharField(db_column='telefono', max_length=50, blank=True, null=True) 
    estado_pers =models.BooleanField(db_column='estado_pers', default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['id_persona']
        db_table = 'Personas'
