# -*- coding: utf-8 -*-
"""
Sistema Automatizado de Planificación Integral Comunal SAPIC

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.forms
#
# Formularios correspondientes a la explicacion situacional
# @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0

from django.core.exceptions import ValidationError
from django.contrib.gis import forms
from django.forms.fields import (
    CharField,
    BooleanField,
)


from explicacion_situacional.modelsExplicacion.modelsExplicacionesSituacional import *

from explicacion_situacional.modelsEncuestas.modelsParticipacion import *


class ExplicacionForms(forms.ModelForm):
    """!
    Clase que permite crear el formulario para la explicacion situacional

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 09-01-2017
    @version 1.0.0
    """

    class Meta:
        """!
        Clase que construye los meta datos del formulario

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 18-09-2017
        @version 1.0.0
        """
        model = ExplicacionSituacional
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """!
        Funcion que muestra el init del formulario

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 18-09-2017
        """
        super(ExplicacionForms, self).__init__(*args, **kwargs)
        self.fields['fk_organizacion'].widget.attrs.update({
                                      'class': 'form-control'})
        self.fields['fk_organizacion'].empty_label = 'Seleccione la \
                                                     organizacion social'
        self.fields['fk_organizacion'].label = 'Organizacion Social'
        self.fields['fk_organizacion'].required = True

        self.fields['coordenadas'].widget = forms.OSMWidget.template_name = 'openlayers-es.html'
        self.fields['coordenadas'].widget = forms.OSMWidget(attrs={
                                    'default_zoom': 5.2, 'map_width': 600,
                                    'map_height': 400, 'default_lat': 8,
                                    'default_lon': -66})
        self.fields['coordenadas'].required = True

        self.fields['map_cartografico'].widget.attrs.update({'class':'form-control',
                                                   'data-show-preview':'true',
                                                   'accept':'image/*'})
        self.fields['map_cartografico'].label = 'Mapa cartografico'
        self.fields['map_cartografico'].required = True



class UbicacionForms(forms.Form):
    """!
    Clase que permite crear el formulario para el tipo de preguntas que requieren ubicacion

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 20-09-2017
    @version 1.0.0
    """
    ubicacion = CharField()

    class Meta:
        """!
        Clase que construye los meta datos del formulario

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 18-09-2017
        @version 1.0.0
        """
        fields = ('ubicacion')

    def __init__(self, *args, **kwargs):
        """!
        Funcion que muestra el init del formulario

        @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 18-09-2017
        """
        super(UbicacionForms, self).__init__(*args, **kwargs)

        self.fields['ubicacion'].widget = forms.OSMWidget.template_name = 'openlayers-es.html'
        self.fields['ubicacion'].widget = forms.OSMWidget(attrs={
                                    'default_zoom': 5.2, 'map_width': 600,
                                    'map_height': 400, 'default_lat': 8,
                                    'default_lon': -66})
        self.fields['ubicacion'].required = True

class RespuestaSinoForm(forms.Form):
    """!
    Clase que permite crear el formulario para las respuestas de tipo SiNo

    @author Manuel Zambrano
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 29-08-2018
    @version 1.0.0
    """

    respuesta = forms.BooleanField(label='Respuesta',
                                widget=forms.Select(choices=((True,'Si'),
                                                            (False,'No')
                                                            )
                                                    ),
                                required=False
                                )
    justificacion = forms.CharField(label='Respuesta', 
                                    widget=forms.Textarea(),
                                    required=False,
                                    min_length = 128,
                                    ) 

    def __init__(self,*arg,**kwargs):
        """!
        Funcion que muestra el init del formulario

        @author Manuel Zambrano
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 29-08-2018
        @version 1.0.0
        """
        super(RespuestaSinoForm, self).__init__(*arg,**kwargs)
        self.fields['justificacion'].widget.attrs.update({'placeholder': 'Justificacion','style':'width:370px;height:191px;'})

    def clean(self):
        """!
        Funcion que sobreescribe el metodo clean() de la clase, validación para el campo de justificacion  

        @author Manuel Zambrano
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 29-08-2018
        @version 1.0.0
        """
        cleaned_data = super(RespuestaSinoForm,self).clean()
        clean_respuesta = cleaned_data.get('respuesta')
        clean_justificacion = cleaned_data.get('justificacion')
        if not clean_respuesta:
            if not clean_justificacion:
                raise forms.ValidationError(
                "Verifique el campo de justificacion",
                code = "justificacion_error"
                )

class RespuestaAbiertaForm(forms.Form):
    """!
    Clase que permite crear el formulario para las respuestas de tipo Abierta

    @author Manuel Zambrano
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 29-08-2018
    @version 1.0.0
    """

    respuesta = forms.CharField(label='Respuesta', 
                                widget=forms.Textarea(),
                                min_length=128
                                )

    def __init__(self,*arg,**kwargs):
        """!
        Funcion que muestra el init del formulario

        @author Manuel Zambrano
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 29-08-2018
        @version 1.0.0
        """
        
        super(RespuestaAbiertaForm, self).__init__(*arg,**kwargs)
        self.fields['respuesta'].widget.attrs.update({'placeholder': 'Respuesta','style':'width:370px;height:191px;'})

class RespuestaOpcionesForm(forms.Form):
    """!
    Clase que permite crear el formulario para las respuestas de tipo Opciones

    @author Manuel Zambrano
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 29-08-2018
    @version 1.0.0
    """

    respuesta = forms.ModelChoiceField(label = 'Opcion', 
                                    queryset = Opcion.objects.all(),
                                    required=True, 
                                    empty_label=None
                                    )

    def __init__(self,*arg,**kwargs):
        """!
        Funcion que muestra el init del formulario

        @author Manuel Zambrano
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 29-08-2018
        @version 1.0.0
        """

        super(RespuestaOpcionesForm, self).__init__(*arg,**kwargs)

    
        

        
        
        
        