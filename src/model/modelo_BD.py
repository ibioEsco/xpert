import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field
from typing import Optional, Annotated
from fastapi import Depends
import os

from beanie import Document, Indexed, init_beanie






class UsuarioIn(Document):
    primero_nombre: Annotated[str, Indexed()]
    segundo_nombre: str = None
    primer_apellido: str 
    segundo_apellido: str = None
    cedula: Annotated[int, Indexed(unique=True)]
    email: Annotated[str, Indexed()]
    
class loginIn(Document):
    usurio: Annotated[str, Indexed(unique=True)]
    password: Annotated[str, Indexed()]



async def init():
    # Create Motor client
    client = AsyncIOMotorClient(os.getenv("MONGO_URL"))

    # Init beanie with the Product document class
    await init_beanie(database=client.usuariosdb, 
                      document_models=[UsuarioIn, loginIn])
    
    
async def insert_usuario(usuario: UsuarioIn):
    """
    Insert a new user into the database.
    """
    await usuario.insert()
    return usuario


#listar todos los usuarios
async def listar_usuario():
    """
    List all users in the database.
    """
    usuarios = await UsuarioIn.find_all().to_list()
    return usuarios

async def autenticar_usuario(usuario: str, password: str):
    """
    Authenticate a user by username and password.
    """
    user = await loginIn.find_one(loginIn.usurio == usuario)
    return user
    
