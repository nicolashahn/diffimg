# python-image-diff
Get the % difference in images using PIL's histogram + generate a diff image. Images should be the same size.

### Usage
`./diff_images.py image1 image2 [-r/--ratio] [-d/--delete] [-f/--filename DIFF_IMG_FILE]`

## Sample image 1
![Alt text](/mario-circle-cs.png "Image 1")

## Sample image 2
![Alt text](/mario-circle-node.png "Image 2")

## Resulting diff image
![Alt text](/diff_img.jpg "Difference Image")

## Difference percentage output
`Images differ by 1.86650262467%`
