
from fastapi import APIRouter, Depends

from ...datalayer.sessions import SessionRepository
from ... import model

from ..user.dependencies import user_by_id

from .schema import Session, SessionIn
from .dependencies import session_by_id


router = APIRouter(
	prefix='/users/{user_id}/sessions',
	tags=['Sessions']
)


@router.post('', response_model=Session)
async def post_session(
	session:	SessionIn,
	user:		model.User =		Depends(user_by_id),
	sessions:	SessionRepository =	Depends(SessionRepository)
):
	return sessions.add(model.Session(owner=user, start_time=session.start_time))


@router.get('', response_model=list[Session])
async def get_sessions_of_user(
	user:		model.User =		Depends(user_by_id),
	sessions:	SessionRepository =	Depends(SessionRepository)
):
	return sessions.get_all_owned_by(user.id)


@router.get('/{session_id}', response_model=Session)
async def get_session(session:model.Session = Depends(session_by_id)):
	return session


@router.delete('/{session_id}', response_model=Session)
async def delete_session(
	session:	model.Session =		Depends(session_by_id),
	sessions:	SessionRepository =	Depends(SessionRepository)
):
	sessions.delete(session)
	return session
