
from fastapi import Depends
from sqlalchemy.orm import Session as DBSession

from ..model.user import User
from .database import get_db

class UserRepository:

	def __init__(self, db_session:DBSession = Depends(get_db)):
		self.db_session = db_session

	def add(self, db_user: User):
		self.db_session.add(db_user)
		self.db_session.commit()
		self.db_session.refresh(db_user)
		return db_user

	def get(self, user_id:int):
		return self.db_session.query(User).filter(User.id == user_id).first()

	def get_by_email(self, email:str):
		return self.db_session.query(User).filter(User.email == email).first()

	def get_all(self, skip:int = 0, limit:int = 100):
		return self.db_session.query(User).offset(skip).limit(limit).all()

	def delete(self, user:User):
		self.db_session.delete(user)
		self.db_session.commit()
