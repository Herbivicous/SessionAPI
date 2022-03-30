
from fastapi import APIRouter, Depends

from ...datalayer.actions import ActionRepository
from ... import model

from ..activity.dependencies import activity_by_id

from .schema import Action, ActionIn
from .dependencies import action_by_id


router = APIRouter(
	prefix='/users/{user_id}/sessions/{session_id}/activities/{activity_id}/actions',
	tags=['Actions']
)


@router.post('', response_model=Action)
async def post_action(
	action:		ActionIn,
	activity:	model.Activity =	Depends(activity_by_id),
	actions:	ActionRepository =	Depends(ActionRepository)
):
	return actions.add(model.Action(activity_id=activity.id))


@router.get('', response_model=list[Action])
async def get_actions_of_activity(
	activity:	model.Activity =	Depends(activity_by_id),
	actions:	ActionRepository =	Depends(ActionRepository)
):
	return actions.get_all_in_activity(activity.id)


@router.get('/{action_id}', response_model=Action)
async def get_action(action:model.Action = Depends(action_by_id)):
	return action


@router.delete('/{action_id}', response_model=Action)
async def delete_action(
	action:		model.Action =		Depends(action_by_id),
	actions:	ActionRepository =	Depends(ActionRepository)
):
	actions.delete(action)
	return action
