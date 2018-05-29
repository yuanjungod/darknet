import os
import cv2
from PIL import Image

back_ground_list = ["/home/yuanjun/train_data/background/%s" % back for
               back in os.listdir("/home/yuanjun/train_data/background")]

back_list_len = len(back_ground_list)

def train():
    image_list = [["/home/yuanjun/train_data/segment_data/images/train/%s" % i, "/home/yuanjun/train_data/segment_data/train/%s" % i]
                for i in os.listdir("/home/yuanjun/train_data/segment_data/train")]
    for i in range(len(image_list)):
        print(i)
        print(image_list[i])
        image = Image.open(image_list[i][1])
        back = Image.open(back_ground_list[i%back_list_len])
        back = back.resize((640, 480))
        back.paste(image,(0, 0))
        back.save(image_list[i][0])


def train_val():
    image_list = [["/home/yuanjun/train_data/segment_data/images/train_val/%s" % i, "/home/yuanjun/train_data/segment_data/train_val/%s" % i]
                for i in os.listdir("/home/yuanjun/train_data/segment_data/train_val")]
    for i in range(len(image_list)):
        print(i)
        print(image_list[i])
        image = Image.open(image_list[i][1])
        back = Image.open(back_ground_list[i%back_list_len])
        back = back.resize((640, 480))
        back.paste(image,(0, 0))
        back.save(image_list[i][0])

train()
train_val()