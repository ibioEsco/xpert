from typing import Union

from fastapi import FastAPI
from src.api.gatos_api import router as enuratador_gatos
from src.api.usuarios_api import router as enuratador_usuarios
from src.model.modelo_BD import init
from src.api.login_api import router as enuratador_login

app = FastAPI()
app.include_router(enuratador_gatos, prefix="/v1", tags=["gatos"])
app.include_router(enuratador_usuarios, prefix="/v1", tags=["usuarios"])
app.include_router(enuratador_login, prefix="/v1", tags=["login"])





@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.on_event("startup")
async def app_init():
    await init()


