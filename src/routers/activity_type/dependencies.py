
from fastapi import Depends

from ...datalayer.activity_types import ActivityTypeRepository
from ... import model

from ..user.dependencies import user_by_id

from .exceptions import ActivityTypeNotFound
from ..activity.schema import ActivityIn

def activity_type_by_id(
	activity_type_id:	int,
	user:				model.User =				Depends(user_by_id),
	activity_types:	ActivityTypeRepository =	Depends(ActivityTypeRepository),
) -> model.ActivityType:

	if (activity_type := activity_types.get(user.id, activity_type_id)):
		return activity_type

	raise ActivityTypeNotFound(user.id, activity_type_id)

def activity_type_from_activity(
	activity:			ActivityIn,
	user:				model.User =				Depends(user_by_id),
	activity_types:		ActivityTypeRepository =	Depends(ActivityTypeRepository),
) -> model.ActivityType:

	if (activity_type := activity_types.get(user.id, activity.activity_type_id)):
		return activity_type

	raise ActivityTypeNotFound(user.id, activity.activity_type_id)
