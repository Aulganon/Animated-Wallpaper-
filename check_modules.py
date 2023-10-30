
from pathlib import Path

def ifPathExist(path):
    if Path.is_file(path):
        return True
    return False

# checks if given file is
# allowed in opencv video capture
def IsVideo(file):
    from config import allowed_video_formats as avf 
    if Path(file).suffix in avf:
        return True
    return False
    
def IsImage(file):
    pass
# end this 