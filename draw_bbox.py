import os
import json
from PIL import Image
import cv2

train1_json_path = '/media/lxg/D/keyan/tianchi/guangdong1/data_augment/data_crop/train1_crop.json'
the_image_root_path = '/media/lxg/D/keyan/tianchi/guangdong1/data_augment/data_crop/train1_crop/'
the_new_image_draw_path = '/media/lxg/D/keyan/tianchi/guangdong1/data_augment/data_crop/draw_bbox/image/'
defect_name2label = {
    '破洞': 1, '水渍': 2, '油渍': 2, '污渍': 2, '三丝': 3, '结头': 4, '花板跳': 5, '百脚': 6, '毛粒': 7,
    '粗经': 8, '松经': 9, '断经': 10, '吊经': 11, '粗维': 12, '纬缩': 13, '浆斑': 14, '整经结': 15, '星跳': 16, '跳花': 16,
    '断氨纶': 17, '稀密档': 18, '浪纹档': 18, '色差档': 18, '磨痕': 19, '轧痕': 19, '修痕': 19, '烧毛痕': 19, '死皱': 20, '云织': 20,
    '双纬': 20, '双经': 20, '跳纱': 20, '筘路': 20, '纬纱不良': 20,
}
with open(train1_json_path,'rb') as f:
    params = json.load(f)
    for i, img_crop in enumerate(params):

        x_min,y_min,x_max,y_max = img_crop['bbox'][0],img_crop['bbox'][1],img_crop['bbox'][2],img_crop['bbox'][3]

        fname = the_image_root_path + img_crop['name']
        img = cv2.imread(fname)
        # 画矩形框
        cv2.rectangle(img, (int(x_min),int(y_min)), (int(x_max),int(y_max)), (0,255,0), 4)
        # 标注文本
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(defect_name2label[img_crop['defect_name']])
        
        cv2.putText(img, text, (int(x_min), int(y_min-10)), font, 2, (0,0,255), 1)
        cv2.imwrite(the_new_image_draw_path + img_crop['name'], img)

            
            
            



        








