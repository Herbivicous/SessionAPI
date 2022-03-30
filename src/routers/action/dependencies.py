
from fastapi import Depends

from ...datalayer.actions import ActionRepository

from ..activity.dependencies import activity_by_id

from .exceptions import ActionNotFound

def action_by_id(action_id:int, activity = Depends(activity_by_id), actions:ActionRepository = Depends(ActionRepository)):

	if (action := actions.get(activity.id, action_id)):
		return action

	raise ActionNotFound(activity.id, action_id)
