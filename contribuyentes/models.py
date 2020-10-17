from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class RcContrib(models.Model):
    cod_con = models.IntegerField(max_length=4, unique=True)    # codigo contribuyente
    nom_con = models.CharField(max_length=255)                  # nombre o razon social
    
    class TipoPersona(models.TextChoices):
        JURIDICA = 'J', _('Juridica')
        NATURAL = 'N', _('Natural')
        GOVIERNO = 'G', _('Govierno')
    
    tipo_persona = models.CharField(                            # tipo de persona
        max_length = 1,
        choices = TipoPersona.Choices,
        default = TipoPersona.JURIDICA
    )

    ced_rif = models.CharField(max_length=15, unique=True)      # cedula rif
    cod_edo = models.IntegerField(max_length=2)                 # codigo estado
    cod_mun = models.IntegerField(max_length=2)                 # codigo municipio
    cod_par = models.IntegerField(max_length=2)                 # codigo parroquia
    dir_cont = models.CharField(max_length=250)                 # direccion del contribuyente
    telf_empresa = models.CharField(max_length=30)              # telefono de la empresa

    class Estatus(models.TextChoices):
        ACTIVO = 'A', _('Activo')
        PENDIENTE = 'P', _('Pendiente')

    status = models.CharField(                                  # status del expediente
        max_length = 1,
        choices = Estatus.Choices,
        default = Estatus.PENDIENTE
    )

    con_acti_economica = models.IntegerField(max_length=2)      # actividad economica
    transeunte = models.CharField(max_lengt=1)                  # transeunte permanente o temporal
    residente = models.BooleanField()                           # (tipo) es residente
    fec_inicio = models.DateField(auto_now=True)                # fecha expedicion de expediente
    periodo = models.IntegerField(max_length=4)                 # periodo de registro
    fec_final = models.DateField()                              # fecha vencimiento de expediente
    fax = models.CharField()
    num_patente = models.CharField(max_length=255)              # numero de patente
    razon_comer = models.CharField(max_length=255)              # razon comercial
    fecha_inscripcion = models.DateField()                      # fecha de inscripcion del REGISTRO MERCANTIL
    tomo = models.CharField()                                   # tomo de registro
    protocolo = models.CharField()                              # protocolo de registro
    tipo_empresa = models.CharField()                           # tipo empresa CA SA SLR
    
    class Sucursal(models.TextChoices):
        PRINCIPAL = 'P', _('Principal')
        SUCURSAL = 'S', _('Sucursal')
    
    sucursal = models.CharField(                                # sucursal
        max_lenght = 1,
        choices = Sucursal.Choices,
        default = Sucursal.PRINCIPAL
    )

    fecha_fin_registro = models.DateField()                     # fecha vencimiento del REGISTRO MERCANTIL
    numero_acta = models.CharField(max_length=50)               # numero de acta constitutiva
    fecha_regis_acta = models.DateField()                       # fecha registro de acta
    fecha_fin_acta = models.DateField()                         # fecha vencimiento de acta
    correo_empresa = models.CharField(maxlength=50)             # correo de la empresa
    correo_contacto = models.CharField(maxlength=50)            # correo de contacto
    whatsapp = models.CharField(max_length=50)                  # red social whatsapp
    fecha_fin_junta = models.DateField()                        # fecha de vencimiento de junta
    usu_reg = models.IntegerField()                             # codigo de usuario de registro de expediente
    usu_apro = models.IntegerField()                            # codigo de usuario de aprobacion de expediente
