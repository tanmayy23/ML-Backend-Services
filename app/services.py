from fastapi import FastAPI

app = FastAPI(title = "ML Backend Service")

@app.get("/health")
def health_check():
    return {"status":"ok"}

