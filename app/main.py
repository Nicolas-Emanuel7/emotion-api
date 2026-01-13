from fastapi import FastAPI
from app.predict import router

app = FastAPI(title="Emotion Detection API")
app.include_router(router)
