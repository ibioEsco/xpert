# Xpert API

API REST para gestión de usuarios y razas de gatos, desarrollada con **FastAPI**, **Beanie** (ODM para MongoDB), y desplegada con **Docker**.

---

## Características

- Autenticación segura con JWT.
- Gestión de usuarios y login.
- Consulta de razas de gatos usando [TheCatAPI](https://thecatapi.com/).
- Persistencia de datos en MongoDB.
- Contenedores orquestados con Docker Compose.

---

## Requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- (Opcional para desarrollo) Python 3.11+

---

## Instalación y ejecución

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/xpert.git
cd xpert
```

### 2. Configura el archivo `.env`

Crea un archivo `.env` en la raíz del proyecto con tus variables de entorno, por ejemplo:

```
API_KEY=tu_api_key_de_thecatapi
MONGO_URL=mongodb://admin:admin@mongo:27017/
SECRET_KEY=tu_clave_secreta
```

### 3. Construye y levanta los servicios con Docker Compose

```bash
docker-compose up --build
```

Esto levantará dos contenedores:
- **mongo-db**: Base de datos MongoDB.
- **fastapi-app**: API FastAPI.

### 4. Accede a la documentación interactiva

Abre en tu navegador: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Estructura del proyecto

```
xpert/
├── src/
│   ├── api/
│   ├── core/
│   └── model/
├── requirements.txt
├── Dockerfile
├── docker-compose.yaml
└── .env
```

---

## Uso de la API

- **Login:**  
  `POST /login`  
  Envía usuario y contraseña en el cuerpo (no en la URL).

- **Consultar razas de gatos:**  
  `GET /gatos/razas`

- **Consultar imágenes de gatos por raza:**  
  `GET /gatos/imagen/{raza_id}`

---

## Comandos útiles

- Ver logs del contenedor FastAPI:
  ```
  docker logs -f --tail 100 fastapi-app
  ```
- Acceder al contenedor:
  ```
  docker exec -it fastapi-app bash
  ```
- Apagar y limpiar:
  ```
  docker-compose down -v
  ```

---

## Notas

- El archivo `.env` **pedirlo al administrador*.


---

## Licencia

MIT