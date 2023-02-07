from django import forms
from .models import Actividad, Encuentro
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Field, Column, ButtonHolder, HTML

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'
        
class ActividadCreacionForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre']
    
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields["nombre"].widget.attrs["class"] = "form-control"    
        
class ActividadEdicionForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre']
    
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields["nombre"].widget.attrs["class"] = "form-control"    
        
        
class EncuentroCreacionForm(forms.ModelForm):
    fecha = forms.DateField(
        input_formats=['%d/%m/%Y'], 
        widget=forms.DateInput(format='%d/%m/%Y')
    )
    
    hora = forms.TimeField(
        input_formats=['%H:%M'], 
        widget=forms.TimeInput(format='%H:%M')
    )
    
    class Meta:
        model = Encuentro
        fields = ["descripcion", "actividad", "lugar", "fecha", "hora"]
        labels = {
            'descripcion': _('Descripción'),
        }
        
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        

        for key, value in self.fields.items():
            value.widget.attrs["class"] = "form-control"  
            
        self.fields["fecha"].widget.attrs["class"] = "datepicker form-control"   
        self.fields["hora"].widget.attrs["class"] = "timepicker form-control"   
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column(
                Field('descripcion', wrapper_class='col-md-6 col-sm-12'),
                Field('actividad', wrapper_class='col-md-6 col-sm-12'),  
            css_class='row'), 
            Column(
                Field('lugar', wrapper_class='col-md-6 col-sm-12'),
                Field('fecha', wrapper_class='col-md-6 col-sm-12'),  
            css_class='row'),
            Column(
                Field('hora', wrapper_class='col-md-6 col-sm-12'),
            css_class='row'),
            ButtonHolder(
                Submit('submit_guardar', 'Guardar', css_class='btn btn-primary'),
                HTML('<button name="submit_cancelar" formnovalidate  class="btn btn-secondary">Cancelar</button>')
            )
        )