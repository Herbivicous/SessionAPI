
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..datalayer.database import Base

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	email = Column(String, unique=True, index=True)

	sessions = relationship("Session", back_populates="owner")
	activity_types = relationship("ActivityType", back_populates="owner")

	def __str__(self):
		return f'<Session {self.email=} {self.id=}>'
