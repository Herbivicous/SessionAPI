
from fastapi import Depends

from ...datalayer.activities import ActivityRepository
from ... import model

from ..session.dependencies import session_by_id

from .exceptions import ActivityNotFound

def activity_by_id(
	activity_id:	int,
	session:		model.Session =			Depends(session_by_id),
	activities:		ActivityRepository =	Depends(ActivityRepository)
) -> model.Activity:

	if (activity := activities.get(session.id, activity_id)):
		return activity

	raise ActivityNotFound(session.id, activity_id)
