import cv2
import pickle

if __name__ == "__main__":
    # Read the image
    img = cv2.imread('/home/ruichen/AdelaiDet/test_images/content000.jpg')
    with open('/home/ruichen/AdelaiDet/test_images_seg_res/img_prediction_mask.pkl') as handle:
        mask = pickle.load(handle)[0]
    img_bg = cv2.bitwise_and(img, img, mask = mask)
    cv2.imwrite('test.jpg', img_bg)