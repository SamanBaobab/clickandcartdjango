from django.shortcuts import render

from apps.account.forms.register_forms import RegisterForm


# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        #Traitement si le formulaire est valide
        print("Formulaire validé", form.cleaned_data)
    return render(request, 'account/register.html', {
        'form': form
    })