import cv2
import glob



images = glob.glob(r"*jpg")

for i in images:
    img=cv2.imread(i,0)
    res_img=cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
    cv2.imshow("hez", res_img)
    cv2.waitKey(200)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+i, res_img)
