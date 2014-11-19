from SimpleCV import Camera, Color, RunningSegmentation, Display

cam = Camera()
firstImg = cam.getImage()
rs = RunningSegmentation(alpha=0.5)
rs.addImage(firstImg)
disp = Display(firstImg.size())

while disp.isNotDone():
    img = cam.getImage()
    rs.addImage(img)
    diffImg = rs.getSegmentedImage(False)
    if diffImg:
        blobs = diffImg.dilate(3).findBlobs()
        if blobs:
            img.dl().polygon(blobs[-1].mConvexHull, color=Color.RED)
    img.show()