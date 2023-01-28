from pathlib import Path
from typing import NamedTuple

from blind_watermark import WaterMark, bw_notes

bw_notes.close()
READ_WM_MODE: str = "img"


class WmShape(NamedTuple):
    width: int
    height: int

    def raw(self):
        return (
            self.height,
            self.width,
        )


def embed(
    image: Path, watermark_image: Path, output: Path, mode: str = READ_WM_MODE
) -> int:
    watermark = WaterMark(mode=mode)

    watermark.read_img(str(image.absolute()))
    watermark.read_wm(str(watermark_image.absolute()))
    watermark.embed(str(output.absolute()))

    return 0


def extract(
    image: str, wm_shape: WmShape, out_wm_name: Path, mode: str = READ_WM_MODE
) -> str:
    watermark = WaterMark(mode=mode)

    wm_extract = watermark.extract(
        str(image),
        wm_shape=wm_shape.raw(),
        out_wm_name=str(out_wm_name),
    )

    return wm_extract
