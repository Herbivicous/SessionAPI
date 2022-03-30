
from pydantic import BaseModel

class _UserBase(BaseModel):
	email:str


class UserIn(_UserBase):
	pass


class User(_UserBase):
	id:int

	class Config:
		orm_mode = True
