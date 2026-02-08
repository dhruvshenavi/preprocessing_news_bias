from pydantic import BaseModel, HttpUrl

# change according to requirement


class Article(BaseModel): # the schema for the input request for preprocessing api. change this according to orchestration method

    title: str | None = None
    content: str | None = None
    url: HttpUrl
    error_code: int | None = None
    error_message: str | None = None
    source: str | None = None

class Preprocess_object(BaseModel):
    title: str | None = None
    content: str | None = None
    url: HttpUrl
    source: str | None = None



class PreprocessingError(Exception):
    def __init__(self, error_code: int, message: str):
        self.error_code = error_code
        self.message = message
        super().__init__(message)
