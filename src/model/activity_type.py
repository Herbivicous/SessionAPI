
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..datalayer.database import Base

class ActivityType(Base):
	__tablename__ = "activity_types"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String)

	owner_id = Column(Integer, ForeignKey("users.id"))
	owner = relationship("User", back_populates="activity_types")

	def __str__(self):
		return f'<ActivityType {self.owner_id=} {self.id=} {self.name=}>'
