
from datetime import datetime
from pydantic import BaseModel

class _ActivityBase(BaseModel):
	start_time:datetime
	activity_type_id:int


class ActivityIn(_ActivityBase):
	pass


class Activity(_ActivityBase):
	id:int
	session_id:int

	class Config:
		orm_mode = True
