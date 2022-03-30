
from fastapi import Depends
from sqlalchemy.orm import Session as DBSession

from ..model import ActivityType
from .database import get_db

class ActivityTypeRepository:

	def __init__(self, db_session:DBSession = Depends(get_db)):
		self.db_session = db_session

	def add(self, db_activity_type: ActivityType):
		self.db_session.add(db_activity_type)
		self.db_session.commit()
		self.db_session.refresh(db_activity_type)
		return db_activity_type

	def get(self, user_id:int, activity_type_id:int) -> ActivityType:
		return self.db_session.query(ActivityType).filter(
			ActivityType.id == activity_type_id, ActivityType.owner_id == user_id
		).first()

	def get_all_owned_by(self, user_id:int) -> list[ActivityType]:
		return self.db_session.query(ActivityType).filter(ActivityType.owner_id == user_id).all()

	def delete(self, activity_type:ActivityType):
		self.db_session.delete(activity_type)
		self.db_session.commit()
