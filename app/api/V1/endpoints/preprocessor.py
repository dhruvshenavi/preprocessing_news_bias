from fastapi import APIRouter
from starlette.concurrency import run_in_threadpool
from app.schema.preprocess import Article
from app.services.preprocessing.article_preprocessing import ready_data

router = APIRouter()

@router.post("/preprocess")
async def preprocess(data: Article):
    return await run_in_threadpool(ready_data, data)


# change according to preprocessor