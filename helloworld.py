from SimpleCV import *
eyes_cascade = HaarCascade('/home/malithsen/downloads/eye_tree.xml')
face_cascade = HaarCascade('face.xml')
COLOUR = Color.RED
def main():
    cam  = Camera()
    disp = Display()
    while disp.isNotDone():
        img = cam.getImage()
        img = img.scale(0.5).flipHorizontal()
        faces = img.findHaarFeatures(face_cascade)
        img.dl().circle((150, 75), 25, COLOUR, filled = True)
        # print img.listHaarFeatures()
        if faces:
            faces = faces.sortArea()
            # print faces
            face = faces[-1]
            face.draw()
            # myface = face.crop()
            # kp = img.findKeypoints()
            # if kp:
            #     kp.draw()
            eyes = img.findHaarFeatures(eyes_cascade)
            if eyes:
                eyes.draw()
                # myface.show()
            # for face in faces:
            #     face.draw()
        img.show()

if __name__ == "__main__":
    main()
