from pathlib import Path
import sys

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the parent directory of the current file
ROOT = FILE.parent
# Add the root path to the sys.path list if it is not already there
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Get the relative path of the root directory with respect to the current working directory
ROOT = ROOT.relative_to(Path.cwd())

# Sources
IMAGE = "Image"
VIDEO = "Video"
WEBCAM = "Webcam"
YOUTUBE = "YouTube"

SOURCES_LIST = [IMAGE, VIDEO, WEBCAM, YOUTUBE]

# Images config
IMAGES_DIR = ROOT / "images"
DEFAULT_IMAGE = IMAGES_DIR / "image_1.jpg"
DEFAULT_DETECT_IMAGE = IMAGES_DIR / "image_2.jpg"

# Videos config
VIDEO_DIR = ROOT / "videos"
VIDEOS_DICT = {
    "sample_video_1": VIDEO_DIR / "video_1.mp4",
    "sample_video_2": VIDEO_DIR / "video_2.mp4",
}

# ML Model config
MODEL_DIR = ROOT / "weights"
DETECTION_MODEL = MODEL_DIR / "yolov8n.pt"
SEGMENTATION_MODEL = MODEL_DIR / "yolov8n-seg.pt"  # you can use custom models as well


# Webcam
WEBCAM_PATH = 1
