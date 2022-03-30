
from contextlib import closing

from unittest import TestCase
from fastapi.testclient import TestClient

from .fake_database import get_test_db, SessionLocal

from ...src.datalayer.database import get_db
from ...src import model
from ...api import app

class ClientTestCase(TestCase):

	def setUp(self):
		app.dependency_overrides[get_db] = get_test_db
		self.client = TestClient(app)

	def tearDown(self):
		with closing(SessionLocal()) as session:
			session.query(model.User).delete()
			session.query(model.Session).delete()
			session.commit()
