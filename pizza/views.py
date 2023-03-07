from django.shortcuts import render
from pizza import forms

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    if request.method == 'POST':
        filled_form = forms.PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'Thanks for ordering! Your %s %s and %s pizza is on its way!' %(filled_form.cleaned_data['size'],
              filled_form.cleaned_data['topping1'],
              filled_form.cleaned_data['topping2'])
            new_form = forms.PizzaForm()
            context = {
                'pizzaform': new_form,
                'note': note
            }
            return render(request, 'pizza/order.html', context)
    else:
        form = forms.PizzaForm()
        context = {
            'pizzaform': form
        }
        return render(request, 'pizza/order.html', context)
