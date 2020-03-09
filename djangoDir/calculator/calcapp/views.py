from django.shortcuts import render
from .forms import CalcForm
from cexprtk import evaluate_expression

# Create your views here.


def calc_exp(expression):

    result = evaluate_expression(expression, {})
    return result


def calc_view(request):

    result, form = calc_form(request)
    return render(request, 'calcapp/calcform.html', {'form': form, 'result': result})


def calc_form(request):

    form = CalcForm()
    result = ''
    try:
        if request.method == 'POST':
            form = CalcForm(request.POST)
            if form.is_valid():
                expression = form.cleaned_data.get('expression')
                result = calc_exp(expression)

    except Exception as e:
        result = e

    return result, form
