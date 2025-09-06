from fastapi import FastAPI

app = FastAPI(title="Salon Manager")

@app.get("/")
async def root():
    return {"ok": True, "service": "salon-manager", "version": "0.0.1"}
