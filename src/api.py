from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


@app.post("/leitura")
async def create_leitura(leitura: dict):
    """Create a new sensor reading"""
    # Here you would normally save the leitura to the database
    return {"message": "Leitura created successfully", "leitura": leitura}