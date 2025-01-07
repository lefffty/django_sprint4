from django.shortcuts import render


def page_not_found(request, exception):
    """Обработка ошибки 404"""
    return render(
        request,
        'pages/404.html',
        status=404,
    )


def csrf_failure(request, reason=''):
    """Обработка ошибки 403 CSRF"""
    return render(
        request,
        'pages/403csrf.html',
        status=403
    )


def tr_handler500(request):
    """Обработка ошибки 500"""
    return render(
        request,
        template_name='pages/500.html',
        status=500
    )
