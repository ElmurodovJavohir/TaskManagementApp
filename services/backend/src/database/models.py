from tortoise import fields, models
from fastapi_admin.models import AbstractAdmin
import datetime


class Users(models.Model):
    id = fields.IntField(pk=True)

    username = fields.CharField(max_length=20, unique=True)
    full_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Tasks(models.Model):
    id = fields.IntField(pk=True)

    title = fields.CharField(max_length=256)
    description = fields.TextField()
    user = fields.ForeignKeyField("models.Users", related_name="tasks")

    due_date = fields.DatetimeField()
    completed = fields.BooleanField(default=False)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.user_id} on {self.created_at}"


class Admin(AbstractAdmin):
    last_login = fields.DatetimeField(
        description="Last Login", default=datetime.datetime.now
    )
    email = fields.CharField(max_length=200, default="")
    avatar = fields.CharField(max_length=200, default="")
    intro = fields.TextField(default="")
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}#{self.username}"
