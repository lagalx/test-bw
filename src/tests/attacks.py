from pathlib import Path

from src.contstatnts import ATTACKS_PATH, EMBEDED_PATH, EXTRACT_PATH, WM_SHAPE
from src.tests.embed_extract import EMBEDED_IMAGE_PATH
from src.utils import gausian_blur, rotate
from src.watermark import extract

ROTATE_ATTACK_OUT: Path = ATTACKS_PATH / "rotated.jpg"
ROTATE_ATTACK_EXTRACT: Path = EXTRACT_PATH / "rotated.jpg"
ROTATE_ATTACK_RECOVER: Path = ATTACKS_PATH / "rotated_recover.jpg"
ROTATE_ATTACK_ANGLE: int = 12

PHOTO_ATTACK: Path = ATTACKS_PATH / "photo.jpg"
PHOTO_ATTACK_EXTRACT: Path = EXTRACT_PATH / "photo.jpg"

CROPED_ATTACK: Path = ATTACKS_PATH / "croped.jpg"
CROPED_ATTACK_EXTRACT: Path = EXTRACT_PATH / "croped.jpg"

BLURED_ATTACK = Path = ATTACKS_PATH / "blured.jpg"
BLURED_ATTACK_EXTRACT: Path = EXTRACT_PATH / "blured.jpg"

NOISED_ATTACK = Path = ATTACKS_PATH / "noised.jpg"
NOISED_ATTACK_EXTRACT: Path = EXTRACT_PATH / "noised.jpg"


def rotate_attack(embeded_path: Path):
    rotate(embeded_path, ROTATE_ATTACK_OUT, angle=ROTATE_ATTACK_ANGLE)
    rotate(ROTATE_ATTACK_OUT, ROTATE_ATTACK_RECOVER, angle=-ROTATE_ATTACK_ANGLE)

    extract(
        image=ROTATE_ATTACK_RECOVER,
        wm_shape=WM_SHAPE,
        out_wm_name=ROTATE_ATTACK_EXTRACT,
    )


def cropped_attack():
    extract(
        image=CROPED_ATTACK,
        wm_shape=WM_SHAPE,
        out_wm_name=CROPED_ATTACK_EXTRACT,
    )


def blured_attack(embeded_path):
    gausian_blur(embeded_path, BLURED_ATTACK, (39, 39))

    extract(
        image=BLURED_ATTACK,
        wm_shape=WM_SHAPE,
        out_wm_name=BLURED_ATTACK_EXTRACT,
    )


def noise_attack():
    extract(
        image=NOISED_ATTACK,
        wm_shape=WM_SHAPE,
        out_wm_name=NOISED_ATTACK_EXTRACT,
    )


def photo_attack():
    extract(
        image=PHOTO_ATTACK,
        wm_shape=WM_SHAPE,
        out_wm_name=PHOTO_ATTACK_EXTRACT,
    )


def main():
    rotate_attack(EMBEDED_IMAGE_PATH)
    # blured_attack(EMBEDED_IMAGE_PATH)


if __name__ == "__main__":
    main()
