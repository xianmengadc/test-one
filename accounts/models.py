from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin, Group)


class UserManager(BaseUserManager):
    def create_user(self, name, mobile, district, password):

        if not name:
            raise ValueError("必须填写用户名称")

        if not mobile:
            raise ValueError("必须填写用户名mobile")

        user = self.model(mobile=mobile, name=name)
        self.name = name
        self.district = district
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, mobile, district, password):
        user = self.create_user(
            mobile=mobile,
            name=name,
            district=district,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

USER_DISTRICT = (
    ('碑林区', '碑林区'),
    ('南院门', '南院门'),
    ('柏树林', '柏树林'),
    ('长乐坊', '长乐坊'),
    ('东关南', '东关南'),
    ('太乙路', '太乙路'),
    ('文艺路', '文艺路'),
    ('长安路', '长安路'),
    ('张家村', '张家村'),
    ('西咸新区', '西咸新区'),
)

class User(AbstractBaseUser, PermissionsMixin):
    # group_name = models.CharField(max_length=32, blank=True, null=True, verbose_name="用户组名称")
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name="用户姓名")
    mobile = models.CharField(max_length=32, unique=True, verbose_name="手机号")
    district = models.CharField(max_length=32, choices=USER_DISTRICT, verbose_name="所属用户组")
    avatar = models.ImageField(blank=True, null=True, verbose_name="头像")
    score = models.CharField(max_length=32, null=True, blank=True, verbose_name="分数")
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="创建日期")
    available_date = models.CharField(max_length=32, null=True, blank=True, verbose_name="几号考")
    is_active = models.BooleanField(default=True, verbose_name="是否激活")
    is_staff = models.BooleanField(default=False, verbose_name="工作人权限")  # a admin user; non super-user
    is_admin = models.BooleanField(default=False, verbose_name="超级用户权限")  # a superuser

    objects = UserManager()

    USERNAME_FIELD = 'mobile'

    REQUIRED_FIELDS = ['district', 'name']

    class Meta:
        verbose_name_plural = "账户管理"



    def __str__(self):
        return '{0} {1} {2}'.format(self.mobile, self.name, self.score)

    @property
    def get_group_name(self):
        if self.groups.exists():
            return self.groups.all()[0]
        return [i.name for i in self.groups.all()]



'''
from accounts.models import User
u = User.objects.get(pk=4)

'''