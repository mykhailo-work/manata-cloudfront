from fastapi import FastAPI, Request, Header, Response

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, cache_time: int = None):
    response_data = {
        "request": request,
        "name": "index.html",
        "context": {"query_token": cache_time},
    }
    
    if cache_time is None:
        response_data["headers"] = {
            "Cache-Control": cache_time,
        }
    return templates.TemplateResponse(**response_data)
