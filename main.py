import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from backend.routes import chat
from backend.routes import upload

# Load the .env file.
load_dotenv()

# App.
app = FastAPI()
app.include_router(chat.router)
app.include_router(upload.router)

# Run.
uvicorn.run(app, host="0.0.0.0", port=8000)
