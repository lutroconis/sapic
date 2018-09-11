# -*- coding: utf-8 -*-
"""
Sistema Automatizado de Planificación Integral Comunal SAPIC

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.views
#
# Vistas correspondientes a la explicacion situacional
# @author Ing. Erwin Paredes (eparedes at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0

import time
import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from explicacion_situacional.modelsEncuestas.modelsParticipacion import (
    RespuestaSino, RespuestaOpciones,
    RespuestaAbierta, RespuestaUbicacion
    )

from django.views.generic import (
    TemplateView,
    UpdateView
)
from django.contrib import messages
from utils.views import LoginRequeridoPerAuth

from django.contrib.gis import forms

from explicacion_situacional.modelsEncuestas.modelsConsultas import (
    Consulta,
    Opcion,
)



from .forms import (
    RespuestaSinoForm, RespuestaAbiertaForm ,
    RespuestaOpcionesForm
)



def ParticipoCaracterizacionEconomica(request,pk):
    """!
    Chequea la participacion del usuario en la caracterización economica de la comunidad

    @author Ing. Erwin Leonel P.  (eparedes at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 30-005-2017
    @version 1.0.0
    """
    user = request.user
    if(user and pk):
        respuesta_sino = RespuestaSino.objects.filter(pregunta__consulta=pk,user=user)
        respuesta_abierta = RespuestaAbierta.objects.filter(pregunta__consulta=pk,user=user)
        respuesta_opciones = RespuestaOpciones.objects.filter(opcion__pregunta__consulta=pk,user=user)
        if(respuesta_sino or respuesta_abierta or respuesta_opciones):
            return redirect('explicacion:caracterizacion_economica')
        return redirect('explicacion:participar_encuesta_economica',pk=2)
    else:
        return redirect('explicacion:explicacion_situacional')


def ModificarRespuesta(request):
    if request.method == "POST":
        id = request.POST["ID"]
        respuesta = request.POST.get("respuesta")
        registro = RespuestaSino.objects.get(id=id)
        registro.respuesta = respuesta
        registro.save()
    return redirect('explicacion:caracterizacion_economica')


class ModificarRespuestaView(LoginRequeridoPerAuth, TemplateView):
    """!
    Clase que mustra el template y gestiona la vista para modificar una respuesta en una encuesta
    
    @author Manuel Zambrano 
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 30-08-2018
    @version 1.0.0
    """

    template_name = 'modificar.respuesta.html'
    group_required = [u"Administradores", u"Voceros", u"Integrantes"] 


    def get(self,*arg,**kwargs): 
        """!
        Metodo que maneja las peticiones HTTP GET de la vista, Carga los valores iniciales al formulario

        @author Manuel Zambrano
        @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 30-08-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @param kwargs <b>{object}</b> Objeto que contiene las variables de la url
        @param arg <b>{object}</b> 
        @return retorna los datos de contexto
        """

        if kwargs['tipo'] == '1' :
            respuesta =  RespuestaOpciones.objects.select_related().get(
                                                            pk = kwargs['pk'],
                                                            user=self.request.user
                                                            )
            formulario = RespuestaOpcionesForm()
            formulario.fields['respuesta']._set_queryset(Opcion.objects.filter(
                                                pregunta=respuesta.opcion.pregunta
                                                ))
            formulario.fields['respuesta'].initial= respuesta.opcion
            

        if kwargs['tipo'] == '4' : #Hacer para cada tipo de respuesta8 
            respuesta = RespuestaSino.objects.select_related().get(
                                                            pk = kwargs['pk'],
                                                            user=self.request.user
                                                            )
            if respuesta.respuesta == True:
                formulario = RespuestaSinoForm(initial={
                                                    'respuesta':respuesta.respuesta,
                    })
            else:
                justificacion = RespuestaAbierta.objects.select_related().get(
                                                            user = self.request.user, 
                                                            pregunta = respuesta.pregunta
                                                            )
                formulario = RespuestaSinoForm(initial={
                                                    'respuesta':respuesta.respuesta,
                                                    'justificacion':justificacion.texto_respuesta,
                    })

        if kwargs['tipo'] == '5' :
            respuesta = RespuestaAbierta.objects.select_related().get(
                                                            pk = kwargs['pk'],
                                                            user=self.request.user
                                                            )
            formulario = RespuestaAbiertaForm(initial={
                                                'respuesta':respuesta.texto_respuesta,
                })

        kwargs['formulario'] = formulario
        kwargs['o'] = respuesta


        return super(ModificarRespuestaView,self).get(self,**kwargs)

    def post(self,*arg,**kwargs):
        """!
        Metodo que maneja las peticiones HTTP POST de la vista, Guarda la modificacion de la pregunta

        @author Manuel Zambrano
        @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 03-09-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @param kwargs <b>{object}</b> Objeto que contiene las variables de la url
        @param arg <b>{object}</b> 
        @return Redirecciona a la tabla de ecuestas
        """

        if kwargs['tipo'] == '1' :
            respuesta =  RespuestaOpciones.objects.select_related().get(
                                                            pk = kwargs['pk'],
                                                            user=self.request.user
                                                            )
            formulario = RespuestaOpcionesForm(self.request.POST,initial={
                'respuesta':respuesta.opcion,
                })
            if formulario.is_valid() and formulario.has_changed():
                opcion = formulario.cleaned_data['respuesta']
                respuesta.opcion = opcion
                respuesta.save()

        if kwargs['tipo'] == '5':
            respuesta = RespuestaAbierta.objects.select_related().get(
                                                            pk = kwargs['pk'], 
                                                            user=self.request.user
                                                            )
            formulario = RespuestaAbiertaForm(self.request.POST, initial={
                'respuesta':respuesta.texto_respuesta,
                })
            if formulario.is_valid() and formulario.has_changed():
                texto_respuesta = formulario.cleaned_data['respuesta']
                respuesta.texto_respuesta = texto_respuesta
                respuesta.save()

        if kwargs['tipo'] == '4':
            respuesta = RespuestaSino.objects.select_related().get(
                                                            pk = kwargs['pk'],
                                                            user = self.request.user
                                                            )
            formulario = RespuestaSinoForm(self.request.POST)         
            if formulario.is_valid():
                if formulario.cleaned_data['respuesta'] :
                    respuesta.respuesta = formulario.cleaned_data['respuesta']
                    respuesta.save()
                else:   
                    try:
                        justificacion = RespuestaAbierta.objects.select_related().get(
                                                            user = self.request.user, 
                                                            pregunta = respuesta.pregunta
                                                            )
                        texto_respuesta = formulario.cleaned_data['justificacion']
                        justificacion.texto_respuesta = texto_respuesta
                        justificacion.es_justificacion = True
                        respuesta.respuesta = formulario.cleaned_data['respuesta']
                        respuesta.save()
                        justificacion.save()
                    except:
                        justificacion = RespuestaAbierta()
                        justificacion.pregunta = respuesta.pregunta
                        justificacion.texto_respuesta = formulario.cleaned_data['justificacion']
                        justificacion.user = self.request.user
                        justificacion.es_justificacion = True
                        justificacion.save()
                        respuesta.respuesta = formulario.cleaned_data['respuesta']
                        respuesta.save()
            else : 
                messages.error(self.request, 'Error el formulario  \
                                                No es Valido') #provicional, mientras se valida el formulario con js
        return redirect(self.request.META.get("HTTP_REFERER"))

