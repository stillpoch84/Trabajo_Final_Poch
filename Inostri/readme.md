# I Nostri

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```

# Instruccion de uso de la página
La página es de uso intuitivo. Cada botón del navegador permite entrar a las distintas clases y ahí se encuentran listadas alfabéticamente. 
A su vez, cada una tiene su botón para agregar un objeto a la base de datos y permite buscar (busca por nombre y por su 2da característica listada).
