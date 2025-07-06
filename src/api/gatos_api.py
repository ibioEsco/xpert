from fastapi import (APIRouter,
                     HTTPException,)
from src.util.log import Logger

from src.core.gatos import (lista_raza_gatos, 
                            gato_por_id,
                            gato_por_parametro)

router = APIRouter()
logger = Logger(log_file="app.log").get_logger()

@router.get("/gatos")
async def raza_gatos():
    """
    Endpoint para obtener la lista de razas de gatos.
    """
    try:
        razas = lista_raza_gatos()
        if not razas:
            logger.error("No se encontraron razas de gatos")
            raise HTTPException(status_code=404, detail="No se encontraron razas de gatos")
        logger.info("Razas de gatos obtenidas exitosamente")
        return razas
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener las razas de los gatos: {str(e)}")
    
@router.get("/gatos/{raza_id}")
async def raza_gato_id(raza_id: str):
    """
    Endpoint para obtener un gato por su ID de raza.
    """
    try:
        gato_id = gato_por_id(raza_id)
        if not gato_id:
            logger.error(f"Gato con ID {raza_id} no encontrado")
            raise ValueError("Gato no encontrado")
        logger.info(f"Gato con ID {raza_id} obtenido exitosamente")
        return gato_id
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el gato: {str(e)}")
    
@router.get("/gatos/buscar/")
async def buscar_gato(
    limite: int = 1,
    pagina: int = 0,
    orden: str = None,
    ha_creeds: int = 0,
    razasids: str = None,
    categorias: str = None,
    sub_id: str = None
):
    """
    Endpoint para buscar gatos con parámetros opcionales.
    """
    try:
        gatos = gato_por_parametro(
            limite=limite,
            pagina=pagina,
            RAND=orden,
            ha_creeds=ha_creeds,
            razasids=razasids,
            categorias=categorias,
            sub_id=sub_id
        )
        if not gatos:
            logger.error("No se encontraron gatos con los parámetros proporcionados")
            raise ValueError("No se encontraron gatos con los parámetros proporcionados")
        logger.info("Gatos encontrados exitosamente")
        return gatos
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar gatos: {str(e)}")
    
