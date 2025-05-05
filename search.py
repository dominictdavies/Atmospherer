import requests
from duckduckgo_search import DDGS
from datetime import datetime
import os


def fetch_wallpaper_image(search_terms, folder="wallpapers"):
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{timestamp}_{search_terms.replace(' ', '_')}.jpg"
    save_path = os.path.join(folder, filename)

    results = DDGS().images(search_terms + " wallpaper", layout="wide", max_results=1)

    if not results:
        raise ValueError("No image results found.")

    image_url = results[0]["image"]
    response = requests.get(image_url)

    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"Image saved to {save_path}")
    else:
        raise Exception("Failed to download image.")

    return save_path


if __name__ == "__main__":
    fetch_wallpaper_image("juicy green apple")
