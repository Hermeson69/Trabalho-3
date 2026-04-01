from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.features.temperature.temp_router import router as temp_router

app = FastAPI(
    title="Trabalho 3 API",
    description="API for sensor readings",
    version="0.1.0",
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(temp_router)


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to Trabalho 3 API"}