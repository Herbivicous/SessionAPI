
from .client_test_case import ClientTestCase

class TestUser(ClientTestCase):

	def test_post_user(self):
		response = self.client.post("/users", json={'email': 'test_email'})

		assert response.status_code == 200
		assert response.json()['email'] == "test_email"


	def test_post_user_same_email(self):
		_ = self.client.post("/users", json={'email': 'test_email'})
		response = self.client.post("/users", json={'email': 'test_email'})

		assert response.status_code == 400


	def test_get_user(self):
		post_response = self.client.post("/users", json={'email': 'test_email'})
		user_id = post_response.json()['id']

		response = self.client.get(f"/users/{user_id}")

		assert response.status_code == 200
		assert response.json()['email'] == "test_email"


	def test_get_non_existing_user(self):

		response = self.client.get("/users/404")

		assert response.status_code == 404


	def test_delete_user(self):
		post_response = self.client.post("/users", json={'email': 'test_email'})
		user_id = post_response.json()['id']

		delete_response = self.client.delete(f"/users/{user_id}")
		get_response = self.client.get(f"/users/{user_id}")

		assert delete_response.status_code == 200
		assert delete_response.json()['email'] == "test_email"

		assert get_response.status_code == 404


	def test_get_all_users(self):
		_ = self.client.post("/users", json={'email': 'test_email1'})
		_ = self.client.post("/users", json={'email': 'test_email2'})
		_ = self.client.post("/users", json={'email': 'test_email3'})

		response = self.client.get("/users")

		assert response.status_code == 200
		assert response.json() == [
			{'email': 'test_email1', 'id': 1},
			{'email': 'test_email2', 'id': 2},
			{'email': 'test_email3', 'id': 3}
		]
