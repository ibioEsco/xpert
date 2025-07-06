
from fastapi import HTTPException
from src.model.modelo_BD import (UsuarioIn, loginIn, insert_usuario)
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm,SecurityScopes
import os
import time
import jwt
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
TOKEN_EXPIRATION_SECONDS = int(os.getenv("TOKEN_EXPIRATION_SECONDS", 1800))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=os.getenv("URL_BACK")+"/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": time.time() + TOKEN_EXPIRATION_SECONDS})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def login_usuario(usuario: UsuarioIn ):
    """
    Function to log in a user.
    """
    try:
        nombre_usuario = usuario.primero_nombre +"_"+usuario.primer_apellido 
        login = loginIn(
            usurio=nombre_usuario,
            password="$2b$12$Bj/SZwlLT/f7AwPoG3L2ouM5VoPfydvGjyw2VJ43Ll5GMO6p/X.Gu"
        )
        usuario_login = await insert_usuario(login)
        print(usuario_login)
        

        
        return {"message": "Login successful", "usuario": usuario_login}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during login: {str(e)}")