# Control de Fichajes

Aplicación de demostración hecha con Django

## Preparación

Crear entorno virtual:

```sh
python3 -m venv .venv
```

Para la activación:

```sh
.venv/bin/activate
```

(En Windows utilizar .venv\Scripts\activate).

Con el entorno virtual activado, instalar dependencias:

```sh
pip install -r requirements.txt
```


## Puesta en marcha

Configurar los ajustes de la base de datos en `hola/settings.py`.

Lanzar el servidor integrado:

```sh
python3 manage.py runserver
```

Abrir el enlace `http://127.0.0.1:8000` desde un navegador.
