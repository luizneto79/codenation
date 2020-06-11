from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    env = models.CharField(max_length=50)
    version = models.CharField(max_length=5)
    address = models.GenericIPAddressField()


class User(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateTime()
    email = models.EmailField()
    password = models.CharField(min_length=8, max_length=50)


class Group(models.Model):
    name = models.CharField(max_length=50)


class Event(models.Model):
    level = models.CharField(max_length=20)
    data = models.TextField()
    arquivado = models.BooleanField(default=False)
    date = models.DateField()
    agent_id = models.ForeignKey(Agent, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)


class GroupUser(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
