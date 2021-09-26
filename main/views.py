from django.shortcuts import render
from .models import Table
from django.core.paginator import Paginator
from .forms import FilterForm
from django.contrib import messages


def index(request):
     '''Главная страница с формами фильтрации и пагинацией'''
     all_table_rows = Table.objects.all()
     paginator = Paginator(all_table_rows, 3)
     filter_form = FilterForm(request.POST)
     if 'page' in request.GET:
         page_num = request.GET['page']
     else:
         page_num = 1
     page = paginator.get_page(page_num)
     context = {'page': page, 'page_rows': page.object_list, 'filter_form': filter_form}
     return render(request, 'main/index.html', context)


def about(request):
    '''Информация о проекте'''
    return render(request, 'main/about.html')


def filter_methods(request):
    '''Обновление главной страницы с результатами фильтрации'''
    fitering_data = Table.objects.all()
    filter_form = FilterForm()
    if request.method == 'GET':
        if 'column_name' in request.GET:
            filter_form = FilterForm(request.GET)
            column_name = filter_form.data['column_name']
            filter_method = filter_form.data['filter_method']
            value = filter_form.data['value']
            if filter_method == "Больше":
                if column_name == 'Количество':
                    fitering_data = fitering_data.filter(quantity__gt=value)
                elif column_name == 'расстояние':
                    fitering_data = fitering_data.filter(distance__gt=value)
            if filter_method == "Меньше":
                if column_name == 'Количество':
                    fitering_data = fitering_data.filter(quantity__lt=value)
                elif column_name == 'расстояние':
                    fitering_data = fitering_data.filter(distance__lt=value)
            if filter_method == "Равно":
                if column_name == 'Количество':
                    fitering_data = fitering_data.filter(quantity=value)
                elif column_name == 'расстояние':
                    fitering_data = fitering_data.filter(distance=value)
                elif column_name == 'Название':
                    fitering_data = fitering_data.filter(title=value)
            if filter_method == "Содержит":
                if column_name == 'Название':
                    fitering_data = fitering_data.filter(title__icontains=value)
            messages.add_message(request, messages.SUCCESS, 'Объявление добавлено')
            filter_form = FilterForm(
                initial={'column_name': column_name, 'filter_method': filter_method, 'value': value})
        paginator = Paginator(fitering_data, 3)
        if 'page' in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        context = {'page': page, 'page_rows': page.object_list, 'filter_form': filter_form}
        return render(request, 'main/index.html', context)
