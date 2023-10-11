import math
import glob
from ultralytics import YOLO
import cv2
import cvzone

model_clss = YOLO('./best-cls.pt')
model_coco = YOLO("./yolov8n.pt")

def get_files(path):
    files = []
    try:
        # # Using '*' pattern
        # print('\nNamed with wildcard *:')
        # for files in glob.glob(path + '*'):
        #     print(files)
        #
        # # Using '?' pattern
        # print('\nNamed with wildcard ?:')
        # for files in glob.glob(path + '?.txt'):
        #     print(files)

        # Using [0-9] pattern
        #print('\nNamed with wildcard ranges:')
        files = glob.glob(path + '/*[0-9].*')
        return files
    except ValueError as e:
        print(str(e))
        pass
        return files

def get_classify(img):
    name, conf_cls = "Unknow","0"
    try:
        # Predict with the model
        results = model_clss(img)  # predict on an image

        names_dict = results[0].names
        #print(names_dict)
        # print(results[0].probs)
        # data = results[0].probs.data.tolist()
        name = names_dict[results[0].probs.top1]
        conf_cls = results[0].probs.top1conf.tolist()
        return name, conf_cls
    except ValueError as e:
        print(str(e))
        pass
        return  name, conf_cls

window = "Test"

files = get_files('kdc_benloi')

for f in files:
    img = cv2.imread(f)
    get_classify(img=img)

    result_cocos = model_coco(img, show=False, classes=[2, 5, 7])  # show=True

    for r in result_cocos:
        boxes2 = r.boxes
        # print(len(boxes))
        for box2 in boxes2:
            x12, y12, x22, y22 = box2.xyxy[0]
            x12, y12, x22, y22 = int(x12), int(y12), int(x22), int(y22)
            w2, h2 = x22 - x12, y22 - y12
            conf2 = math.ceil((box2.conf[0] * 100)) / 100
            class_id2 = int(box2.cls[0])
            currentClass2 = model_coco.model.names[class_id2]
            cx2, cy2 = x12 + w2 // 2, y12 + h2 // 2

            car_crop = img[y12:y22, x12:x22]
            if car_crop is not None:
                name, conf_cls = get_classify(img=car_crop)
                if conf_cls >= 0.2:
                    cvzone.cornerRect(img, (x12, y12, w2, h2), l=9)
                    cvzone.putTextRect(img, f'{name}_{round(conf_cls, 2)}', (max(0, x12), max(35, y12)),
                                       scale=2, thickness=3, offset=3)
                elif conf_cls < 0.2:
                    cvzone.cornerRect(img, (x12, y12, w2, h2), l=9)
                    cvzone.putTextRect(img, f'Unknow', (max(0, x12), max(35, y12)),
                                       scale=2, thickness=3, offset=3)
        frame_ = cv2.resize(img, (1280, 720))
        cv2.imshow(window, frame_)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break