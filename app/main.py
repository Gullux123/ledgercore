
from fastapi import FastAPI

app = FastAPI(
    title="LedgerCore API",
    description="A simulated double-entry payment ledger",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "LedgerCore API"
    }
