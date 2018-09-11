# -*- coding: utf-8 -*-
"""!
Vista que controla los procesos de las organizaciones sociales

@author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
@copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
@date 27-07-2017
@version 1.0.0
"""

from users.models import *

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.auth.models import (
    Group, User
)
from django.core.urlresolvers import (
    reverse_lazy, reverse
)
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.views.generic.base import RedirectView
from django.views.generic import (
    TemplateView
)
from django.views.generic.edit import (
    FormView, UpdateView
)

from .forms import *

#from .forms import (
#    FormularioRegisterOrgSocial, FormsetVocero
#)
from multi_form_view import MultiModelFormView

from .models import (
    OrganizacionSocial, Vocero
)

from utils.views import LoginRequeridoPerAuth

class RegisterOrgView(LoginRequeridoPerAuth, MultiModelFormView):
    """!
    Muestra el formulario de registro de la organizacion social

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 27-07-2017
    @version 1.0.0
    """
    template_name = "organizacion.register.html"
    form_classes = {
      'organizacion_social': FormularioRegisterOrgSocial,
      'voceros': FormsetVocero,
    }
    #success_url = reverse_lazy('utils:inicio')
    success_url = reverse_lazy('organizaciones:registrar_organizacion')
    record_id = None
    group_required = [u"Administradores"]

    def get_objects(self):
        self.record_id = self.kwargs.get('record_id', None)
        try:
            record = Vocero.objects.select_related().get(fk_org_social=self.record_id)
        except Vocero.DoesNotExist:
            record = None
        return {
          'voceros': record,
          'organizacion_social': record.fk_org_social if record else None,
        }

    def forms_valid(self, forms, **kwargs):
        """
        Valida el formulario de registro del perfil de usuario
        @return: Dirige con un mensaje de exito a el home
        """
        nueva_organizacion = forms['organizacion_social'].save()
        nuevos_voceros = self.form_classes['voceros'](self.request.POST, instance=nueva_organizacion)
        if nuevos_voceros.is_valid():
            nuevos_voceros.save()
        messages.success(self.request, "El Usuario %s registro con exito la \
                                        Organizacion Social %s"
                                         % (str(self.request.user), str(nueva_organizacion.nombre)))
        return redirect(self.success_url)

    def forms_invalid(self, forms, **kwargs):
        messages.error(self.request, "%s" % (str(forms['organizacion_social'].errors.as_data())))

        return super(RegisterOrgView, self).forms_invalid(forms)


class ListOrgView(LoginRequeridoPerAuth, TemplateView):
    """!
    Listar organizaciones de la plataforma por los Administradores

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 30-05-2017
    @version 1.0.0
    """
    template_name = "organizacion.register.html"
    model = OrganizacionSocial
    success_url = reverse_lazy('organizaciones:registrar_organizacion')
    group_required = [u"Administradores"]

    def __init__(self):
        super(ListOrgView, self).__init__()

    def post(self, *args, **kwargs):
        '''
        Cambia el estado activo a el usuario
        @return: Dirige a la tabla que muestra los usuarios de la apliacion
        '''
        accion = self.request.POST
        activar = accion.get('activar', None)
        inactivar = accion.get('inactivar', None)
        estado = False

        if activar is not None:
            org = activar
            estado = True
        elif inactivar is not None:
            org = inactivar
            estado = False
        else:
            messages.error(self.request, "Esta intentando hacer \
                                          una acción incorrecta")
        try:
            org_act = self.model.objects.get(pk=org)
            org_act.activa = estado
            org_act.save()
            if estado:
                messages.success(self.request, "Se ha activado \
                                                la organizacion: %s\
                                                " % (str(org_act)))
            else:
                messages.warning(self.request, "Se ha inactivado \
                                                la organizacion: %s\
                                                " % (str(org_act)))
        except:
            messages.info(self.request, "La organizacion social no existe")
        return redirect(self.success_url)

class ListOrgVocView(LoginRequeridoPerAuth, TemplateView):
    """!
    Listar organizaciones de la plataforma

    @author Ing. Leonel P. Hernandez M. (lhernandez at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 30-05-2017
    @version 1.0.0
    """
    template_name = "organizaciones.list.html"
    model = OrganizacionSocial
    success_url = reverse_lazy('organizaciones:listar_organizacion')
    group_required = [u"Administradores", u"Voceros"]

    def __init__(self):
        super(ListOrgVocView, self).__init__()

    def post(self, *args, **kwargs):
        '''
        Cambia el estado activo a el usuario
        @return: Dirige a la tabla que muestra los usuarios de la apliacion
        '''
        accion = self.request.POST
        activar = accion.get('activar', None)
        inactivar = accion.get('inactivar', None)
        estado = False

        if activar is not None:
            org = activar
            estado = True
        elif inactivar is not None:
            org = inactivar
            estado = False
        else:
            messages.error(self.request, "Esta intentando hacer \
                                          una acción incorrecta")
        try:
            org_act = self.model.objects.get(pk=org)
            org_act.activa = estado
            org_act.save()
            if estado:
                messages.success(self.request, "Se ha activado \
                                                la organizacion: %s\
                                                " % (str(org_act)))
            else:
                messages.warning(self.request, "Se ha inactivado \
                                                la organizacion: %s\
                                                " % (str(org_act)))
        except:
            messages.info(self.request, "La organizacion social no existe")
        return redirect(self.success_url)

class ModificarOrg(LoginRequeridoPerAuth, MultiModelFormView):
    """!
    Construye el modals para la actualizacion de la Organización

    @author Ing. Lully Troconis (ltroconis at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 31-01-2018
    @version 1.0.0
    """

    model = OrganizacionSocial
    form_classes = {
      'organizaciones' : FormularioRegisterOrgSocial,
    }
    template_name = 'organizaciones.modificar.org.html'
    success_url = reverse_lazy('organizaciones:listar_org')
    group_required = [u"Administradores", u"Voceros"]
    record_id = None

    def get_context_data(self, **kwargs):
        """
        Carga el formulario en la vista, para registrar usuarios
        @return: El contexto con los objectos para la vista
        """
        context = super(ModificarOrg, self).get_context_data(**kwargs)
        self.record_id = self.kwargs.get('pk', None)
        if self.record_id is not None:
            try:
                organizacion = OrganizacionSocial.objects.get(pk=self.record_id)
                self.form_classes['organizaciones'](instance=organizacion)
            except:
                organizacion = organizacion

        context['upOrg'] = organizacion
        return context

    def get_objects(self, **kwargs):
        """
        Carga el formulario en la vista,para actualizar el perfil del  usuario
        @return: El contexto con los objectos para la vista
        """
        self.record_id = self.kwargs.get('pk', None)
        try:
            record = self.model.objects.select_related().get(pk=self.record_id)
        except OrganizacionSocial.DoesNotExist:
            record = record
            print (record)
        return {
            'organizaciones': record}

    def get_success_url(self):
        return reverse('organizaciones:listar_org')

    def forms_valid(self, forms, **kwargs):
        """
        Valida el formulario de registro del perfil de usuario
        @return: Dirige con un mensaje de éxito a el home
        """
        self.record_id = self.kwargs.get('pk', None)
        objeto = get_object_or_404(OrganizacionSocial, pk=self.record_id)
        print(record_id)
        if self.record_id is not None:
            messages.success(self.request, "Organización Comunal %s Actualizada con éxito\
                                           " % (str(objeto.nombre)))
        return super(ModificarOrg, self).forms_valid(forms)
