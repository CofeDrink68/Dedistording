import cv2
import numpy as np
import Dedistording as dediLib
from video import create_capture

mtx = np.array([[667.17063916, 0, 306.17038799],[0, 666.49926003, 202.22813635],[0, 0, 1]])
dist = (0.174438364, -0.975875979, -0.000947201236, -0.00531611798, 1.23491951)

dedist = dediLib.Dedistortion(mtx, dist, 480, 640)

cam = create_capture(0)

while True:
    ret, img = cam.read()
    w, h, c = img.shape
    imgCorrected = dedist.correction(img)
    w2, h2, c2 = img.shape
    cv2.imshow("Normal", img)
    cv2.imshow("Corrected", imgCorrected)
    print(str(w)+str(" ")+str(h)+str(" -> ")+str(w2)+str(" ")+str(h2))
    if cv2.waitKey(5) == 27:
        break
cv2.destroyAllWindows()
