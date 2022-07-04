# DanbooruInsights
Some simple scripts I made for analysis of the [Danbooru2021 dataset](https://www.gwern.net/Danbooru2021) as well as the resulting plots with explanations.
Analysis is done using only the metadata files (total size of 21GB) rather than the actual dataset.
The order of scripts is chosen in a way that is intended to be didactic rather than in chronological order.

## Aspect Ratio
[Aspect Ratio](./aspect_ratio) plots the distribution of image size and aspect ratio in one dimension each.

## Dimension 2d
[Dimension 2d](./dimension_2d) is concerned with the two-dimensional distribution of image widths and image heights and to what degree images conform to common aspect ratios.

## Disk Usage Calculator
[Disk Usage Calculator](./disk_usage_calculator) is a small utility for calculating the projected disk usage for the dataset
when considering tag, rating, and file extension filters as well as resizing the files.
