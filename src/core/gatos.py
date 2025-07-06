import requests
import os

def lista_raza_gatos():
    
    response = requests.get("https://api.thecatapi.com/v1/breeds")
    print("Obteniendo gatos...")
    return response.json()


def gato_por_id(raza_id):
    response = requests.get(f"https://api.thecatapi.com/v1/images/search?breed_ids={raza_id}")
    if response.status_code == 404:
        raise ValueError("Raza de gato no encontrada")
    return response.json()

def gato_por_parametro(
    limite=1,
    pagina=0,
    RAND="random",
    ha_creeds=0,
    razasids=None,
    categorias=None,
    sub_id=None
):
    headers = {"x-api-key" :os.getenv("API_KEY")}


    url = "https://api.thecatapi.com/v1/images/search"
    params = {
        "limit": limite,
        "page": pagina,
        "order": RAND,
        "has_breeds": ha_creeds
    }
    if razasids:
        params["breed_ids"] = razasids
    if categorias:
        params["breed_ids"] = categorias
    if sub_id:
        params["sub_id"] = sub_id

    response = requests.get(url, params=params,headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Error en la consulta: {response.status_code}")
    return response.json()
    
if __name__ == "__main__":
    try:
        lista_raza_gatos()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los gatos: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")