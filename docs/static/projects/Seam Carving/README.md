# [Seam Carving](https://github.com/tcutler96/Seam-Carving)
This project shows how to shrink an image while keeping important parts intact by implementing a method called seam carving. It works by finding a path of pixels with the lowest visual importance then removing that path. Repeating this many times reduces the width of the image without distorting it or losing important details.

## Method
The code uses Sobel filters to detect edges. It converts the image to grey scale then computes the gradient in the x and y directions. The gradient magnitude becomes the energy map. High energy means strong edges and low energy means weak edges. A table of minimum energy is built from bottom to top. For each pixel the code looks at the three pixels below it and chooses the best option. This gives a full map of the cheapest path from any point at the top to the bottom. Once the minimum energy table is built, the code walks from the top row to the bottom row following the lowest cost directions. This seam is then removed from both the image and the energy map, reducing the width by one pixel. This process is repeated as many times as needed.

## Minimum Energy Path Visualiser
![Street](<static/projects/Seam Carving/street_min_energy.gif>)

## Example Shrinking
![Clocks](<static/projects/Seam Carving/clocks_seam_carving.png>)
