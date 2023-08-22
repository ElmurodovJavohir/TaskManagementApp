from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Tasks
from tortoise import Tortoise

Tortoise.init_models(["src.database.models"], "models")
TaskInSchema = pydantic_model_creator(
    Tasks, name="TaskIn", exclude=["user_id"], exclude_readonly=True
)
TaskOutSchema = pydantic_model_creator(
    Tasks,
    name="Task",
    exclude=[
        "modified_at",
        "user.password",
        "user.created_at",
        "user.modified_at",
    ],
)


class UpdateTask(BaseModel):
    title: Optional[str]
    content: Optional[str]
