
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from ..datalayer.database import Base

class Session(Base):
	__tablename__ = "sessions"

	id = Column(Integer, primary_key=True, index=True)
	start_time = Column(DateTime)

	owner_id = Column(Integer, ForeignKey("users.id"))
	owner = relationship("User", back_populates="sessions")

	activities = relationship("Activity", back_populates="session")

	def __str__(self):
		return f'<Session {self.owner_id=} {self.id=}>'
