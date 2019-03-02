from rest_framework import permissions, exceptions
from django.urls import resolve
from accounts.models import User
class CanReadCompanyData(permissions.BasePermission):
    def has_permission(self, request, view):

        print('PERMISSION', request.user.district)

        if request.user.district == '碑林区': district = 'blq'
        if request.user.district == '南院门': district = 'nym'
        if request.user.district == '柏树林': district = 'bsl'
        if request.user.district == '长乐坊': district = 'clf'
        if request.user.district == '东关南': district = 'dgn'
        if request.user.district == '太乙路': district = 'tyl'
        if request.user.district == '文艺路': district = 'wyl'
        if request.user.district == '长安路': district = 'cal'
        if request.user.district == '张家村': district = 'zjc'
        if request.user.district == '西咸新区': district = 'xxxq'
        xinchen_perm = '南院门' in request.user.district or district == 'nym'
        perm_str = 'baseline.can_view_{}_baseline'.format(district)

        if request.user.has_perm(perm_str) and xinchen_perm: return True
        else:
            raise exceptions.PermissionDenied({"message": "you have no access to 系统"})
