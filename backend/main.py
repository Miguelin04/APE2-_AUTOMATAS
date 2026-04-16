from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from automatas import (
    generar_cadenas, pertenece, union, concatenacion,
    kleene_star, kleene_plus, analizar_crecimiento
)
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos Pydantic
class GenerarCadenasReq(BaseModel):
    alfabeto: List[str]
    max_len: int

class PerteneceReq(BaseModel):
    cadena: str
    lenguaje: List[str]

class BinarioReq(BaseModel):
    l1: List[str]
    l2: List[str]

class UnarioReq(BaseModel):
    l: List[str]
    max_iter: int

class AnalisisReq(BaseModel):
    l: List[str]

# API Endpoints
@app.post("/api/generar_cadenas")
def api_generar_cadenas(req: GenerarCadenasReq):
    return {"resultado": generar_cadenas(req.alfabeto, req.max_len)}

@app.post("/api/pertenece")
def api_pertenece(req: PerteneceReq):
    return {"resultado": pertenece(req.cadena, req.lenguaje)}

@app.post("/api/union")
def api_union(req: BinarioReq):
    return {"resultado": union(req.l1, req.l2)}

@app.post("/api/concatenacion")
def api_concatenacion(req: BinarioReq):
    return {"resultado": concatenacion(req.l1, req.l2)}

@app.post("/api/kleene_star")
def api_kleene_star(req: UnarioReq):
    return {"resultado": kleene_star(req.l, req.max_iter)}

@app.post("/api/kleene_plus")
def api_kleene_plus(req: UnarioReq):
    return {"resultado": kleene_plus(req.l, req.max_iter)}

@app.post("/api/analizar_crecimiento")
def api_analizar_crecimiento(req: AnalisisReq):
    return {"resultado": analizar_crecimiento(req.l)}

# Mount frontend
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

@app.get("/")
def serve_index():
    return FileResponse(os.path.join(frontend_dir, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
