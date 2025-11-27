# [Kernels and Convolutions](https://github.com/tcutler96/Kernels-and-Convolutions)
This project shows how to process images using kernels and convolutions. In image processing, a kernel or convolution matrix is a small grid of numbers that changes a pixel based on its nearby pixels. The output pixel becomes a simple function of its neighbours. By sliding the kernel over the image, applying convolutions along the way, it is possible to blur, sharpen, detect edges, and more.

The code in this project applies several common kernels and shows how each one changes the image. It includes functions for filtering, edge detection, colour mapping, and full canny edge detection. It also includes helper functions to plot results with Matplotlib. Additionally, these processes are carried out from first principles using only Python and NumPy and does not rely on any image processing libraries so you can see how each step works.

## Basic Manipulations
![train_basic](<static/projects/Kernels and Convolutions/train_basic.png>)

## Coloured Edges
![night_sky_coloured](<static/projects/Kernels and Convolutions/night_sky_coloured.png>)

## Canny Process
![flower_canny](<static/projects/Kernels and Convolutions/flower_canny.png>)
