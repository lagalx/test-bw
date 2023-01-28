from pathlib import Path

from src import watermark
from src.contstatnts import (
    DOC_PATH,
    DOC_WM_EMBEDED,
    EMBEDED_PATH,
    EXTRACT_PATH,
    WATERMARK_PATH,
    WM_SHAPE,
)

EMBEDED_IMAGE_PATH = EMBEDED_PATH / DOC_WM_EMBEDED
EXTRACT_IMAGE_PATH = EXTRACT_PATH / DOC_WM_EMBEDED


def embed():
    print(f"Embeding {str(EMBEDED_IMAGE_PATH)}...")
    watermark.embed(
        image=DOC_PATH,
        watermark_image=WATERMARK_PATH,
        output=EMBEDED_IMAGE_PATH,
    )


def extract():
    print(f"Extracting {str(EMBEDED_IMAGE_PATH)}...")
    watermark.extract(
        image=EMBEDED_IMAGE_PATH,
        wm_shape=WM_SHAPE,
        out_wm_name=EXTRACT_IMAGE_PATH,
    )


def full_test():
    embed()
    extract()


def main():
    full_test()


if __name__ == "__main__":
    main()
