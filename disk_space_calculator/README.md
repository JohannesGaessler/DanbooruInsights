# Disk Space Calculator

Projected disk usage based on color type and rating:

| Rating       | All Images, Count | All Images, Disk Usage | Monochrome, Count | Monochrome, Disk Usage | Color, Count | Color, Disk Usage |
|--------------|-------------------|------------------------|-------------------|------------------------|--------------|-------------------|
| Safe         | 3868648           | 3.73 TiB               | 365513            | 193.2 GiB              | 3503135      | 3.55 TiB          |
| Questionable | 682575            | 704.5 GiB              | 36119             | 17.2 GiB               | 646456       | 687.3 GiB         |
| Explicit     | 450349            | 512.0 GiB              | 33602             | 22.0 GiB               | 416747       | 490.0 GiB         |
| Total        | 5001572           | 4.92 TiB               | 435234            | 232.34 GiB             | 4566338      | 4.70 TiB          |

Monochrome is defined as files with the monochrome tag.
Color is defined as files without the monochrome tag.
Note that the projected disk usage is given in GiB / TiB (what your computer tells you) and not as GB / TB (what is being sold to you).
Restricting file extensions to just "jpg", "jpeg", and "png" does not significantly reduce disk usage
with less than a 3% reduction in disk usage on average for the whole dataset.

However, additionally resizing images to 2048 / 1024 / 512 pixels significantly reduces disk usage:
| Rating               | All Images, 2048 px    | All Images, 1024 px    | All Images, 512 px     |
|----------------------|------------------------|------------------------|------------------------|
| Safe                 | 2.41 TiB               | 1.22 TiB               | 369.9 GiB              |
| Questionable         | 420.3 GiB              | 208.4 GiB              | 59.7 GiB               |
| Explicit             | 302.0 GiB              | 151.2 GiB              | 42.3 GiB               |
| Total                | 3.12 TiB               | 1.57 TiB               | 471.9 GiB              |
| Disk Usage Reduction | 36.6%                  | 68.1%                  | 90.6%                  |
