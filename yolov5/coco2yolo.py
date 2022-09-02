import os
import json


path= os.getcwd()
# file_list= ['train.json', 'val.json']

file_list= ['data.json']

for the_name in file_list:
    file_dir= os.path.join(path, the_name)
   
    dir_name= os.path.split(file_dir)[-1].split('.')[0]
    # os.mkdir(dir_name)

    # load json data
    with open(file_dir, "r") as json_file:
        json_data = json.load(json_file)


    img_w, img_h = [1080, 1920]


    for i in range(1): #(len(json_data['images']):
        width= json_data['images'][i]['width']
        height= json_data['images'][i]['height']
        img_id= json_data['images'][i]['id']
        path= json_data['images'][i]['path']

        file_name= json_data['images'][i]['file_name']
        bbox = json_data['annotations'][0]['bbox']

        x_center = bbox[1]+bbox[3]/2
        y_center = bbox[0]+bbox[2]/2
        c_x= x_center/width
        c_y= y_center/height

        w= bbox[3]/width
        h= bbox[2]/height

        txt_dir= os.path.join(dir_name, file_name.split('.')[0]+'.txt')
        # f=open(txt_dir, 'w')
        content='{} {} {} {} {}'.format(1, c_x, c_y, w, h)
        # f.write(content)
        
        
        with open(txt_dir, 'w') as f:
            f.write(content)
            f.close()
