import os
import ctypes


def set_wallpaper(image_path):
    abs_path = os.path.abspath(image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)


if __name__ == "__main__":
    set_wallpaper("wallpapers/juicy_green_apple.jpg")
