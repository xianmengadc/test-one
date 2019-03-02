from rest_framework import serializers
from .models import Companies, ActivityInfo, EmployeeUint, legalPerson, fixedAsset, nationUnit, privateUncommerciallyOrg


class CompaniesSerializer(serializers.ModelSerializer):


    class Meta:

        model = Companies

        fields = ('id', 'social_num', 'legal_unite_company_size', 'name', 'province', 'city', 'district', 'address',
                'street_district', 'community', 'building_unique_code', 'legal_person', 'mobile', 'comp_type',
                'accounting_rule', 'main_activity_1', 'main_activity_2', 'main_activity_3', 'need_611_1', 'need_611_2',
                'need_611_3', 'need_611_4', 'need_611_5', 'need_611_6', 'done_611', 'done_611_1', 'done_611_2', 'done_611_3',
                'done_611_4', 'done_611_5', 'done_611_6', 'interviewee', 'interviewee_contact', 'added_by',
                'modified_by', 'complete_done', 'is_valid')

        datatables_always_serialize = ('id', 'social_num', 'is_valid')

class ActivityInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityInfo

        fields = ('unit_category', 'social_num', 'org_num', 'name', 'address', 'zone_num', 'mobile', 'main_activity',
                  'main_social_num', 'catrgory_code', 'incumbency_num', 'manage_income', 'inmanage_pay')

class EmployeeUintSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeUint

        fields = ('main_social_num', 'final_count_human', 'final_count_female', 'graduate', 'bachelor', 'junior_college',
                  'skill_count', 'technician_one', 'technician_two', 'technician_three', 'technician_four','technician_five')

class legalPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = legalPerson

        fields = ('added_tax_value', 'asset_all', 'business_cost', 'business_income', 'business_profit', 'business_tax_more',
                  'catering_guest_room', 'catering_meals', 'catering_turnover', 'catering_turnover_online', 'debt_all',
                  'depreciation', 'doing_project', 'early_inventory', 'end_inventory', 'fixed_asset_value', 'invest_income',
                  'piling_operate_turnover', 'piling_product_cost', 'piling_product_offline_sale', 'piling_product_online_sale',
                  'piling_product_sale', 'piling_product_stock', 'staff_wages')

class fixedAssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = fixedAsset
        fields = '__all__'

class nationUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = nationUnit

        fields = ('area_building', 'building', 'current_assets', 'expend_labor_union', 'expend_labour', 'expend_management',
                  'expend_medical', 'expend_retire', 'expend_salary', 'expend_service', 'expend_subsidy',
                  'expend_taxes_additional', 'expend_welfare', 'income_fiscal_appropriation', 'income_manage',
                  'income_undertaking', 'intangible_assets_price', 'inventory_current_assets', 'inventory_early',
                  'land_tenure', 'machinery_equipment', 'main_social_num', 'original_price', 'permanent_investment',
                  'public_infrastructure', 'public_infrastructure_accumulated_depreciation', 'total_assets',
                  'total_expend', 'total_income', 'total_liabilities', 'total_net_asset', 'transportation_equipment')

class privateUncommerciallyOrgSerializer(serializers.ModelSerializer):

    class Meta:
        model = privateUncommerciallyOrg

        fields = ('area_building', 'building', 'cultural_price', 'current_assets', 'expend_action_current_expense',
                  'expend_action_depreciation_assets', 'expend_action_salary', 'expend_action_taxes', 'expend_management',
                  'expend_management_current_expense', 'expend_management_depreciation_assets', 'expend_management_salary',
                  'expend_management_taxes', 'income_donate', 'income_membership_fees', 'intangible_price',
                  'inventory_current_assets', 'inventory_early', 'machinery_equipment', 'main_social_num',
                  'net_asset_change', 'original_price', 'permanent_investment', 'total_assets', 'total_income',
                  'total_liabilities', 'total_net_asset', 'total_operational_action', 'total_this_year',
                  'transportation_equipment')
