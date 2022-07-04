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
pixels = widths * heights
aspect_ratios = widths / heights

plt.figure()
start = 100
stop = 10000
plt.hist(np.sqrt(pixels), bins=np.logspace(start=np.log10(start), stop=np.log10(stop), num=121))
plt.xlim(start, stop)
plt.xscale("log")
plt.xlabel(r"$\sqrt{n_\mathrm{px}}$")
plt.ylabel("Number of images")
plt.savefig("size.png", dpi=240)

plt.figure()
start = 0.2
stop = 3
plt.hist(aspect_ratios, bins=np.logspace(start=np.log10(start), stop=np.log10(stop), num=121))
aspect_ratios = np.array([(2, 3), (1, 1.41), (3, 4), (4, 5), (1, 1), (4, 3), (1.41, 1), (16, 9)])
plt.vlines(
    x=aspect_ratios[:, 0]/aspect_ratios[:, 1],
    ymin=0,
    ymax=1000000,
    colors=(1.0, 0.0, 0.0, 0.5),
)
plt.xlim(start, stop)
plt.ylim(0, 800000)
plt.xscale("log")
plt.xlabel("width / height")
plt.ylabel("Number of images")
plt.savefig("aspect_ratio.png", dpi=240)

plt.show()
