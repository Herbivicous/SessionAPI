
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as DBSession

from ...datalayer.activity_types import ActivityTypeRepository
from ... import model

from ..user.dependencies import user_by_id

from .schema import ActivityType, ActivityTypeIn
from .dependencies import activity_type_by_id


router = APIRouter(
	prefix='/users/{user_id}/activities',
	tags=['ActivitiesType']
)


@router.post('', response_model=ActivityType)
async def post_activity_type(
	activity_type:	ActivityTypeIn,
	user:			model.User =				Depends(user_by_id),
	activity_types:	ActivityTypeRepository =	Depends(ActivityTypeRepository)
):
	return activity_types.add(model.ActivityType(owner=user, name=activity_type.name))


@router.get('', response_model=list[ActivityType])
async def get_activity_types_of_user(
	user:		model.User =				Depends(user_by_id),
	activities:	ActivityTypeRepository =	Depends(ActivityTypeRepository)
):
	return activities.get_all_owned_by(user.id)


@router.get('/{activity_type_id}', response_model=ActivityType)
async def get_activity_type(activity_type:model.ActivityType = Depends(activity_type_by_id)):
	return activity_type


@router.delete('/{activity_type_id}', response_model=ActivityType)
async def delete_activity_type(
	activity_type:	model.ActivityType =		Depends(activity_type_by_id),
	activity_types:	ActivityTypeRepository =	Depends(ActivityTypeRepository)
):
	activity_types.delete(activity_type)
	return activity_type
