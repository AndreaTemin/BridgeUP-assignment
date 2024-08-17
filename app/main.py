from fastapi import FastAPI, HTTPException
from app.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "This is the BridgeUP-assignmente project, welcome!"}
