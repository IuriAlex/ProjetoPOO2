from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI(
    title="ProjetoPOOII ",
    version='1',
    description="Api desenvolvida na disciplina de Programação Orientado a Objeto II"
)

from Fastapi.App.views.DepartamentoCrud import departamento
from Fastapi.App.views.FuncionarioCrud import funcionario
from Fastapi.App.views.GerenteCrud import gerente
from Fastapi.App.views.ProjetoCrud import projeto
from Fastapi.App.views.RegistroDePresencaCrud import registroDePresenca
from Fastapi.App.views.TrabalhaEmCrud import trabalhaEm

app.include_router(departamento)
app.include_router(funcionario)
app.include_router(gerente)
app.include_router(projeto)
app.include_router(registroDePresenca)
app.include_router(trabalhaEm)


@app.get("/apiname", include_in_schema=False, response_class=HTMLResponse)
async def apiname() -> str:
    return "ProjetoPOOII"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5432, log_level="info", reload=True)

# localhost:5432/docs