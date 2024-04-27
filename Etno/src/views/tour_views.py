from django.shortcuts import render, redirect
from src.models import tour_models,application_models
from src import forms



def main_info():
    return """Туристический сайт ЭТНО. Дагестан, республика на северо-востоке Кавказа, расположенная на территории Северного Кавказа и Северо-Восточного Казахстана.
Дагестана – это республика, которая на протяжении многих лет привлекает к себе внимание туристов со всего мира.
Здесь есть на что посмотреть, например, исторические места, природные достопримечательности, музеи, памятники архитектуры, а также горные и морские курорты.
Так что, если вы любите активный отдых, то тур в Дагестан, это то, что вам нужно."""


def gallery(request):
    context = dict()
    context['about_info'] = main_info()
    context['imgs'] = tour_models.Image.objects.all()
    return render(request, 'tour/gallery.html', context=context)


def main_page(request):
    context = dict()
    context['about_info'] = main_info()
    context['tours'] = tour_models.Tour.objects.all()
    context['attractions'] = tour_models.Attraction.objects.all()
    return render(request, 'tour/index.html', context=context)


def tour(request, id):
    context = dict()
    context['tour'] = tour_models.Tour.objects.get(pk=id)
    context['tour_imgs'] = tour_models.Image.objects.filter(tour_id_id=id)[:6]
    context['tour_attractions'] = tour_models.Attraction.objects.filter(tour_id_id=id)
    context['form'] = forms.GetEmailForm()

    return render(request, 'tour/tour.html', context=context)


def about(request):
    context = dict()
    context['about_info'] = main_info()
    context['tours'] = tour_models.Tour.objects.all().count()
    context['attractions'] = tour_models.Attraction.objects.all().count()
    return render(request, 'tour/about.html', context=context)


