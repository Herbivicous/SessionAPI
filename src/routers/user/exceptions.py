
from fastapi import HTTPException

class EmailAlreadyRegistered(HTTPException):
	def __init__(self, email:str):
		detail = f'Email {email!r} already registered'
		super().__init__(status_code=400, detail=detail)

class UserNotFound(HTTPException):
	def __init__(self, user_id:int):
		detail = f'User {user_id!r} not found'
		super().__init__(status_code=404, detail=detail)
