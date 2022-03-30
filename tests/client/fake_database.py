
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ...src.datalayer.database import Base
from ...src import model

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app_test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
	SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_test_db():
	session = SessionLocal()
	try:
		yield session
	finally:
		session.close()
