# Usar una imagen base oficial de Python
FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos requirements.txt y manage.py
COPY requirements.txt manage.py /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto
COPY . /app/

# Exponer el puerto que usará la aplicación
EXPOSE 8000

# # Usar una imagen base oficial de Nginx
# FROM nginx:latest

# # Copiar la configuración de Nginx al contenedor
# COPY nginx.conf /etc/nginx/nginx.conf

# Comando para correr la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
