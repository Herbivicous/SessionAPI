
from datetime import datetime
from pydantic import BaseModel

class _SessionBase(BaseModel):
	start_time:datetime


class SessionIn(_SessionBase):
	pass


class Session(_SessionBase):
	id:int
	owner_id:int

	class Config:
		orm_mode = True
