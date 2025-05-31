from fastapi import FastAPI, Request, Header, Response

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]
)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, response: Response, cache_time: int = None):
    response.headers["Cache-Control"] = cache_time or "no-cache"
    return templates.TemplateResponse(
        request=request, name="index.html", context={"query_token": cache_time}
    )
