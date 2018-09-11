# -*- coding: utf-8 -*-
"""
SAPIC

Copyleft (@) 2017 CENDITEL nodo Mérida - Copyleft (@) 2017 CENDITEL nodo Mérida - https://planificacion.cenditel.gob.ve/trac/wiki/WikiStart#a5.-SistemaAutomatizadodePlanificaciónIntegralComunalSAPIC
"""
## @package explicacion_situacional.views.caracterizacionFisicaViews
#
# Vistas correspondientes a la explicacion situacional
# @author Ing. Leonel Paolo Hernandez Macchiarulo (lhernandez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
# @version 1.0

from django.views.generic import (
    TemplateView,
)

from explicacion_situacional.models import ExplicacionSituacional, TipoPregunta

from utils.views import LoginRequeridoPerAuth

from explicacion_situacional.modelsEncuestas.modelsConsultas import (
    Consulta
)

from explicacion_situacional.modelsEncuestas.modelsParticipacion import (
    RespuestaSino, RespuestaOpciones,
    RespuestaAbierta, RespuestaUbicacion
)


class CaracterizacionPoliticaView(LoginRequeridoPerAuth, TemplateView):
    """!
    Clase que muestra el templates de la caracterización política de la comunidad

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 30-005-2017
    @version 1.0.0
    """
    template_name = "caracterizacion.politica.html"
    group_required = [u"Administradores", u"Voceros", u"Integrantes"]

    def get_context_data(self, **kwargs):
        """!
        Metodo que permite cargar de nuevo valores en los datos de contexto de la vista

        @author Lully Troconis (ltroconis at cenditel.gob.ve)
        @author Manuel Zambrano
        @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 03-07-2018
        @date 08-09-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @param kwargs <b>{object}</b> Objeto que contiene los datos de contexto
        @return Retorna los datos de contexto
        """
        consulta = None
        si_no, opciones, abierta, ubicacion, consultas = [], [], [], [], []
        try:
            servicios_pks = [pk_val for pk_val in range(19, 25)]
            for pk in servicios_pks:
                consulta = Consulta.objects.select_related().get(pk=pk)
                respuesta_si_no = list(RespuestaSino.objects.filter(user=self.request.user, pregunta__consulta=consulta))
                si_no = si_no + respuesta_si_no
                respuesta_opciones = list(RespuestaOpciones.objects.filter(user = self.request.user,opcion__pregunta__consulta = consulta))
                opciones = opciones + respuesta_opciones
                respuesta_abierta = list(RespuestaAbierta.objects.filter(user = self.request.user, pregunta__consulta = consulta))
                abierta = abierta + respuesta_abierta
                respuesta_ubicacion = list(RespuestaUbicacion.objects.filter(user = self.request.user, pregunta__consulta = consulta))
                ubicacion = ubicacion + respuesta_ubicacion
                if respuesta_si_no or respuesta_abierta or respuesta_ubicacion or respuesta_opciones:
                    consultas.append(pk)
            kwargs['si_no'] = si_no
            kwargs['opciones'] = opciones
            kwargs['abierta'] = abierta
            kwargs['ubicacion'] = ubicacion
            kwargs['consultas'] = consultas
        except Exception as e:
            print("Ocurrió un error durante la consulta" + str(e))
        return super(CaracterizacionPoliticaView, self).get_context_data(**kwargs)




