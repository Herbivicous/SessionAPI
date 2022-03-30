
import logging
from fastapi import FastAPI

from src.routers import (
	user_router,
	session_router,
	activity_router,
	activity_type_router,
	action_router
)
from src.datalayer.database import Base, engine

# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router)
app.include_router(activity_type_router)
app.include_router(session_router)
app.include_router(activity_router)
app.include_router(action_router)
