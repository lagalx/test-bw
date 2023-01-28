from pathlib import Path

import cv2
import imutils


def rotate(image_path: Path, out_path: Path, angle:int):
    image = cv2.imread(str(image_path))
    rotated_image = imutils.rotate(image, angle=angle)
    cv2.imwrite(str(out_path), rotated_image)
    cv2.waitKey(0)

    return rotated_image

def gausian_blur(image_path: Path, out_path: Path, core: tuple[int,int]):
    image = cv2.imread(str(image_path))
    blured_image = cv2.GaussianBlur(image, core, 0)
    cv2.imwrite(str(out_path), blured_image)
    cv2.waitKey(0)

    return blured_image
