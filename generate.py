from dotenv import load_dotenv
from openai import OpenAI
import requests
from datetime import datetime
import re
import os


def generate_image(description: str):
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    img = client.images.generate(
        model="dall-e-3", prompt=description, n=1, size="1792x1024"
    )
    image_url = img.data[0].url
    image_data = requests.get(image_url).content

    filename = f"{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png"
    save_path = os.path.join("wallpapers", filename)

    with open(save_path, "wb") as f:
        f.write(image_data)

    return save_path


if __name__ == "__main__":
    print(
        generate_image(
            "A vibrant scene showing a quick brown fox leaping gracefully over a sleeping, relaxed dog on a grassy field."
        )
    )
