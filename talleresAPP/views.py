from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from . import models, forms
# Create your views here.

def login(request):
    return render(request, 'pages/login.html')

class registroAdulto(SessionWizardView):
    template_name = 'pages/register.html'
    form_list = [forms.regisAdulto1, forms.regisAdulto2, forms.regisAdulto3]

    def done(self, form_list, **kwargs):
        # Aquí puedes procesar los datos de los formularios
        form_data = [form.cleaned_data for form in form_list]
        return render(self.request, 'done.html', {
            'form_data': form_data,
        })

def index(request):
    #se hace una consulta a talleres con un join a instructor
    lisTalleres = models.Taller.objects.select_related('instructor').all()
    return render(request, 'pages/index.html', {'talleres': lisTalleres})

def talleres(request): 
    #se hace una consulta a talleres con un join a instructor,sala y municipalidad
    lisTalleres = models.Taller.objects.select_related('instructor','sala','municipalidad').all()
    return render(request, 'pages/talleres.html',{'talleres': lisTalleres})