from SimpleCV import *
from pymouse import PyMouse

cam = Camera()
disp = Display()
m = PyMouse()
frames = 0
CLICK_ON = True
NORM_DISPLAY = True

def toggleClickability(f):
    global CLICK_ON
    if not (f % 30 or CLICK_ON):
        CLICK_ON = True

while disp.isNotDone():
    if disp.mouseRight:
            NORM_DISPLAY = not(NORM_DISPLAY)
            print "Display Mode:", "Normal" if NORM_DISPLAY else "Segmented"
    frames += 1
    img = cam.getImage().scale(0.5).flipHorizontal()
    orange_distance = img.colorDistance(Color.LEGO_ORANGE).dilate(2).invert()
    segmented = orange_distance.stretch(125,255)
    blobs = segmented.findBlobs()
    if blobs:
        # blobs.draw()
        x, y = blobs.x(), blobs.y()
        if len(blobs)>1 and CLICK_ON:
            print "Click"
            m.click(x[-1], y[-1])
            CLICK_ON = False
        print x, y
        m.move(x[0]*6-400, y[0]*6-380)
    toggleClickability(frames)
    if NORM_DISPLAY:
        img.show()
    else:
        segmented.show()
