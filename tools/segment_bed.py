import cv2
import pickle

if __name__ == "__main__":
    # Read the image
    img = cv2.imread('/home/ruichen/AdelaiDet/test_images/test1.jpg')
    with open('/home/ruichen/AdelaiDet/test_images_seg_res/img_prediction_mask.pkl', 'rb') as handle:
        mask = pickle.load(handle)[0].tolist()

    for i in range(0, len(mask)):
        for j in range(0, len(mask[0])):
            if mask[i][j] == False:
                img[i][j] = [255, 255, 255]


    #img_bg = cv2.bitwise_and(img, img, mask = mask)
    cv2.imwrite('/home/ruichen/AdelaiDet/seg_images/test.jpg', img)