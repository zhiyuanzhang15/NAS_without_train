import os

data_dir = r'C:\AI_project\data\ImageNet'

def read_csv_labels(fname):
    """读取 fname 来给标签字典返回一个文件名"""
    with open(fname, 'r') as f:
        lines = f.readlines()
    tokens = [l.rstrip().split(' ')[0] for l in lines]
    return tokens

labels_image_file = read_csv_labels(os.path.join(data_dir,'val.txt'))

def get_image(number_of_image, image_dir):
    image = []
    for i in range(number_of_image):
        dir = os.path.join(image_dir,labels_image_file[i])
        image.append(dir)
    
    return image

image_dir = r'C:\AI_project\data\torch_imagenet\validation'

