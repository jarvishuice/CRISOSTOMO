# Importa Python desde Dockerhub
FROM python:3.11

# Crea un directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt dentro del directorio /app

RUN htop
# Ejecuta Uvicorn para iniciar la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
