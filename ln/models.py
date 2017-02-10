from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser

from ln.managers import UserManager


class User(AbstractBaseUser):
    login = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=15, choices=(
        ('removed', 'Removed'),
        ('no_active', 'No active'),
        ('active', 'Active')), default='no_active')
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=50)
    date_registry = models.DateField(auto_now=True)

    objects = UserManager()

    REQUIRED_FIELDS = ()
    USERNAME_FIELD = 'login'

    def get_short_name(self):
        pass

    def get_full_name(self):
        pass

    class Meta:
        db_table = 'user'


class Phone(models.Model):
    user = models.ForeignKey(User)
    value = models.CharField(max_length=11)
    status = models.CharField(max_length=15, choices=(
        ('no_active', 'No active'),
        ('active', 'Active')))

    class Meta:
        db_table = 'phone'


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return 'Category <%s>' % self.name


class Movie(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    date_show = models.DateField(auto_now=False)

    class Meta:
        db_table = 'movie'

    def __str__(self):
        return '<%s> %s ( price is %s hrn)' % (self.id, self.name,
                                               self.price)


admin.site.register(Category)
admin.site.register(Movie)