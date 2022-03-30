
from fastapi import HTTPException

class ActionNotFound(HTTPException):
	def __init__(self, activity_id:int, action_id:int):
		detail = f'Action {action_id!r} not found for activity {activity_id!r}'
		super().__init__(status_code=404, detail=detail)
