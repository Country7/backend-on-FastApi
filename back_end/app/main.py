from fastapi import FastAPI
from app.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from app.handlers import router


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION) # создаем объект класса FastAPI
    application.include_router(router, prefix=API_PREFIX) # добавляем к приложению роутер из файла back_end/app/handlers.py
    return application   # возвращаем этот объект



app = get_application()

