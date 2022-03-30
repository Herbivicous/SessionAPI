
from fastapi import Depends
from sqlalchemy.orm import Session as DBSession

from ..model import Activity
from .database import get_db

class ActivityRepository:

	def __init__(self, db_session:DBSession = Depends(get_db)):
		self.db_session = db_session

	def add(self, db_activity:Activity) -> Activity:
		self.db_session.add(db_activity)
		self.db_session.commit()
		self.db_session.refresh(db_activity)
		return db_activity

	def get(self, session_id:int, activity_id:int) -> Activity:
		return self.db_session.query(Activity).filter(
			Activity.id == activity_id,
			Activity.session_id == session_id,
		).first()

	def get_all_in_session(self, session_id:int) -> list[Activity]:
		return self.db_session.query(Activity).filter(
			Activity.session_id == session_id,
		).all()

	def delete(self, activity:Activity):
		self.db_session.delete(activity)
		self.db_session.commit()
