
from fastapi import Depends
from sqlalchemy.orm import Session as DBSession

from ..model.session import Session
from .database import get_db

class SessionRepository:

	def __init__(self, db_session:DBSession = Depends(get_db)):
		self.db_session = db_session

	def add(self, db_session: Session):
		self.db_session.add(db_session)
		self.db_session.commit()
		self.db_session.refresh(db_session)
		return db_session

	def get(self, user_id:int, session_id:int):
		return self.db_session.query(Session).filter(
			Session.id == session_id, Session.owner_id == user_id
		).first()

	def get_all_owned_by(self, user_id:int):
		return self.db_session.query(Session).filter(Session.owner_id == user_id).all()

	def delete(self, session:Session):
		self.db_session.delete(session)
		self.db_session.commit()
