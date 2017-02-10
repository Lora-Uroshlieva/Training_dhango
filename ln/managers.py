from django.db import models


class UserManager(models.Manager):
    def registration(self, login, password):
        user = self.create(login=login, password=password)

        user.save()
        return user.pk


