import json
from pathlib import Path
from typing import Any


# Ruta del archivo JSON, calculada desde la ubicación de este módulo.
RUTA_DATOS = Path(__file__).parent.parent / "data" / "expedientes.json"
# Valores permitidos para los campos de prioridad y estado.
PRIORIDADES_VALIDAS = {"alta", "media", "baja"}
ESTADOS_VALIDOS = {"abierto", "en_progreso", "cerrado"}

def cargar_expedientes(ruta: Path) -> list[dict[str, Any]]:
    # Abrimos el archivo como texto UTF-8 y convertimos el JSON en objetos Python.
    # Los errores de archivo inexistente o JSON inválido se propagarán al llamador.
    with ruta.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_expedientes(
    ruta: Path,
    expedientes: list[dict[str, Any]],
) -> None:
    # El modo "w" reemplaza el contenido anterior del archivo.
    with ruta.open("w", encoding="utf-8") as archivo:
        # indent ordena el JSON y ensure_ascii=False conserva tildes y ñ.
        json.dump(expedientes, archivo, indent=2, ensure_ascii=False)


def buscar_por_id(
    expedientes: list[dict[str, Any]],
    expediente_id: str,
) -> dict[str, Any] | None:
    # Revisamos los expedientes uno por uno hasta encontrar el ID.
    for expediente in expedientes:
        # .get("id") evita un error si el campo id no está en un registro.
        if expediente.get("id") == expediente_id:
            return expediente

    # Si termina el recorrido sin coincidencias, indicamos que no existe.
    return None

def filtrar_expedientes(
    expedientes: list[dict[str, Any]],
    campo: str,
    valor: str,
) -> list[dict[str, Any]]:
    # Normalizamos el valor una sola vez para comparar sin distinguir mayúsculas.
    valor_buscado = valor.lower()

    # Conservamos solo los expedientes cuyo campo coincide con el valor.
    return [
        expediente
        for expediente in expedientes
        if str(expediente.get(campo, "")).lower() == valor_buscado
    ]

def crear_expediente(
    expedientes: list[dict[str, Any]],
    nuevo_expediente: dict[str, Any],
) -> None:
    # Quitamos espacios sobrantes y normalizamos los valores controlados.
    expediente_id = nuevo_expediente.get("id", "").strip()
    titulo = nuevo_expediente.get("titulo", "").strip()
    prioridad = nuevo_expediente.get("prioridad", "").strip().lower()
    estado = nuevo_expediente.get("estado", "").strip().lower()

    if not expediente_id:
        raise ValueError("El ID es obligatorio.")

    if buscar_por_id(expedientes, expediente_id) is not None:
        raise ValueError(f"Ya existe un expediente con el ID {expediente_id}.")

    if not titulo:
        raise ValueError("El título es obligatorio.")

    if prioridad not in PRIORIDADES_VALIDAS:
        raise ValueError("La prioridad debe ser alta, media o baja.")

    if estado not in ESTADOS_VALIDOS:
        raise ValueError("El estado debe ser abierto, en_progreso o cerrado.")

    # Guardamos los valores ya normalizados en el nuevo expediente.
    nuevo_expediente["id"] = expediente_id
    nuevo_expediente["titulo"] = titulo
    nuevo_expediente["prioridad"] = prioridad
    nuevo_expediente["estado"] = estado

    expedientes.append(nuevo_expediente)


def cambiar_estado(
    expedientes: list[dict[str, Any]],
    expediente_id: str,
    nuevo_estado: str,
) -> None:
    # Normalizamos el estado y comprobamos que sea uno de los permitidos.
    nuevo_estado = nuevo_estado.strip().lower()
    if nuevo_estado not in ESTADOS_VALIDOS:
        raise ValueError("El estado debe ser abierto, en_progreso o cerrado.")

    # Buscamos el expediente y avisamos si el ID no existe.
    expediente = buscar_por_id(expedientes, expediente_id.strip())
    if expediente is None:
        raise ValueError(f"No existe un expediente con el ID {expediente_id}.")

    # Actualizamos el registro encontrado.
    expediente["estado"] = nuevo_estado


def mostrar_menu() -> None:
    # Mostramos las operaciones disponibles en cada vuelta del programa.
    print("\nGestor de expedientes")
    print("1. Listar expedientes")
    print("2. Buscar por ID")
    print("3. Filtrar por estado o prioridad")
    print("4. Crear expediente")
    print("5. Cambiar estado")
    print("0. Salir")

def mostrar_expedientes(expedientes: list[dict[str, Any]]) -> None:
    # Informamos cuando una búsqueda o un filtro no devuelve resultados.
    if not expedientes:
        print("No se encontraron expedientes.")
        return
    # Mostramos los datos principales de cada expediente.
    for expediente in expedientes:
        print(
            f"{expediente.get('id', 'Sin ID')} | "
            f"{expediente.get('prioridad', 'Sin prioridad')} | "
            f"{expediente.get('estado', 'Sin estado')} | "
            f"{expediente.get('titulo', 'Sin título')}"
        )

