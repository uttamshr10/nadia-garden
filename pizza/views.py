from django.shortcuts import render
from .forms import PizzaForm

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'Thanks for ordering! Your %s %s and %s pizza is on its way!' %(filled_form.cleaned_data['size'],
              filled_form.cleaned_data['topping1'],
              filled_form.cleaned_data['topping2'])
            new_form = PizzaForm()
            context = {
                'pizzaform': new_form,
                'note': note
            }
            return render(request, 'pizza\order.html', context)
    else:
        form = PizzaForm()
        context = {
            'pizzaform': form
        }
        return render(request, 'pizza/order.html', context)
