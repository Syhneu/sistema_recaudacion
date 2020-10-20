from django import forms
from . import models

class ContribuyentesForm(forms.ModelForm):
    class Meta:
        model = models.RcContrib
        fields = (
            # 1. Datos de la empresa
            'num_patente', 'fec_inicio', 'fec_final', 'periodo',
            'tipo_persona', 'residente', 'sucursal',
            'ced_rif', 'nom_con',
            'razon_comer',
            'telf_empresa', 'whatsapp',
            'dir_cont',
            'correo_empresa', 'correo_contacto',
            'cod_edo', 'cod_mun', 'cod_par',
            'fecha_fin_junta',

            # 2. Clasificacion economica
            # TODO relacion con modelo rcactividades
            'con_acti_economica',

            # 3. Registro mercantil de la empresa
            'tomo', 'protocolo',
            'fecha_inscripcion', 'fecha_fin_registro',
            #capital
            
            # 4. Representantes de la empresa
            # TODO relacion con modelo rcrepresentante
            'cod_con','cedula','nr_civi','nombre','cargo','direccion',
            'telefono','cod_con','correo','celular'

            # 5. Registro acta de asamblea
            'numero_acta', 'fecha_regis_acta', 'fecha_fin_acta',
            #objeto de la empresa

            # 6. Registro de accionistas
            # TODO relacion con modelo rcaccionistas
            'cod_repre','cedula','nombre','nr_civi','cargo','direccion',
            'telefono', 'cod_con','correo','celular'
        )

        labels = {
            'num_patente': 'Nº Patente',
            'fec_inicio': 'Fecha Expedición',
            'fec_final': 'Fecha Vencimiento',
            'periodo': 'Año',
            'tipo_persona': 'Tipo Persona',
            'residente': 'Tipo',
            'sucursal': 'Sucursal',
            'ced_rif': 'RIF / Cédula',
            'nom_con': 'Denominación Comercial',
            'razon_comer': 'Razón Social',
            'telf_empresa': 'Teléfono Empresa',
            'whatsapp': 'N° WhatsApp',
            'dir_cont': 'Direccion',
            'correo_empresa': 'Correo Empresa',
            'correo_contacto': 'Correo Contacto',
            'cod_edo': 'Estado',
            'cod_mun': 'Municipio',
            'cod_par': 'Parroquia',
            'fecha_fin_junta': 'Fecha Vencimiento - Junta Directiva',
        }

        widgets = {
            'num_patente': forms.TextInput(attrs={'class': 'form-control'}),
            'fec_inicio': forms.TextInput(attrs={'class': 'form-control'}),
            'fec_final': forms.TextInput(attrs={'class': 'form-control'}),
        }