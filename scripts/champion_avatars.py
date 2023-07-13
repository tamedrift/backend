import os

import requests

from wildrift_cn.models import Champion


def run():
    champions = Champion.objects.values("heroId", "avatar")
    for champion in champions:
        # Extract the filename from the URL
        filename = champion["heroId"]
        filepath = f"avatars/{filename}.png"

        # Skip if exists
        if os.path.exists(filepath):
            print(f"Already exists: {filename}")
            continue

        url = champion["avatar"]
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Save the image to disk
                with open(filepath, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded image: {filename}")
            else:
                print(f"Failed to download image: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download image: {url} - {str(e)}")
