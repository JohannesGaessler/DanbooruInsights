# Dimension 2d
Image widths (x axis) and heights (y axis) are filled into a two-dimensional histogram.
The x and y axes as well as the bin sizes are scaled logarithmically.
Images with different sizes but the same aspect ratio will be located on lines with a slope of 1 in log-log space.
The y intercept of said lines determines the aspect ratio.
The purpose of the visualization is to provide an intuitive understanding where there are clusters of images and whether images conform to specific aspect ratios.

The Python script in this directory can filter images by certain tags.
## All Images
![All images](./dimension_2d.png)
Dark blue indicates few images while yellow indicates many images.
The following aspect ratios are highlighted: 2:3, 1:1.41 (see [ISO 216](https://en.wikipedia.org/wiki/ISO_216)), 3:4, 4:5, 1:1, 4:3, 1.41:1, and 16:9.
The most common aspect ratio is 1:1.41 with roughly a quarter of images adhering to this aspect ratio (see below).
However, almost half of all images do not conform to one of those aspect ratios.
A few clusters can be spotted (e.g. 800x600 or 600x800) and there is a clear preference for images where at least one dimension is a multitude of 100.
## Monochrome Only
![Monochrome only](./dimension_2d_monochrome.png)
When considering only images with the "monochrome" tag the distribution changes significantly.
The preference for the 1:41 aspect ratio becomes even more pronounced with more than 40% of all monochrome images adhering to this aspect ratio.
However, only about 10% of the images in the dataset have the monochrome tag.
## Color Only
![Color only](./dimension_2d_rgb.png)
Danbooru does not seem to have an explicit tag for color images.
Instead images seem to be assumed color images by default.
The distribution of color images is therefore determined by excluding the monochrome tag.
About 90% of images do not have the monochrome tag.
The distribution of color image dimensions is not significantly different from the distribution when considering all images.
## Numerical Data
The following table contains numerical data regarding the prevalence of aspect ratios.
An image is considered to be adhering to an aspect ratio when the ratio of the discreet width and height of an image falls within 1.5% of the aspect ratio.

| Aspect Ratio | All, Absolute | All, Percentage | Monochrome, Absolute | Monochrome, Percentage | Color, Absolute | Color, Percentage |
| ------------ | ------------- | --------------- | -------------------- | ---------------------- | --------------- | ----------------- |
| 2:3          | 199610        | 3.99%           | 14068                | 3.23%                  | 185542          | 4.06%             |
| 1:1.41       | 1241037       | 24.81%          | 187371               | 43.05%                 | 1053666         | 23.07%            |
| 3:4          | 321387        | 6.43%           | 19646                | 4.51%                  | 301741          | 6.61%             |
| 4:5          | 159944        | 3.20%           | 7696                 | 1.77%                  | 152248          | 3.33%             |
| 1:1          | 302347        | 6.05%           | 15141                | 3.48%                  | 287206          | 6.29%             |
| 4:3          | 198689        | 3.97%           | 9559                 | 2.20%                  | 189130          | 4.14%             |
| 1.41:1       | 217298        | 4.34%           | 11711                | 2.69%                  | 205587          | 4.50%             |
| 16:9         | 95084         | 1.90%           | 1828                 | 0.42%                  | 93256           | 2.04%             |
| Other        | 2266176       | 45.31%          | 168214               | 48.65%                 | 2097962         | 45.94%            |
| Total        | 5001572       | 100.00%         | 435234               | 100.00%                | 4566338         | 100.00%           |

The aspect ratios of images are overall diffuse.
When desiring at least a million images and a consistent aspect ratio only the 1:1.41 aspect ratio is suitable.
The 1:1 aspect ratio while popular for neural networks is not widely used in the Danbooru dataset.
