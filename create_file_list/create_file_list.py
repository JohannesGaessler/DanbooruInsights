#!/usr/bin/env python3

import json
import os
from glob import glob
import numpy as np
from multiprocessing import Pool

METADATA_PATH = "/run/media/johannesg/WD-Green-750G/Danbooru2021/metadata"
WITH_TAGS = []
WITHOUT_TAGS = []
RATINGS = {"s": True, "q": True, "e": True}
FILE_EXTENSIONS = [
    "avi", "bmp", "gif", "html", "jpeg", "jpg", "mp3", "mp4", "mpg", "pdf",
    "png", "rar", "swf", "webm", "wmv", "zip"
]
#FILE_EXTENSIONS = ["jpeg", "jpg", "png"]  # images only
#FILE_EXTENSIONS = ["avi", "gif", "mp4", "mpg", "webm", "wmv", "zip"]  # animated only
MAX_SIZE = 10000000000  # max size of images/videos

files = sorted(glob(os.path.join(METADATA_PATH, "posts*.json")))


def analyze_file(json_file):
    danbooru_ids = []
    file_extensions = []
    with open(json_file, "r", encoding="utf8") as f:
        line = f.readline()
        while line:
            metadata_dict = json.loads(line)
            tags_okay = True
            for tag in WITH_TAGS:
                if tag not in metadata_dict["tag_string"]:
                    tags_okay = False
            for tag in WITHOUT_TAGS:
                if tag in metadata_dict["tag_string"]:
                    tags_okay = False
            rating_okay = RATINGS[metadata_dict["rating"]]
            file_extension = metadata_dict["file_ext"]
            file_extension_okay = file_extension in FILE_EXTENSIONS
            size_okay = int(metadata_dict["image_width"]) <= MAX_SIZE \
                and int(metadata_dict["image_height"]) <= MAX_SIZE
            if tags_okay and rating_okay and file_extension_okay and size_okay:
                try:
                    danbooru_id = int(metadata_dict["id"])
                except KeyError:
                    line = f.readline()
                    continue
                danbooru_ids.append(danbooru_id)
                file_extensions.append(file_extension)
            line = f.readline()
    return danbooru_ids, file_extensions


with Pool(processes=len(files)) as pool:
    partial_results = pool.map(analyze_file, files)

danbooru_ids = []
file_extensions = []
for danbooru_ids_i, file_extensions_i in partial_results:
    danbooru_ids += danbooru_ids_i
    file_extensions += file_extensions_i
print(f"{len(danbooru_ids)} files")

with open("out.txt", "w", encoding="ascii") as f:
    for danbooru_id, file_extension in zip(danbooru_ids, file_extensions):
        f.write(f"original/{danbooru_id % 1000:04d}/{danbooru_id}.{file_extension}\n")
