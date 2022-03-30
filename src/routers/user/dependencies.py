
from fastapi import Depends

from ...datalayer.users import UserRepository
from ... import model

from .exceptions import UserNotFound

def user_by_id(
	user_id:str, users:UserRepository = Depends(UserRepository)
) -> model.User:

	if (user := users.get(user_id)):
		return user

	raise UserNotFound(user_id)

def user_by_email(
	email:str, users:UserRepository = Depends(UserRepository)
) -> model.User:

	if (user := users.get_by_email(email)):
		return user

	raise UserNotFound(email)
