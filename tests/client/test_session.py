
from datetime import datetime

from .client_test_case import ClientTestCase

class TestSession(ClientTestCase):

	def setUp(self):
		super().setUp()

		response = self.client.post("/users", json={'email': 'test_email'})

		self.user_id = response.json()['id']
		self.session_json = {
			'start_time': datetime(1998, 3, 25, 8, 45, 30).isoformat()
		}


	def test_post_session(self):
		response = self.client.post(self.session_url(), json=self.session_json)

		assert response.status_code == 200


	def test_post_session_non_existing_user(self):
		response = self.client.post(self.session_url(self.user_id+1), json=self.session_json)

		assert response.status_code == 404


	def test_get_session(self):
		post_response = self.client.post(self.session_url(), json=self.session_json)
		session_id = post_response.json()['id']

		response = self.client.get(self.session_url(session_id=session_id))

		assert response.status_code == 200


	def test_get_non_existing_session(self):

		response = self.client.get(self.session_url(session_id=404))

		assert response.status_code == 404


	def test_get_session_wrong_user(self):
		session_id = self.client.post(self.session_url(), json=self.session_json).json()['id']

		response = self.client.get(self.session_url(self.user_id+1, session_id))

		assert response.status_code == 404


	def test_get_all_sessions_of_user(self):
		_ = self.client.post(self.session_url(), json=self.session_json)
		_ = self.client.post(self.session_url(), json=self.session_json)
		_ = self.client.post(self.session_url(), json=self.session_json)

		response = self.client.get(self.session_url())

		assert response.status_code == 200
		assert response.json() == [
			{'id': 1, 'owner_id': 1, 'start_time': '1998-03-25T08:45:30'},
			{'id': 2, 'owner_id': 1, 'start_time': '1998-03-25T08:45:30'},
			{'id': 3, 'owner_id': 1, 'start_time': '1998-03-25T08:45:30'}
		]


	def test_get_all_sessions_of_wrong_user(self):
		response = self.client.post("/users", json={'email': 'test_email2'})
		user_id = response.json()['id']

		_ = self.client.post(self.session_url(), json=self.session_json)
		_ = self.client.post(self.session_url(), json=self.session_json)
		_ = self.client.post(self.session_url(), json=self.session_json)

		response = self.client.get(self.session_url(user_id))

		assert response.status_code == 200
		assert response.json() == []


	def session_url(self, user_id=None, session_id=None) -> str:

		match (user_id, session_id):

			case (None, None):
				return f'/users/{self.user_id}/sessions'

			case (user_id, None):
				return f'/users/{user_id}/sessions'

			case (None, session_id):
				return f'/users/{self.user_id}/sessions/{session_id}'

			case (user_id, session_id):
				return f'/users/{user_id}/sessions/{session_id}'
