
import time
from pathlib import Path

# this is a testing module 
# Setting image as wallpaper
def wallpaper_from_image(source, image_path):

    if not (source):
        drive = Path(__file__).parent.resolve()
        image_path = str(Path(drive, source))
        return image_path

def ifPathExist(path):
    if Path.is_file(path):
        return True
    return False
 
def video_show(videofile_path):
    import cv2
    counter = 0
    while True:
        isclosed = 0
        capture = cv2.VideoCapture(videofile_path)
        counter +=1
        while True:
            ret,frame = capture.read()
            if ret:
                
                timer1 = time.time()
                cv2.imwrite("frame.png", frame)
                timer2 = time.time()
                show("frame.png")
                timer3 = time.time()
                print(f'resulting time = [{(timer2 - timer1), (timer3 - timer1)}]')
                if cv2.waitKey(1) == 27:
                    isclosed = 1
                    break
            else:
                break
            
        cv2.destroyWindow(f"Frame{counter}")
        if isclosed:
            break
    capture.release()
    cv2.destroyAllWindows()


def show(image_name:str):
    import ctypes
    from ctypes import wintypes
    from pathlib import Path
    
    SPI_SETDESKWALLPAPER  = 0x0014
    SPIF_UPDATEINIFILE    = 0x0001
    SPIF_SENDWININICHANGE = 0x0002
    
    drive = Path(__file__).parent.resolve()
    image_path = str(Path(drive, image_name))
    # set SINGLE image to wallpaper
    user32 = ctypes.WinDLL('user32')
    SystemParametersInfo = user32.SystemParametersInfoW
    SystemParametersInfo.argtypes = ctypes.c_uint,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint
    SystemParametersInfo.restype = wintypes.BOOL
    SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path , 0)
    