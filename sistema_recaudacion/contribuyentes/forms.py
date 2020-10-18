from django import forms

class RegistroContribuyente(forms.Form):
  ##1. Datos de la Empresa
  numpatente = forms.CharField(max_length=255)
  año = forms.IntegerField()
  fecha_expedicion = forms.DateInput()
  fecha_vencimiento = forms.DateInput()
  tipo_persona = forms.CheckboxInput()
  tipo = forms.CheckboxInput()
  sucursal = forms.CheckboxInput()
  rif_ci = forms.CharField(max_length=11)
  razon_social = forms.CharField(max_length=255)
  denom_comercial = forms.CharField(max_length=255)
  tlf_celular = forms.IntegerField()
  whatsapp = forms.IntegerField()
  tlf_empresa = forms.IntegerField()
  direccion = forms.CharField(max_length=255)
  correo_empresa = forms.EmailInput()
  correo_contacto = forms.EmailInput()
  estado = forms.Select()
  municipio = forms.CharField(max_length=30)
  parroquia = forms.CharField(max_length=50)
  situacion_empresa = forms.CheckboxInput()
  fecha_vencimiento_junta = forms.DateInput()
  
 ##Clasificacion actividad economica
  clasificacion = forms.CharField(max_length=30)
  codigo_actividad = forms.CharField(max_length=30)
  descripcion = forms.CharField(max_length=255)

  ##Registro Mercantil Empresa
  num_registro = forms.CharField(max_length=40)
  tomo = forms.TextInput()
  protocolo = forms.TextInput()
  fecha_exp_registro = forms.DateInput()
  fecha_ven_registro = forms.DateInput()
  capital_inicial_activo = forms.NumberInput()
  aumento_capital = forms.NumberInput()
  fecha_aumento_capital = forms.DateInput()

  ##Representantes Empresa
  cedula = forms.CharField(max_length=11)
  nombre_apellido = forms.CharField(max_length=50)
  cargo = forms.TextInput()
  celular = forms.IntegerField()

  ##Registo acta de asamblea
  num_registro_asamblea = forms.TextInput()
  fecha_exp_acta = forms.DateInput()
  fecha_ven_acta = forms.DateInput()
  objeto_empresa = forms.Textarea()

  ##Registro accionistas 
  cedula_accionista = forms.CharField(max_length=11)
  nombre_apellido_accionista = forms.CharField(max_length=50)
  tipo_accionista = forms.CharField(max_length=20)
  celular_accionista = forms.IntegerField()