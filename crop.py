import os
import json
from PIL import Image
train1_json_path = './train1/Annotations/anno_train.json'
the_image_root_path = './train1/defect_Images/'
def crop_img():
    with open(train1_json_path,'rb') as f:
        params = json.load(f)
        list_dict = []
        for i, img_crop in enumerate(params):
            #print('image_crop:',img_crop)
            #获取图片的名字
            image_name = img_crop['name']

            #获取图片不带后缀 的名字#########
            #the_root_file_name = os.path.splitext(os.path.basename(image_name))[0]
            ###########################

            #print(the_root_file_name)
            #读取图片####################
            the_start_image_path = './train1/defect_Images/' + image_name
            img_open = Image.open(the_start_image_path)
            h = img_open.height
            w = img_open.width
            #print("h:",h)
            #print('w',w)
            ###########################

            #裁剪图片保存路径##############
            #image_path_crop = './train_crop/' + the_root_file_name + '_' + str(i) + '.jpg'
            image_path_crop = './train1_crop/' + str(i) + '.jpg'
            ###########################
        
            #判断x_min的位置，是在500之前还是之后
            x_min,y_min,x_max,y_max = img_crop['bbox'][0],img_crop['bbox'][1],img_crop['bbox'][2],img_crop['bbox'][3]
            #print('x_min:',x_min)

            if x_max <= w/2:
                cbox =  [0,0,w/2,h]
                image_cropped = img_open.crop(cbox)
                image_cropped.save(image_path_crop)
                bbox_crop = img_crop['bbox']
                #print(cbox)
            elif x_min >= w/2:
                cbox = [w/2,0,w,h]
                image_cropped = img_open.crop(cbox)
                image_cropped.save(image_path_crop)
                bbox_crop = [round(img_crop['bbox'][0]-w/2,2),img_crop['bbox'][1],round(img_crop['bbox'][2]-w/2,2),img_crop['bbox'][3]]
                #print(cbox)
            else:
                cbox = [610,0,1836,1000]
                image_cropped = img_open.crop(cbox)
                image_cropped.save(image_path_crop)
                #bbox_crop = img_crop['bbox']
                bbox_crop = [round(img_crop['bbox'][0]-609,2),img_crop['bbox'][1],round(img_crop['bbox'][2]-609,2),img_crop['bbox'][3]]
                #print(cbox)
            dict_to_json = {}
            dict_to_json['name'] = str(i) + '.jpg'
            dict_to_json['defect_name'] = img_crop['defect_name']
            dict_to_json['bbox'] = bbox_crop
            list_dict.append(dict_to_json)
    f.close()
    return list_dict
def write_to_json(list_dict):
    with open('/media/lxg/D/keyan/tianchi/guangdong1/data_augment/data_crop/train1_crop.json','w') as r:
        json.dump(list_dict,r)
    r.close()
a = crop_img()
write_to_json(a)
        








