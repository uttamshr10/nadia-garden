from django.shortcuts import render
from pizza import forms, models
from django.forms import formset_factory

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multiple_form = forms.MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = forms.PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = 'Thanks for ordering! Your %s %s and %s pizza is on its way!' %(filled_form.cleaned_data['size'],
              filled_form.cleaned_data['topping1'],
              filled_form.cleaned_data['topping2'])
            new_form = forms.PizzaForm()
            context = {
                'created_pizza_pk': created_pizza_pk,
                'pizzaform': new_form,
                'note': note,
                'multiple_form': multiple_form
            }
            return render(request, 'pizza/order.html', context)
    else:
        form = forms.PizzaForm()
        context = {
            'pizzaform': form,
            'multiple_form': multiple_form
        }
        return render(request, 'pizza/order.html', context)

def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = forms.MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(forms.PizzaForm, extra = number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizzas have been ordered.'
        else:
            note = 'Order was not created, please try again.'
            return render(request, 'pizza/pizzas.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/pizzas.html', {'formset': formset})

def edit_order(request, pk):
    pizza = models.Pizza.objects.get(pk = pk)
    form = forms.PizzaForm(instance = pizza)
    if request.method == 'POST':
        filled_form = forms.PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated'
            return render(request, 'pizza/edit_order.html', {'note': note, 'pizzaform': form, 'pizza': pizza})
    return render(request, 'pizza/edit_order.html', {'pizzaform': form, 'pizza': pizza})
