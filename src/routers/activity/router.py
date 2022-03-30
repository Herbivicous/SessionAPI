
from fastapi import APIRouter, Depends

from ...datalayer.activities import ActivityRepository
from ... import model

from ..session.dependencies import session_by_id
from ..activity_type.dependencies import activity_type_from_activity

from .schema import Activity, ActivityIn
from .dependencies import activity_by_id


router = APIRouter(
	prefix='/users/{user_id}/sessions/{session_id}/activities',
	tags=['Activities']
)


@router.post('', response_model=Activity)
async def post_activity(
	activity:		ActivityIn,
	session:		model.Session =			Depends(session_by_id),
	activity_type:	model.ActivityType =	Depends(activity_type_from_activity),
	activities:		ActivityRepository =	Depends(ActivityRepository)
):
	model_session_activity = model.Activity(
		session=session, activity_type_id=activity_type.id, start_time=activity.start_time
	)
	return activities.add(model_session_activity)


@router.get('', response_model=list[Activity])
async def get_activities_of_session(
	session:	model.Session =			Depends(session_by_id),
	activities:	ActivityRepository =	Depends(ActivityRepository)
):
	return activities.get_all_in_session(session.owner_id, session.id)


@router.get('/{session_activity_id}', response_model=Activity)
async def get_activity(activity:model.Activity = Depends(activity_by_id)):
	return activity


@router.delete('/{session_activity_id}', response_model=Activity)
async def delete_activity_id(
	activity:	model.Activity =		Depends(activity_by_id),
	activities:	ActivityRepository =	Depends(ActivityRepository)
):
	activities.delete(activity)
	return activity
