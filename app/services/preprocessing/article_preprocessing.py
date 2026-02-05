from app.schema.preprocess import Article, Preprocess_object
from app.services.preprocessing.article_preprocessor import apply_preprocessing


def ready_data(data: Article) -> Article:
    return apply_preprocessing(Preprocess_object(title=data.title, content=data.content, url=data.url, source=data.source))

