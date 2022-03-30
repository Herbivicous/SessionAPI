
from pydantic import BaseModel

class _ActionBase(BaseModel):
	pass


class ActionIn(_ActionBase):
	pass


class Action(_ActionBase):
	id:int
	activity_id:int

	class Config:
		orm_mode = True
