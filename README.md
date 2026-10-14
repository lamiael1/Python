# Actividad de tarde · Gestor de expedientes

## Objetivo

Construir un programa de consola para gestionar expedientes almacenados en un fichero JSON. El programa será la base de datos simulada que utilizaremos durante el día 2 con FastAPI.

Al terminar deberías poder ejecutar un menú que permita consultar, crear y actualizar expedientes sin modificar directamente el fichero JSON.

## Preparación

Abre esta carpeta completa en VS Code y ejecuta estos comandos desde la terminal integrada de PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
git init
git status
```

No hay librerías externas para instalar en esta actividad. Python incluye el módulo `json` en su biblioteca estándar.

## Ejecución

Cuando implementes el programa, ejecútalo así:

```powershell
python app/main.py
```

## Datos iniciales

Los expedientes se encuentran en `data/expedientes.json`. Cada uno incluye:

```text
id, titulo, prioridad, estado, solicitante, fecha_creacion
```

Valores válidos:

- Prioridad: `alta`, `media` o `baja`.
- Estado: `abierto`, `en_progreso` o `cerrado`.

## Tareas obligatorias

Completa las funciones marcadas con `TODO` en `app/main.py`.

1. Cargar el fichero JSON con `cargar_expedientes`.
2. Listar los expedientes mostrando ID, prioridad, estado y título.
3. Buscar un expediente por identificador.
4. Filtrar por estado o prioridad.
5. Crear un expediente validando los campos y evitando IDs duplicados.
6. Cambiar el estado de un expediente existente.
7. Guardar la lista actualizada en el fichero JSON.
8. Crear un menú de consola que permita acceder a cada operación.

## Manejo de errores esperado

El programa no debe cerrarse ante estos casos:

- El fichero de datos no existe o contiene JSON inválido.
- El usuario escribe una opción de menú inexistente.
- El ID no existe o ya existe.
- La prioridad o el estado no son válidos.
- Se deja vacío un campo obligatorio.

Usa excepciones concretas, por ejemplo `FileNotFoundError`, `json.JSONDecodeError` y `ValueError`. Evita `except:` sin indicar el tipo de error.

## Tipado y organización

- Añade anotaciones de tipo a las funciones nuevas.
- Cada función debe tener una responsabilidad clara.
- Extrae funciones auxiliares cuando el menú o una operación se vuelvan difíciles de leer.
- Puedes dividir la solución en más módulos dentro de `app/` si lo consideras útil.

## Git: hitos mínimos

Trabaja en una rama propia y crea commits pequeños. Ejemplo:

```powershell
git switch -c feature/gestor-expedientes
git add .gitignore README.md
git commit -m "chore: configura el proyecto inicial"

git add app/main.py
git commit -m "feat: lista expedientes desde JSON"

git add app/main.py
git commit -m "feat: permite buscar expedientes por ID"

git add app/main.py
git commit -m "fix: valida la prioridad al crear expedientes"
```

## Entregable

Antes de terminar, verifica:

- `python app/main.py` se ejecuta sin errores.
- El README sigue explicando cómo ejecutar el programa.
- `.venv/` y `__pycache__/` no aparecen en `git status`.
- El historial tiene al menos tres commits con mensajes claros.
- Puedes mostrar una breve demo: listar, buscar, crear o actualizar un expediente.

## Retos opcionales

- Filtrar también por solicitante.
- Ordenar por prioridad o fecha de creación.
- Añadir una opción para eliminar un expediente tras pedir confirmación.
- Guardar una copia de seguridad antes de modificar el JSON.
- Separar persistencia, validación y menú en módulos distintos.
