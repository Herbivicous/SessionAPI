
from fastapi import Depends
from sqlalchemy.orm import Session as DBSession

from ..model.action import Action
from .database import get_db

class ActionRepository:

	def __init__(self, db_session:DBSession = Depends(get_db)):
		self.db_session = db_session

	def add(self, db_action: Action):
		self.db_session.add(db_action)
		self.db_session.commit()
		self.db_session.refresh(db_action)
		return db_action

	def get(self, session_activity_id: int, action_id: int):
		return self.db_session.query(Action).filter(
			Action.id == action_id,
			Action.session_activity_id == session_activity_id
		).first()

	def get_all_in_session_activity(self, session_activity_id: int):
		return self.db_session.query(Action).filter(
			Action.session_activity_id == session_activity_id
		).all()

	def delete(self, action: Action):
		self.db_session.delete(action)
		self.db_session.commit()
