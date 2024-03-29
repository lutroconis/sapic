# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from .views.caracterizacionFisicaView import *
from .views.caracterizacionEconomicaView import *
from .views.caracterizacionSocialView import *
from .views.caracterizacionPoliticaView import *
from .views.genericEncuestasView import *
from .ajax import *
from explicacion_situacional.functions import *
from rest_framework import routers


urlpatterns = [
                url(r'^explicacion-situacional/',
                    ExplicacionSituacionalView.as_view(),
                    name="explicacion_situacional"),
                url(r'^caracterizacion-fisica/$',
                    CaracterizacionFisicaView.as_view(),
                    name="caracterizacion_fisica"),
                url(r'^ubicacion-geografica/',
                    RegisterUbicMapView.as_view(),
                    name="ubicacion_geografica"),
                url(r'^caracterizacion-fisica/condicion-suelos/(?P<pk>25+)$',
                    EncuestasParticiparView.as_view(),
                    name="condicion_suelos"),

                url(r'^participo-caracterizacion-economica/(?P<pk>2+)$',
                    ParticipoCaracterizacionEconomica,
                    name="participo_caracterizacion_economica"),
                url(r'^caracterizacion-economica/$',
                    CaracterizacionEconomicaView.as_view(),
                    name="caracterizacion_economica"),
                url(r'^caracterizacion-economica/participar_encuesta_economica/(?P<pk>2+)$',
                    EncuestasParticiparView.as_view(),
                    name="participar_encuesta_economica"),
                url(r'^modificar-respuesta/$',
                    ModificarRespuesta,
                    name="modificar_respuesta"),


                url(r'^modificar-respuesta/(?P<tipo>.+)/(?P<pk>.+)$',
                    ModificarRespuestaView.as_view(),
                    name="modificar_respuesta_"),

                #Caracterización social
                url(r'^caracterizacion-social/$',
                    CaracterizacionSocialView.as_view(),
                    name="caracterizacion_social"),
                url(r'^caracterizacion-social/servicio-agua/(?P<pk>3+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_agua"),
                url(r'^caracterizacion-social/servicio-electricidad/(?P<pk>4+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_electricidad"),
                url(r'^caracterizacion-social/servicio-infraestructura/(?P<pk>5+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_infraestructura"),
                url(r'^caracterizacion-social/servicio-saneamiento/(?P<pk>6+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_saneamiento"),
                url(r'^caracterizacion-social/servicio-salud/(?P<pk>7+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_salud"),
                url(r'^caracterizacion-social/servicio-educativo/(?P<pk>8+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_educativo"),
                url(r'^caracterizacion-social/servicio-recreativo/(?P<pk>9+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_recreativo"),
                url(r'^caracterizacion-social/servicio-deportivo/(?P<pk>10+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_deportivo"),
                url(r'^caracterizacion-social/servicio-cultura/(?P<pk>11+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_cultura"),
                url(r'^caracterizacion-social/servicio-telecomunicacion/(?P<pk>12+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_telecomunicacion"),
                url(r'^caracterizacion-social/servicio-comunicacion/(?P<pk>13+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_comunicacion"),
                url(r'^caracterizacion-social/servicio-policia/(?P<pk>14+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_policia"),
                url(r'^caracterizacion-social/servicio-bombero/(?P<pk>15+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_bombero"),
                url(r'^caracterizacion-social/servicio-proteccion/(?P<pk>16+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_proteccion"),
                url(r'^caracterizacion-social/servicio-jurisdiccion/(?P<pk>17+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_jurisdiccion"),
                url(r'^caracterizacion-social/servicio-incidente/(?P<pk>18+)$',
                    EncuestasParticiparView.as_view(),
                    name="servicio_incidente"),
                
                # Caracterización política
                url(r'^caracterizacion-politica/$',
                    CaracterizacionPoliticaView.as_view(),
                    name="caracterizacion_politica"),
                url(r'^caracterizacion-politica/produccion-cc/(?P<pk>19+)$',
                    EncuestasParticiparView.as_view(),
                    name="produccion_cc"),
                url(r'^caracterizacion-politica/organizacion-c/(?P<pk>20+)$',
                    EncuestasParticiparView.as_view(),
                    name="organizacion_c"),
                url(r'^caracterizacion-politica/produccion-c/(?P<pk>21+)$',
                    EncuestasParticiparView.as_view(),
                    name="produccion_c"),
                url(r'^caracterizacion-politica/relacion_entorno/(?P<pk>22+)$',
                    EncuestasParticiparView.as_view(),
                    name="relacion_entorno"),
                url(r'^caracterizacion-politica/actor-relacionado/(?P<pk>23+)$',
                    EncuestasParticiparView.as_view(),
                    name="actor_relacionado"),
                url(r'^caracterizacion-politica/comunicacion-politica/(?P<pk>24+)$',
                    EncuestasParticiparView.as_view(),
                    name="comunicacion_politica"),

                # Ajax
                url(r'^validar-participacion-ajax',
                    validar_participacion,
                    name="validar_participacion_ajax"),

              ]
