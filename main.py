from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

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

class OperacionTrigonometrica(BaseModel):
    a: float
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

@app.post("/raiz", status_code=status.HTTP_200_OK)
def raiz(datos: Operacion):
    """Calcula la raíz n-ésima (b) de un número (a)."""
    if datos.b == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El índice de la raíz (b) no puede ser cero"
        )
    return {"resultado": datos.a ** (1 / datos.b)}


@app.post("/modulo", status_code=status.HTTP_200_OK)
def modulo(datos: Operacion):
    """Calcula el residuo de la división entre a y b."""
    if datos.b == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede calcular el módulo con un divisor de cero"
        )
    return {"resultado": datos.a % datos.b}


@app.post("/logaritmo", status_code=status.HTTP_200_OK)
def logaritmo(datos: Operacion):
    """Calcula el logaritmo de a en base b."""
    if datos.a <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El argumento (a) debe ser mayor que cero"
        )
    if datos.b <= 0 or datos.b == 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La base (b) debe ser mayor que cero y diferente de 1"
        )
    n = 100000.0
    ln_a = n * (datos.a ** (1 / n) - 1)
    ln_b = n * (datos.b ** (1 / n) - 1)
    return {"resultado": ln_a / ln_b}
@app.post("/seno", status_code=status.HTTP_200_OK)
def seno(datos: OperacionTrigonometrica):
    """Calcula el seno de 'a' (en radianes)."""
    return {"resultado": round(math.sin(datos.a), 4)}


@app.post("/coseno", status_code=status.HTTP_200_OK)
def coseno(datos: OperacionTrigonometrica):
    """Calcula el coseno de 'a' (en radianes)."""
    return {"resultado": round(math.cos(datos.a), 4)}
