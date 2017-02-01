from django.db import models
from django.contrib import admin


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