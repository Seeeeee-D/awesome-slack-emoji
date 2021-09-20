import argparse
import json
import os
import sys
import urllib
from pdb import set_trace as pst
from typing import Dict, List, Tuple
from urllib import error, request

from tqdm import tqdm

JSON_FOLDER = os.path.join(os.path.dirname(__file__), "jsons")
DST_FOLDER = os.path.join(os.path.dirname(__file__), "emoji")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder_name", required=True, type=str)

    args = parser.parse_args()
    return args


def load_json(json_path: str) -> dict:
    path = os.path.join(JSON_FOLDER, json_path + ".json")
    with open(path, "r", encoding="utf-8") as f:
        json_load = json.load(f)
    return json_load


def get_emoji_json(load_json: dict) -> dict:
    return load_json["emoji"]


class SlackEmoji:
    def __init__(self, emoji_json: dict, folder_name: str) -> None:
        self.name: str = emoji_json["name"]
        self.url: str = emoji_json["url"]
        self.save_folder: str = os.path.join(DST_FOLDER, folder_name)
        self.img: bytes = None
        self.img_type: str = self.get_img_type()

    def download_image(self) -> None:
        try:
            with request.urlopen(self.url) as web_file:
                self.img = web_file.read()

        except error.URLError as e:
            print(e)

    def save_image(self) -> None:
        assert self.img is not None
        assert self.img_type is not None

        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)

        with open(
            os.path.join(self.save_folder, self.name + self.img_type), "wb"
        ) as img_file:
            img_file.write(self.img)

    def get_img_type(self):
        if ".png" in self.url:
            return ".png"
        elif ".gif" in self.url:
            return ".gif"
        elif ".jpg" in self.url:
            return ".jpg"
        else:
            return None


if __name__ == "__main__":
    args = get_args()
    json_load = load_json(args.folder_name)
    emoji_jsons = get_emoji_json(json_load)

    pbar = tqdm(enumerate(emoji_jsons), total=len(emoji_jsons))
    for i, emoji_json in pbar:
        emoji = SlackEmoji(emoji_json, args.folder_name)
        emoji.download_image()
        emoji.save_image()
        pbar.set_description(f"{i}")
        pbar.update()
    print("FINISH!!")
    pass
