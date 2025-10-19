from typing import Annotated

from fastapi import APIRouter, Form, Request, status
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers.python import PythonLexer
from pygments.styles import get_all_styles

from .schemas import ExtractionResponse
from .utils import extract_video_timestamps, load_extraction_response
import json

router = APIRouter(tags=["Extraction"], prefix="/extract")

DEFAULT_STYLE = "monokai"
# DEFAULT_STYLE = "default"


@router.post("/", status_code=status.HTTP_201_CREATED)
async def extract(videourl: Annotated[str, Form()], request: Request, style: Annotated[str, Form()] = DEFAULT_STYLE):
    code, extraction = await extract_video_timestamps(videourl)
    formatter = HtmlFormatter(style=style)
    context = {
        "all_styles": list(get_all_styles()),
        "style": style,
        "style_definitions": formatter.get_style_defs(),
        "style_bg_color": formatter.style.background_color,
        "highlighted_code": highlight(code, PythonLexer(), formatter),
        "code": code,
        "num_lines": len(code.split("\n")),
        "file_name": extraction.video_id + ".json",
        "file_path": request.url_for("data", path=f"{extraction.video_id}.json"),
    }
    return context
