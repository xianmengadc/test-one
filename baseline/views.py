# Create your views here.
from django.shortcuts import render, redirect
from django_filters import rest_framework as filters
from django.db import connection
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework_datatables.filters import DatatablesFilterBackend
from rest_framework import viewsets, permissions
from baseline.permissions import CanReadCompanyData
from rest_framework.decorators import api_view, detail_route
from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory, modelformset_factory
from django.contrib.auth import get_user_model
from .models import User, Companies, ActivityInfo, EmployeeUint, legalPerson, fixedAsset, ProjectCount, nationUnit, \
    privateUncommerciallyOrg
from .serializers import CompaniesSerializer, ActivityInfoSerializer, EmployeeUintSerializer, legalPersonSerializer, \
    fixedAssetSerializer, nationUnitSerializer, privateUncommerciallyOrgSerializer
import re
from django.utils import timezone


class CompaniesViewset(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    filter_backends = (filters.DjangoFilterBackend, DatatablesFilterBackend)
    filterset_fields = '__all__'
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, CanReadCompanyData,)


# 611主表单位基本情况
class CompaniesForm(forms.ModelForm):
    # A项非必填
    industry_code = forms.CharField(required=False)
    profess_category = forms.CharField(required=False)
    legal_unite_company_size = forms.CharField(required=False)
    legal_unite_obtainemploy = forms.CharField(required=False)
    legal_unite_person_income = forms.CharField(required=False)
    legal_unite_person_assets = forms.CharField(required=False)

    social_num = forms.CharField(required=False)
    org_num = forms.CharField(required=False)
    landline_branch_num = forms.CharField(required=False)
    mobile = forms.CharField(required=False)
    fax_code = forms.CharField(required=False)
    fax_branch_code = forms.CharField(required=False)
    postalcode = forms.CharField(required=False)
    email = forms.CharField(required=False)
    website = forms.CharField(required=False)
    register_province = forms.CharField(required=False)
    register_city = forms.CharField(required=False)
    register_district = forms.CharField(required=False)
    register_address = forms.CharField(required=False)
    register_community = forms.CharField(required=False)
    operate_status = forms.CharField(required=False)
    # B项非必填
    retail_management_form = forms.CharField(required=False)
    retail_management_brand = forms.CharField(required=False)
    retail_opetrate_type = forms.CharField(required=False)
    retail_business_area = forms.CharField(required=False)
    retail_hotel_diet_star = forms.CharField(required=False)
    retail_hotel_diet_area = forms.CharField(required=False)
    # C项
    legal_unite_hkmatai = forms.CharField(required=False)
    legal_unite_hypotaxis = forms.CharField(required=False)
    legal_unite_stake = forms.CharField(required=False)
    accounting_rule = forms.CharField(required=False)
    legal_unite_accounting_standard = forms.CharField(required=False)
    is_higher_legal = forms.CharField(required=False)
    legal_unite_social_num = forms.CharField(required=False)
    legal_unite_org_num = forms.CharField(required=False)
    legal_unite_name = forms.CharField(required=False)
    has_branch = forms.CharField(required=False)
    # D项
    parent_type = forms.CharField(required=False)
    parent_comp_social_num = forms.CharField(required=False)
    parent_comp_org_num = forms.CharField(required=False)
    parent_comp_name = forms.CharField(required=False)
    parent_comp_address = forms.CharField(required=False)
    branch_comp_count_obtainemploy = forms.CharField(required=False)
    branch_comp_count_obtainemploy_female = forms.CharField(required=False)
    branch_comp_operate_income = forms.CharField(required=False)
    branch_comp_nooperate_defray = forms.CharField(required=False)
    branch_comp_house_sale_area = forms.CharField(required=False)
    branch_comp_house_nosale_area = forms.CharField(required=False)

    class Meta:
        model = Companies
        fields = '__all__'

    def clean(self):
        #  A 法人单位和产业活动单位基本情况
        # 专业类别
        profess_category = self.cleaned_data.get('profess_category')
        # 单位类型
        comp_type = self.cleaned_data.get('comp_type')
        # 统一社会信用代码
        social_num = self.cleaned_data.get('social_num')
        # 组织机构代码
        org_num = self.cleaned_data.get('org_num')
        # 单位详细名称
        name = self.cleaned_data.get('name')
        # 开业（成立）时间--年
        est_year = self.cleaned_data.get('est_year')
        # 开业（成立）时间--月
        est_month = self.cleaned_data.get('est_month')
        # 手机号
        mobile = self.cleaned_data.get('mobile')
        # 长途区号
        landline_area_code = self.cleaned_data.get('landline_area_code')
        # 固定电话
        landline_num = self.cleaned_data.get('landline_num')
        # 传真号码
        fax_code = self.cleaned_data.get('fax_code')
        # 邮政编码
        postalcode = self.cleaned_data.get('postalcode')
        # 单位所在地--省
        province = self.cleaned_data.get('province')
        # 单位所在地--城市
        city = self.cleaned_data.get('city')
        # 单位所在地--区
        district = self.cleaned_data.get('district')
        # 街（村）,门牌号--地址
        address = self.cleaned_data.get('address')
        # 街道办事处
        street_district = self.cleaned_data.get('street_district')
        # 单位注册地--省
        register_province = self.cleaned_data.get('register_province')
        # 单位注册地--城市
        register_city = self.cleaned_data.get('register_city')
        # 单位注册地--区
        register_district = self.cleaned_data.get('register_district')
        # 单位注册地--地址
        register_address = self.cleaned_data.get('register_address')
        # 单位注册地--街道办事处
        register_street_district = self.cleaned_data.get('register_street_district')
        # 运营状态
        operate_status = self.cleaned_data.get('operate_status')
        # 主要业务活动
        main_activity_1 = self.cleaned_data.get('main_activity_1')
        # 机构类型
        org_type = self.cleaned_data.get('org_type')
        # 登记注册类型
        register_type = self.cleaned_data.get('register_type')
        # 是否为批发、零售、住宿或者餐饮法人或产业活动单位
        is_piling = self.cleaned_data.get('is_piling')

        # B 批零住餐和产业活动单位
        # 批发和零售业、住宿和餐饮业单位经营形式
        retail_management_form = self.cleaned_data.get('retail_management_form')
        # 连锁品牌（商标或者商号名称）
        retail_management_brand = self.cleaned_data.get('retail_management_brand')
        # 零售状业(最多选择三个)
        retail_opetrate_type = self.cleaned_data.get('retail_opetrate_type')
        # 批发和零售业年末零售营业面积
        retail_business_area = self.cleaned_data.get('retail_business_area')
        # 住宿业单位星级评定
        retail_hotel_diet_star = self.cleaned_data.get('retail_hotel_diet_star')
        # 住宿和餐饮业年末零售营业面积
        retail_hotel_diet_area = self.cleaned_data.get('retail_hotel_diet_area')

        # C 法人单位
        # 港澳台投资情况
        legal_unite_hkmatai = self.cleaned_data.get('legal_unite_hkmatai')
        # 隶属关系
        legal_unite_hypotaxis = self.cleaned_data.get('legal_unite_hypotaxis')
        # 企业控股情况
        legal_unite_stake = self.cleaned_data.get('legal_unite_stake')
        # 执行会计标准类别
        accounting_rule = self.cleaned_data.get('accounting_rule')
        # 执行企业会计准则
        legal_unite_accounting_standard = self.cleaned_data.get('legal_unite_accounting_standard')
        # 本法人单位是否有上一级法人
        is_higher_legal = self.cleaned_data.get('is_higher_legal')
        # 上一级法人统一社会信用代码或者
        legal_unite_social_num = self.cleaned_data.get('legal_unite_social_num')
        # 上一级法人组织机构代码
        legal_unite_org_num = self.cleaned_data.get('legal_unite_org_num')
        # 上一级法人单位详细名称
        legal_unite_name = self.cleaned_data.get('legal_unite_name')
        # 是否有下属产业活动单位
        has_branch = self.cleaned_data.get('has_branch')

        # D 产业活动单位归属法人单位情况
        # 归属法人单位-单位类别
        parent_type = self.cleaned_data.get('parent_type')
        # 归属法人单位-统一社会信用代码
        parent_comp_social_num = self.cleaned_data.get('parent_comp_social_num')
        # 归属法人单位-组织机构代码
        parent_comp_org_num = self.cleaned_data.get('parent_comp_org_num')
        # 归属法人单位-详细名称
        parent_comp_name = self.cleaned_data.get('parent_comp_name')
        # 归属法人单位-详细地址
        parent_comp_address = self.cleaned_data.get('parent_comp_address')
        # 从业人员期末人数
        branch_comp_count_obtainemploy = self.cleaned_data.get('branch_comp_count_obtainemploy')
        # 从业人员人数(女性)
        branch_comp_count_obtainemploy_female = self.cleaned_data.get('branch_comp_count_obtainemploy_female')
        # 经营性单位收入
        branch_comp_operate_income = self.cleaned_data.get('branch_comp_operate_income')
        # 非经营性支出
        branch_comp_nooperate_defray = self.cleaned_data.get('branch_comp_nooperate_defray')
        # 商品房待销售面积
        branch_comp_house_nosale_area = self.cleaned_data.get('branch_comp_house_nosale_area')
        # 商品房销售面积
        branch_comp_house_sale_area = self.cleaned_data.get('branch_comp_house_sale_area')
        # 申报人
        interviewee = self.cleaned_data.get('interviewee')
        # 申报人联系电话
        interviewee_contact = self.cleaned_data.get('interviewee_contact')

        # 统一社会信用代码或组织机构代码不能同时为空
        if not social_num and not org_num:
            raise ValidationError('您的A项109项(统一社会信用代码或组织机构代码)二选一必填,若无请填0')
        if social_num:
            if len(social_num) != 18:
                raise ValidationError('您的A项109项(统一社会信用代码)不够18位，请核对后重新填写')
        if org_num:
            if len(org_num) != 9:
                raise ValidationError('您的A项109项(组织机构代码)不够9位，请核对后重新填写')

        # 验证年份
        REGEX_YEAR_18 = "^(18[56789])[0-9]$"
        REGEX_YEAR_19 = "^(19[0-9])[0-9]$"
        REGEX_YEAR_20 = "^(20[01])[0-9]$"
        year_18 = re.compile(REGEX_YEAR_18)
        year_19 = re.compile(REGEX_YEAR_19)
        year_20 = re.compile(REGEX_YEAR_20)
        if not year_19.match(est_year) and not year_20.match(est_year) and not year_18.match(est_year):
            raise ValidationError('您的A项202项(开业成立时间-年)格式填写错误,请核对后重新填写(年份时间段在1800--2018)')
        # 验证月份
        REGEX_MONTH = "^(0)[1-9]$"
        REGEX_MONTH_BIG = "^(1)[012]$"
        month = re.compile(REGEX_MONTH)
        month_big = re.compile(REGEX_MONTH_BIG)
        if not month.match(est_month) and not month_big.match(est_month):
            raise ValidationError('您的A项202项(开业成立时间-月)格式填写错误,请核对后重新填写(eg:9月份请填09，不要填9)')

        # 长途区号
        if landline_area_code:
            AREA_CODE_3 = "^[0-9]{3}$"
            AREA_CODE_4 = "^[0-9]{4}$"
            AREA_CODE_5 = "^[0-9]{5}$"
            area_code_3 = re.compile(AREA_CODE_3)
            area_code_4 = re.compile(AREA_CODE_4)
            area_code_5 = re.compile(AREA_CODE_5)
            if not area_code_3.match(landline_area_code) and not area_code_4.match(
                    landline_area_code) and not area_code_5.match(landline_area_code):
                raise ValidationError('您的A项203项(长途区号)格式错误,请核对后重新填写')

        # 固定电话或传真已填写，请填写长途区号
        if (landline_num or fax_code) and not landline_area_code:
            raise ValidationError('您的A项203项(固定电话)或203项(传真)已填写，请填写203项(长途区号)')

        # 固定电话格式不正确
        if landline_num:
            if len(landline_num) != 8:
                raise ValidationError('您的A项203项(固定电话)格式错误，请勿填写移动电话或前面加长途区号，请核对后重新填写')

        # 传真号码格式不正确
        if fax_code:
            if len(fax_code) != 8:
                raise ValidationError('您的A项203项(传真)格式错误，请勿填写移动电话或前面加长途区号，请核对后重新填写')

        # 验证手机号
        if mobile:
            REGEX_MOBILE = "^(13[0-9]|14[57]|15[012356789]|16[0123456789]|17[0-9]|18[0-9]|19[0123456789])[0-9]{8}$"
            shouji = re.compile(REGEX_MOBILE)
            if not shouji.match(mobile):
                raise ValidationError('您的A项203项请填写手机号码，或手机号码格式错误')

        # 验证邮政编码
        if postalcode:
            POST_CODE = "^[0-9]{6}"
            post = re.compile(POST_CODE)
            if not post.match(postalcode):
                raise ValidationError('您的A项的203项(邮政编码)没有填写或格式不正确，请核对后重新填写')

        # 单位所在地
        if not province or not city or not district or not address or not street_district:
            raise ValidationError('您的105项单位所在地不能为空,请填写省或市或街(村)门牌号或街道办事处或街道办事处')

        if operate_status != '6':
            # 验证主要业务活动
            if not main_activity_1:
                raise ValidationError("您的A项103项(主要业务活动)没有填写，请询问后填写")

            # 单位注册地
            if '装修' in main_activity_1 or '建筑' in main_activity_1 or (profess_category == 'C'):
                if not register_province or not register_city or not register_district or not register_address or not register_street_district:
                    raise ValidationError("您所在的行业是建筑业,您的A项106项(单位注册地信息)没有填写,请详细填写您的单位注册地信息")

            # 机构类型
            if not org_type:
                raise ValidationError('您的A项211项(机构类型)不能为空,请选择好您的机构类型')
            # 登记注册类型
            if not register_type:
                raise ValidationError('您的A项205项(登记注册类型)不能为空,请选择好您的登记注册类型')

            # A项205项和211项不匹配
            if register_type:
                if (register_type != '190') and (org_type == '53' or org_type == '54' or org_type == '55'):
                    raise ValidationError('您的A项205项(登记注册类型)与211项(机构类型)不匹配,请核对后重新填写')
                if register_type != '110' and org_type == '30' :
                    raise ValidationError('您的A项205项(登记注册类型)与211项(机构类型)不匹配,请核对后重新填写')

            # 是否批零住餐单位未勾选
            if not is_piling:
                raise ValidationError('贵单位是否为批零住餐单位或产业活动单位未勾选')

            # B项是否要填
            # 是否是批零单位或住餐单位
            if is_piling == '1':
                if not retail_management_form and profess_category == 'E':
                    raise ValidationError("贵单位是批零住餐单位，请填写B项ES1项的单位经营形式")
                else:
                    if (retail_management_form == '2' or retail_management_form == '3' or retail_management_form == '4') and not retail_management_brand:
                        raise ValidationError("贵单位的ES1的单位形式选择是2或3或4，请填写ES1项的连锁品牌")
                if (retail_opetrate_type or retail_business_area) and (retail_hotel_diet_star or retail_hotel_diet_area):
                    raise ValidationError("请确定您是批零单位还是住餐单位，不能同时为批零单位和住餐单位，请核对后重新填写")

                if retail_opetrate_type and retail_business_area:
                    if ('1050' in retail_opetrate_type) and (int(retail_business_area) < 6001):
                        raise ValidationError("贵单位E02项零售业态选择的是1050大型超市，请填写E03项营业面积应该大于等于6000平方米,请根据实际情况重新选择E02项或填写面积")
                    if ('1040' in retail_opetrate_type) and (int(retail_business_area) > 6001):
                        raise ValidationError("贵单位E02项零售业态选择的是1040超市，请填写E03项营业面积应该小于等于6000平方米,请根据实际情况重新选择E02项或填写面积")
                    if int(retail_business_area) < 0:
                        raise ValidationError("贵单位为批零单位，请填写E03项营业面积应该大于等于0(没有零售业务的批发单位此项应填0),请核实后修改")
                # if '批发' in main_activity_1 and (not retail_opetrate_type or not retail_business_area):
                #     raise ValidationError("贵单位是批零单位，请填写E02项和E03项")

                if profess_category:
                    # 住餐单位
                    if profess_category == 'S':
                        if not retail_hotel_diet_star and not retail_hotel_diet_area:
                            raise ValidationError("贵单位是住餐单位，请填写S02项或S03项")
                        if int(retail_hotel_diet_area) < 0 :
                            raise ValidationError("贵单位为住餐单位，S03年末餐饮营业面积应大于等于0，请核实后修改")
                    #  批零单位
                    # if profess_category == 'E':
                    #     if not retail_opetrate_type and not retail_business_area:
                    #         raise ValidationError("贵单位是批零单位，请填写E02项和E03项")

            # C项是否要填
            if comp_type == '1':
                if (register_type == '210' or register_type == '220' or register_type == '230' or register_type == '240' or register_type == '290') and not legal_unite_hkmatai:
                    raise ValidationError("贵单位的205项(登记注册类型是港澳台商投资)，C项216项(港澳台商投资情况)必填，请选择")
                if (register_type == '110' or register_type == '120' or register_type == '130' or register_type == '141' or
                    register_type == '142' or register_type == '143' or register_type == '149' or register_type == '151' or
                    register_type == '159' or register_type == '160' or register_type == '171' or register_type == '172' or
                    register_type == '173' or register_type == '174' or register_type == '190' or register_type == '310' or
                    register_type == '320' or register_type == '330' or register_type == '340' or register_type == '390')  and legal_unite_hkmatai:
                    raise ValidationError("贵单位的205项(登记注册类型是非港澳台商投资)，C项216项(港澳台商投资情况)非必填，请检查")

                if legal_unite_stake != '3' and (
                        register_type == '172' or register_type == '173' or register_type == '174'):
                    raise ValidationError("贵单位是私营企业，C项206项(企业控股情况)只能选3(私人控股)")
                # if legal_unite_hypotaxis != '90' and org_type == '10':
                #     raise ValidationError("贵单位的211项(机构类型)选择的是企业，您在207项(隶属关系)只能选择90(其他)")

                # 当211项机构类型选择10企业的时候，206项企业控股情况必填
                if org_type == '10' and not legal_unite_stake:
                    raise ValidationError("您的211项机构类型选择的是10企业，C项的206项企业控股情况必填，请检查")

                if not legal_unite_hypotaxis:
                    raise ValidationError("C项隶属关系不能为空,请填写")
                # if not legal_unite_stake:
                #     raise ValidationError("C项企业控股情况不能为空,请填写")
                if not accounting_rule:
                    raise ValidationError("C项执行会计标准类别不能为空,请填写")
                if accounting_rule != '1' and not legal_unite_accounting_standard:
                    raise ValidationError("C项执行会计标准类别不是1(企业会计标准制度),请不要填写210项(执行企业会计准则情况)")
                if accounting_rule == '1':
                    if org_type != '10' and org_type != '20' and org_type != '51':
                        raise ValidationError("您的209项(执行会计标准类别)选择的是1(企业会计制度)，与您的211项(机构类型)不匹配，请修改后重新提交")
                if accounting_rule == '2':
                    if org_type != '20' and org_type != '10':
                        raise ValidationError("您的209项(执行会计标准类别)选择的是2(事业单位会计制度)，与您的211项(机构类型)不匹配，请修改后重新提交")
                if accounting_rule == '3':
                    if org_type != '30':
                        raise ValidationError("您的209项(执行会计标准类别)选择的是3(行政单位会计制度)，与您的211项(机构类型)不匹配，请修改后重新提交")
                if not legal_unite_accounting_standard:
                    raise ValidationError("C项执行企业会计准则情况不能为空,请填写")
                if is_higher_legal == '1':
                    if not legal_unite_social_num and not legal_unite_org_num:
                        raise ValidationError("C项上一级法人统一社会信用代码或组织机构代码不能为空,请填写")
                    if legal_unite_social_num == social_num:
                        raise ValidationError("C项上一级法人统一社会信用代码不能与109本法人代码相同,请核对后重新填写")
                    if legal_unite_org_num and social_num:
                        if legal_unite_org_num == social_num:
                            raise ValidationError("C项上一级法人组织机构代码不能与109本法人代码相同,请核对后重新填写")
                if not has_branch:
                    raise ValidationError("C项本法人单位是否有下属产业活动单位不能为空,请填写")

            # D项是否要填
            if comp_type == '2':
                if not parent_type:
                    raise ValidationError("D项182项产业活动单位归属法人单位,单位类别为必填项,请选择您的单位类别")
                else:
                    if parent_type and parent_type != '2':
                        raise ValidationError("D项182项中的单位类别，请选择2(法人单位分支机构)")
                if not parent_comp_social_num and not parent_comp_org_num:
                    raise ValidationError("D项法人单位统一社会信用代码或组织机构代码不得为空,请确认后填写")
                if parent_comp_social_num == social_num:
                    raise ValidationError("D项182项法人单位统一社会信用代码不能与109项统一社会信用代码相同,请确认后填写")
                if parent_comp_org_num and org_num:
                    if parent_comp_org_num == org_num:
                        raise ValidationError("D项182项法人单位统组织机构代码不能与109项组织机构代码相同,请确认后填写")
                if not parent_comp_name or not parent_comp_address:
                    raise ValidationError("D项法人单位详细名称或详细地址不得为空,请填写后重新提交")
                if parent_comp_name == name:
                    raise ValidationError("D项法人单位详细名称不能与本单位详细名称相同,请核对后重新提交")

                if branch_comp_count_obtainemploy:
                    if int(branch_comp_count_obtainemploy) < 0:
                        raise ValidationError("D项198项(从业人员人数)必须大于0")
                else:
                    raise ValidationError("D项198项(从业人员人数)必须填写")

                if branch_comp_count_obtainemploy_female:
                    if int(branch_comp_count_obtainemploy_female) < 0:
                        raise ValidationError("D项198项(从业人员人数(女性))必须大于0")
                else:
                    raise ValidationError("D项198项(从业人员人数(女性))必须填写")

                # if branch_comp_count_obtainemploy < branch_comp_count_obtainemploy_female:
                #     raise ValidationError("D项198项从业人员期末人数必须大于其中女性人数，请核对后重新填写")

                if (branch_comp_operate_income and branch_comp_nooperate_defray) or (
                        not branch_comp_operate_income and not branch_comp_nooperate_defray):
                    raise ValidationError("D项195和196项二选一，不能两个都填写或两个都不填写")
                if branch_comp_operate_income:
                    if int(branch_comp_operate_income) < 0:
                        raise ValidationError("D项195项(经营性单位收入)必须大于0")

                if branch_comp_nooperate_defray:
                    if int(branch_comp_nooperate_defray) < 0:
                        raise ValidationError("D项196项(非经营性支出)必须大于0")

                if profess_category == 'X':
                    if not retail_hotel_diet_area:
                        if branch_comp_house_nosale_area and branch_comp_house_sale_area:
                            if int(branch_comp_house_nosale_area) < 0 or int(branch_comp_house_sale_area) < 0:
                                raise ValidationError("D项197项(本年商品房销售面积或年末待售面积)必须大于等于0")
                        else:
                            raise ValidationError("D项197项(本年商品房销售面积或年末待售面积)必须填写,没有请填0")

            # 申报人和联系电话
            if not interviewee and not interviewee_contact:
                raise ValidationError("申报人和联系电话必须填写，请核对后重新提交")


# 611-1法人单位所属产业活动单位情况
class ActivityInfoForm(forms.ModelForm):
    social_num = forms.CharField(required=False, label="统一社会信用代码")
    org_num = forms.CharField(required=False, label="组织机构代码")
    zone_num = forms.CharField(required=False, label="区划代码")
    catrgory_code = forms.CharField(required=False, label="行业代码(小类)(GT/T4754-2017)")

    class Meta:
        model = ActivityInfo
        fields = ('unit_category', 'social_num', 'org_num', 'name', 'address', 'zone_num', 'mobile',
                  'main_activity', 'catrgory_code', 'incumbency_num', 'manage_income', 'inmanage_pay')

    def clean(self):
        # 联系电话
        mobile = self.cleaned_data.get('mobile')
        # 从业人员期末人数
        incumbency_num = self.cleaned_data.get('incumbency_num')
        # 经营性单位收入
        manage_income = self.cleaned_data.get('manage_income')
        # 非经营性单位支出
        inmanage_pay = self.cleaned_data.get('inmanage_pay')

        # 验证手机号
        # if mobile:
        #     REGEX_MOBILE = "^(13[0-9]|15[012356789]|16[0-9]|17[678]|18[0-9]|14[57])[0-9]{8}$"
        #     shouji = re.compile(REGEX_MOBILE)
        #     if not shouji.match(mobile):
        #         raise ValidationError('7项(手机号码)格式错误')

        if incumbency_num:
            if incumbency_num < 0:
                raise ValidationError("10项(从业人员期末人数)必须大于0")
        if manage_income:
            if manage_income < 0:
                raise ValidationError("11项(经营性单位收入)必须大于0")
        if inmanage_pay:
            if inmanage_pay < 0:
                raise ValidationError("12项(非经营性单位支出)必须大于0")


# 611-2 单位从业人员情况
class EmployeeUintForm(forms.ModelForm):
    class Meta:
        model = EmployeeUint
        fields = (
        'main_social_num', 'final_count_human', 'final_count_female', 'graduate', 'bachelor', 'junior_college',
        'skill_count', 'technician_one', 'technician_two', 'technician_three', 'technician_four', 'technician_five')

    def clean(self):
        # 从业人员期末人数
        final_count_human = self.cleaned_data.get('final_count_human')
        # 从业人员期末人数（女性）
        final_count_female = self.cleaned_data.get('final_count_female')
        # 具有研究生学历
        graduate = self.cleaned_data.get('graduate')
        # 具有大学本科学历
        bachelor = self.cleaned_data.get('bachelor')
        # 具有大专学历
        junior_college = self.cleaned_data.get('junior_college')
        # 技能人员总数
        skill_count = self.cleaned_data.get('skill_count')
        # 具有高级技师（国家职业资格一级）
        technician_one = self.cleaned_data.get('technician_one')
        # 具有技师（国家职业资格二级）
        technician_two = self.cleaned_data.get('technician_two')
        # 具有高级技能人员（国家职业资格三级）
        technician_three = self.cleaned_data.get('technician_three')
        # 具有中级技能人员（国家职业资格四级）
        technician_four = self.cleaned_data.get('technician_four')
        # 具有初级技能人员（国家职业资格五级）
        technician_five = self.cleaned_data.get('technician_five')

        total_college = graduate + bachelor + junior_college

        # 从业人员期末人数总数不能小于其中女性人数
        if final_count_human < final_count_female:
            raise ValidationError("02项(从业人员期末人数其中女性)不能大于01项(从业人员期末总人数)")
        # 研究生学历+大学本科学历+大学专科学历总人数不能大于期末总人数
        if total_college > final_count_human:
            raise ValidationError("具有高等学历人数(03项研究生学历人员+04项大学本科学历人员+05项大学专科学历人员)不能大于01项(从业人员期末总人数)")
        if skill_count:
            total_skill = technician_one + technician_two + technician_three + technician_four + technician_five
            # 技能人员总数不能大于或等于从业人员期末人数
            if final_count_human < skill_count:
                raise ValidationError("06项(技能人员总数)不能大于或等于01项(从业人员期末人数)")
            # 技能人员总数应该等于 具有高级技师，具有技师，具有高级技能人员，具有中级技能人员，具有初级技能人员
            if total_skill != skill_count:
                raise ValidationError("各级技能人员总数(07项高级技师+08项技师+09项高级技能人员+10项中级技能人员+11项初级技能人员)不等于06项(技能人员总数)，请核对后重新填写")


# 611-3表企业法人主要经济指标
class legalPersonForm(forms.ModelForm):
    piling_product_cost = forms.CharField(required=False)
    piling_product_sale = forms.CharField(required=False)
    piling_product_online_sale = forms.CharField(required=False)
    piling_product_offline_sale = forms.CharField(required=False)
    piling_product_stock = forms.CharField(required=False)
    piling_operate_turnover = forms.CharField(required=False)
    explain = forms.CharField(required=False)
    staff_wages_explain = forms.CharField(required=False)

    catering_turnover = forms.CharField(required=False)
    catering_turnover_online = forms.CharField(required=False)
    catering_guest_room = forms.CharField(required=False)
    catering_meals = forms.CharField(required=False)

    class Meta:
        model = legalPerson
        fields = (
        'added_tax_value', 'asset_all', 'business_cost', 'business_income', 'business_profit', 'business_tax_more',
        'catering_guest_room', 'catering_meals', 'catering_turnover', 'catering_turnover_online', 'debt_all',
        'depreciation', 'doing_project', 'early_inventory', 'end_inventory', 'fixed_asset_value', 'invest_income',
        'piling_operate_turnover', 'piling_product_cost', 'piling_product_offline_sale', 'piling_product_online_sale',
        'piling_product_sale', 'piling_product_stock', 'staff_wages')

    def clean(self):
        # 是否是批零主餐单位
        is_plzc_write = self.data['is_plzc_write']
        # 固定资产净值
        fixed_asset_value = self.cleaned_data.get('fixed_asset_value')
        # 在建工程
        doing_project = self.cleaned_data.get('doing_project')
        # 资产合计
        asset_all = self.data['asset_all']
        # 期末存货
        end_inventory = self.cleaned_data.get('end_inventory')
        # 负债合计
        debt_all = self.data['debt_all']
        # 营业收入
        business_income = self.data['business_income']
        # 营业利润
        business_profit = self.data['business_profit']
        # 营业成本
        business_cost = self.data['business_cost']
        # 商品购进额为0时的解释说明
        explain = self.cleaned_data.get('explain')
        # 应付职工薪酬为0或人均值小于1w时填报
        staff_wages_explain = self.cleaned_data.get('staff_wages_explain')
        # 应交增值税应该大于0
        added_tax_value = self.cleaned_data.get('added_tax_value')

        # 批零业（True）  住餐业（False）
        is_piling = self.data['is_piling']
        # 商品购进额(批零业)
        piling_product_cost = self.cleaned_data.get('piling_product_cost')
        # 期末商品库存额（批零业）
        piling_product_stock = self.cleaned_data.get('piling_product_stock')
        # 服务营业额(批零业)
        piling_operate_turnover = self.cleaned_data.get('piling_operate_turnover')
        # 商品销售额（批发和零售业）
        piling_product_sale = self.cleaned_data.get('piling_product_sale')
        # 其中：通过公共网络实现的商品销售额（批发和零售业）
        piling_product_online_sale = self.cleaned_data.get('piling_product_online_sale')
        # 其中：零售额（批发和零售业）
        piling_product_offline_sale = self.cleaned_data.get('piling_product_offline_sale')

        # 营业额(住宿和餐饮业)
        catering_turnover = self.cleaned_data.get('catering_turnover')
        # 其中：通过公共网络实现的营业额(住宿和餐饮业)
        catering_turnover_online = self.cleaned_data.get('catering_turnover_online')
        # 其中：客房收入(住宿和餐饮业)
        catering_guest_room = self.cleaned_data.get('catering_guest_room')
        # 餐费收入(住宿和餐饮业)
        catering_meals = self.cleaned_data.get('catering_meals')

        # "资产总计"应大于等于"固定资产净值"
        if int(asset_all) < int(fixed_asset_value):
            raise ValidationError("资产负债类中213项(资产总计)应大于等于250项(固定资产净值)+212项(在建工程)+205项(期末存货)")

        # 205项期末存货必须小于213项资产总计
        if int(end_inventory) > int(asset_all):
            raise ValidationError("资产负债类中205项(期末存货)必须小于213项(项资产总计)，请核对")

        # 323项营业利润必须小于301项营业收入
        if int(business_profit) > int(business_income):
            raise ValidationError("损益，人工及增值税类中323项(营业利润)必须小于301项(营业收入)，请核对")

        # 在建工程应该小于1亿元
        # if int(doing_project) > 100000000:
        #     raise ValidationError("资产负债类中212项(在建工程)应小于1亿元")

        # 营业成本过高，请核实(营业成本是营业收入的100倍以上):
        # if int(business_cost) * 100 < int(business_income):
        #     raise ValidationError("307项营业成本过高(是301项营业收入的100倍以上)，请核实！")

        # “资产总计”应大于等于“固定资产净值”、“在建工程”与“期末存货”之和
        # total = int(fixed_asset_value) + int(doing_project) + int(end_inventory)
        # if int(asset_all) < total:
        #     raise ValidationError("资产负债类中213项(资产总计)应大于等于250项(固定资产净值)+212项(在建工程)+205项(期末存货)")
        # 资产总计大于等于0；负债合计大于等于0；营业收入大于等于0
        # if int(debt_all) < 0:
        #     raise ValidationError("资产负债类中217项(负债合计)应大于0")
        if int(asset_all) < 0:
            raise ValidationError("资产负债类中213项(资产合计)应大于0")
        if int(business_income) < 0:
            raise ValidationError("损益，人工及增值税类中301项(营业收入)应大于0")

        # 应交增值税应该大于0
        # if int(added_tax_value) < 0:
        #     raise ValidationError("损益，人工及增值税类中402项(应交增值税)应大于0")
        # 应交增值税added_tax_value/营业收入business_income应该大于17%
        # if int(added_tax_value)/int(business_income) < 0.17:
        #     raise ValidationError("应交增值税added_tax_value/营业收入business_income应该大于17%")

        if is_plzc_write == 'True':
            if is_piling == 'True':
                # 批零业审核关系
                if int(piling_product_cost) == 0 and explain == '':
                    raise ValidationError("批零业的01项商品购进额为空，请填写为空的原因")
                else:
                    if int(piling_product_cost) != 0:
                        pilingcha = int(piling_product_cost) - int(piling_product_sale)
                        if pilingcha == int(piling_product_stock):
                            raise ValidationError("批零业情况中01项(商品购进额)-02项(商品销售额)不应等于05项(期末商品库存额)")
                    if int(piling_product_cost) >= 0 and int(piling_product_stock) >= 0 and int(piling_operate_turnover) >= 0 and int(piling_product_sale) >= 0 and int(piling_product_online_sale) >= 0 and int(piling_product_offline_sale) >= 0:
                        if int(piling_product_online_sale) > int(piling_product_sale):
                            raise ValidationError("03项(通过线上销售额)不能大于02项(商品总销售额(批零业))")
                        if int(piling_product_offline_sale) > int(piling_product_sale):
                            raise ValidationError("04项(零售额)不能大于02项9商品总销售额(批零业))")
                        # if int(piling_product_cost) == int(piling_product_sale):
                        #     raise ValidationError("01项(商品购进额)不能等于02项商品总销售额(批零业))")

                    else:
                        raise ValidationError("批零业的(01项，02项，03项，04项，05项，06项)各项数据必须大于或等于0")
            else:
                # 住餐业审核关系
                if int(catering_turnover) >= 0 and int(catering_turnover_online) >= 0 and int(catering_guest_room) >= 0 and int(catering_meals) >= 0:
                    if int(catering_turnover) < int(catering_guest_room) + int(catering_meals):
                        raise ValidationError("07项(营业额)大于等于09项其中：客房收入+10项(餐费收入)(住餐业)")
                    if int(catering_turnover_online) > int(catering_turnover):
                        raise ValidationError("08项(通过公共网络线上销售额)不能大于07项营业额(住餐业)")
                    if int(catering_guest_room) > int(catering_turnover):
                        raise ValidationError("09项(客房收入)不能大于07项营业额(住餐业)")
                    if int(catering_meals) > int(catering_turnover):
                        raise ValidationError("10项(餐费收入)不能大于07项营业额(住餐业)")
                else:
                    raise ValidationError("住餐业的(07项08项09项10项)各项数据必须大于或等于0")


# 611-4表单位固定资产投资项目情况
class fixedAssetForm(forms.ModelForm):
    class Meta:
        model = fixedAsset
        fields = '__all__'

    def clean(self):
        # 固定资产投资完成额 大于等于 500万以上项目财务支出完成投资额
        complete_pay = self.cleaned_data.get('complete_pay')
        # 其中：计划总投资500万元以上项目财务支出法完成资额:乙
        plan_hundred = self.cleaned_data.get('plan_hundred')
        # 计划总投资5000万元以上项目（个）：丙
        plan_thousand = self.data['plan_thousand']
        # 固定资产投资完成额说明
        explain = self.data['explain']

        total = int(plan_thousand) * 5000
        if complete_pay < plan_hundred:
            raise ValidationError("固定资产投资完成额 大于等于 500万以上项目财务支出完成投资额")

        if complete_pay < total:
            raise ValidationError("固定资产投资完成额小于计划投资500万以上+计划总投资5000万以上的项目的和")

        if complete_pay == 0:
            if not explain:
                raise ValidationError("甲项固定资产投资完成额为0，请填写固定资产投资完成额说明")

class ProjectCountForm(forms.ModelForm):
    class Meta:
        model = ProjectCount
        fields = (
        'main_social_num', 'social_num', 'org_num', 'number', 'name', 'province', 'city', 'district', 'address',
        'street_code', 'industry_code', 'start_time', 'all_time', 'all_invest', 'start_all_invest', 'total_invest')


# 611-5表行政事业单位主要经济指标
class nationUnitForm(forms.ModelForm):
    class Meta:
        model = nationUnit
        fields = (
        'area_building', 'building', 'current_assets', 'expend_labor_union', 'expend_labour', 'expend_management',
        'expend_medical', 'expend_retire', 'expend_salary', 'expend_service', 'expend_subsidy',
        'expend_taxes_additional', 'expend_welfare', 'income_fiscal_appropriation', 'income_manage',
        'income_undertaking', 'intangible_assets_price', 'inventory_current_assets', 'inventory_early',
        'land_tenure', 'machinery_equipment', 'main_social_num', 'original_price', 'permanent_investment',
        'public_infrastructure', 'public_infrastructure_accumulated_depreciation', 'total_assets',
        'total_expend', 'total_income', 'total_liabilities', 'total_net_asset', 'transportation_equipment')

    def clean(self):
        # 流动资产合计
        current_assets = self.cleaned_data.get('current_assets')
        # 其中：存货
        inventory_current_assets = self.cleaned_data.get('inventory_current_assets')
        # 固定资产原价
        original_price = self.cleaned_data.get('original_price')
        # 其中：土地房屋和构筑物
        area_building = self.cleaned_data.get('area_building')
        # 其中：机器设备
        machinery_equipment = self.cleaned_data.get('machinery_equipment')
        # 其中：运输设备
        transportation_equipment = self.cleaned_data.get('transportation_equipment')
        # 无形资产原价
        intangible_assets_price = self.cleaned_data.get('intangible_assets_price')
        # 公共基础设施原价
        public_infrastructure = self.cleaned_data.get('public_infrastructure')
        # 公共基础设施累计折旧
        public_infrastructure_accumulated_depreciation = self.cleaned_data.get('public_infrastructure_accumulated_depreciation')
        # 土地资产使用权
        land_tenure = self.cleaned_data.get('land_tenure')
        # 资产合计
        total_assets = self.cleaned_data.get('total_assets')
        # 负债合计
        total_liabilities = self.cleaned_data.get('total_liabilities')
        # 净资产合计
        total_net_asset = self.cleaned_data.get('total_net_asset')
        # 本年收入合计
        total_income = self.cleaned_data.get('total_income')
        # 财政拨款收入
        income_fiscal_appropriation = self.cleaned_data.get('income_fiscal_appropriation')
        # 事业收入
        income_undertaking = self.cleaned_data.get('income_undertaking')
        # 经营收入
        income_manage = self.cleaned_data.get('income_manage')
        # 本年支出合计
        total_expend = self.cleaned_data.get('total_expend')
        # 工资福利支出
        expend_salary = self.cleaned_data.get('expend_salary')
        # 商品和服务支出
        expend_service = self.cleaned_data.get('expend_service')
        # 其中：劳务费
        expend_labour = self.cleaned_data.get('expend_labour')
        # 工会经费
        expend_labor_union = self.cleaned_data.get('expend_labor_union')
        # 福利费
        expend_welfare = self.cleaned_data.get('expend_welfare')
        # 税金及附加费用
        expend_taxes_additional = self.cleaned_data.get('expend_taxes_additional')
        # 对个人和家庭的补助
        expend_subsidy = self.cleaned_data.get('expend_subsidy')
        # 其中：退（离）休费
        expend_retire = self.cleaned_data.get('expend_retire')
        # 其中：医疗费补助
        expend_medical = self.cleaned_data.get('expend_medical')

        # 流动资产合计大于存货
        if current_assets < inventory_current_assets:
            raise ValidationError("02项(流动资产合计)不能小于03项(其中：存货)")

        # 固定资产原价大于等于构筑物+机器设备+运输设备的和
        total_original_price = int(area_building) + int(machinery_equipment) + int(transportation_equipment)
        if original_price < total_original_price:
            raise ValidationError("05项(固定资产原价)不能小于06项(土地，房屋和构筑物)+07项(机器设备)+08项(运输设备)")

        # 10无形资产原价大于等于11土地使用价
        if int(intangible_assets_price) < int(land_tenure):
            raise ValidationError("10项无形资产原价大于等于11项土地使用价")

        # 12项公共基础设施原价应大于等于13项公共基础设施累计折旧
        if int(public_infrastructure) < int(public_infrastructure_accumulated_depreciation):
            raise ValidationError("12项公共基础设施原价应大于等于13项公共基础设施累计折旧")

        # 资产总计大于或等于流动资产合计+固定资产原价
        total_assets_all = int(current_assets) + int(original_price)
        if total_assets < total_assets_all:
            raise ValidationError("14项(资产总计)大于或等于02项(流动资产合计)+05项(固定资产原价)")

        # 净资产合计=资产合计-负债合计
        total_net_asset_all = int(total_assets) - int(total_liabilities)
        if total_net_asset != total_net_asset_all:
            raise ValidationError("16项(净资产合计)=14项(资产合计)-15项(负债合计)")

        # 本年收入合计大于等于财政拨款收入+事业收入+经营收入
        total_income_all = int(income_fiscal_appropriation) + int(income_manage) + int(income_undertaking)
        if total_income < total_income_all:
            raise ValidationError("17项(本年收入合计)大于等于18项(财政拨款收入)+19项(事业收入)+20项(经营收入)")

        # 本年支出合计大于等于工资福利支出+商品和服务支出+对个人和家庭的补助
        total_expend_all = int(expend_salary) + int(expend_service) + int(expend_subsidy)
        if total_expend < total_expend_all:
            raise ValidationError("21项(本年支出合计)大于等于22项(工资福利支出)+23项(商品和服务支出)+28项(对个人和家庭的补助)")

        # 商品和服务支出大于等于劳务费+工会经费+福利费+税金及附加费用
        expend_service_all = int(expend_labour) + int(expend_labor_union) + int(expend_welfare) + int(
            expend_taxes_additional)
        if expend_service < expend_service_all:
            raise ValidationError("商品和服务支出大于等于劳务费+工会经费+福利费+税金及附加费用")

        # 对个人和家庭的补助大于等于退休费+医疗费补助
        expend_subsidy_all = int(expend_retire) + int(expend_medical)
        if expend_subsidy < expend_subsidy_all:
            raise ValidationError("对个人和家庭的补助大于等于退休费+医疗费补助")


# 611-6表民间非盈利组织主要经济指标
class privateUncommerciallyOrgForm(forms.ModelForm):
    class Meta:
        model = privateUncommerciallyOrg
        fields = ('area_building', 'building', 'cultural_price', 'current_assets', 'expend_action_current_expense',
                  'expend_action_depreciation_assets', 'expend_action_salary', 'expend_action_taxes',
                  'expend_management',
                  'expend_management_current_expense', 'expend_management_depreciation_assets',
                  'expend_management_salary',
                  'expend_management_taxes', 'income_donate', 'income_membership_fees', 'intangible_price',
                  'inventory_current_assets', 'inventory_early', 'machinery_equipment', 'main_social_num',
                  'net_asset_change', 'original_price', 'permanent_investment', 'total_assets', 'total_income',
                  'total_liabilities', 'total_net_asset', 'total_operational_action', 'total_this_year',
                  'transportation_equipment')

    def clean(self):
        # 流动资产合计
        current_assets = self.cleaned_data.get('current_assets')
        # 其中：存货
        inventory_current_assets = self.cleaned_data.get('inventory_current_assets')
        # 固定资产原价
        original_price = self.cleaned_data.get('original_price')
        # 其中：土地房屋和构筑物
        area_building = self.cleaned_data.get('area_building')
        # 其中：机器设备*
        machinery_equipment = self.cleaned_data.get('machinery_equipment')
        # 其中：运输设备
        transportation_equipment = self.cleaned_data.get('transportation_equipment')

        # 资产合计
        total_assets = self.cleaned_data.get('total_assets')
        # 负债合计
        total_liabilities = self.cleaned_data.get('total_liabilities')
        # 净资产合计
        total_net_asset = self.cleaned_data.get('total_net_asset')

        # 本年收入合计
        total_income = self.cleaned_data.get('total_income')
        # 捐赠收入
        income_donate = self.cleaned_data.get('income_donate')
        # 会费收入
        income_membership_fees = self.cleaned_data.get('income_membership_fees')

        # 本年费用合计
        total_this_year = self.cleaned_data.get('total_this_year')
        # 业务活动成本
        total_operational_action = self.cleaned_data.get('total_operational_action')
        # 人员费用
        expend_action_salary = self.cleaned_data.get('expend_action_salary')
        # 日常费用
        expend_action_current_expense = self.cleaned_data.get('expend_action_current_expense')
        # 固定资产折旧
        expend_action_depreciation_assets = self.cleaned_data.get('expend_action_depreciation_assets')
        # 税费
        expend_action_taxes = self.cleaned_data.get('expend_action_taxes')

        # 管理费用
        expend_management = self.cleaned_data.get('expend_management')
        # 人员费用
        expend_management_salary = self.cleaned_data.get('expend_management_salary')
        # 日常费用
        expend_management_current_expense = self.cleaned_data.get('expend_management_current_expense')
        # 固定资产折旧
        expend_management_depreciation_assets = self.cleaned_data.get('expend_management_depreciation_assets')
        # 税费
        expend_management_taxes = self.cleaned_data.get('expend_management_taxes')

        # 流动资产合计大于存货
        if current_assets < inventory_current_assets:
            raise ValidationError("资产负债中，流动资产合计不能小于存货")

        # 固定资产原价大于等于构筑物+机器设备+运输设备的和
        total_original_price = area_building + machinery_equipment + transportation_equipment
        if original_price < total_original_price:
            raise ValidationError("资产负债中，固定资产原价不能小于构筑物，机器设备，运输设备的和")

        # 净资产总计大于或等于流动资产合计+固定资产原价
        total_net_asset_all = total_assets - total_liabilities
        if total_net_asset < total_net_asset_all:
            raise ValidationError("资产负债中，净资产总计大于或等于流动资产合计+固定资产原价")

        # 本年收入合计大于等于捐赠收入+会费收入
        total_income_all = income_donate + income_membership_fees
        if total_income < total_income_all:
            raise ValidationError("资产负债中，财务状况中，本年收入合计大于等于捐赠收入+会费收入")

        # 本年费用合计大于等于业务活动成本+管理费用
        total_this_year_all = total_operational_action + expend_management
        if total_this_year < total_this_year_all:
            raise ValidationError("财务状况中，本年费用合计>=业务活动成本+管理费用")

        # 业务活动成本大于等于人员费用+日常费用+固定资产折旧+税费
        total_operational_action_all = expend_action_salary + expend_action_current_expense + expend_action_depreciation_assets + expend_action_taxes
        if total_operational_action < total_operational_action_all:
            raise ValidationError("财务状况中，业务活动成本大于等于人员费用+日常费用+固定资产折旧+税费")

        # 管理费用大于等于人员费用+ 日常费用+ 固定资产折旧+ 税费
        expend_management_all = expend_management_salary + expend_management_current_expense + expend_management_depreciation_assets + expend_management_taxes
        if expend_management < expend_management_all:
            raise ValidationError("财务状况中，管理费用大于等于人员费用+ 日常费用+ 固定资产折旧+ 税费")


@api_view(['GET'])
def dataView(request, name):
    output = Companies.objects.filter(name=name)
    return JsonResponse(output)


def page_not_found(request):
    return render_to_response('404.html')


#   首页列表
@login_required
def index(request):
    # 碑林区总数
    total_count = Companies.objects.filter(is_valid=True).count()
    total_phase1_count = Companies.objects.filter(record_type__contains="phase1", is_valid=True).count()
    total_phase2_count = Companies.objects.filter(record_type__contains="phase2", is_valid=True).count()
    total_complete_done_count = Companies.objects.filter(complete_done=True, is_valid=True).count()
    total_complete_done_phase1_count = Companies.objects.filter(complete_done=True, record_type__contains="phase1",
                                                                is_valid=True).count()
    total_complete_done_phase2_count = Companies.objects.filter(complete_done=True, record_type__contains="phase2",
                                                                is_valid=True).count()
    total_no_complete_done_count = Companies.objects.filter(complete_done=False, is_valid=True).count()
    total_no_complete_done_phase1_count = Companies.objects.filter(complete_done=False, record_type__contains="phase1",
                                                                   is_valid=True).count()
    total_no_complete_done_phase2_count = Companies.objects.filter(complete_done=False, record_type__contains="phase2",
                                                                   is_valid=True).count()
    total_today_complete_done_count = Companies.objects.filter(complete_done=True,
                                                               submit_date__year=timezone.now().year,
                                                               submit_date__month=timezone.now().month,
                                                               submit_date__day=timezone.now().day,
                                                               is_valid=True).count()
    total_today_complete_done_phase1_count = Companies.objects.filter(complete_done=True,
                                                                      record_type__contains="phase1",
                                                                      submit_date__year=timezone.now().year,
                                                                      submit_date__month=timezone.now().month,
                                                                      submit_date__day=timezone.now().day,
                                                                      is_valid=True).count()
    total_today_complete_done_phase2_count = Companies.objects.filter(complete_done=True,
                                                                      record_type__contains="phase2",
                                                                      submit_date__year=timezone.now().year,
                                                                      submit_date__month=timezone.now().month,
                                                                      submit_date__day=timezone.now().day,
                                                                      is_valid=True).count()
    # 南院门统计
    nym_count = Companies.objects.filter(street_district__contains="南院门", is_valid=True).count()
    nym_phase1_count = Companies.objects.filter(street_district__contains="南院门", record_type__contains="phase1",
                                                is_valid=True).count()
    nym_phase2_count = Companies.objects.filter(street_district__contains="南院门", record_type__contains="phase2",
                                                is_valid=True).count()
    nym_complete_done_count = Companies.objects.filter(street_district__contains="南院门", complete_done=True,
                                                       is_valid=True).count()
    nym_complete_done_phase1_count = Companies.objects.filter(street_district__contains="南院门", complete_done=True,
                                                              record_type__contains="phase1", is_valid=True).count()
    nym_complete_done_phase2_count = Companies.objects.filter(street_district__contains="南院门", complete_done=True,
                                                              record_type__contains="phase2", is_valid=True).count()
    nym_no_complete_done_count = Companies.objects.filter(street_district__contains="南院门", complete_done=False,
                                                          is_valid=True).count()
    nym_no_complete_done_phase1_count = Companies.objects.filter(street_district__contains="南院门", complete_done=False,
                                                                 record_type__contains="phase1", is_valid=True).count()
    nym_no_complete_done_phase2_count = Companies.objects.filter(street_district__contains="南院门", complete_done=False,
                                                                 record_type__contains="phase2", is_valid=True).count()
    nym_today_complete_done_count = Companies.objects.filter(street_district__contains="南院门", complete_done=True,
                                                             submit_date__year=timezone.now().year,
                                                             submit_date__month=timezone.now().month,
                                                             submit_date__day=timezone.now().day,
                                                             is_valid=True).count()
    nym_today_complete_done_phase1_count = Companies.objects.filter(street_district__contains="南院门", complete_done=True,
                                                                    record_type__contains="phase1",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    nym_today_complete_done_phase2_count = Companies.objects.filter(street_district__contains="南院门", complete_done=True,
                                                                    record_type__contains="phase2",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    # 柏树林统计
    bsl_count = Companies.objects.filter(street_district__contains="柏树林", is_valid=True).count()
    bsl_phase1_count = Companies.objects.filter(street_district__contains="柏树林", record_type__contains="phase1",
                                                is_valid=True).count()
    bsl_phase2_count = Companies.objects.filter(street_district__contains="柏树林", record_type__contains="phase2",
                                                is_valid=True).count()
    bsl_complete_done_count = Companies.objects.filter(street_district__contains="柏树林", complete_done=True,
                                                       is_valid=True).count()
    bsl_complete_done_phase1_count = Companies.objects.filter(street_district__contains="柏树林", complete_done=True,
                                                              record_type__contains="phase1", is_valid=True).count()
    bsl_complete_done_phase2_count = Companies.objects.filter(street_district__contains="柏树林", complete_done=True,
                                                              record_type__contains="phase2", is_valid=True).count()
    bsl_no_complete_done_count = Companies.objects.filter(street_district__contains="柏树林", complete_done=False,
                                                          is_valid=True).count()
    bsl_no_complete_done_phase1_count = Companies.objects.filter(street_district__contains="柏树林", complete_done=False,
                                                                 record_type__contains="phase1", is_valid=True).count()
    bsl_no_complete_done_phase2_count = Companies.objects.filter(street_district__contains="柏树林", complete_done=False,
                                                                 record_type__contains="phase2", is_valid=True).count()
    bsl_today_complete_done_count = Companies.objects.filter(street_district__contains="柏树林", complete_done=True,
                                                             submit_date__year=timezone.now().year,
                                                             submit_date__month=timezone.now().month,
                                                             submit_date__day=timezone.now().day,
                                                             is_valid=True).count()
    bsl_today_complete_done_phase1_count = Companies.objects.filter(street_district__contains="柏树林", complete_done=True,
                                                                    record_type__contains="phase1",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    bsl_today_complete_done_phase2_count = Companies.objects.filter(street_district__contains="柏树林", complete_done=True,
                                                                    record_type__contains="phase2",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    # 长乐坊统计
    clf_count = Companies.objects.filter(street_district__contains="长乐坊", is_valid=True).count()
    clf_phase1_count = Companies.objects.filter(street_district__contains="长乐坊", record_type__contains="phase1",
                                                is_valid=True).count()
    clf_phase2_count = Companies.objects.filter(street_district__contains="长乐坊", record_type__contains="phase2",
                                                is_valid=True).count()
    clf_complete_done_count = Companies.objects.filter(street_district__contains="长乐坊", complete_done=True,
                                                       is_valid=True).count()
    clf_complete_done_phase1_count = Companies.objects.filter(street_district__contains="长乐坊", complete_done=True,
                                                              record_type__contains="phase1", is_valid=True).count()
    clf_complete_done_phase2_count = Companies.objects.filter(street_district__contains="长乐坊", complete_done=True,
                                                              record_type__contains="phase2", is_valid=True).count()
    clf_no_complete_done_count = Companies.objects.filter(street_district__contains="长乐坊", complete_done=False,
                                                          is_valid=True).count()
    clf_no_complete_done_phase1_count = Companies.objects.filter(street_district__contains="长乐坊", complete_done=False,
                                                                 record_type__contains="phase1", is_valid=True).count()
    clf_no_complete_done_phase2_count = Companies.objects.filter(street_district__contains="长乐坊", complete_done=False,
                                                                 record_type__contains="phase2", is_valid=True).count()
    clf_today_complete_done_count = Companies.objects.filter(street_district__contains="长乐坊", complete_done=True,
                                                             submit_date__year=timezone.now().year,
                                                             submit_date__month=timezone.now().month,
                                                             submit_date__day=timezone.now().day,
                                                             is_valid=True).count()
    clf_today_complete_done_phase1_count = Companies.objects.filter(street_district__contains="长乐坊", complete_done=True,
                                                                    record_type__contains="phase1",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    clf_today_complete_done_phase2_count = Companies.objects.filter(street_district__contains="长乐坊", complete_done=True,
                                                                    record_type__contains="phase2",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    # 东关南统计
    dgn_count = Companies.objects.filter(street_district__contains="东关南", is_valid=True).count()
    dgn_phase1_count = Companies.objects.filter(street_district__contains="东关南", record_type__contains="phase1",
                                                is_valid=True).count()
    dgn_phase2_count = Companies.objects.filter(street_district__contains="东关南", record_type__contains="phase2",
                                                is_valid=True).count()
    dgn_complete_done_count = Companies.objects.filter(street_district__contains="东关南", complete_done=True,
                                                       is_valid=True).count()
    dgn_complete_done_phase1_count = Companies.objects.filter(street_district__contains="东关南", complete_done=True,
                                                              record_type__contains="phase1", is_valid=True).count()
    dgn_complete_done_phase2_count = Companies.objects.filter(street_district__contains="东关南", complete_done=True,
                                                              record_type__contains="phase2", is_valid=True).count()
    dgn_no_complete_done_count = Companies.objects.filter(street_district__contains="东关南", complete_done=False,
                                                          is_valid=True).count()
    dgn_no_complete_done_phase1_count = Companies.objects.filter(street_district__contains="东关南", complete_done=False,
                                                                 record_type__contains="phase1", is_valid=True).count()
    dgn_no_complete_done_phase2_count = Companies.objects.filter(street_district__contains="东关南", complete_done=False,
                                                                 record_type__contains="phase2", is_valid=True).count()
    dgn_today_complete_done_count = Companies.objects.filter(street_district__contains="东关南", complete_done=True,
                                                             submit_date__year=timezone.now().year,
                                                             submit_date__month=timezone.now().month,
                                                             submit_date__day=timezone.now().day,
                                                             is_valid=True).count()
    dgn_today_complete_done_phase1_count = Companies.objects.filter(street_district__contains="东关南", complete_done=True,
                                                                    record_type__contains="phase1",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    dgn_today_complete_done_phase2_count = Companies.objects.filter(street_district__contains="东关南", complete_done=True,
                                                                    record_type__contains="phase2",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    # 太乙路统计
    tyl_count = Companies.objects.filter(street_district__contains="太乙路", is_valid=True).count()
    tyl_phase1_count = Companies.objects.filter(street_district__contains="太乙路", record_type__contains="phase1",
                                                is_valid=True).count()
    tyl_phase2_count = Companies.objects.filter(street_district__contains="太乙路", record_type__contains="phase2",
                                                is_valid=True).count()
    tyl_complete_done_count = Companies.objects.filter(street_district__contains="太乙路", complete_done=True,
                                                       is_valid=True).count()
    tyl_complete_done_phase1_count = Companies.objects.filter(street_district__contains="太乙路", complete_done=True,
                                                              record_type__contains="phase1", is_valid=True).count()
    tyl_complete_done_phase2_count = Companies.objects.filter(street_district__contains="太乙路", complete_done=True,
                                                              record_type__contains="phase2", is_valid=True).count()
    tyl_no_complete_done_count = Companies.objects.filter(street_district__contains="太乙路", complete_done=False,
                                                          is_valid=True).count()
    tyl_no_complete_done_phase1_count = Companies.objects.filter(street_district__contains="太乙路", complete_done=False,
                                                                 record_type__contains="phase1", is_valid=True).count()
    tyl_no_complete_done_phase2_count = Companies.objects.filter(street_district__contains="太乙路", complete_done=False,
                                                                 record_type__contains="phase2", is_valid=True).count()
    tyl_today_complete_done_count = Companies.objects.filter(street_district__contains="太乙路", complete_done=True,
                                                             submit_date__year=timezone.now().year,
                                                             submit_date__month=timezone.now().month,
                                                             submit_date__day=timezone.now().day,
                                                             is_valid=True).count()
    tyl_today_complete_done_phase1_count = Companies.objects.filter(street_district__contains="太乙路", complete_done=True,
                                                                    record_type__contains="phase1",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    tyl_today_complete_done_phase2_count = Companies.objects.filter(street_district__contains="太乙路", complete_done=True,
                                                                    record_type__contains="phase2",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    # 文艺路统计
    wyl_count = Companies.objects.filter(street_district__contains="文艺路", is_valid=True).count()
    wyl_phase1_count = Companies.objects.filter(street_district__contains="文艺路", record_type__contains="phase1",
                                                is_valid=True).count()
    wyl_phase2_count = Companies.objects.filter(street_district__contains="文艺路", record_type__contains="phase2",
                                                is_valid=True).count()
    wyl_complete_done_count = Companies.objects.filter(street_district__contains="文艺路", complete_done=True,
                                                       is_valid=True).count()
    wyl_complete_done_phase1_count = Companies.objects.filter(street_district__contains="文艺路", complete_done=True,
                                                              record_type__contains="phase1", is_valid=True).count()
    wyl_complete_done_phase2_count = Companies.objects.filter(street_district__contains="文艺路", complete_done=True,
                                                              record_type__contains="phase2", is_valid=True).count()
    wyl_no_complete_done_count = Companies.objects.filter(street_district__contains="文艺路", complete_done=False,
                                                          is_valid=True).count()
    wyl_no_complete_done_phase1_count = Companies.objects.filter(street_district__contains="文艺路", complete_done=False,
                                                                 record_type__contains="phase1", is_valid=True).count()
    wyl_no_complete_done_phase2_count = Companies.objects.filter(street_district__contains="文艺路", complete_done=False,
                                                                 record_type__contains="phase2", is_valid=True).count()
    wyl_today_complete_done_count = Companies.objects.filter(street_district__contains="文艺路", complete_done=True,
                                                             submit_date__year=timezone.now().year,
                                                             submit_date__month=timezone.now().month,
                                                             submit_date__day=timezone.now().day,
                                                             is_valid=True).count()
    wyl_today_complete_done_phase1_count = Companies.objects.filter(street_district__contains="文艺路", complete_done=True,
                                                                    record_type__contains="phase1",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    wyl_today_complete_done_phase2_count = Companies.objects.filter(street_district__contains="文艺路", complete_done=True,
                                                                    record_type__contains="phase2",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    # 长安路统计
    cal_count = Companies.objects.filter(street_district__contains="长安路", is_valid=True).count()
    cal_phase1_count = Companies.objects.filter(street_district__contains="长安路", record_type__contains="phase1",
                                                is_valid=True).count()
    cal_phase2_count = Companies.objects.filter(street_district__contains="长安路", record_type__contains="phase2",
                                                is_valid=True).count()
    cal_complete_done_count = Companies.objects.filter(street_district__contains="长安路", complete_done=True,
                                                       is_valid=True).count()
    cal_complete_done_phase1_count = Companies.objects.filter(street_district__contains="长安路", complete_done=True,
                                                              record_type__contains="phase1", is_valid=True).count()
    cal_complete_done_phase2_count = Companies.objects.filter(street_district__contains="长安路", complete_done=True,
                                                              record_type__contains="phase2", is_valid=True).count()
    cal_no_complete_done_count = Companies.objects.filter(street_district__contains="长安路", complete_done=False,
                                                          is_valid=True).count()
    cal_no_complete_done_phase1_count = Companies.objects.filter(street_district__contains="长安路", complete_done=False,
                                                                 record_type__contains="phase1", is_valid=True).count()
    cal_no_complete_done_phase2_count = Companies.objects.filter(street_district__contains="长安路", complete_done=False,
                                                                 record_type__contains="phase2", is_valid=True).count()
    cal_today_complete_done_count = Companies.objects.filter(street_district__contains="长安路", complete_done=True,
                                                             submit_date__year=timezone.now().year,
                                                             submit_date__month=timezone.now().month,
                                                             submit_date__day=timezone.now().day,
                                                             is_valid=True).count()
    cal_today_complete_done_phase1_count = Companies.objects.filter(street_district__contains="长安路", complete_done=True,
                                                                    record_type__contains="phase1",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    cal_today_complete_done_phase2_count = Companies.objects.filter(street_district__contains="长安路", complete_done=True,
                                                                    record_type__contains="phase2",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    # 张家村统计
    zjc_count = Companies.objects.filter(street_district__contains="张家村", is_valid=True).count()
    zjc_phase1_count = Companies.objects.filter(street_district__contains="张家村", record_type__contains="phase1",
                                                is_valid=True).count()
    zjc_phase2_count = Companies.objects.filter(street_district__contains="张家村", record_type__contains="phase2",
                                                is_valid=True).count()
    zjc_complete_done_count = Companies.objects.filter(street_district__contains="张家村", complete_done=True,
                                                       is_valid=True).count()
    zjc_complete_done_phase1_count = Companies.objects.filter(street_district__contains="张家村", complete_done=True,
                                                              record_type__contains="phase1", is_valid=True).count()
    zjc_complete_done_phase2_count = Companies.objects.filter(street_district__contains="张家村", complete_done=True,
                                                              record_type__contains="phase2", is_valid=True).count()
    zjc_no_complete_done_count = Companies.objects.filter(street_district__contains="张家村", complete_done=False,
                                                          is_valid=True).count()
    zjc_no_complete_done_phase1_count = Companies.objects.filter(street_district__contains="张家村", complete_done=False,
                                                                 record_type__contains="phase1", is_valid=True).count()
    zjc_no_complete_done_phase2_count = Companies.objects.filter(street_district__contains="张家村", complete_done=False,
                                                                 record_type__contains="phase2", is_valid=True).count()
    zjc_today_complete_done_count = Companies.objects.filter(street_district__contains="张家村", complete_done=True,
                                                             submit_date__year=timezone.now().year,
                                                             submit_date__month=timezone.now().month,
                                                             submit_date__day=timezone.now().day,
                                                             is_valid=True).count()
    zjc_today_complete_done_phase1_count = Companies.objects.filter(street_district__contains="张家村", complete_done=True,
                                                                    record_type__contains="phase1",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()
    zjc_today_complete_done_phase2_count = Companies.objects.filter(street_district__contains="张家村", complete_done=True,
                                                                    record_type__contains="phase2",
                                                                    submit_date__year=timezone.now().year,
                                                                    submit_date__month=timezone.now().month,
                                                                    submit_date__day=timezone.now().day,
                                                                    is_valid=True).count()

    return render(request, 'index.html', {
        # 碑林区统计
        'total_count': total_count, 'total_phase1_count': total_phase1_count, 'total_phase2_count': total_phase2_count,
        'total_complete_done_count': total_complete_done_count,
        'total_complete_done_phase1_count': total_complete_done_phase1_count,
        'total_complete_done_phase2_count': total_complete_done_phase2_count,
        'total_no_complete_done_count': total_no_complete_done_count,
        'total_no_complete_done_phase1_count': total_no_complete_done_phase1_count,
        'total_no_complete_done_phase2_count': total_no_complete_done_phase2_count,
        'total_today_complete_done_count': total_today_complete_done_count,
        'total_today_complete_done_phase1_count': total_today_complete_done_phase1_count,
        'total_today_complete_done_phase2_count': total_today_complete_done_phase2_count,
        # 南院门统计
        'nym_count': nym_count, 'nym_phase1_count': nym_phase1_count, 'nym_phase2_count': nym_phase2_count,
        'nym_complete_done_count': nym_complete_done_count,
        'nym_complete_done_phase1_count': nym_complete_done_phase1_count,
        'nym_complete_done_phase2_count': nym_complete_done_phase2_count,
        'nym_no_complete_done_count': nym_no_complete_done_count,
        'nym_no_complete_done_phase1_count': nym_no_complete_done_phase1_count,
        'nym_no_complete_done_phase2_count': nym_no_complete_done_phase2_count,
        'nym_today_complete_done_count': nym_today_complete_done_count,
        'nym_today_complete_done_phase1_count': nym_today_complete_done_phase1_count,
        'nym_today_complete_done_phase2_count': nym_today_complete_done_phase2_count,
        # 柏树林统计
        'bsl_count': bsl_count, 'bsl_phase1_count': bsl_phase1_count, 'bsl_phase2_count': bsl_phase2_count,
        'bsl_complete_done_count': bsl_complete_done_count,
        'bsl_complete_done_phase1_count': bsl_complete_done_phase1_count,
        'bsl_complete_done_phase2_count': bsl_complete_done_phase2_count,
        'bsl_no_complete_done_count': bsl_no_complete_done_count,
        'bsl_no_complete_done_phase1_count': bsl_no_complete_done_phase1_count,
        'bsl_no_complete_done_phase2_count': bsl_no_complete_done_phase2_count,
        'bsl_today_complete_done_count': bsl_today_complete_done_count,
        'bsl_today_complete_done_phase1_count': bsl_today_complete_done_phase1_count,
        'bsl_today_complete_done_phase2_count': bsl_today_complete_done_phase2_count,
        # 长乐坊统计
        'clf_count': clf_count, 'clf_phase1_count': clf_phase1_count, 'clf_phase2_count': clf_phase2_count,
        'clf_complete_done_count': clf_complete_done_count,
        'clf_complete_done_phase1_count': clf_complete_done_phase1_count,
        'clf_complete_done_phase2_count': clf_complete_done_phase2_count,
        'clf_no_complete_done_count': clf_no_complete_done_count,
        'clf_no_complete_done_phase1_count': clf_no_complete_done_phase1_count,
        'clf_no_complete_done_phase2_count': clf_no_complete_done_phase2_count,
        'clf_today_complete_done_count': clf_today_complete_done_count,
        'clf_today_complete_done_phase1_count': clf_today_complete_done_phase1_count,
        'clf_today_complete_done_phase2_count': clf_today_complete_done_phase2_count,
        # 东关南统计
        'dgn_count': dgn_count, 'dgn_phase1_count': dgn_phase1_count, 'dgn_phase2_count': dgn_phase2_count,
        'dgn_complete_done_count': dgn_complete_done_count,
        'dgn_complete_done_phase1_count': dgn_complete_done_phase1_count,
        'dgn_complete_done_phase2_count': dgn_complete_done_phase2_count,
        'dgn_no_complete_done_count': dgn_no_complete_done_count,
        'dgn_no_complete_done_phase1_count': dgn_no_complete_done_phase1_count,
        'dgn_no_complete_done_phase2_count': dgn_no_complete_done_phase2_count,
        'dgn_today_complete_done_count': dgn_today_complete_done_count,
        'dgn_today_complete_done_phase1_count': dgn_today_complete_done_phase1_count,
        'dgn_today_complete_done_phase2_count': dgn_today_complete_done_phase2_count,
        # 太乙路统计
        'tyl_count': tyl_count, 'tyl_phase1_count': tyl_phase1_count, 'tyl_phase2_count': tyl_phase2_count,
        'tyl_complete_done_count': tyl_complete_done_count,
        'tyl_complete_done_phase1_count': tyl_complete_done_phase1_count,
        'tyl_complete_done_phase2_count': tyl_complete_done_phase2_count,
        'tyl_no_complete_done_count': tyl_no_complete_done_count,
        'tyl_no_complete_done_phase1_count': tyl_no_complete_done_phase1_count,
        'tyl_no_complete_done_phase2_count': tyl_no_complete_done_phase2_count,
        'tyl_today_complete_done_count': tyl_today_complete_done_count,
        'tyl_today_complete_done_phase1_count': tyl_today_complete_done_phase1_count,
        'tyl_today_complete_done_phase2_count': tyl_today_complete_done_phase2_count,
        # 文艺路统计
        'wyl_count': wyl_count, 'wyl_phase1_count': wyl_phase1_count, 'wyl_phase2_count': wyl_phase2_count,
        'wyl_complete_done_count': wyl_complete_done_count,
        'wyl_complete_done_phase1_count': wyl_complete_done_phase1_count,
        'wyl_complete_done_phase2_count': wyl_complete_done_phase2_count,
        'wyl_no_complete_done_count': wyl_no_complete_done_count,
        'wyl_no_complete_done_phase1_count': wyl_no_complete_done_phase1_count,
        'wyl_no_complete_done_phase2_count': wyl_no_complete_done_phase2_count,
        'wyl_today_complete_done_count': wyl_today_complete_done_count,
        'wyl_today_complete_done_phase1_count': wyl_today_complete_done_phase1_count,
        'wyl_today_complete_done_phase2_count': wyl_today_complete_done_phase2_count,
        # 长安路统计
        'cal_count': cal_count, 'cal_phase1_count': cal_phase1_count, 'cal_phase2_count': cal_phase2_count,
        'cal_complete_done_count': cal_complete_done_count,
        'cal_complete_done_phase1_count': cal_complete_done_phase1_count,
        'cal_complete_done_phase2_count': cal_complete_done_phase2_count,
        'cal_no_complete_done_count': cal_no_complete_done_count,
        'cal_no_complete_done_phase1_count': cal_no_complete_done_phase1_count,
        'cal_no_complete_done_phase2_count': cal_no_complete_done_phase2_count,
        'cal_today_complete_done_count': cal_today_complete_done_count,
        'cal_today_complete_done_phase1_count': cal_today_complete_done_phase1_count,
        'cal_today_complete_done_phase2_count': cal_today_complete_done_phase2_count,
        # 张家村统计
        'zjc_count': zjc_count, 'zjc_phase1_count': zjc_phase1_count, 'zjc_phase2_count': zjc_phase2_count,
        'zjc_complete_done_count': zjc_complete_done_count,
        'zjc_complete_done_phase1_count': zjc_complete_done_phase1_count,
        'zjc_complete_done_phase2_count': zjc_complete_done_phase2_count,
        'zjc_no_complete_done_count': zjc_no_complete_done_count,
        'zjc_no_complete_done_phase1_count': zjc_no_complete_done_phase1_count,
        'zjc_no_complete_done_phase2_count': zjc_no_complete_done_phase2_count,
        'zjc_today_complete_done_count': zjc_today_complete_done_count,
        'zjc_today_complete_done_phase1_count': zjc_today_complete_done_phase1_count,
        'zjc_today_complete_done_phase2_count': zjc_today_complete_done_phase2_count

    })


#  管理员查看学生录入情况
@login_required
def user_admin(request):
    clf_data = Companies.objects.filter(street_district__contains="长乐坊", complete_done=True, is_valid=True)
    for clf in clf_data:
        clf_name = legalPerson.objects.filter(main_social_num=clf, business_profit__gt=0, business_income__gt=0, staff_wages__gt=0)

    User = get_user_model()
    # 东关南统计
    # 南院门管理员
    nym_count = Companies.objects.filter(street_district__contains="南院门", complete_done=True, submit_date__year=timezone.now().year, submit_date__month=timezone.now().month, submit_date__day=timezone.now().day, is_valid=True).count()
    nyn_users = User.objects.filter(district__contains="南院门")
    nym_user_count = {'all': nym_count}
    for user in nyn_users:
        count = Companies.objects.filter(street_district__contains="南院门", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True, modified_by=user).count()
        nym_user_count.update({user.name: count})
    # 柏树林管理员
    bsl_count = Companies.objects.filter(street_district__contains="柏树林", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True).count()
    bsl_users = User.objects.filter(district__contains="柏树林")
    bsl_user_count = {'all': bsl_count}
    for user in bsl_users:
        count = Companies.objects.filter(street_district__contains="柏树林", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True, modified_by=user).count()
        bsl_user_count.update({user.name: count})
    # 长乐坊管理员
    clf_count = Companies.objects.filter(street_district__contains="长乐坊", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True).count()
    clf_users = User.objects.filter(district__contains="长乐坊")
    clf_user_count = {'all': clf_count}
    for user in clf_users:
        count = Companies.objects.filter(street_district__contains="长乐坊", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True, modified_by=user).count()
        clf_user_count.update({user.name: count})
    # 东关南管理员
    dgn_count = Companies.objects.filter(street_district__contains="东关南", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True).count()
    users = User.objects.filter(district__contains="东关南")
    dgn_user_count = {'all': dgn_count}
    for user in users:
        count = Companies.objects.filter(street_district__contains="东关南", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True, modified_by=user).count()
        dgn_user_count.update({user.name: count})
    # 太乙路管理员
    tyl_count = Companies.objects.filter(street_district__contains="太乙路", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True).count()
    tyl_users = User.objects.filter(district__contains="太乙路")
    tyl_user_count = {'all': tyl_count}
    for user in tyl_users:
        count = Companies.objects.filter(street_district__contains="太乙路", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True, modified_by=user).count()
        tyl_user_count.update({user.name: count})

    # 文艺路管理员

    wyl_count = Companies.objects.filter(street_district__contains="文艺路", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True).count()
    wyl_users = User.objects.filter(district__contains="文艺路")
    wyl_user_count = {'all': wyl_count}
    for user in wyl_users:
        count = Companies.objects.filter(street_district__contains="文艺路", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True, modified_by=user).count()
        wyl_user_count.update({user.name: count})

    # 长安路管理员
    cal_count = Companies.objects.filter(street_district__contains="长安路", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True).count()
    cal_users = User.objects.filter(district__contains="长安路")
    cal_user_count = {'all': cal_count}
    for user in cal_users:
        count = Companies.objects.filter(street_district__contains="长安路", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True, modified_by=user).count()
        cal_user_count.update({user.name: count})

    # 张家村管理员

    zjc_count = Companies.objects.filter(street_district__contains="张家村", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True).count()
    zjc_users = User.objects.filter(district__contains="张家村")
    zjc_user_count = {'all': zjc_count}
    for user in zjc_users:
        count = Companies.objects.filter(street_district__contains="张家村", complete_done=True,
                                         submit_date__year=timezone.now().year,
                                         submit_date__month=timezone.now().month,
                                         submit_date__day=timezone.now().day,
                                         is_valid=True, modified_by=user).count()
        zjc_user_count.update({user.name: count})

    return render(request, 'user_admin.html', {
        'group_name': request.user.get_group_name.name,
        # 南院门统计
        'nym_count': nym_count, 'nym_user_count': nym_user_count,
        # 柏树林统计
        'bsl_count': bsl_count, 'bsl_user_count': bsl_user_count,
        # 长乐坊统计
        'clf_count': clf_count, 'clf_user_count': clf_user_count,
        # 东关南统计
        'dgn_count': dgn_count, 'dgn_user_count': dgn_user_count,
        # 太乙路统计
        'tyl_count': tyl_count, 'tyl_user_count': tyl_user_count,
        # 文艺路统计
        'wyl_count': wyl_count, 'wyl_user_count': wyl_user_count,
        # 长安路统计
        'cal_count': cal_count, 'cal_user_count': cal_user_count,
        # 张家村统计
        'zjc_count': zjc_count, 'zjc_user_count': zjc_user_count

        })


def xxxq(request):
    return render(request, 'xxxq.html')


# 用户登录
def login(request):
    return render(request, 'login.html')


# 404页面
def page404(request):
    return render(request, '404.html')


def get_done_status(cid, name):
    count = name.objects.filter(main_social_num=cid).count()
    if not count:
        return False
    else:
        return True


# 需要添加页面
def add_611_1(cid, comp_type, social_num, org_num, name, address, park_code, mobile, main_activity_1, industry_code):
    main_social_num_id = Companies.objects.get(id=cid)
    if social_num:
        org_num = social_num[9:16] + 'B'
    else:
        org_num = org_num[1:-1] + 'B'
    name = name + '(本部)'
    ActivityInfo.objects.update_or_create(
        main_social_num=main_social_num_id, name=name,
        defaults={
            'unit_category': comp_type,
            'org_num': org_num,
            'address': address,
            'zone_num': park_code,
            'mobile': mobile,
            'main_activity': main_activity_1,
            'catrgory_code': industry_code
        }
    )
    return True


# 判断所有表是否都已经完成
def has_complete_done(cid):
    try:
        companies = Companies.objects.get(id=cid)
        has_done = companies.complete_done
        if has_done is False:
            need_list = []
            has_done = True
            if companies.need_611_1 == True: need_list.append('1')
            if companies.need_611_2 == True: need_list.append('2')
            if companies.need_611_3 == True: need_list.append('3')
            if companies.need_611_4 == True: need_list.append('4')
            if companies.need_611_5 == True: need_list.append('5')
            if companies.need_611_6 == True: need_list.append('6')

            if not need_list and companies.comp_type == '2':
                if companies.modified_by.name != 'system':
                    companies.complete_done = has_done
                    companies.save()

            for c in need_list:
                if c == '1':
                    if not companies.done_611_1:
                        return ''
                if c == '2':
                    if not companies.done_611_2:
                        return ''
                if c == '3':
                    if not companies.done_611_3:
                        return ''
                if c == '4':
                    if not companies.done_611_4:
                        return ''
                if c == '5':
                    if not companies.done_611_5:
                        return ''
                if c == '6':
                    if not companies.done_611_6:
                        return ''

                companies.complete_done = has_done
                companies.save()
    except Companies.DoesNotExist:
        companies = ''

def get_permission(get_group_name):
    permission = True
    if get_group_name == '碑林区管理员': permission = False
    if get_group_name == '南院门管理员': permission = False
    if get_group_name == '柏树林管理员': permission = False
    if get_group_name == '长乐坊管理员': permission = False
    if get_group_name == '东关南管理员': permission = False
    if get_group_name == '太乙路管理员': permission = False
    if get_group_name == '文艺路管理员': permission = False
    if get_group_name == '长安路管理员': permission = False
    if get_group_name == '张家村管理员': permission = False
    return permission

# 修改企业信息
@api_view(['GET', 'PUT', 'POST'])
@login_required
def edit_com(request, street_district, cid):
    try:
        companies = Companies.objects.get(id=cid)
    except Companies.DoesNotExist:
        companies = ''

    permission = get_permission(request.user.get_group_name.name)

    if request.method == 'POST':
        form = CompaniesForm(request.POST)
        # [print(f.name, f.value(), f.errors) for f in form]
        if form.is_valid():
            data = form.cleaned_data


            # 验证统一社会信用代码的唯一性
            if data['social_num']:
                get_comp = Companies.objects.filter(social_num=data['social_num'], is_valid=True).count()
                if get_comp > 1:
                    response_data = {'next': '', 'code': -1, 'msg': ['您的109项统一社会信用代码已存在，请核对后重新填写']}
                    return JsonResponse(response_data, safe=False)
            else:
                if data['org_num'] and data['org_num'] != '000000000':
                    get_comp = Companies.objects.filter(org_num=data['org_num'], is_valid=True).count()
                    if get_comp > 1:
                        response_data = {'next': '', 'code': -1, 'msg': ['您的109项组织机构代码已存在，请核对后重新填写']}
                        return JsonResponse(response_data, safe=False)
                else:
                    get_comp = Companies.objects.filter(name=data['name'], is_valid=True).count()
                    if get_comp > 1:
                        response_data = {'next': '', 'code': -1, 'msg': ['您的102项单位详细名称已存在，请核对后重新填写']}
                        return JsonResponse(response_data, safe=False)

            if data['operate_status'] != '6':
                if data['branch_comp_count_obtainemploy'] == '':
                    data['branch_comp_count_obtainemploy'] = 0
                if data['branch_comp_count_obtainemploy_female'] == '':
                    data['branch_comp_count_obtainemploy_female'] = 0
                if data['branch_comp_operate_income'] == '':
                    data['branch_comp_operate_income'] = 0
                if data['branch_comp_nooperate_defray'] == '':
                    data['branch_comp_nooperate_defray'] = 0
                if data['branch_comp_house_sale_area'] == '':
                    data['branch_comp_house_sale_area'] = 0
                if data['branch_comp_house_nosale_area'] == '':
                    data['branch_comp_house_nosale_area'] = 0

                data['need_611_1'] = data['need_611_2'] = data['need_611_3'] = data['need_611_4'] = data['need_611_5'] = \
                data['need_611_6'] = False
                if cid == 0:
                    data['done_611_1'] = data['done_611_2'] = data['done_611_3'] = data['done_611_4'] = data['done_611_5'] = \
                    data['done_611_6'] = False
                    data['is_higher_legal'] = False
                else:
                    data['done_611_1'] = get_done_status(cid, ActivityInfo)
                    data['done_611_2'] = get_done_status(cid, EmployeeUint)
                    data['done_611_3'] = get_done_status(cid, legalPerson)
                    data['done_611_4'] = get_done_status(cid, fixedAsset)
                    data['done_611_5'] = get_done_status(cid, nationUnit)
                    data['done_611_6'] = get_done_status(cid, privateUncommerciallyOrg)

                if data['has_branch'] == '1' and data['comp_type'] == '1':
                    data['need_611_1'] = True

                if data['comp_type'] == '1':
                    data['need_611_2'] = data['need_611_4'] = True

                if (data['accounting_rule'] == '1' and data['org_type'] == '10') or \
                    ((data['org_type'] == '20' or data['org_type'] == '51' or data['org_type'] == '52' or
                         data['org_type'] == '55') and data['accounting_rule'] == '1') or data['org_type'] == '56' or data['org_type'] == '55':
                    if data['comp_type'] == '1':
                        data['need_611_3'] = True

                if data['org_type'] == '30' or data['org_type'] == '53' or \
                        data['org_type'] == '54' or data['accounting_rule'] == '2' or data['accounting_rule'] == '3':
                    data['need_611_5'] = True

                if data['accounting_rule'] == '4':
                    data['need_611_6'] = True
                if data['org_type'] == '40' or (
                        data['accounting_rule'] != '1' and (data['org_type'] == '51' or data['org_type'] == '52')):
                    data['need_611_6'] = True
                if data['name'][-1] == '寺' or '八仙宫' in data['name'] or '基督教' in data['name']:
                    data['need_611_6'] = True
            else:
                data['need_611_1'] = data['need_611_2'] = data['need_611_3'] = data['need_611_4'] = data['need_611_5'] = \
                    data['need_611_6'] = False
                data['complete_done'] = data['done_611_1'] = data['done_611_2'] = data['done_611_3'] = data['done_611_4'] = data['done_611_5'] = \
                    data['done_611_6'] = True
                data['is_higher_legal'] = False
                data['branch_comp_house_nosale_area'] = data['branch_comp_house_sale_area'] = data['branch_comp_nooperate_defray'] = \
                    data['branch_comp_count_obtainemploy'] = data['branch_comp_count_obtainemploy_female'] = \
                    data['branch_comp_operate_income'] = 0


            if cid == 0:

                obj, created = Companies.objects.get_or_create(
                    # A项
                    comp_type=data['comp_type'],
                    profess_category=data['profess_category'],
                    social_num=data['social_num'],
                    org_num=data['org_num'],
                    name=data['name'],
                    legal_person=data['legal_person'],
                    est_year=data['est_year'],
                    est_month=data['est_month'],
                    landline_area_code=data['landline_area_code'],
                    landline_num=data['landline_num'],
                    landline_branch_num=data['landline_branch_num'],
                    mobile=data['mobile'],
                    fax_code=data['fax_code'],
                    fax_branch_code=data['fax_branch_code'],
                    postalcode=data['postalcode'],
                    website=data['website'],
                    province=data['province'],
                    city=data['city'],
                    district=data['district'],
                    address=data['address'],
                    street_district=data['street_district'],
                    community=data['community'],
                    register_province=data['register_province'],
                    register_city=data['register_city'],
                    register_district=data['register_district'],
                    register_address=data['register_address'],
                    register_street_district=data['register_street_district'],
                    register_community=data['register_community'],
                    operate_status=data['operate_status'],
                    main_activity_1=data['main_activity_1'],
                    org_type=data['org_type'],
                    register_type=data['register_type'],
                    is_piling=data['is_piling'],
                    # B项
                    retail_management_form=data['retail_management_form'],
                    retail_management_brand=data['retail_management_brand'],
                    # 零售业态(最多选择三个)
                    retail_opetrate_type=data['retail_opetrate_type'],
                    retail_business_area=data['retail_business_area'],
                    retail_hotel_diet_star=data['retail_hotel_diet_star'],
                    retail_hotel_diet_area=data['retail_hotel_diet_area'],
                    # C项
                    legal_unite_hkmatai=data['legal_unite_hkmatai'],
                    legal_unite_hypotaxis=data['legal_unite_hypotaxis'],
                    legal_unite_stake=data['legal_unite_stake'],
                    accounting_rule=data['accounting_rule'],
                    legal_unite_accounting_standard=data['legal_unite_accounting_standard'],
                    is_higher_legal=data['is_higher_legal'],
                    legal_unite_social_num=data['legal_unite_social_num'],
                    legal_unite_org_num=data['legal_unite_org_num'],
                    legal_unite_name=data['legal_unite_name'],
                    has_branch=data['has_branch'],
                    # D项
                    parent_type=data['parent_type'],
                    parent_comp_social_num=data['parent_comp_social_num'],
                    parent_comp_org_num=data['parent_comp_org_num'],
                    parent_comp_name=data['parent_comp_name'],
                    parent_comp_address=data['parent_comp_address'],
                    branch_comp_count_obtainemploy=data['branch_comp_count_obtainemploy'],
                    branch_comp_count_obtainemploy_female=data['branch_comp_count_obtainemploy_female'],
                    branch_comp_operate_income=data['branch_comp_operate_income'],
                    branch_comp_nooperate_defray=data['branch_comp_nooperate_defray'],
                    branch_comp_house_sale_area=data['branch_comp_house_sale_area'],
                    branch_comp_house_nosale_area=data['branch_comp_house_nosale_area'],
                    added_by=data['added_by'],
                    added_date=timezone.now(),
                    modified_by=data['added_by'],
                    modified_date=timezone.now(),
                    submit_date=timezone.now(),
                    interviewee=data['interviewee'],
                    interviewee_contact=data['interviewee_contact'],
                    complete_done=data['complete_done'],
                    need_611_1=data['need_611_1'],
                    need_611_2=data['need_611_2'],
                    need_611_3=data['need_611_3'],
                    need_611_4=data['need_611_4'],
                    need_611_5=data['need_611_5'],
                    need_611_6=data['need_611_6'],
                    is_valid=True,
                    done_611=True,
                    done_611_1=False,
                    done_611_2=False,
                    done_611_3=False,
                    done_611_4=False,
                    done_611_5=False,
                    done_611_6=False
                )
                mid = obj.id
            else:
                data['submit_date'] = companies.submit_date
                if not companies.submit_date:
                    data['submit_date'] = timezone.now()

                Companies.objects.update_or_create(
                    id=cid,
                    defaults={
                        # A项
                        'comp_type': data['comp_type'],
                        'profess_category': data['profess_category'],
                        'social_num': data['social_num'],
                        'org_num': data['org_num'],
                        'name': data['name'],
                        'legal_person': data['legal_person'],
                        'est_year': data['est_year'],
                        'est_month': data['est_month'],
                        'landline_area_code': data['landline_area_code'],
                        'landline_num': data['landline_num'],
                        'landline_branch_num': data['landline_branch_num'],
                        'mobile': data['mobile'],
                        'fax_code': data['fax_code'],
                        'fax_branch_code': data['fax_branch_code'],
                        'postalcode': data['postalcode'],
                        'website': data['website'],
                        'province': data['province'],
                        'city': data['city'],
                        'district': data['district'],
                        'address': data['address'],
                        'street_district': data['street_district'],
                        'community': data['community'],
                        'register_province': data['register_province'],
                        'register_city': data['register_city'],
                        'register_district': data['register_district'],
                        'register_address': data['register_address'],
                        'register_street_district': data['register_street_district'],
                        'register_community': data['register_community'],
                        'operate_status': data['operate_status'],
                        'main_activity_1': data['main_activity_1'],
                        'org_type': data['org_type'],
                        'register_type': data['register_type'],
                        'is_piling': data['is_piling'],
                        # B项
                        'retail_management_form': data['retail_management_form'],
                        'retail_management_brand': data['retail_management_brand'],
                        # 零售业态(最多选择三个)
                        'retail_opetrate_type': data['retail_opetrate_type'],
                        'retail_business_area': data['retail_business_area'],
                        'retail_hotel_diet_star': data['retail_hotel_diet_star'],
                        'retail_hotel_diet_area': data['retail_hotel_diet_area'],
                        # C项
                        'legal_unite_hkmatai': data['legal_unite_hkmatai'],
                        'legal_unite_hypotaxis': data['legal_unite_hypotaxis'],
                        'legal_unite_stake': data['legal_unite_stake'],
                        'accounting_rule': data['accounting_rule'],
                        'legal_unite_accounting_standard': data['legal_unite_accounting_standard'],
                        'is_higher_legal': data['is_higher_legal'],
                        'legal_unite_social_num': data['legal_unite_social_num'],
                        'legal_unite_org_num': data['legal_unite_org_num'],
                        'legal_unite_name': data['legal_unite_name'],
                        'has_branch': data['has_branch'],
                        # D项
                        'parent_type': data['parent_type'],
                        'parent_comp_social_num': data['parent_comp_social_num'],
                        'parent_comp_org_num': data['parent_comp_org_num'],
                        'parent_comp_name': data['parent_comp_name'],
                        'parent_comp_address': data['parent_comp_address'],
                        'branch_comp_count_obtainemploy': data['branch_comp_count_obtainemploy'],
                        'branch_comp_count_obtainemploy_female': data['branch_comp_count_obtainemploy_female'],
                        'branch_comp_operate_income': data['branch_comp_operate_income'],
                        'branch_comp_nooperate_defray': data['branch_comp_nooperate_defray'],
                        'branch_comp_house_sale_area': data['branch_comp_house_sale_area'],
                        'branch_comp_house_nosale_area': data['branch_comp_house_nosale_area'],
                        'interviewee': data['interviewee'],
                        'interviewee_contact': data['interviewee_contact'],
                        'modified_by': request.user,
                        'modified_date': timezone.now(),
                        'submit_date': data['submit_date'],
                        'complete_done': data['complete_done'],
                        'need_611_1': data['need_611_1'],
                        'need_611_2': data['need_611_2'],
                        'need_611_3': data['need_611_3'],
                        'need_611_4': data['need_611_4'],
                        'need_611_5': data['need_611_5'],
                        'need_611_6': data['need_611_6'],
                        'done_611': True,
                        'done_611_1': data['done_611_1'],
                        'done_611_2': data['done_611_2'],
                        'done_611_3': data['done_611_3'],
                        'done_611_4': data['done_611_4'],
                        'done_611_5': data['done_611_5'],
                        'done_611_6': data['done_611_6']
                    }
                )
                mid = cid

            if data['need_611_1'] == True:
                add_611_1(mid, data['comp_type'], data['social_num'], data['org_num'], data['name'], data['address'],
                          data['park_code'], data['mobile'], data['main_activity_1'], data['industry_code'])
            if data['operate_status'] != '6':
                has_complete_done(mid)
            response_data = {'next': mid, 'code': 0, 'msg': 'update success'}
            return JsonResponse(response_data, safe=False)
        else:
            response_data = {'next': '', 'code': -1, 'msg': form.errors}
            return JsonResponse(response_data, safe=False)
    else:
        print('hello world')

    return render(request, 'edit_com.html',
                  {'companies': companies, 'street_district': street_district, 'cid': cid, 'permission': permission})


# 删除611-1表的单个数据
def delete_611_1(request, cid):
    res = ActivityInfo.objects.filter(id=request.POST['comp_611_1_list_id']).delete()
    if res[0] == 1:
        response_data = {'next': '', 'code': 0, 'msg': 'delete success'}
        return JsonResponse(response_data, safe=False)
    else:
        response_data = {'next': '', 'code': -1, 'msg': 'delete fail'}
        return JsonResponse(response_data, safe=False)


# 填写或修改611-1表
@login_required
def edit_611_1(request, cid):
    companies = Companies.objects.get(id=cid)

    try:
        count = ActivityInfo.objects.filter(main_social_num=cid).count()
    except Companies.DoesNotExist:
        count = 0

    permission = get_permission(request.user.get_group_name.name)

    if request.method == 'POST':
        print(request.POST)
        form = ActivityInfoForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            main_social_num_id = Companies.objects.get(id=cid)
            if not data['inmanage_pay']:
                data['inmanage_pay'] = 0
            ActivityInfo.objects.update_or_create(
                main_social_num=main_social_num_id, name=data['name'],
                defaults={
                    'social_num': data['social_num'],
                    'org_num': data['org_num'],
                    'address': data['address'],
                    'mobile': data['mobile'],
                    'main_activity': data['main_activity'],
                    'incumbency_num': data['incumbency_num'],
                    'manage_income': data['manage_income'],
                    'inmanage_pay': data['inmanage_pay'],
                    'added_by': request.user,
                    'added_date': timezone.now(),
                    'modified_by': request.user,
                    'modified_date': timezone.now()
                }
            )

            # print(connection.queries)
            companies.done_611_1 = True
            companies.save()
            has_complete_done(cid)
            next = request.GET.get('next')
            response_data = {'next': next, 'code': 0, 'msg': 'update success'}
            return JsonResponse(response_data, safe=False)
        else:
            next = request.GET.get('next')
            response_data = {'next': next, 'code': -1, 'msg': form.errors}
            return JsonResponse(response_data, safe=False)

    else:
        print('611-1数据更新')

    activities = ActivityInfo.objects.filter(main_social_num=cid)
    print(activities)

    return render(request, "edit_611_1.html",
                  {'companies': companies, 'cid': cid, 'count': count, 'activities': activities,
                   'permission': permission})


# 填写或修改611-2表
@api_view(['GET', 'PUT', 'POST'])
@login_required
def edit_611_2(request, cid):
    companies = Companies.objects.get(id=cid)
    # print(companies)
    try:
        employeeobj = EmployeeUint.objects.get(main_social_num=cid)
    except EmployeeUint.DoesNotExist:
        employeeobj = ''

    permission = get_permission(request.user.get_group_name.name)

    if request.method == 'POST':
        form = EmployeeUintForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            if data['skill_count'] == '':
                data['skill_count'] = 0
            if data['technician_one'] == '':
                data['technician_one'] = 0
            if data['technician_two'] == '':
                data['technician_two'] = 0
            if data['technician_three'] == '':
                data['technician_three'] = 0
            if data['technician_four'] == '':
                data['technician_four'] = 0
            if data['technician_five'] == '':
                data['technician_five'] = 0

            EmployeeUint.objects.update_or_create(
                main_social_num=data['main_social_num'],
                defaults={'final_count_human': data['final_count_human'],
                          'final_count_female': data['final_count_female'],
                          'graduate': data['graduate'],
                          'bachelor': data['bachelor'],
                          'junior_college': data['junior_college'],
                          'skill_count': data['skill_count'],
                          'technician_one': data['technician_one'],
                          'technician_two': data['technician_two'],
                          'technician_three': data['technician_three'],
                          'technician_four': data['technician_four'],
                          'technician_five': data['technician_five'],
                          'added_by': request.user,
                          'added_date': timezone.now(),
                          'modified_by': request.user,
                          'modified_date': timezone.now()}
            )

            # print(connection.queries)
            companies.done_611_2 = True
            companies.save()
            has_complete_done(cid)
            next = request.GET.get('next')
            response_data = {'next': next, 'code': 0, 'msg': 'update success'}
            return JsonResponse(response_data, safe=False)
        else:
            response_data = {'next': '', 'code': -1, 'msg': form.errors}
            return JsonResponse(response_data, safe=False)
    else:
        print('hello world')

    return render(request, 'edit_611_2.html',
                  {'companies': companies, 'cid': cid, 'employeeobj': employeeobj, 'permission': permission})


# 填写或修改611-3表
@api_view(['GET', 'PUT', 'POST'])
@login_required
def edit_611_3(request, cid):
    companies = Companies.objects.get(id=cid)

    try:
        legalobj = legalPerson.objects.get(main_social_num=cid)
    except legalPerson.DoesNotExist:
        legalobj = ''

    is_plzc_write = is_piling = False
    if companies.profess_category == 'E' or companies.is_piling == '1':
        is_plzc_write = True
        if not companies.retail_hotel_diet_star and not companies.retail_hotel_diet_area:
            is_piling = True

    permission = get_permission(request.user.get_group_name.name)

    count_job = 0
    done_611_2 = True
    if companies.comp_type == '2':
        count_job = companies.branch_comp_count_obtainemploy
    else:
        # 如果需要填写611-2表但是没有填写，提示要填写611-2表
        if companies.need_611_2 == 'True' and companies.done_611_2 == 'False':
            done_611_2 = False
        else:
            try:
                employeobj = EmployeeUint.objects.get(main_social_num=cid)
                count_job = employeobj.final_count_human
            except EmployeeUint.DoesNotExist:
                done_611_2 = False



    if request.method == 'POST':
        form = legalPersonForm(request.POST)
        # print(form.is_valid());
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            main_social_num_id = Companies.objects.get(id=cid)

            if not data['piling_product_cost'] and not data['piling_product_sale'] and not data[
                'piling_product_online_sale'] and not data['piling_product_offline_sale'] and not data[
                'piling_product_stock'] and not data['piling_operate_turnover']:
                data['piling_product_cost'] = data['piling_product_sale'] = data['piling_product_online_sale'] = data[
                    'piling_product_offline_sale'] = data['piling_product_stock'] = data['piling_operate_turnover'] = 0

            if not data['catering_turnover'] and not data['catering_turnover_online'] and not data[
                'catering_guest_room'] and not data['catering_meals']:
                data['catering_turnover'] = data['catering_turnover_online'] = data['catering_guest_room'] = data[
                    'catering_meals'] = 0

            if data['piling_product_cost'] != '0':
                data['explain'] = ''

            legalPerson.objects.update_or_create(
                main_social_num=main_social_num_id,
                defaults={'added_tax_value': data['added_tax_value'],
                          'asset_all': data['asset_all'],
                          'business_cost': data['business_cost'],
                          'business_income': data['business_income'],
                          'business_profit': data['business_profit'],
                          'business_tax_more': data['business_tax_more'],
                          'catering_guest_room': data['catering_guest_room'],
                          'catering_meals': data['catering_meals'],
                          'catering_turnover': data['catering_turnover'],
                          'catering_turnover_online': data['catering_turnover_online'],
                          'debt_all': data['debt_all'],
                          'depreciation': data['depreciation'],
                          'doing_project': data['doing_project'],
                          'early_inventory': data['early_inventory'],
                          'end_inventory': data['end_inventory'],
                          'fixed_asset_value': data['fixed_asset_value'],
                          'invest_income': data['invest_income'],
                          'piling_operate_turnover': data['piling_operate_turnover'],
                          'piling_product_cost': data['piling_product_cost'],
                          'piling_product_offline_sale': data['piling_product_offline_sale'],
                          'piling_product_online_sale': data['piling_product_online_sale'],
                          'piling_product_sale': data['piling_product_sale'],
                          'piling_product_stock': data['piling_product_stock'],
                          'staff_wages': data['staff_wages'],
                          'staff_wages_explain': data['staff_wages_explain'],
                          'explain': data['explain'],
                          'added_by': request.user,
                          'added_date': timezone.now(),
                          'modified_by': request.user,
                          'modified_date': timezone.now()}
            )

            # print(connection.queries)
            companies.done_611_3 = True
            companies.save()
            has_complete_done(cid)
            next = request.GET.get('next')
            response_data = {'next': next, 'code': 0, 'msg': 'update success'}
            return JsonResponse(response_data, safe=False)
        else:
            response_data = {'next': '', 'code': -1, 'msg': form.errors}
            return JsonResponse(response_data, safe=False)
    else:
        print('hello world')

    return render(request, 'edit_611_3.html', {'companies': companies, 'cid': cid, 'legalobj': legalobj,
                                               'is_plzc_write': is_plzc_write, 'is_piling': is_piling,
                                               'permission': permission, 'done_611_2': done_611_2, 'count_job': count_job})


# 填写或修改611-4表
@login_required
def edit_611_4(request, cid):
    companies = Companies.objects.get(id=cid)

    try:
        fixedobj = fixedAsset.objects.get(main_social_num=cid)
        count = ProjectCount.objects.filter(main_social_num=cid).count()
    except fixedAsset.DoesNotExist:
        count = 0
        fixedobj = ''

    permission = get_permission(request.user.get_group_name.name)

    # ProjectCountModelFormset = modelformset_factory(ProjectCount, form=ProjectCountForm)
    # formset = ProjectCountModelFormset(request.POST or None, queryset=ProjectCount.objects.filter(main_social_num=cid))
    formset = ''
    if request.method == 'POST':
        form = fixedAssetForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                data = form.cleaned_data
                if data['complete_pay'] != 0:
                    data['explain'] = ''
                fixedAsset.objects.update_or_create(
                    main_social_num=data['main_social_num'],
                    defaults={'complete_pay': data['complete_pay'],
                              'plan_hundred': data['plan_hundred'],
                              'explain': data['explain'],
                              'added_by': request.user,
                              'added_date': timezone.now(),
                              'modified_by': request.user,
                              'modified_date': timezone.now()}
                )
                companies.done_611_4 = True
                companies.save()
                has_complete_done(cid)
                next = request.GET.get('next')
                response_data = {'next': next, 'code': 0, 'msg': 'update success'}
                return JsonResponse(response_data, safe=False)
            else:
                response_data = {'next': '', 'code': -1, 'msg': form.errors}
                return JsonResponse(response_data, safe=False)
            # if formset.is_valid():
            #     for formes in formset:
            #         projectObj = formes.save(commit=False)
            #         if formes.cleaned_data:
            #             projectObj.save()
            #     print(connection.queries)
        else:
            response_data = {'next': '', 'code': -1, 'msg': form.errors}
            return JsonResponse(response_data, safe=False)
    else:
        print('hello world')

    return render(request, 'edit_611_4.html',
                  {'companies': companies, 'cid': cid, 'fixedobj': fixedobj, 'count': count, 'formset': formset,
                   'permission': permission})


# 填写或修改611-5表
@login_required
def edit_611_5(request, cid):
    companies = Companies.objects.get(id=cid)

    try:
        nationobj = nationUnit.objects.get(main_social_num=cid)
    except nationUnit.DoesNotExist:
        nationobj = ''

    permission = get_permission(request.user.get_group_name.name)

    print(nationobj)
    if request.method == 'POST':

        form = nationUnitForm(request.POST)
        # print(form.is_valid());
        if form.is_valid():
            data = form.cleaned_data
            nationUnit.objects.update_or_create(
                main_social_num=data['main_social_num'],
                defaults={'area_building': data['area_building'],
                          'building': data['building'],
                          'current_assets': data['current_assets'],
                          'expend_labor_union': data['expend_labor_union'],
                          'expend_labour': data['expend_labor_union'],
                          'expend_management': data['expend_management'],
                          'expend_medical': data['expend_medical'],
                          'expend_retire': data['expend_retire'],
                          'expend_salary': data['expend_salary'],
                          'expend_service': data['expend_service'],
                          'expend_subsidy': data['expend_subsidy'],
                          'expend_taxes_additional': data['expend_taxes_additional'],
                          'expend_welfare': data['expend_welfare'],
                          'income_fiscal_appropriation': data['income_fiscal_appropriation'],
                          'income_manage': data['income_manage'],
                          'income_undertaking': data['income_undertaking'],
                          'intangible_assets_price': data['intangible_assets_price'],
                          'inventory_current_assets': data['inventory_current_assets'],
                          'inventory_early': data['inventory_early'],
                          'land_tenure': data['land_tenure'],
                          'machinery_equipment': data['machinery_equipment'],
                          'original_price': data['original_price'],
                          'permanent_investment': data['permanent_investment'],
                          'public_infrastructure': data['public_infrastructure'],
                          'public_infrastructure_accumulated_depreciation': data[
                              'public_infrastructure_accumulated_depreciation'],
                          'total_assets': data['total_assets'],
                          'total_expend': data['total_expend'],
                          'total_income': data['total_income'],
                          'total_liabilities': data['total_liabilities'],
                          'total_net_asset': data['total_net_asset'],
                          'transportation_equipment': data['transportation_equipment'],
                          'added_by': request.user,
                          'added_date': timezone.now(),
                          'modified_by': request.user,
                          'modified_date': timezone.now()}
            )
            print(connection.queries)

            companies.done_611_5 = True
            companies.save()
            has_complete_done(cid)
            next = request.GET.get('next')
            response_data = {'next': next, 'code': 0, 'msg': 'update success'}
            return JsonResponse(response_data, safe=False)
        else:
            response_data = {'next': '', 'code': -1, 'msg': form.errors}
            return JsonResponse(response_data, safe=False)

    else:
        print('hello world')

    return render(request, 'edit_611_5.html',
                  {'companies': companies, 'cid': cid, 'nationobj': nationobj, 'permission': permission})


# 填写或修改611-6表
@login_required
def edit_611_6(request, cid):
    companies = Companies.objects.get(id=cid)

    try:
        privateobj = privateUncommerciallyOrg.objects.get(main_social_num=cid)
    except privateUncommerciallyOrg.DoesNotExist:
        privateobj = ''

    permission = get_permission(request.user.get_group_name.name)

    if request.method == 'POST':
        form = privateUncommerciallyOrgForm(request.POST)
        # print(form.is_valid());
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            privateUncommerciallyOrg.objects.update_or_create(
                main_social_num=data['main_social_num'],
                defaults={'area_building': data['area_building'],
                          'building': data['building'],
                          'cultural_price': data['cultural_price'],
                          'current_assets': data['current_assets'],
                          'expend_action_current_expense': data['expend_action_current_expense'],
                          'expend_action_depreciation_assets': data['expend_action_depreciation_assets'],
                          'expend_action_salary': data['expend_action_salary'],
                          'expend_action_taxes': data['expend_action_taxes'],
                          'expend_management': data['expend_management'],
                          'expend_management_current_expense': data['expend_management_current_expense'],
                          'expend_management_depreciation_assets': data['expend_management_depreciation_assets'],
                          'expend_management_salary': data['expend_management_salary'],
                          'expend_management_taxes': data['expend_management_taxes'],
                          'income_donate': data['income_donate'],
                          'income_membership_fees': data['income_membership_fees'],
                          'intangible_price': data['intangible_price'],
                          'inventory_current_assets': data['inventory_current_assets'],
                          'inventory_early': data['inventory_early'],
                          'machinery_equipment': data['machinery_equipment'],
                          'net_asset_change': data['net_asset_change'],
                          'original_price': data['original_price'],
                          'permanent_investment': data['permanent_investment'],
                          'total_assets': data['total_assets'],
                          'total_income': data['total_income'],
                          'total_liabilities': data['total_liabilities'],
                          'total_net_asset': data['total_net_asset'],
                          'total_operational_action': data['total_operational_action'],
                          'total_this_year': data['total_this_year'],
                          'transportation_equipment': data['transportation_equipment'],
                          'added_by': request.user,
                          'added_date': timezone.now(),
                          'modified_by': request.user,
                          'modified_date': timezone.now()}

            )
            print(connection.queries)
            companies.done_611_6 = True
            companies.save()
            has_complete_done(cid)
            next = request.GET.get('next')
            response_data = {'next': next, 'code': 0, 'msg': 'update success'}
            return JsonResponse(response_data, safe=False)
        else:
            response_data = {'next': '', 'code': -1, 'msg': form.errors}
            return JsonResponse(response_data, safe=False)

    else:
        print('hello world')

    return render(request, 'edit_611_6.html',
                  {'companies': companies, 'cid': cid, 'privateobj': privateobj, 'permission': permission})


# 普查底册
@login_required
def baseline(request, district):
    comp_list = Companies.objects.filter(street_district__contains=district)[:10]
    return render(request, 'baseline.html', {'district': district, 'data': comp_list})


# 普查数据
@login_required
def basedata(request, street_district):
    comp_list = Companies.objects.filter(street_district__contains=street_district)

    permission = get_permission(request.user.get_group_name.name)

    return render(request, 'basedata.html',
                  {'street_district': street_district, 'data': comp_list, 'system_user': '2', 'permission': permission})

# 获取611-3表  文艺路营业利润大于0的企业名单
def get_all(request):
    clf_data = Companies.objects.filter(street_district__contains="长乐坊", complete_done=True, is_valid=True)
    all_clf_data = {}
    for clf in clf_data:
        clf_name = legalPerson.objects.filter(main_social_num=clf, business_profit__gt=0)
        all_clf_data.update({clf_name})


    return render(request, 'get_all.html',
                  {'all_clf_data': all_clf_data})