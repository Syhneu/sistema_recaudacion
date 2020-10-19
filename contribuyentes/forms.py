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
            'dir_cont'
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
            'num_patente': 'Nº Patente'
        }

        # widgets = { }