
from fastapi import APIRouter, Depends

from ...datalayer.users import UserRepository
from ... import model

from .schema import User, UserIn
from .dependencies import user_by_id
from .exceptions import EmailAlreadyRegistered


router = APIRouter(
	prefix='/users',
	tags=['Users']
)


@router.post('', response_model=User)
async def post_user(user:UserIn, users:UserRepository = Depends(UserRepository)):

	if users.get_by_email(user.email):
		raise EmailAlreadyRegistered(user.email)

	return users.add(model.User(email=user.email))


@router.get('', response_model=list[User])
async def get_all_users(users:UserRepository = Depends(UserRepository)):
	return users.get_all()


@router.get('/{user_id}', response_model=User)
async def get_user(user:model.User = Depends(user_by_id)):
	return user


@router.delete('/{user_id}', response_model=User)
async def delete_user(user:model.User = Depends(user_by_id), users:UserRepository = Depends(UserRepository)):
	users.delete(user)
	return user
