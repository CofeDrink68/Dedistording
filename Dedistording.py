import cv2
import numpy as np

class Dedistortion:
    def __init__(self, mtx, dist, w, h):
        self.mtx = mtx
        self.dist = dist
        self.w = w
        self.h = h
        self.newcameramtx, self.roi = cv2.getOptimalNewCameraMatrix(self.mtx,self.dist,(self.w,self.h),1,(self.w,self.h))

    def correction(self, img):
        self.res = cv2.undistort(img, self.mtx, self.dist, None, self.newcameramtx)
        # self.x2,self.y2,self.w2,self.h2 = self.roi
        # self.res = self.res[self.y2:self.y2+self.h2, self.x2:self.x2+self.w2]
        return self.res
