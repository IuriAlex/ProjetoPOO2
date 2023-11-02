from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI(
    title="ProjetoPOOII ",
    version='1',
    description="Api desenvolvida na disciplina de Programação Orientado a Objeto II"
)

from Fastapi.App.views.FuncionarioCrud import funcionario

app.include_router(funcionario)


@app.get("/apiname", include_in_schema=False, response_class=HTMLResponse)
async def apiname() -> str:
    return "AvaliacaoPOOII"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5935, log_level="info", reload=True)