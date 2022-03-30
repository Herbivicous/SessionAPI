
from fastapi import HTTPException

class ActivityNotFound(HTTPException):
	def __init__(self, session_id:int, activity_id:int):
		detail = f'Activity {activity_id!r} not found for session {session_id!r}'
		super().__init__(status_code=404, detail=detail)
