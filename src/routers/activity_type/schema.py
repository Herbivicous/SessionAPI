
from pydantic import BaseModel

class _ActivityTypeBase(BaseModel):
	name:str


class ActivityTypeIn(_ActivityTypeBase):
	pass


class ActivityType(_ActivityTypeBase):
	id:int
	owner_id:int

	class Config:
		orm_mode = True
