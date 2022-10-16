from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from employment.models import Vacancy

@permission_required('employment.view_vacancy')
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'employment/vacancy_list.html', {'vacancy_list': vacancies})










# Без использования декоратора
# def vacancy_list(request):
#     if not request.user.has_perm('employment.view_vacancy'):
#         raise PermissionDenied()
#     vacancies = Vacancy.objects.all()
#     return render(request, 'employment/vacancy_list.html', {'vacancy_list': vacancies})
