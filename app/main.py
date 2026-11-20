from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health

app = FastAPI(
    title="Customer Portal API",
    description="Backend API for Customer Portal",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)


@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Welcome to Customer portal!",
        "version": "1.0.0"
    }