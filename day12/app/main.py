from fastapi import FastAPI

from database import init_db
from routers.tasks import router

app = FastAPI(
    title="Task API"
)


@app.on_event("startup")
def startup():
    init_db()


app.include_router(router)