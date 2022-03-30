
import random
import string
import asyncio
import httpx
from datetime import datetime

def random_string(length:int):
	return ''.join(random.sample(string.ascii_lowercase, length))

async def post_users(client):
	return await client.post('/users', json={'email': random_string(8)})

async def post_activity_types(client, user_id):
	return await client.post(
		f'/users/{user_id}/activities',
		json={'name': random_string(4)}
	)

async def post_sessions(client, user_id):
	return await client.post(
		f'/users/{user_id}/sessions',
		json={'start_time': str(datetime.now())}
	)

async def post_activities(client, user_id, session_id, activity_type_id):
	return await client.post(
		f'/users/{user_id}/sessions/{session_id}/activities',
		json={'start_time': str(datetime.now()), 'activity_type_id': activity_type_id}
	)

async def post_action(client, user_id, session_id, activity_id):
	return await client.post(
		f'/users/{user_id}/sessions/{session_id}/activities/{activity_id}/actions',
		json={}
	)


async def main():

	async with httpx.AsyncClient(base_url='http://localhost:8000') as client:

		user_requests = [post_users(client) for _ in range(3)]
		for user_request in asyncio.as_completed(user_requests):

			user_id = (await user_request).json()['id']

			activities_requests = [post_activity_types(client, user_id) for _ in range(3)]
			for activity_request in asyncio.as_completed(activities_requests):

				activity_type_id = (await activity_request).json()['id']

				session_requests = [post_sessions(client, user_id) for _ in range(3)]
				for session_request in asyncio.as_completed(session_requests):

					session_id = (await session_request).json()['id']

					session_activity_requests = [post_activities(client, user_id, session_id, activity_type_id) for _ in range(3)]
					for session_activity_request in asyncio.as_completed(session_activity_requests):

						session_activity_id = (await session_activity_request).json()['id']

						action_requests = [post_action(client, user_id, session_id, session_activity_id) for _ in range(3)]
						for action_request in asyncio.as_completed(action_requests):

							print((await action_request).json())

if __name__ == '__main__':
	asyncio.run(main())
