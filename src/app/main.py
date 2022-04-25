import uvicorn

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .data.todo import todos

app = FastAPI()
dev_mode = True

def main():
    configure(dev_mode=True)
    uvicorn.run(app, host='127.0.0.1', port=8000)


def configure_routes():
    app.mount('/static', StaticFiles(directory='app/static'), name='static')

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/search", response_class=HTMLResponse)
async def search_todo(request: Request, search: str = Form(...)):

    if not len(search):
        return templates.TemplateResponse("todo.html", {"todos": []})

    res_todos = []
    for todo in todos:
        if search in todo["title"]:
            res_todos.append(todo)
    
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": res_todos
        })

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


def configure(dev_mode: bool):
    configure_routes()

if __name__ == '__main__':
    main()
else:
    configure(dev_mode=True)