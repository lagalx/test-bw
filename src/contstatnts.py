from pathlib import Path

from src.watermark import WmShape

WM_SHAPE: WmShape = WmShape(270, 270)


IMAGES_PATH: Path = Path.cwd() / "img"
ORIGINALS_PATH: Path = IMAGES_PATH / "originals"

DOC_PATH: Path = ORIGINALS_PATH / "doc.jpg"
WATERMARK_PATH: Path = ORIGINALS_PATH / "watermark.jpg"
DOC_WM_EMBEDED: str = "doc_embeded.jpg"


OUT_PATH: Path = IMAGES_PATH / "out"

EMBEDED_PATH: Path = OUT_PATH / "embeded"
EXTRACT_PATH: Path = OUT_PATH / "extract"
ATTACKS_PATH: Path = OUT_PATH / "attacks"
