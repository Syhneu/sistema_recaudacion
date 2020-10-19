from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class RcContrib(models.Model):
    cod_con = models.IntegerField(primary_key=True)    # codigo contribuyente
    nom_con = models.CharField(max_length=255)                  # nombre o razon social
    
    class TipoPersona(models.TextChoices):
        JURIDICA = 'J', _('Juridica')
        NATURAL = 'N', _('Natural')
        GOBIERNO = 'G', _('Gobierno')
    
    tipo_persona = models.CharField(                            # tipo de persona
        max_length = 1,
        choices = TipoPersona.choices,
        default = TipoPersona.JURIDICA
    )

    ced_rif = models.CharField(max_length=15, unique=True)      # cedula rif
    cod_edo = models.IntegerField()                             # codigo estado
    cod_mun = models.IntegerField()                             # codigo municipio
    cod_par = models.IntegerField()                             # codigo parroquia
    dir_cont = models.TextField()                               # direccion del contribuyente
    telf_empresa = models.CharField(max_length=30)              # telefono de la empresa

    class Estatus(models.TextChoices):
        ACTIVO = 'A', _('Activo')
        PENDIENTE = 'P', _('Pendiente')

    status = models.CharField(                                  # status del expediente
        max_length = 1,
        choices = Estatus.choices,
        default = Estatus.PENDIENTE
    )

    con_acti_economica = models.IntegerField()                  # actividad economica
    transeunte = models.CharField(max_length=1)                 # transeunte permanente o temporal

    class Residente(models.TextChoices):
        RESIDENTE = 'R', _('Residente')
        NO_RESIDENTE = 'N', _('No Residente')

    residente = models.CharField(                               # (tipo) es residente
        max_length = 1,
        choices = Residente.choices,
        default = Residente.RESIDENTE
    )

    fec_inicio = models.DateField(auto_now=True)                # fecha expedicion de expediente
    periodo = models.IntegerField()                             # periodo de registro
    fec_final = models.DateField()                              # fecha vencimiento de expediente
    fax = models.CharField(max_length=25)
    num_patente = models.CharField(max_length=255)              # numero de patente
    razon_comer = models.CharField(max_length=255)              # razon comercial
    fecha_inscripcion = models.DateField()                      # fecha de inscripcion del REGISTRO MERCANTIL
    tomo = models.CharField(max_length=40)                      # tomo de registro
    protocolo = models.CharField(max_length=40)                 # protocolo de registro
    tipo_empresa = models.CharField(max_length=2)               # tipo empresa CA SA SLR
    
    class Sucursal(models.TextChoices):
        PRINCIPAL = 'P', _('Principal')
        SUCURSAL = 'S', _('Sucursal')
    
    sucursal = models.CharField(                                # sucursal
        max_length = 1,
        choices = Sucursal.choices,
        default = Sucursal.PRINCIPAL
    )

    fecha_fin_registro = models.DateField()                     # fecha vencimiento del REGISTRO MERCANTIL
    numero_acta = models.CharField(max_length=50)               # numero de acta constitutiva
    fecha_regis_acta = models.DateField()                       # fecha registro de acta
    fecha_fin_acta = models.DateField()                         # fecha vencimiento de acta
    correo_empresa = models.CharField(max_length=50)             # correo de la empresa
    correo_contacto = models.CharField(max_length=50)            # correo de contacto
    whatsapp = models.CharField(max_length=50)                  # red social whatsapp
    fecha_fin_junta = models.DateField()                        # fecha de vencimiento de junta
    usu_reg = models.IntegerField()                             # codigo de usuario de registro de expediente
    usu_apro = models.IntegerField()                            # codigo de usuario de aprobacion de expediente

class RcRepresentante(models.Model):
    cod_con = models.ForeignKey(RcContrib, on_delete= models.CASCADE)
    cedula = models.CharField(max_length=12)
    nr_civi = models.CharField(max_length=100)
    nombre = models.TextField()
    cargo = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    cod_con = models.IntegerField(max_length=4)
    correo = models.EmailField()
    celular = models.CharField(max_length=30)

class RcAccionistas(models.Model):
    cod_repre = models.ForeignKey(RcContrib, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=12)
    nombre = models.TextField()
    nr_civi = models.TextField()
    cargo = models.TextField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=11)
    cod_con = models.models.IntegerField(max_length=4)
    correo = models.EmailField()
    celular = models.CharField(max_length=11)
