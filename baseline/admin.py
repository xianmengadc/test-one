    # Register your models here.
from django.contrib import admin
from .models import  Companies, CompaniesAdmin, ActivityInfo, ActivityInfoAdmin, \
    fixedAsset, fixedAssetAdmin, ProjectCount, ProjectCountAdmin, EmployeeUint, EmployeeUintAdmin, legalPerson, \
    legalPersonAdmin, nationUnit, nationUnitAdmin, privateUncommerciallyOrg, privateUncommerciallyOrgAdmin

# Register your models here.

admin.site.register(Companies, CompaniesAdmin)
admin.site.register(ActivityInfo, ActivityInfoAdmin)
admin.site.register(fixedAsset, fixedAssetAdmin)
admin.site.register(ProjectCount, ProjectCountAdmin)
admin.site.register(EmployeeUint, EmployeeUintAdmin)
admin.site.register(legalPerson, legalPersonAdmin)
admin.site.register(nationUnit, nationUnitAdmin)
admin.site.register(privateUncommerciallyOrg, privateUncommerciallyOrgAdmin)
