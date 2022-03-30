
from fastapi import HTTPException

class SessionNotFound(HTTPException):
	def __init__(self, user_id:int, session_id:int):
		detail = f'Session {session_id!r} not found for user {user_id!r}'
		super().__init__(status_code=404, detail=detail)
