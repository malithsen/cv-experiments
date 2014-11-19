from SimpleCV import Camera, Display, Color

ON_CIRCLE = False
def parm_on_obj(a, b, r, obj):
    global ON_CIRCLE

    x = [a - r, a + r]
    y = [b - r, b + r]
    if (x[0] < obj.x < x[1]) and (y[0] < obj.y < y[1]):
        ON_CIRCLE = True
        return Color.YELLOW
    else:
        ON_CIRCLE = False
        return Color.RED


def main():
    global ON_CIRCLE

    colour = Color.RED
    cam  = Camera()
    disp = Display()
    obj_x = 150
    obj_y = 75
    radius = 25
    normaldisplay = True
    while disp.isNotDone():
        if disp.mouseRight:
            normaldisplay = not(normaldisplay)
            print "Display Mode:", "Normal" if normaldisplay else "Segmented"

        img = cam.getImage()
        img = img.scale(0.5).flipHorizontal()
        dist = img.colorDistance(Color.BLACK).dilate(2)
        img.dl().circle((obj_x, obj_y), radius, colour, filled = True)
        segmented = dist.stretch(200,255)
        palm = img.findHaarFeatures('/home/malithsen/downloads/palm.xml')
        fist = img.findHaarFeatures('/home/malithsen/downloads/agest.xml')
        if palm:
            # palm = palm.sortArea()
            palm = palm[-1]
            colour = parm_on_obj(obj_x, obj_y, radius, palm)
            palm.draw()
        elif fist:
            # fist = fist.sortArea()
            fist = fist[-1]
            fist.draw()
            if ON_CIRCLE:
                colour = Color.GREEN
                obj_x, obj_y = fist.x, fist.y
        if normaldisplay:
            img.show()
        else:
            segmented.show()

if __name__ == "__main__":
    main()