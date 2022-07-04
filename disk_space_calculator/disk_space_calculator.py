#!/usr/bin/env python3

import json
import os
from glob import glob
import numpy as np
from multiprocessing import Pool

METADATA_PATH = "/run/media/johannesg/WD-Green-750G/Danbooru2021/metadata"
WITH_TAGS = []
WITHOUT_TAGS = []
RATINGS = ["s", "q", "e"]

files = sorted(glob(os.path.join(METADATA_PATH, "posts*.json")))


def analyze_file(json_file):
    count = [0, 0, 0]
    disk_space = [0, 0, 0]
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
            rating_index = RATINGS.index(metadata_dict["rating"])
            if tags_okay:
                count[rating_index] += 1
                disk_space[rating_index] += int(metadata_dict["file_size"])
            line = f.readline()
    return count, disk_space


with Pool(processes=len(files)) as pool:
    partial_results = pool.map(analyze_file, files)

partial_results = np.array(partial_results)
counts = np.sum(partial_results[:, 0, :], axis=0)
disk_usages = np.sum(partial_results[:, 1, :], axis=0)

print(f"With tags {WITH_TAGS}")
print(f"Without tags {WITHOUT_TAGS}")
print()
print("=== Safe ===")
print(f"{counts[0]} files")
print(f"{disk_usages[0] / 1000 ** 3:.2f} GB")
print(f"{disk_usages[0] / 1024 ** 3:.2f} GiB")
print(f"{disk_usages[0] / 1000 ** 4:.2f} TB")
print(f"{disk_usages[0] / 1024 ** 4:.2f} TiB")
print()
print("=== Questionable ===")
print(f"{counts[1]} files")
print(f"{disk_usages[1] / 1000 ** 3:.2f} GB")
print(f"{disk_usages[1] / 1024 ** 3:.2f} GiB")
print(f"{disk_usages[1] / 1000 ** 4:.2f} TB")
print(f"{disk_usages[1] / 1024 ** 4:.2f} TiB")
print()
print("=== Explicit ===")
print(f"{counts[2]} files")
print(f"{disk_usages[2] / 1000 ** 3:.2f} GB")
print(f"{disk_usages[2] / 1024 ** 3:.2f} GiB")
print(f"{disk_usages[2] / 1000 ** 4:.2f} TB")
print(f"{disk_usages[2] / 1024 ** 4:.2f} TiB")
print()
print("=== Total ===")
print(f"{np.sum(counts)} files")
total = np.sum(disk_usages)
print(f"{total / 1000 ** 3:.2f} GB")
print(f"{total / 1024 ** 3:.2f} GiB")
print(f"{total / 1000 ** 4:.2f} TB")
print(f"{total / 1024 ** 4:.2f} TiB")
print()
