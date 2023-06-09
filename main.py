from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, tags=["api"], prefix="/api/products")

@app.get("/")
def root():
    return {"message": "FastAPI is not working! sds hello sdsdhola"}