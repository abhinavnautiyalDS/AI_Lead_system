from fastapi import FastAPI
from app.api.routes import router
from app.database.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Lead Qualification System"
)

app.include_router(router)

@app.get("/")
def home():

    return {
        "message": "AI Lead Qualification System Running"
    }