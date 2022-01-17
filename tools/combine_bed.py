import cv2
import pickle

if __name__ == "__main__":
    # Read the image
    img1 = cv2.imread('/home/ruichen/AdelaiDet/test_images/test1.jpg')
    img2 = cv2.imread('/home/ruichen/AdelaiDet/test_images/bed1.png')
    with open('/home/ruichen/AdelaiDet/test_images_seg_res/img_prediction_mask.pkl', 'rb') as handle:
        mask = pickle.load(handle)[0].tolist()

    for i in range(0, len(mask)):
        for j in range(0, len(mask[0])):
            if mask[i][j] == True:
                img1[i][j] = img2[i][j]


    #img_bg = cv2.bitwise_and(img, img, mask = mask)
    cv2.imwrite('/home/ruichen/AdelaiDet/seg_images/combine1.jpg', img1)