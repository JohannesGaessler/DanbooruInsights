#!/usr/bin/env python3

import json
import os
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

METADATA_PATH = "/run/media/johannesg/WD-Green-750G/Danbooru2021/metadata"
WITH_TAGS = []
WITHOUT_TAGS = []

files = sorted(glob(os.path.join(METADATA_PATH, "posts*.json")))


def analyze_file(json_file):
    widths = []
    heights = []
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
            if tags_okay:
                widths.append(int(metadata_dict["image_width"]))
                heights.append(int(metadata_dict["image_height"]))
            line = f.readline()
    return widths, heights


with Pool(processes=len(files)) as pool:
    dimensions = pool.map(analyze_file, files)

widths = []
heights = []
for dimensions_i in dimensions:
    widths += dimensions_i[0]
    heights += dimensions_i[1]
widths = np.array(widths, dtype=float)
heights = np.array(heights, dtype=float)
image_aspect_ratios = widths / heights

aspect_ratios = [(16, 9), (4, 3), (1, 1), (3, 4), (1, 1.41)]
num_pictures_total = image_aspect_ratios.shape[0]
print(f"Total: {num_pictures_total}")
num_pictures = []
for aspect_ratio_w, aspect_ratio_h in aspect_ratios:
    ratio_fits = np.abs(image_aspect_ratios * (aspect_ratio_h / aspect_ratio_w) - 1) < 0.02
    num_pictures_i = np.sum(ratio_fits)
    print(
        f"{aspect_ratio_w}/{aspect_ratio_h}: "
        f"{num_pictures_i}, {num_pictures_i/num_pictures_total*100:.2f}%"
    )
    num_pictures.append(num_pictures_i)
num_other = num_pictures_total - np.sum(num_pictures)
print(f"Other: {num_other}, {num_other/num_pictures_total*100:.2f}%")

plt.figure(figsize=(6, 6))
start = 400
stop = 5000
plt.hist2d(widths, heights, bins=np.logspace(start=np.log10(start), stop=np.log10(stop), num=241))
plt.plot([start, stop/1.41], [start*1.41, stop], label="1:1.41", alpha=0.25)
plt.plot([start, stop*3/4], [start*4/3, stop], label="3:4", alpha=0.25)
plt.plot([start, stop], [start, stop], label="1:1", alpha=0.25)
plt.plot([start*4/3, stop], [start, stop*3/4], label="4:3", alpha=0.25)
plt.plot([start*16/9, stop], [start, stop*9/16], label="16:9", alpha=0.25)
plt.xscale("log")
plt.yscale("log")
plt.xticks([start, 1000, stop], labels=[start, 1000, stop])
plt.yticks([start, 1000, stop], labels=[start, 1000, stop])
plt.legend(loc="upper left")
plt.xlabel("Image width [pixel]")
plt.ylabel("Image height [pixel]")
title = "Distribution of image dimensions"
if WITH_TAGS:
    title += f"\nwith tags {WITH_TAGS}"
if WITH_TAGS and WITHOUT_TAGS:
    title += " and"
if WITHOUT_TAGS:
    title += f"\nwithout tags {WITHOUT_TAGS}"
plt.title(title)
plt.savefig("dimension_2d.png", dpi=240)
plt.show()
