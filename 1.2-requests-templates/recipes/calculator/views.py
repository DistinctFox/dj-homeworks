from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def calculator(request: HttpRequest) -> HttpResponse:
    dish_name = request.path.strip('/')
    servings = int(request.GET.get('servings', default=0))
    recipe = DATA[dish_name]

    if servings > 0:
        for k, v in recipe.items():
            recipe[k] = v*servings

    context = {
        'recipe': recipe
    }

    print(context)
    return render(request, 'calculator/index.html', context)
