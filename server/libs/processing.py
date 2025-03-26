import cv2
from pathlib import Path

def apply_denoise_filter(image_path: str, save_dir: Path) -> str:
    img = cv2.imread(image_path)
    denoised = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    processed_path = str(save_dir / f"processed_{Path(image_path).name}")
    cv2.imwrite(processed_path, denoised)
    return processed_path