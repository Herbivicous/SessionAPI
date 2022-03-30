
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..datalayer.database import Base

class Action(Base):
	__tablename__ = "actions"

	id = Column(Integer, primary_key=True, index=True)

	activity_id = Column(Integer, ForeignKey("activities.id"))
	activity = relationship("Activity", back_populates="actions")

	def __str__(self):
		return f'<Action {self.activity_id=} {self.id=}>'
