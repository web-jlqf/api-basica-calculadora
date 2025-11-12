from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI(title="API REST Calculadora")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],  # Permitir todos los encabezados
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)


# Modelo de datos para operaciones POST
class Operacion(BaseModel):
    a: float
    b: float

# ----------------------------
# GET con parámetros en la URL
# ----------------------------
@app.get("/sumar", status_code=status.HTTP_200_OK)
def sumar(a: float, b: float):
    """
    Suma dos números enviados como parámetros en la URL.
    Ejemplo: /sumar?a=2&b=3
    """
    return {"resultado": a + b}

@app.get("/restar", status_code=status.HTTP_200_OK)
def restar(a: float, b: float):
    """Resta dos números enviados como parámetros."""
    return {"resultado": a - b}

@app.get("/factorial", status_code=status.HTTP_200_OK)
def factorial(n: float):
    """Calcula el factorial"""
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return {"resultado": fact}



# ----------------------------
# POST con cuerpo JSON
# ----------------------------
@app.post("/multiplicar", status_code=status.HTTP_201_CREATED)
def multiplicar(datos: Operacion):
    """Multiplica dos números enviados en el cuerpo JSON."""
    return {"resultado": datos.a * datos.b}

@app.post("/dividir", status_code=status.HTTP_200_OK)
def dividir(datos: Operacion):
    """Divide dos números, validando la división entre cero."""
    if datos.b == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede dividir entre cero"
        )
    return {"resultado": datos.a / datos.b}

@app.post("/potencia", status_code=status.HTTP_200_OK)
def potencia(datos: Operacion):
    """Calcula la potencia"""
    return {"resultado": datos.a ** datos.b}


@app.post("/factorial", status_code=status.HTTP_200_OK)
def factorial(datos: OperacionTrigonometrica):
    """Calcula el factorial"""
    n = int(datos.a)
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return {"resultado": fact}

class OperacionTrigonometrica(BaseModel):
    a: float

@app.post("/seno", status_code=status.HTTP_200_OK)
def seno(datos: OperacionTrigonometrica):
    """
    Calcula el seno de 'a' (en radianes).
    Ejemplo: {"a": 1.57}
    """
    return {"resultado": round(math.sin(datos.a), 4)}

@app.post("/coseno", status_code=status.HTTP_200_OK)
def coseno(datos: OperacionTrigonometrica):
    """
    Calcula el coseno de 'a' (en radianes).
    Ejemplo: {"a": 0}
    """
    return {"resultado": round(math.cos(datos.a), 4)}

