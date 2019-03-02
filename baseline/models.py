from django.db import models
from django.contrib import admin
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

LIST_TYPE = (
    ('phase1', '清查底册一阶段'),
    ('phase2', '清查底册二阶段')
)

IS_CULTURE = (
    ('1', '是文化产业'),('2', '不是文化产业')
)

# 单位类型
COMP_TYPE = (
    ('1', '法人单位'), ('2', '产业活动单位')
)

IS_TRUE = (
    ('1', '是'), ('2', '否')
)

# 运营状态
OPERATE_STATUS = (
    ('1', '正常运营'), ('2', '停业歇业'), ('3', '筹建'), ('4', '当年关闭'),
    ('5', '当年破产'), ('6', '当年注销'), ('7', '当年吊销'), ('9', '其他')
)

# 机构类型
ORG_TYPE = (
    ('10', '企业'), ('20', '事业单位'), ('30', '机关'), ('40', '社会团体'),
    ('51', '民办非企业'), ('52', '基金会'), ('53', '居委会'), ('54', '村委会'), ('55', '农民专业合作社'),
    ('56', '农村集体经济组织'), ('90', '其他')
)

# 登记注册类型
REGISTER_TYPE = (
    ('110', '国有'), ('120', '集体'), ('130', '股份合作'), ('141', '国有联营'),
    ('142', '集体联营'), ('143', '国有与集体联营'), ('149', '其他联营'), ('151', '国有独资'),
    ('159', '其他有限责任公司'), ('160', '股份有限公司'), ('171', '私营独资'), ('172', '私营合伙'),
    ('173', '私营有限责任公司'), ('174', '私营股份有限公司'), ('190', '其他'), ('210', '与港澳台合资经营'),
    ('220', '与港澳台合作经营'), ('230', '港澳台独资'), ('240', '港澳台投资股份有限公司'), ('290', '其他港澳台投资'),
    ('310', '中外合资经营'), ('320', '中外合作经营'), ('330', '外资企业'), ('340', '外商投资股份有限公司'),
    ('390', '其他外商投资')
)

# 批发零售业的经营形式
MODE_OPERATION = (
    ('1', '独立门店'), ('2', '连锁总店[总部]'), ('3', '连锁直营店'), ('4', '连锁加盟店'), ('9', '其他')
)

# 零售业态  有店铺零售
RETAIL_STATUS = (
    ('1010', '食杂店'),('1020', '便利店'), ('1030', '折扣店'), ('1040', '超市'), ('1050', '大型超市'), ('1060', '仓储会员店'),
    ('1070', '百货店'), ('1080', '专业店'), ('1090', '专卖店'), ('1100', '家居建材商店'), ('1110', '购物中心'), ('1120', '厂家直销中心'),
    ('2010', '电视购物'),('2020', '邮购'), ('2030', '网上商店'), ('2040', '自动售货亭'), ('2050', '电话购物'), ('2090', '其他')
)

# 单位星级评定情况
STAR_LEVEL = (
    ('1', '一星'), ('2', '二星'), ('3', '三星'), ('4', '四星'), ('5', '五星'), ('9', '其他'),
)

#   隶属关系
INVEST = (
    ('1', '港商投资'),  ('2', '外商控股'),  ('3', '台商投资')
)

#   隶属关系
HYPOTAXIS = (
    ('10', '中央'),  ('11', '地方'),  ('90', '其他')
)

# 企业控股情况
STAKE = (
    ('1', '国有控股'),('2', '集体控股'),('3', '私人控股'),('4', '港澳台商控股'),('5', '外商控股'),('9', '其他')
)

# 执行会计标准类别
ACCOUNTING_RULE = (
    ('1', '企业会计制度'), ('2', '事业单位会计制度'), ('3', '行政单位会计制度'), ('4', '民间非营利组织会计制度'),
    ('9', '其他')
)

# 执行企业会计准则情况
ACCOUNTING_STANDARD = (
    ('0', '未知'), ('1', '执行企业会计准则'), ('2', '执行《小企业会计准则》'), ('3', '执行其他企业会计制度'), ('9', '执行其他企业会计制度')
)

# 单位规模
COMPANY_SIZE = (
    ('1', '大型'),('2', '中型'),('3', '小型'),('4', '微型'),
)

# 单位类别
PARENT_TYPE = (('1', '法人单位本部'), ('2','法人单位下属其他产业活动单位'))

# 专业类别
PROFESS_CATEGORY =(
    ('A', '农业'), ('B', '工业'), ('C', '建筑业'), ('E', '批发和零售业'), ('S', '住宿和餐饮业'), ('X', '房地产开发经营业'),
    ('H', '投资'), ('I', '劳资'), ('L', '社科文'), ('F', '服务业'), ('J', '名录库'), ('Z', '请选择')
)

STREET_DISTRICT = (
    ('1', '南院门'), ('2', '柏树林'), ('3', '长乐坊'), ('4', '东关南'),
    ('5', '太乙路'), ('6', '文艺路'), ('7', '长安路'), ('8', '张家村'),
)

# 611主表单位基本情况(阶段1)
class Companies(models.Model):
    # 法人单位和产业活动单位  start
    # 法人基本信息
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name="单位详细名称")
    social_num = models.CharField(max_length=64, blank=True, null=True, verbose_name="统一社会信用代码")
    org_num = models.CharField(max_length=64, blank=True, null=True, verbose_name="组织机构代码", help_text='没有统一社会信用代码则需填写组织机构代码')
    legal_person = models.CharField(max_length=32, blank=True, null=True, verbose_name="法定代表人")
    est_year = models.CharField(max_length=12, blank=True, null=True, verbose_name="开业成立时间-年")
    est_month = models.CharField(max_length=12, blank=True, null=True, verbose_name="开业成立时间-月")
    industry_category = models.CharField(max_length=64, blank=True, null=True, verbose_name="行业类别")

    # 联系信息
    landline_area_code = models.CharField(max_length=12, blank=True, null=True, verbose_name="长途区号")
    landline_num = models.CharField(max_length=32, blank=True, null=True, verbose_name="固定电话")
    landline_branch_num = models.CharField(max_length=32, blank=True, null=True, verbose_name="电话分机")
    mobile = models.CharField(max_length=32, blank=True, null=True, verbose_name="移动电话")
    fax_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="传真号码")
    fax_branch_code = models.CharField(max_length=64, blank=True, null=True, verbose_name="传真分机")
    postalcode = models.CharField(max_length=32, blank=True, null=True, verbose_name="邮政编码")
    email = models.EmailField(blank=True, null=True, verbose_name="电子邮箱")
    website = models.CharField(max_length=32, blank=True, null=True,verbose_name="网址")

    # 单位所在地信息
    province = models.CharField(max_length=32, default="陕西省", verbose_name="单位所在地-省(自治区、直辖市)")
    city = models.CharField(max_length=32, default="西安市", verbose_name="单位所在地-市(地、州、盟)")
    district = models.CharField(max_length=32, default="碑林区", verbose_name="单位所在地-县(市、区、旗)")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="单位所在地-街(村)、门牌号")
    street_district = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位所在地-街道办事处")
    community = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位所在地-社区(居委会)")
    district_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位所在地区划代码")
    survey_area_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位所在地-普查小区代码")
    building_area_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位所在地-建筑物编码")
    building_unique_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="平台端建筑物唯一编码")
    park_name = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位所在地-园区企业所属园区详细名称")
    park_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位所在地-所属园区代码")

    # 注册地信息
    register_province = models.CharField(max_length=32, blank=True, null=True, default="陕西省", verbose_name="单位注册地-省(自治区、直辖市)")
    register_city = models.CharField(max_length=32, blank=True, null=True, default="西安市", verbose_name="单位注册地-市(地、州、盟)")
    register_district = models.CharField(max_length=32, blank=True, null=True, default="碑林区", verbose_name="单位注册地-县(市、区、旗)")
    register_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="单位注册地-街(村)、门牌号")
    register_street_district = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位注册地-街道办事处")
    register_community = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位注册地-社区(居委会)")
    register_district_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位注册地区划代码")
    register_survey_area_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位注册地-普查小区代码")
    register_building_area_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位注册地-建筑物编码")
    register_park_name = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位注册地-园区企业所属园区详细名称")
    register_park_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="单位注册地-所属园区代码")

    # 运营状态
    operate_status = models.CharField(max_length=12, choices=OPERATE_STATUS, default='1', blank=True, null=True,verbose_name="运营状态")

    # 行业信息
    main_activity_1 = models.CharField(max_length=128, blank=True, null=True, verbose_name="核实后主要业务活动1")
    main_activity_2 = models.CharField(max_length=128, blank=True, null=True, verbose_name="核实后主要业务活动2")
    main_activity_3 = models.CharField(max_length=128, blank=True, null=True, verbose_name="核实后主要业务活动3")
    industry_code = models.CharField(max_length=128, blank=True, null=True, verbose_name="核实后行业代码")
    industry_name = models.CharField(max_length=128, blank=True, null=True, verbose_name="核实后行业名称")
    economic_code = models.CharField(max_length=128, blank=True, null=True, verbose_name="核实后经济活动代码")
    economic_name = models.CharField(max_length=128, blank=True, null=True, verbose_name="核实后经济活动名称")
    is_culture = models.CharField(max_length=12, choices=IS_CULTURE, blank=True, null=True, verbose_name="是否文化产业单位")

    # 单位类型与成立时间
    org_type = models.CharField(max_length=12, choices=ORG_TYPE, default='10', blank=True, null=True, verbose_name="机构类型")
    register_type = models.CharField(max_length=12, choices=REGISTER_TYPE, default='110', blank=True, null=True, verbose_name="登记注册类型")
    comp_type = models.CharField(max_length=12, choices=COMP_TYPE, default='1', blank=True, null=True, verbose_name="单位类型")
    # 法人单位和产业活动单位  end

    # 批发零售业  start
    retail_management_form = models.CharField(max_length=12, choices=MODE_OPERATION, default='1', blank=True, null=True, verbose_name="批零单位经营形式")
    retail_management_brand = models.CharField(max_length=255, blank=True, null=True, verbose_name="连锁品牌", help_text="经营形式选择2,3.4的单位填报", error_messages={"required":"请填写XXXX"})
    retail_opetrate_type = models.CharField(max_length=32, choices=RETAIL_STATUS, blank=True, null=True, verbose_name="零售业态（可多选，不超过3个）")
    retail_business_area = models.CharField(max_length=12, blank=True, null=True, verbose_name="批零业营业面积", help_text="批发零售业填报")
    retail_hotel_diet_star = models.CharField(max_length=12, choices=STAR_LEVEL, blank=True, null=True, verbose_name="住宿单位星级评定", help_text="住宿业单位填报")
    retail_hotel_diet_area = models.CharField(max_length=12, blank=True, null=True, verbose_name="住宿和餐饮业营业面积", help_text="住宿和餐饮业单位填报")
    # 批发零售业  end

    # 法人单位填报  start
    legal_unite_hkmatai = models.CharField(max_length=32, choices=INVEST, default='1', blank=True, null=True, verbose_name="港澳台商投资情况", help_text="限港澳台商投资企业填报")
    legal_unite_hypotaxis = models.CharField(max_length=12, choices=HYPOTAXIS, default='10',blank=True, null=True, verbose_name="隶属关系")
    legal_unite_stake = models.CharField(max_length=12, choices=STAKE, default='1',blank=True, null=True, verbose_name="企业控股情况")
    accounting_rule = models.CharField(max_length=12, choices=ACCOUNTING_RULE, default='1',blank=True, null=True, verbose_name="执行会计标准类别")
    accounting_rule_note = models.CharField(max_length=32, blank=True, null=True, verbose_name="执行会计标准类别-注明")
    legal_unite_accounting_standard = models.CharField(max_length=12, choices=ACCOUNTING_STANDARD, default='1',blank=True, null=True, verbose_name="执行企业会计准则情况")
    legal_unite_company_size = models.CharField(max_length=12, choices=COMPANY_SIZE, default='1',blank=True, null=True, verbose_name="单位规模")
    legal_unite_obtainemploy = models.CharField(max_length=255, blank=True, null=True, verbose_name="从业人员人数")
    legal_unite_obtainemploy_female = models.CharField(max_length=255, blank=True, null=True, verbose_name="从业人员人数(女性)")
    is_higher_legal = models.BooleanField(default=False, verbose_name="是否有上级法人")
    legal_unite_social_num = models.CharField(max_length=255, blank=True, null=True, verbose_name="上级法人统一社会信用代码")
    legal_unite_org_num = models.CharField(max_length=255, blank=True, null=True, verbose_name="上级法人组织机构代码")
    legal_unite_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="上级法人单位详细名称")
    legal_unite_person_income = models.CharField(max_length=255, blank=True, null=True, verbose_name="营业收入", help_text="企业法人单位填报")
    legal_unite_person_assets = models.CharField(max_length=255, blank=True, null=True, verbose_name="资产总计", help_text="企业法人单位填报")
    legal_unite_person_taxes = models.CharField(max_length=255, blank=True, null=True, verbose_name="税金及附加", help_text="企业法人单位填报")
    legal_unite_nonperson_defray = models.CharField(max_length=255, blank=True, null=True, verbose_name="单位支出（费用）", help_text="非企业法人单位填报")
    legal_unite_nonperson_assets = models.CharField(max_length=255, blank=True, null=True, verbose_name="资产总计", help_text="非企业法人单位填报")
    has_branch = models.CharField(max_length=64, choices=IS_TRUE, default='1', blank=True, null=True,verbose_name="是否有下属产业活动单位")
    # 法人单位填报  end

    # 产业活动单位归属法人情况及主要经济指标  start
    branch_cnt = models.CharField(max_length=12, blank=True, null=True, verbose_name="贵单位本部和下属产业活动单位数量")
    branch_type = models.CharField(max_length=12, blank=True, null=True, verbose_name="产业活动单位填写-单位类别")
    parent_type = models.CharField(max_length=12, choices=PARENT_TYPE, default='1', blank=True, null=True, verbose_name="归属法人单位-单位类别")
    parent_comp_social_num = models.CharField(max_length=32, blank=True, null=True, verbose_name="归属法人单位-统一社会信用代码")
    parent_comp_org_num = models.CharField(max_length=32, blank=True, null=True, verbose_name="归属法人单位-组织机构代码")
    parent_comp_name = models.CharField(max_length=128, blank=True, null=True, verbose_name="归属法人单位-详细名称")
    parent_comp_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="归属法人单位-详细地址")
    parent_comp_district_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="归属法人单位-区划代码")
    branch_comp_social_num = models.CharField(max_length=32, blank=True, null=True, verbose_name="下属产业活动单位-统一社会信用代码")
    branch_comp_org_num = models.CharField(max_length=32, blank=True, null=True, verbose_name="下属产业活动单位-组织机构代码")
    branch_comp_name = models.CharField(max_length=128, blank=True, null=True, verbose_name="下属产业活动单位-详细名称")
    branch_comp_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="下属产业活动单位-详细地址")
    branch_comp_district_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="下属产业活动单位-区划代码")
    branch_comp_count_obtainemploy = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name="从业人员人数")
    branch_comp_count_obtainemploy_female = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name="从业人员人数(女性)")

    branch_comp_operate_income = models.PositiveIntegerField(null=True, blank=True, default=0, verbose_name="经营性单位收入", help_text='经营性单位填报')
    branch_comp_nooperate_defray = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name="非经营性支出", help_text='非经营性单位填报')
    branch_comp_house_sale_area = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name="商品房销售面积", help_text='房地产开发经营产业活动单位填报')
    branch_comp_house_nosale_area = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name="商品房待销售面积", help_text='房地产开发经营产业活动单位填报')
    # 产业活动单位归属法人情况及主要经济指标  end

    is_notice = models.BooleanField(default=False, verbose_name="是否通知")
    is_piling = models.CharField(max_length=64, choices=IS_TRUE, default='1', blank=True, null=True, verbose_name="是否为批零住餐单位")

    data_process_place = models.CharField(max_length=32, blank=True, null=True, verbose_name="数据处理地")
    as_legal_person = models.BooleanField(default=False, verbose_name="是否视同法人单位")
    produce_energy = models.BooleanField(default=False,  verbose_name="是否生产能源产品")
    sell_energy = models.BooleanField(default=False, verbose_name="是否经销能源商品")
    involved_military = models.BooleanField(default=False,  verbose_name="是否民参军单位")
    is_orphan = models.BooleanField(default=False, verbose_name="是否为孤儿产业")

    unique_code = models.CharField(max_length=64, blank=True, null=True, verbose_name="底册唯一标识码")
    profess_category = models.CharField(max_length=64, choices=PROFESS_CATEGORY, default='Z', blank=True, null=True, verbose_name="专业类别")
    data_source = models.CharField(max_length=64, blank=True, null=True, verbose_name="资料来源")
    interviewee = models.CharField(max_length=32, blank=True, null=True, verbose_name="申报人")
    interviewee_contact = models.CharField(max_length=32, blank=True, null=True, verbose_name="申报人联系电话")
    recorded_date = models.DateField(blank=True, null=True, verbose_name="填表日期")

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="录入员", related_name="recorded_created_user")
    added_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="录入时间")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="修改员", related_name="recorded_modified_user")
    modified_date = models.DateTimeField(auto_now_add=True, blank=True, null=True,  verbose_name="修改时间")
    submit_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="首次完成时间")
    is_valid = models.BooleanField(blank=True, null=True, verbose_name="是否有效")

    record_type = models.CharField(max_length=12, blank=True, null=True, choices=LIST_TYPE, verbose_name="底册信息类型")
    complete_done = models.BooleanField(default=False, verbose_name="是否完全完成")

    done_611 = models.BooleanField(default=False, verbose_name="是否已完成611表")
    done_611_1 = models.BooleanField(default=False, verbose_name="是否已完成611-1表")
    done_611_2 = models.BooleanField(default=False, verbose_name="是否已完成611-2表")
    done_611_3 = models.BooleanField(default=False, verbose_name="是否已完成611-3表")
    done_611_4 = models.BooleanField(default=False, verbose_name="是否已完成611-4表")
    done_611_5 = models.BooleanField(default=False, verbose_name="是否已完成611-5表")
    done_611_6 = models.BooleanField(default=False, verbose_name="是否已完成611-6表")

    need_611_1 = models.BooleanField(default=False, verbose_name="是否需要填写611-1表")
    need_611_2 = models.BooleanField(default=False, verbose_name="是否需要填写611-2表")
    need_611_3 = models.BooleanField(default=False, verbose_name="是否需要填写611-3表")
    need_611_4 = models.BooleanField(default=False, verbose_name="是否需要填写611-4表")
    need_611_5 = models.BooleanField(default=False, verbose_name="是否需要填写611-5表")
    need_611_6 = models.BooleanField(default=False, verbose_name="是否需要填写611-6表")

    class Meta:
        verbose_name = "611主表单位基本情况(阶段1)"
        verbose_name_plural = "611主表单位基本情况(阶段1)"
        permissions = (

            ('can_view_nym_baseline', '可以浏览所有南院门企业普查'),
            ('can_edit_nym_baseline', '可以编辑所有南院门企业普查'),
            ('can_add_nym_baseline', '可以添加所以南院门企业普查'),

            ('can_view_bsl_baseline', '可以浏览所有柏树林企业普查'),
            ('can_edit_bsl_baseline', '可以编辑所有柏树林企业普查'),
            ('can_add_bsl_baseline', '可以添加所以柏树林企业普查'),

            ('can_view_clf_baseline', '可以浏览所有长乐坊企业普查'),
            ('can_edit_clf_baseline', '可以编辑所有长乐坊企业普查'),
            ('can_add_clf_baseline', '可以添加所以长乐坊企业普查'),

            ('can_view_dgn_baseline', '可以浏览所有东关南企业普查'),
            ('can_edit_dgn_baseline', '可以编辑所有东关南企业普查'),
            ('can_add_dgn_baseline', '可以添加所以东关南企业普查'),

            ('can_view_tyl_baseline', '可以浏览所有太乙路企业普查'),
            ('can_edit_tyl_baseline', '可以编辑所有太乙路企业普查'),
            ('can_add_tyl_baseline', '可以添加所以太乙路企业普查'),

            ('can_view_wyl_baseline', '可以浏览所有文艺路企业普查'),
            ('can_edit_wyl_baseline', '可以编辑所有文艺路企业普查'),
            ('can_add_wyl_baseline', '可以添加所以文艺路企业普查'),

            ('can_view_cal_baseline', '可以浏览所有长安路企业普查'),
            ('can_edit_cal_baseline', '可以编辑所有长安路企业普查'),
            ('can_add_cal_baseline', '可以添加所以长安路企业普查'),

            ('can_view_zjc_baseline', '可以浏览所有张家村企业普查'),
            ('can_edit_zjc_baseline', '可以编辑所有张家村企业普查'),
            ('can_add_zjc_baseline', '可以添加所以张家村企业普查'),

            ('can_view_xxxq_baseline', '可以浏览所有西咸新区企业普查'),
            ('can_edit_xxxq_baseline', '可以编辑所有西咸新区企业普查'),
            ('can_add_xxxq_baseline', '可以添加所以西咸新区企业普查'),

        )

    @property
    def multi_branch(self):
        if self.branch_cnt:
            multi_branch = '是'
        else:
            multi_branch = '否'
        return multi_branch

    # @property
    # def need_611_1(self):
    #     if self.branch_cnt:
    #         need_611_1 = '是'
    #     else:
    #         need_611_1 = '否'
    #     return need_611_1
    #
    # @property
    # def need_611_3(self):
    #     if self.org_type == '10' or self.org_type == '90' \
    #             or self.org_type == '55' \
    #             or self.org_type == '56' or self.accounting_rule == '1':
    #         need_611_3 = '是'
    #     else:
    #         need_611_3 = '否'
    #     return need_611_3
    #
    # @property
    # def need_611_5(self):
    #     if self.org_type == '30' or self.org_type == '53' \
    #             or self.org_type == '54' or self.accounting_rule == '2' or self.accounting_rule == '3':
    #         need_611_5 = '是'
    #     else:
    #         need_611_5 = '否'
    #     return need_611_5
    #
    # @property
    # def need_611_6(self):
    #     if self.accounting_rule == '4' or self.accounting_rule == '9' \
    #             or self.org_type == '40':
    #         need_611_6 = '是'
    #     else:
    #         need_611_6 = '否'
    #     return need_611_6

    def __str__(self):
        return ' {} - {} -  {} - {} - {} - {} '.\
            format( self.social_num,  self.name, self.district, self.legal_person, self.mobile, self.main_activity_1)

class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('id', 'record_type', 'is_valid', 'industry_category', 'submit_date', 'street_district', 'modified_by', 'modified_date', 'social_num', 'name', 'address',
                    'street_district', 'community', 'legal_person', 'mobile', 'comp_type',
                    'accounting_rule', 'main_activity_1', 'done_611', 'done_611_1',
                    'done_611_2', 'done_611_3', 'done_611_4', 'done_611_5', 'done_611_6', 'need_611_1', 'need_611_2',
                    'need_611_3', 'need_611_4', 'need_611_5', 'need_611_6')

    list_filter = ('record_type', 'street_district', 'is_valid', 'industry_category')
    search_fields = ('name', 'social_num')


# 611-1法人单位所属产业活动单位情况
class ActivityInfo(models.Model):

    main_social_num = models.ForeignKey(Companies, on_delete=models.CASCADE, default="12432", verbose_name="统一社会信用代码", help_text="主表的统一社会信用代码")

    unit_category = models.CharField(max_length=128, blank=True, null=True, verbose_name="单位类别")
    social_num = models.CharField(max_length=128, blank=True, null=True, verbose_name="统一社会信用代码")
    org_num = models.CharField(max_length=128, blank=True, null=True, verbose_name="组织机构代码")
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name="单位详细名称*")
    address = models.CharField(max_length=128, blank=True, null=True, verbose_name="详细地址*")
    zone_num = models.CharField(max_length=128, blank=True, null=True, verbose_name="区划代码")
    mobile = models.CharField(max_length=128, blank=True, null=True, verbose_name="联系电话*")
    main_activity = models.CharField(max_length=128, blank=True, null=True, verbose_name="主要业务活动*")
    catrgory_code = models.CharField(max_length=128, blank=True, null=True, verbose_name="行业代码（GB/T4754-2017*")
    incumbency_num = models.PositiveIntegerField(blank=True, null=False, default=0, verbose_name="从业人员期末人数*")
    manage_income = models.PositiveIntegerField(blank=True, null=False, default=0, verbose_name="经营性单位收入*")
    inmanage_pay = models.PositiveIntegerField(blank=True, null=False, default=0, verbose_name="非经营性单位支出*")

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="录入员", related_name="activity_created_by")
    added_date = models.DateTimeField(auto_now_add=True, blank=True, null=True,  verbose_name="录入时间")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE, verbose_name="修改员", related_name="acitvity_modified_by")
    modified_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "611-1法人单位所属产业活动单位情况(详细信息)"
        verbose_name_plural = "611-1法人单位所属产业活动单位情况(详细信息)"
        permissions = (

            ('can_activity_view_nym_baseline', '可以浏览所有南院门产业活动单位情况'),
            ('can_activity_edit_nym_baseline', '可以编辑所有南院门产业活动单位情况'),
            ('can_activity_add_nym_baseline', '可以添加所以南院门产业活动单位情况'),

            ('can_activity_view_bsl_baseline', '可以浏览所有柏树林产业活动单位情况'),
            ('can_activity_edit_bsl_baseline', '可以编辑所有柏树林产业活动单位情况'),
            ('can_activity_add_bsl_baseline', '可以添加所以柏树林产业活动单位情况'),

            ('can_activity_view_clf_baseline', '可以浏览所有长乐坊产业活动单位情况'),
            ('can_activity_edit_clf_baseline', '可以编辑所有长乐坊产业活动单位情况'),
            ('can_activity_add_clf_baseline', '可以添加所以长乐坊产业活动单位情况'),

            ('can_activity_view_dgn_baseline', '可以浏览所有东关南产业活动单位情况'),
            ('can_activity_edit_dgn_baseline', '可以编辑所有东关南产业活动单位情况'),
            ('can_activity_add_dgn_baseline', '可以添加所以东关南产业活动单位情况'),

            ('can_activity_view_tyl_baseline', '可以浏览所有太乙路产业活动单位情况'),
            ('can_activity_edit_tyl_baseline', '可以编辑所有太乙路产业活动单位情况'),
            ('can_activity_add_tyl_baseline', '可以添加所以太乙路产业活动单位情况'),

            ('can_activity_view_wyl_baseline', '可以浏览所有文艺路产业活动单位情况'),
            ('can_activity_edit_wyl_baseline', '可以编辑所有文艺路产业活动单位情况'),
            ('can_activity_add_wyl_baseline', '可以添加所以文艺路产业活动单位情况'),

            ('can_activity_view_cal_baseline', '可以浏览所有长安路产业活动单位情况'),
            ('can_activity_edit_cal_baseline', '可以编辑所有长安路产业活动单位情况'),
            ('can_activity_add_cal_baseline', '可以添加所以长安路产业活动单位情况'),

            ('can_activity_view_zjc_baseline', '可以浏览所有张家村产业活动单位情况'),
            ('can_activity_edit_zjc_baseline', '可以编辑所有张家村产业活动单位情况'),
            ('can_activity_add_zjc_baseline', '可以添加所以张家村产业活动单位情况'),

            ('can_activity_view_xxxj_baseline', '可以浏览所有西咸新区产业活动单位情况'),
            ('can_activity_edit_xxxj_baseline', '可以编辑所有西咸新区产业活动单位情况'),
            ('can_activity_add_xxxj_baseline', '可以添加所以西咸新区产业活动单位情况'),

        )

    @property
    def get_user_info(self):
        return self.main_social_num.added_by

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.social_num, self.name, self.address, self.mobile, self.main_activity)

class ActivityInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_user_info', 'social_num', 'org_num', 'mobile', 'main_activity')
    list_filter = ('name', 'social_num')

# 611-2表单位从业人员情况
class EmployeeUint(models.Model):
    main_social_num = models.ForeignKey(Companies, on_delete=models.CASCADE, default="12432",verbose_name="统一社会信用代码", help_text="主表的统一社会信用代码")

    final_count_human = models.PositiveIntegerField(blank=True, null=True, verbose_name="从业人员期末人数")
    final_count_female = models.PositiveIntegerField(blank=True, null=True, verbose_name="女性人数")
    graduate = models.PositiveIntegerField(blank=True, null=True, verbose_name="研究生学历人员")
    bachelor = models.PositiveIntegerField(blank=True, null=True, verbose_name="大学本科学历人员")
    junior_college = models.PositiveIntegerField(blank=True, null=True, verbose_name="大学专科学历人员")
    skill_count = models.PositiveIntegerField(blank=True, null=True, verbose_name="技能人员")
    technician_one = models.PositiveIntegerField(blank=True, null=True, verbose_name="高级技师", help_text="国家职业资格一级")
    technician_two = models.PositiveIntegerField(blank=True, null=True, verbose_name="技师", help_text="国家职业资格二级")
    technician_three = models.PositiveIntegerField(blank=True, null=True, verbose_name="高级技能人员", help_text="国家职业资格三级")
    technician_four = models.PositiveIntegerField(blank=True, null=True, verbose_name="中级技能人员", help_text="国家职业资格四级")
    technician_five = models.PositiveIntegerField(blank=True, null=True, verbose_name="初级技能人员", help_text="国家职业资格五级")

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name="录入员", related_name="employee_created_by")
    added_date = models.DateTimeField(auto_now_add=True, blank=True, null=True,  verbose_name="录入时间")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                                    verbose_name="修改员", related_name="employee_modified_by")
    modified_date = models.DateTimeField(auto_now_add=True, blank=True, null=True,  verbose_name="修改时间")

    class Meta:
        verbose_name = "611-2表单位从业人员情况"
        verbose_name_plural = "611-2表单位从业人员情况"

        permissions = (

            ('can_employee_view_nym_baseline', '可以浏览所有南院门单位从业人员情况'),
            ('can_employee_edit_nym_baseline', '可以编辑所有南院门单位从业人员情况'),
            ('can_employee_add_nym_baseline', '可以添加所以南院门单位从业人员情况'),

            ('can_employee_view_bsl_baseline', '可以浏览所有柏树林单位从业人员情况'),
            ('can_employee_edit_bsl_baseline', '可以编辑所有柏树林单位从业人员情况'),
            ('can_employee_add_bsl_baseline', '可以添加所以柏树林单位从业人员情况'),

            ('can_employee_view_clf_baseline', '可以浏览所有长乐坊单位从业人员情况'),
            ('can_employee_edit_clf_baseline', '可以编辑所有长乐坊单位从业人员情况'),
            ('can_employee_add_clf_baseline', '可以添加所以长乐坊单位从业人员情况'),

            ('can_employee_view_dgn_baseline', '可以浏览所有东关南单位从业人员情况'),
            ('can_employee_edit_dgn_baseline', '可以编辑所有东关南单位从业人员情况'),
            ('can_employee_add_dgn_baseline', '可以添加所以东关南单位从业人员情况'),

            ('can_employee_view_tyl_baseline', '可以浏览所有太乙路单位从业人员情况'),
            ('can_employee_edit_tyl_baseline', '可以编辑所有太乙路单位从业人员情况'),
            ('can_employee_add_tyl_baseline', '可以添加所以太乙路单位从业人员情况'),

            ('can_employee_view_wyl_baseline', '可以浏览所有文艺路单位从业人员情况'),
            ('can_employee_edit_wyl_baseline', '可以编辑所有文艺路单位从业人员情况'),
            ('can_employee_add_wyl_baseline', '可以添加所以文艺路单位从业人员情况'),

            ('can_employee_view_cal_baseline', '可以浏览所有长安路单位从业人员情况'),
            ('can_employee_edit_cal_baseline', '可以编辑所有长安路单位从业人员情况'),
            ('can_employee_add_cal_baseline', '可以添加所以长安路单位从业人员情况'),

            ('can_employee_view_zjc_baseline', '可以浏览所有张家村单位从业人员情况'),
            ('can_employee_edit_zjc_baseline', '可以编辑所有张家村单位从业人员情况'),
            ('can_employee_add_zjc_baseline', '可以添加所以张家村单位从业人员情况'),

            ('can_employee_view_xxxq_baseline', '可以浏览所有西咸新区单位从业人员情况'),
            ('can_employee_edit_xxxq_baseline', '可以编辑所有西咸新区单位从业人员情况'),
            ('can_employee_add_xxxq_baseline', '可以添加所以西咸新区单位从业人员情况'),

        )

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.final_count_human, self.final_count_female, self.graduate, self.bachelor, self.skill_count)

class EmployeeUintAdmin(admin.ModelAdmin):
    list_display = ('main_social_num', 'final_count_human', 'final_count_human', 'skill_count')

    list_filter = ('final_count_human', 'final_count_human')


# 611-3表企业法人主要经济指标
class legalPerson(models.Model):
    # 基本信息
    main_social_num = models.ForeignKey(Companies, on_delete=models.CASCADE, default="12432343",verbose_name="统一社会信用代码", help_text="主表的统一社会信用代码")
    # 资产负债类（所有单位填报)
    depreciation = models.PositiveIntegerField(blank=True, null=True, verbose_name="本年折旧（资产负债类）", help_text="所有单位填报")
    fixed_asset_value = models.PositiveIntegerField(blank=True, null=True, verbose_name="固定资产净值（资产负债类）", help_text="所有单位填报")
    doing_project = models.PositiveIntegerField(blank=True, null=True, verbose_name="在建工程（资产负债类）", help_text="所有单位填报")
    asset_all = models.IntegerField(blank=True, null=True, verbose_name="资产总计（资产负债类）", help_text="所有单位填报")
    debt_all = models.IntegerField(blank=True, null=True, verbose_name="负债总计（资产负债类）", help_text="所有单位填报")
    early_inventory = models.IntegerField(blank=True, null=True, verbose_name="年初存货（资产负债类）", help_text="所有单位填报")
    end_inventory = models.IntegerField(blank=True, null=True, verbose_name="期末存货（资产负债类）", help_text="所有单位填报")

    # 损益分配、人工成本及增值税
    business_income = models.PositiveIntegerField(blank=True, null=True, verbose_name="营业收入", help_text="所有单位填报")
    business_cost = models.PositiveIntegerField(blank=True, null=True, verbose_name="营业成本", help_text="所有单位填报")
    business_tax_more = models.PositiveIntegerField(blank=True, null=True, verbose_name="税金及附加", help_text="所有单位填报")
    invest_income = models.IntegerField(blank=True, null=True, verbose_name="投资收益", help_text="所有单位填报")
    business_profit = models.IntegerField(blank=True, null=True, verbose_name="营业利润", help_text="所有单位填报")
    staff_wages = models.PositiveIntegerField(blank=True, null=True, verbose_name="应付职工薪酬", help_text="所有单位填报")
    added_tax_value = models.IntegerField(blank=True, null=True, verbose_name="应交增值税", help_text="所有单位填报")
    staff_wages_explain = models.CharField(max_length=255, blank=True, null=True, verbose_name="应付职工薪酬解释说明", help_text="应付职工薪酬为0时，或人均小于1w时，需要填报")

    # 批发业和零售业经营情况(仅批发和零售业填报)
    piling_product_cost = models.PositiveIntegerField(blank=True, null=True, verbose_name="商品购进额")
    piling_product_sale = models.PositiveIntegerField(blank=True, null=True, verbose_name="商品销售额")
    piling_product_online_sale = models.PositiveIntegerField(blank=True, null=True, verbose_name="线上销售额", help_text="通过公共网络实现的")
    piling_product_offline_sale = models.PositiveIntegerField(blank=True, null=True, verbose_name="零售额")
    piling_product_stock = models.PositiveIntegerField(blank=True, null=True, verbose_name="期末商品库存额")
    piling_operate_turnover = models.PositiveIntegerField(blank=True, null=True, verbose_name="服务营业额")

    # 住宿和餐饮业经营情况
    catering_turnover = models.PositiveIntegerField(blank=True, null=True, verbose_name="营业额")
    catering_turnover_online = models.PositiveIntegerField(blank=True, null=True, verbose_name="线上营业额", help_text="通过公共网络实现的")
    catering_guest_room = models.PositiveIntegerField(blank=True, null=True, verbose_name="客房收入")
    catering_meals = models.PositiveIntegerField(blank=True, null=True, verbose_name="餐费收入")
    explain = models.CharField(max_length=255, blank=True, null=True, verbose_name="商品购进额为0时的解释说明",
                               help_text="批零业商品购进额为0时填报")

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name="录入员", related_name="legal_created_by")
    added_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="录入时间")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                                    verbose_name="修改员", related_name="legal_modified_by")
    modified_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "611-3表企业法人主要经济指标"
        verbose_name_plural = "611-3表企业法人主要经济指标"
        permissions = (

            ('can_legal_view_nym_baseline', '可以浏览所有南院门企业法人主要经济指标'),
            ('can_legal_edit_nym_baseline', '可以编辑所有南院门企业法人主要经济指标'),
            ('can_legal_add_nym_baseline', '可以添加所以南院门企业法人主要经济指标'),

            ('can_legal_view_bsl_baseline', '可以浏览所有柏树林企业法人主要经济指标'),
            ('can_legal_edit_bsl_baseline', '可以编辑所有柏树林企业法人主要经济指标'),
            ('can_legal_add_bsl_baseline', '可以添加所以柏树林企业法人主要经济指标'),

            ('can_legal_view_clf_baseline', '可以浏览所有长乐坊企业法人主要经济指标'),
            ('can_legal_edit_clf_baseline', '可以编辑所有长乐坊企业法人主要经济指标'),
            ('can_legal_add_clf_baseline', '可以添加所以长乐坊企业法人主要经济指标'),

            ('can_legal_view_dgn_baseline', '可以浏览所有东关南企业法人主要经济指标'),
            ('can_legal_edit_dgn_baseline', '可以编辑所有东关南企业法人主要经济指标'),
            ('can_legal_add_dgn_baseline', '可以添加所以东关南企业法人主要经济指标'),

            ('can_legal_view_tyl_baseline', '可以浏览所有太乙路企业法人主要经济指标'),
            ('can_legal_edit_tyl_baseline', '可以编辑所有太乙路企业法人主要经济指标'),
            ('can_legal_add_tyl_baseline', '可以添加所以太乙路企业法人主要经济指标'),

            ('can_legal_view_wyl_baseline', '可以浏览所有文艺路企业法人主要经济指标'),
            ('can_legal_edit_wyl_baseline', '可以编辑所有文艺路企业法人主要经济指标'),
            ('can_legal_add_wyl_baseline', '可以添加所以文艺路企业法人主要经济指标'),

            ('can_legal_view_cal_baseline', '可以浏览所有长安路企业法人主要经济指标'),
            ('can_legal_edit_cal_baseline', '可以编辑所有长安路企业法人主要经济指标'),
            ('can_legal_add_cal_baseline', '可以添加所以长安路企业法人主要经济指标'),

            ('can_legal_view_zjc_baseline', '可以浏览所有张家村企业法人主要经济指标'),
            ('can_legal_edit_zjc_baseline', '可以编辑所有张家村企业法人主要经济指标'),
            ('can_legal_add_zjc_baseline', '可以添加所以张家村企业法人主要经济指标'),

            ('can_legal_view_xxxq_baseline', '可以浏览所有西咸新区企业法人主要经济指标'),
            ('can_legal_edit_xxxq_baseline', '可以编辑所有西咸新区企业法人主要经济指标'),
            ('can_legal_add_xxxq_baseline', '可以添加所以西咸新区企业法人主要经济指标'),

        )

    def __str__(self):
        return '{} - {} - {}'.format(self.main_social_num, self.asset_all, self.business_income)

class legalPersonAdmin(admin.ModelAdmin):
    list_diplay = ('main_social_num', 'depreciation', 'business_income', 'catering_turnover')
    list_filter = ('depreciation', 'business_income')


# 611-4表单位固定资产投资项目情况
class fixedAsset(models.Model):
    main_social_num = models.ForeignKey(Companies, on_delete=models.CASCADE, default="124323", verbose_name="统一社会信用代码", help_text="主表的统一社会信用代码")

    complete_pay = models.PositiveIntegerField(blank=True, null=True, verbose_name="单位财务支出法固定资产投资完成额")
    plan_hundred = models.PositiveIntegerField(blank=True, null=True, verbose_name="计划总投资500万以上")
    explain = models.CharField(max_length=255, blank=True, null=True, verbose_name="固定资产投资完成额说明", help_text="单位财务支出法固定资产投资完成额为0时填写")

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name="录入员", related_name="fixed_created_by")
    added_date = models.DateTimeField(auto_now_add=True, blank=True, null=True,  verbose_name="录入时间")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                                    verbose_name="修改员", related_name="fixed_modified_by")
    modified_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "611-4表单位固定资产投资项目情况"
        verbose_name_plural = "611-4表单位固定资产投资项目情况"
        permissions = (

            ('can_fixed_view_nym_baseline', '可以浏览所有南院门单位固定资产投资项目情况'),
            ('can_fixed_edit_nym_baseline', '可以编辑所有南院门单位固定资产投资项目情况'),
            ('can_fixed_add_nym_baseline', '可以添加所以南院门单位固定资产投资项目情况'),

            ('can_fixed_view_bsl_baseline', '可以浏览所有柏树林单位固定资产投资项目情况'),
            ('can_fixed_edit_bsl_baseline', '可以编辑所有柏树林单位固定资产投资项目情况'),
            ('can_fixed_add_bsl_baseline', '可以添加所以柏树林单位固定资产投资项目情况'),

            ('can_fixed_view_clf_baseline', '可以浏览所有长乐坊单位固定资产投资项目情况'),
            ('can_fixed_edit_clf_baseline', '可以编辑所有长乐坊单位固定资产投资项目情况'),
            ('can_fixed_add_clf_baseline', '可以添加所以长乐坊单位固定资产投资项目情况'),

            ('can_fixed_view_dgn_baseline', '可以浏览所有东关南单位固定资产投资项目情况'),
            ('can_fixed_edit_dgn_baseline', '可以编辑所有东关南单位固定资产投资项目情况'),
            ('can_fixed_add_dgn_baseline', '可以添加所以东关南单位固定资产投资项目情况'),

            ('can_fixed_view_tyl_baseline', '可以浏览所有太乙路单位固定资产投资项目情况'),
            ('can_fixed_edit_tyl_baseline', '可以编辑所有太乙路单位固定资产投资项目情况'),
            ('can_fixed_add_tyl_baseline', '可以添加所以太乙路单位固定资产投资项目情况'),

            ('can_fixed_view_wyl_baseline', '可以浏览所有文艺路单位固定资产投资项目情况'),
            ('can_fixed_edit_wyl_baseline', '可以编辑所有文艺路单位固定资产投资项目情况'),
            ('can_fixed_add_wyl_baseline', '可以添加所以文艺路单位固定资产投资项目情况'),

            ('can_fixed_view_cal_baseline', '可以浏览所有长安路单位固定资产投资项目情况'),
            ('can_fixed_edit_cal_baseline', '可以编辑所有长安路单位固定资产投资项目情况'),
            ('can_fixed_add_cal_baseline', '可以添加所以长安路单位固定资产投资项目情况'),

            ('can_fixed_view_zjc_baseline', '可以浏览所有张家村单位固定资产投资项目情况'),
            ('can_fixed_edit_zjc_baseline', '可以编辑所有张家村单位固定资产投资项目情况'),
            ('can_fixed_add_zjc_baseline', '可以添加所以张家村单位固定资产投资项目情况'),

            ('can_fixed_view_xxxq_baseline', '可以浏览所有西咸新区单位固定资产投资项目情况'),
            ('can_fixed_edit_xxxq_baseline', '可以编辑所有西咸新区单位固定资产投资项目情况'),
            ('can_fixed_add_xxxq_baseline', '可以添加所以西咸新区单位固定资产投资项目情况'),

        )
    def __str__(self):
        return '{} - {} - {}'.format(self.main_social_num, self.complete_pay, self.plan_hundred)

class fixedAssetAdmin(admin.ModelAdmin):
    list_diplay = ('main_social_num', 'complete_pay')
    list_filter = ('main_social_num', 'complete_pay')

# 611-4表各表详情
class ProjectCount(models.Model):

    main_social_num = models.ForeignKey(Companies, on_delete=models.CASCADE, default="12432343", verbose_name="统一社会信用代码", help_text="主表的统一社会信用代码")
    social_num = models.CharField(max_length=128, primary_key=True, blank=True, verbose_name="统一社会信用代码")
    org_num = models.CharField(max_length=128, blank=True, null=True, verbose_name="组织机构代码", help_text="尚未领取统一社会信用代码的")
    number = models.CharField(max_length=128, blank=True, null=True, verbose_name="项目编码")
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name="项目名称")
    province = models.CharField(max_length=32, default="陕西省", verbose_name="单位所在地-省(自治区、直辖市)")
    city = models.CharField(max_length=32, default="西安市", verbose_name="单位所在地-市(地、州、盟)")
    district = models.CharField(max_length=32, default="碑林区", verbose_name="单位所在地-县(市、区、旗)")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="单位所在地-街(村)、门牌号")
    street_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="区划代码")
    industry_code = models.CharField(max_length=32, blank=True, null=True, verbose_name="项目行业编码")
    industry_category = models.CharField(max_length=64, blank=True, null=True, verbose_name="行业类别")
    start_time = models.DateField(blank=True, null=True, verbose_name="项目开始时间")
    all_time = models.DateField(blank=True, null=True, verbose_name="项目全部投产时间")
    all_invest = models.PositiveIntegerField(blank=True, null=True, verbose_name="计划总投资额(万元)")
    start_all_invest = models.PositiveIntegerField(blank=True, null=True, verbose_name="自建设开始累计完成投资(万元)")
    total_invest = models.PositiveIntegerField(blank=True, null=True, verbose_name="本年完成投资额(万元)")

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name="录入员", related_name="project_created_by")
    added_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="录入时间")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                                    verbose_name="修改员", related_name="project_modified_by")
    modified_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "611-4表5000万及以上项目情况(单位固定资产投资项目情况)"
        verbose_name_plural = "611-4表5000万及以上项目情况(单位固定资产投资项目情况)"
        permissions = (

            ('can_project_view_nym_baseline', '可以浏览所有南院门5000万以上项目数'),
            ('can_project_edit_nym_baseline', '可以编辑所有南院门5000万以上项目数'),
            ('can_project_add_nym_baseline', '可以添加所以南院门5000万以上项目数'),

            ('can_project_view_bsl_baseline', '可以浏览所有柏树林5000万以上项目数'),
            ('can_project_edit_bsl_baseline', '可以编辑所有柏树林5000万以上项目数'),
            ('can_project_add_bsl_baseline', '可以添加所以柏树林5000万以上项目数'),

            ('can_project_view_clf_baseline', '可以浏览所有长乐坊5000万以上项目数'),
            ('can_project_edit_clf_baseline', '可以编辑所有长乐坊5000万以上项目数'),
            ('can_project_add_clf_baseline', '可以添加所以长乐坊5000万以上项目数'),

            ('can_project_view_dgn_baseline', '可以浏览所有东关南5000万以上项目数'),
            ('can_project_edit_dgn_baseline', '可以编辑所有东关南5000万以上项目数'),
            ('can_project_add_dgn_baseline', '可以添加所以东关南5000万以上项目数'),

            ('can_project_view_tyl_baseline', '可以浏览所有太乙路5000万以上项目数'),
            ('can_project_edit_tyl_baseline', '可以编辑所有太乙路5000万以上项目数'),
            ('can_project_add_tyl_baseline', '可以添加所以太乙路5000万以上项目数'),

            ('can_project_view_wyl_baseline', '可以浏览所有文艺路5000万以上项目数'),
            ('can_project_edit_wyl_baseline', '可以编辑所有文艺路5000万以上项目数'),
            ('can_project_add_wyl_baseline', '可以添加所以文艺路5000万以上项目数'),

            ('can_project_view_cal_baseline', '可以浏览所有长安路5000万以上项目数'),
            ('can_project_edit_cal_baseline', '可以编辑所有长安路5000万以上项目数'),
            ('can_project_add_cal_baseline', '可以添加所以长安路5000万以上项目数'),

            ('can_project_view_zjc_baseline', '可以浏览所有张家村5000万以上项目数'),
            ('can_project_edit_zjc_baseline', '可以编辑所有张家村5000万以上项目数'),
            ('can_project_add_zjc_baseline', '可以添加所以张家村5000万以上项目数'),

            ('can_project_view_xxxq_baseline', '可以浏览所有西咸新区5000万以上项目数'),
            ('can_project_edit_xxxq_baseline', '可以编辑所有西咸新区5000万以上项目数'),
            ('can_project_add_xxxq_baseline', '可以添加所以西咸新区5000万以上项目数'),

        )

    def __str__(self):
        return '{} - {}'.format(self.social_num, self.name)

class ProjectCountAdmin(admin.ModelAdmin):
    list_diplay = ('social_num', 'name')
    list_filter = ('social_num', 'name')

# 611-5表行政事业单位主要经济指标
class nationUnit(models.Model):
    # 基本信息
    main_social_num = models.ForeignKey(Companies, on_delete=models.CASCADE, default="12432343",verbose_name="统一社会信用代码", help_text="主表的统一社会信用代码")
    # 行政事业单位主要经济指标 start
    inventory_early = models.IntegerField(blank=True, null=True, verbose_name="年初存货")
    current_assets = models.PositiveIntegerField(blank=True, null=True, verbose_name="流动资产")
    inventory_current_assets = models.IntegerField(blank=True, null=True, verbose_name="流动资产存货")
    #
    permanent_investment = models.PositiveIntegerField(blank=True, null=True, verbose_name="长期投资")
    original_price = models.PositiveIntegerField(blank=True, null=True, verbose_name="固定资产原价")
    area_building = models.PositiveIntegerField(blank=True, null=True, verbose_name="土地、房屋和构筑物")
    machinery_equipment = models.PositiveIntegerField(blank=True, null=True, verbose_name="机器设备")
    transportation_equipment = models.PositiveIntegerField(blank=True, null=True, verbose_name="运输设备")

    building = models.PositiveIntegerField(blank=True, null=True, verbose_name="在建工程")
    intangible_assets_price = models.PositiveIntegerField(blank=True, null=True, verbose_name="无形资产原价")
    land_tenure = models.PositiveIntegerField(blank=True, null=True, verbose_name="土地使用权")
    public_infrastructure = models.PositiveIntegerField(blank=True, null=True, verbose_name="公共基础设施原价")
    public_infrastructure_accumulated_depreciation = models.PositiveIntegerField(blank=True, null=True, verbose_name="公共基础设施累计折旧")
    total_assets = models.PositiveIntegerField(blank=True, null=True, verbose_name="资产合计")
    total_liabilities = models.PositiveIntegerField(blank=True, null=True, verbose_name="负债合计")
    total_net_asset = models.IntegerField(blank=True, null=True, verbose_name="净资产合计")

    total_income = models.PositiveIntegerField(blank=True, null=True, verbose_name="本年收入合计")
    income_fiscal_appropriation = models.PositiveIntegerField(blank=True, null=True, verbose_name="财政拨款收入")
    income_undertaking = models.PositiveIntegerField(blank=True, null=True, verbose_name="事业收入")
    income_manage = models.PositiveIntegerField(blank=True, null=True, verbose_name="经营收入")

    total_expend = models.PositiveIntegerField(blank=True, null=True, verbose_name="本年支出合计")
    expend_salary = models.PositiveIntegerField(blank=True, null=True, verbose_name="工资福利支出")
    expend_service = models.PositiveIntegerField(blank=True, null=True, verbose_name="商品和服务支出")
    expend_labour = models.PositiveIntegerField(blank=True, null=True, verbose_name="劳务费")
    expend_labor_union = models.PositiveIntegerField(blank=True, null=True, verbose_name="工会经费")
    expend_welfare = models.PositiveIntegerField(blank=True, null=True, verbose_name="福利经费")
    expend_taxes_additional = models.PositiveIntegerField(blank=True, null=True, verbose_name="税金及附加经费")

    expend_subsidy = models.PositiveIntegerField(blank=True, null=True, verbose_name="对个人和家庭的补助")
    expend_retire = models.PositiveIntegerField(blank=True, null=True, verbose_name="退（离）休费")
    expend_medical = models.PositiveIntegerField(blank=True, null=True, verbose_name="医疗费补助")

    expend_management = models.PositiveIntegerField(blank=True, null=True, verbose_name="经营支出")

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name="录入员", related_name="nation_created_by")
    added_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="录入时间")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                                    verbose_name="修改员", related_name="nation_modified_by")
    modified_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "611-5表行政事业单位主要经济指标"
        verbose_name_plural = "611-5表行政事业单位主要经济指标"
        permissions = (

            ('can_nation_view_nym_baseline', '可以浏览所有南院门行政事业单位主要经济指标'),
            ('can_nation_edit_nym_baseline', '可以编辑所有南院门行政事业单位主要经济指标'),
            ('can_nation_add_nym_baseline', '可以添加所以南院门行政事业单位主要经济指标'),

            ('can_nation_view_bsl_baseline', '可以浏览所有柏树林行政事业单位主要经济指标'),
            ('can_nation_edit_bsl_baseline', '可以编辑所有柏树林行政事业单位主要经济指标'),
            ('can_nation_add_bsl_baseline', '可以添加所以柏树林行政事业单位主要经济指标'),

            ('can_nation_view_clf_baseline', '可以浏览所有长乐坊行政事业单位主要经济指标'),
            ('can_nation_edit_clf_baseline', '可以编辑所有长乐坊行政事业单位主要经济指标'),
            ('can_nation_add_clf_baseline', '可以添加所以长乐坊行政事业单位主要经济指标'),

            ('can_nation_view_dgn_baseline', '可以浏览所有东关南行政事业单位主要经济指标'),
            ('can_nation_edit_dgn_baseline', '可以编辑所有东关南行政事业单位主要经济指标'),
            ('can_nation_add_dgn_baseline', '可以添加所以东关南行政事业单位主要经济指标'),

            ('can_nation_view_tyl_baseline', '可以浏览所有太乙路行政事业单位主要经济指标'),
            ('can_nation_edit_tyl_baseline', '可以编辑所有太乙路行政事业单位主要经济指标'),
            ('can_nation_add_tyl_baseline', '可以添加所以太乙路行政事业单位主要经济指标'),

            ('can_nation_view_wyl_baseline', '可以浏览所有文艺路行政事业单位主要经济指标'),
            ('can_nation_edit_wyl_baseline', '可以编辑所有文艺路行政事业单位主要经济指标'),
            ('can_nation_add_wyl_baseline', '可以添加所以文艺路行政事业单位主要经济指标'),

            ('can_nation_view_cal_baseline', '可以浏览所有长安路行政事业单位主要经济指标'),
            ('can_nation_edit_cal_baseline', '可以编辑所有长安路行政事业单位主要经济指标'),
            ('can_nation_add_cal_baseline', '可以添加所以长安路行政事业单位主要经济指标'),

            ('can_nation_view_zjc_baseline', '可以浏览所有张家村行政事业单位主要经济指标'),
            ('can_nation_edit_zjc_baseline', '可以编辑所有张家村行政事业单位主要经济指标'),
            ('can_nation_add_zjc_baseline', '可以添加所以张家村行政事业单位主要经济指标'),

            ('can_nation_view_xxxq_baseline', '可以浏览所有西咸新区行政事业单位主要经济指标'),
            ('can_nation_edit_xxxq_baseline', '可以编辑所有西咸新区行政事业单位主要经济指标'),
            ('can_nation_add_xxxq_baseline', '可以添加所以西咸新区行政事业单位主要经济指标'),

        )
    def __str__(self):
        return '{} - {} - {}'.format(self.main_social_num, self.inventory_early, self.current_assets)


class nationUnitAdmin(admin.ModelAdmin):
    list_display = ('inventory_early', 'current_assets')
    list_filter = ('inventory_early', 'current_assets')

# 611-6表民间非盈利组织主要经济指标
class privateUncommerciallyOrg(models.Model):
    # 基本信息
    main_social_num = models.ForeignKey(Companies, on_delete=models.CASCADE, default="12432343",verbose_name="统一社会信用代码", help_text="主表的统一社会信用代码")

    # 民间非营利组织 start
    inventory_early = models.IntegerField(blank=True, null=True, verbose_name="年初存货")
    current_assets = models.PositiveIntegerField(blank=True, null=True, verbose_name="流动资产合计")
    inventory_current_assets = models.IntegerField(blank=True, null=True, verbose_name="存货")
    permanent_investment = models.PositiveIntegerField(blank=True, null=True, verbose_name="长期投资")

    original_price = models.PositiveIntegerField(blank=True, null=True, verbose_name="固定资产原价")
    area_building = models.PositiveIntegerField(blank=True, null=True, verbose_name="土地、房屋和构筑物")
    machinery_equipment = models.PositiveIntegerField(blank=True, null=True, verbose_name="机器设备")
    transportation_equipment = models.PositiveIntegerField(blank=True, null=True, verbose_name="运输设备")
    building = models.PositiveIntegerField(blank=True, null=True, verbose_name="在建工程")
    cultural_price = models.PositiveIntegerField(blank=True, null=True, verbose_name="文物文化资产")
    intangible_price = models.PositiveIntegerField(blank=True, null=True, verbose_name="无形资产")

    total_assets = models.PositiveIntegerField(blank=True, null=True, verbose_name="资产总计")
    total_liabilities = models.PositiveIntegerField(blank=True, null=True, verbose_name="负债合计")
    total_net_asset = models.IntegerField(blank=True, null=True, verbose_name="净资产合计")
    total_income = models.PositiveIntegerField(blank=True, null=True, verbose_name="本年收入合计")
    income_donate = models.PositiveIntegerField(blank=True, null=True, verbose_name="捐赠收入")
    income_membership_fees = models.PositiveIntegerField(blank=True, null=True, verbose_name="会费收入")

    total_this_year = models.PositiveIntegerField(blank=True, null=True, verbose_name="本年费用合计")
    total_operational_action = models.PositiveIntegerField(blank=True, null=True, verbose_name="业务活动成本")
    expend_action_salary = models.PositiveIntegerField(blank=True, null=True, verbose_name="人员费用", help_text="业务活动成本")
    expend_action_current_expense = models.PositiveIntegerField(blank=True, null=True, verbose_name="日常费用", help_text="业务活动成本")
    expend_action_depreciation_assets = models.PositiveIntegerField(blank=True, null=True, verbose_name="固定资产折旧", help_text="业务活动成本")
    expend_action_taxes = models.PositiveIntegerField(blank=True, null=True, verbose_name="税费", help_text="业务活动成本")

    expend_management = models.PositiveIntegerField(blank=True, null=True, verbose_name="管理费用", help_text="管理费用")
    expend_management_salary = models.PositiveIntegerField(blank=True, null=True, verbose_name="人员费用", help_text="管理费用")
    expend_management_current_expense = models.PositiveIntegerField(blank=True, null=True, verbose_name="日常费用", help_text="管理费用")
    expend_management_depreciation_assets = models.PositiveIntegerField(blank=True, null=True, verbose_name="固定资产折旧", help_text="管理费用")
    expend_management_taxes = models.PositiveIntegerField(blank=True, null=True, verbose_name="税费", help_text="管理费用")
    net_asset_change = models.IntegerField(blank=True, null=True, verbose_name="净资产变动额", help_text="管理费用")

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name="录入员", related_name="private_created_by")
    added_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="录入时间")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE,
                                    verbose_name="修改员", related_name="private_modified_by")
    modified_date = models.DateTimeField(auto_now_add=True, blank=True, null=True,  verbose_name="修改时间")

    class Meta:
        verbose_name = "611-6表民间非盈利组织主要经济指标"
        verbose_name_plural = "611-6表民间非盈利组织主要经济指标"
        permissions = (

            ('can_priorg_view_nym_baseline', '可以浏览所有南院门民间非盈利组织主要经济指标'),
            ('can_priorg_edit_nym_baseline', '可以编辑所有南院门民间非盈利组织主要经济指标'),
            ('can_priorg_add_nym_baseline', '可以添加所以南院门民间非盈利组织主要经济指标'),

            ('can_priorg_view_bsl_baseline', '可以浏览所有柏树林民间非盈利组织主要经济指标'),
            ('can_priorg_edit_bsl_baseline', '可以编辑所有柏树林民间非盈利组织主要经济指标'),
            ('can_priorg_add_bsl_baseline', '可以添加所以柏树林民间非盈利组织主要经济指标'),

            ('can_priorg_view_clf_baseline', '可以浏览所有长乐坊民间非盈利组织主要经济指标'),
            ('can_priorg_edit_clf_baseline', '可以编辑所有长乐坊民间非盈利组织主要经济指标'),
            ('can_priorg_add_clf_baseline', '可以添加所以长乐坊民间非盈利组织主要经济指标'),

            ('can_priorg_view_dgn_baseline', '可以浏览所有东关南民间非盈利组织主要经济指标'),
            ('can_priorg_edit_dgn_baseline', '可以编辑所有东关南民间非盈利组织主要经济指标'),
            ('can_priorg_add_dgn_baseline', '可以添加所以东关南民间非盈利组织主要经济指标'),

            ('can_priorg_view_tyl_baseline', '可以浏览所有太乙路民间非盈利组织主要经济指标'),
            ('can_priorg_edit_tyl_baseline', '可以编辑所有太乙路民间非盈利组织主要经济指标'),
            ('can_priorg_add_tyl_baseline', '可以添加所以太乙路民间非盈利组织主要经济指标'),

            ('can_priorg_view_wyl_baseline', '可以浏览所有文艺路民间非盈利组织主要经济指标'),
            ('can_priorg_edit_wyl_baseline', '可以编辑所有文艺路民间非盈利组织主要经济指标'),
            ('can_priorg_add_wyl_baseline', '可以添加所以文艺路民间非盈利组织主要经济指标'),

            ('can_priorg_view_cal_baseline', '可以浏览所有长安路民间非盈利组织主要经济指标'),
            ('can_priorg_edit_cal_baseline', '可以编辑所有长安路民间非盈利组织主要经济指标'),
            ('can_priorg_add_cal_baseline', '可以添加所以长安路民间非盈利组织主要经济指标'),

            ('can_priorg_view_zjc_baseline', '可以浏览所有张家村民间非盈利组织主要经济指标'),
            ('can_priorg_edit_zjc_baseline', '可以编辑所有张家村民间非盈利组织主要经济指标'),
            ('can_priorg_add_zjc_baseline', '可以添加所以张家村民间非盈利组织主要经济指标'),

            ('can_priorg_view_xxxq_baseline', '可以浏览所有西咸新区民间非盈利组织主要经济指标'),
            ('can_priorg_edit_xxxq_baseline', '可以编辑所有西咸新区民间非盈利组织主要经济指标'),
            ('can_priorg_add_xxxq_baseline', '可以添加所以西咸新区民间非盈利组织主要经济指标'),

        )
    def __str__(self):
        return '{} - {} - {}'.format(self.main_social_num, self.inventory_early, self.current_assets)

class privateUncommerciallyOrgAdmin(admin.ModelAdmin):
    list_display = ('inventory_early', 'current_assets')
    list_filter = ('inventory_early', 'current_assets')