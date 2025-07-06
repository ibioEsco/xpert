from fastapi import (APIRouter,
                     HTTPException,)

from src.model.modelo_BD import (UsuarioIn,
                                 insert_usuario,
                                 listar_usuario)
from src.core.login import login_usuario

router = APIRouter()


@router.post("/usuarios")
async def crear_usuario(usuario: UsuarioIn):
    """
    Endpoint para crear un nuevo usuario.
    """
    try:
        usuario_inser = await insert_usuario(usuario)
        print(usuario_inser)
        login = await login_usuario(usuario)

        return {"message": "Usuario creado exitosamente", "usuario": usuario}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el usuario: {str(e)}")
    
    
    
# listar todos los usuarios
@router.get("/usuarios")
async def listar_usuarios():
    """
    Endpoint para listar todos los usuarios.
    """
    try:

        usuarios =  await listar_usuario()
        return {"message": "Lista de usuarios", "usuarios": [usuarios]}  # Placeholder
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al listar los usuarios: {str(e)}")

    
@router.get("/usuarios/{usuario_id}")
async def obtener_usuario(usuario_id: int):
    """
    Endpoint para obtener un usuario por su ID.
    """
    try:
        # Aquí se debería agregar la lógica para obtener el usuario de la base de datos
        # Por ejemplo: usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        # if not usuario:
        #     raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"message": "Usuario encontrado", "usuario_id": usuario_id}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el usuario: {str(e)}")