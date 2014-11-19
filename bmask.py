from SimpleCV import *
def main():
    cam  = Camera()
    disp = Display()
    # cam.live()
    while disp.isNotDone():
        img = cam.getImage()
        img = img.scale(0.5)
        # mask = img.createBinaryMask(color1=(130,125,100),color2=Color.BLACK)
        # mask = mask.morphClose()
        # result = img - mask.invert()
        # result.show()
        # binary = img.binarize()
        # blobs = binary.findBlobs()
        # blobs.show()
        keys = img.findKeypoints()
        if keys:
            keys.draw()
        img.show()

if __name__ == "__main__":
    main()
