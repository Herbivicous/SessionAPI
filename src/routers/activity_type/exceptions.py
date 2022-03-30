
from fastapi import HTTPException

class ActivityTypeNotFound(HTTPException):
	def __init__(self, user_id:int, activity_type_id:int):
		detail = f'ActivityType {activity_id!r} not found for user {user_id!r}'
		super().__init__(status_code=404, detail=detail)
