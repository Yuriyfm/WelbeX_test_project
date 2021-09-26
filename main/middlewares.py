"""в данном файле хранятся обработчики контекста. по принятым
в Django соглашениям, весь код, "ответственный" за формирование страниц, следует
помещать в шаблон, посредник или обработчик контекста."""

from .models import Table


def filter_context_processor(request):
    '''Промежуточная фунция, которая корректирует URL при переходе по страницам пагинации с примененными фильтрами'''
    context = {}
    context['all'] = ''
    if 'column_name' in request.GET:
        column_name = request.GET['column_name']
        context['column_name'] = '?column_name=' + column_name
        context['all'] += context['column_name']
        filter_method = request.GET['filter_method']
        context['filter_method'] = '&filter_method=' + filter_method
        context['all'] += context['filter_method']
        value = request.GET['value']
        context['value'] = '&value=' + value
        context['all'] += context['value']
        if 'page' in request.GET:
            page = request.GET['page']
            context['page'] = '&page=' + page
            context['all'] += context['page']
    else:
        if 'page' in request.GET:
            page = request.GET['page']
            context['all'] += '?page=' + page
    return context
