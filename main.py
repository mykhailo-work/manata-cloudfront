from fastapi import FastAPI, Request, Header

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated
from fastapi.middleware.trustedhost import TrustedHostMiddleware, CORSMiddleware

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, query_token: Annotated[str | None, Header()] = None):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"query_token": query_token}
    )
