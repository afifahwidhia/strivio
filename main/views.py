from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406402662',
        'name': 'Afifah Widhia Rahayu',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
