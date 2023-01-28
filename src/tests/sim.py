from pathlib import Path

import cv2
from skimage.metrics import structural_similarity

from src.tests.attacks import (
    BLURED_ATTACK_EXTRACT,
    CROPED_ATTACK_EXTRACT,
    NOISED_ATTACK_EXTRACT,
    ROTATE_ATTACK_EXTRACT,
)
from src.tests.embed_extract import EXTRACT_IMAGE_PATH


def check(original: Path, to_check: Path):
    original = cv2.imread(str(original))
    to_check = cv2.imread(str(to_check))
    score = cv2.matchTemplate(original, to_check, cv2.TM_CCOEFF_NORMED)[0][0]
    # score, diff = structural_similarity(
    #     cv2.cvtColor(original, cv2.COLOR_BGR2GRAY),
    #     cv2.cvtColor(to_check, cv2.COLOR_BGR2GRAY),
    #     full=True,
    # )

    return score


def main():

    print("BLURED")
    score = check(EXTRACT_IMAGE_PATH, BLURED_ATTACK_EXTRACT)
    print("Similarity Score: {:.3f}%".format(score * 100))
    print("CROPED")
    score = check(EXTRACT_IMAGE_PATH, CROPED_ATTACK_EXTRACT)

    print("Similarity Score: {:.3f}%".format(score * 100))
    print("ROTATE")
    score = check(EXTRACT_IMAGE_PATH, ROTATE_ATTACK_EXTRACT)

    print("Similarity Score: {:.3f}%".format(score * 100))
    print("NOISED")
    score = check(EXTRACT_IMAGE_PATH, NOISED_ATTACK_EXTRACT)

    print("Similarity Score: {:.3f}%".format(score * 100))


if __name__ == "__main__":
    main()
