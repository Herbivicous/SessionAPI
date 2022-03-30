
from fastapi import Depends

from ...datalayer.sessions import SessionRepository

from ..user.dependencies import user_by_id

from .exceptions import SessionNotFound

def session_by_id(session_id:int, user = Depends(user_by_id), sessions:SessionRepository = Depends(SessionRepository)):

	if (session := sessions.get(user.id, session_id)):
		return session

	raise SessionNotFound(user.id, session_id)
