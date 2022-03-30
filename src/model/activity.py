
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from ..datalayer.database import Base

class Activity(Base):
	__tablename__ = "activities"

	id = Column(Integer, primary_key=True, index=True)
	start_time = Column(DateTime)

	activity_type_id = Column(Integer, ForeignKey("activity_types.id"))

	session_id = Column(Integer, ForeignKey("sessions.id"))
	session = relationship("Session", back_populates="activities")

	actions = relationship("Action", back_populates="activity")

	def __str__(self):
		return f'<Activity {self.session_id=} {self.activity_type_id=} {self.id=}>'
