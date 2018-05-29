import os

label_dict = {
    "ID_test_005": 0,
    "ID_test_006": 1,
    "ID_test_007": 2,
    "ID_test_008": 3,
    "ID_test_009": 4,
    "ID_test_011": 5,
    "ID_test_012": 6,
    "ID_test_014": 7,
    "ID_test_016": 8,
    "ID_test_017": 9,
    "ID_test_018": 10,
    "ID_test_019": 11,
    "ID_test_020": 12,
    "ID_test_021": 13
}

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[2])/2.0
    y = (box[1] + box[3])/2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def train():
    train_file = open('train.txt', 'w')

    for i in os.listdir("/home/yuanjun/train_data/segment_data/images/train"):
        if i.find("txt") != -1:
            continue
        train_file.write("/home/malin/code/darknet/segment_data/segment_data/images/train/%s\n" % i)
        list_file = open('/home/yuanjun/train_data/segment_data/labels/train/%s.txt'% i.split(".")[0], 'w')
        print("segment_data/label/%s.txt" % i.split(".")[0])
        origin_file = open("/home/yuanjun/train_data/segment_data/label/%s.txt" % i.split(".")[0], "r")
        lines = origin_file.readlines()
        for line in lines:
            # print "##########################################################################"
            a = line.split(" ")
            box = convert([640.0, 480.0], [float(a[4]), float(a[5]), float(a[6]), float(a[7])])
            # label = int(a[0].split("_")[-1])
            print(label_dict[a[0]])
            list_file.write("%s %s %s %s %s\n" % (label_dict[a[0]], box[0], box[1], box[2], box[3]))
            # if label < 4:
            #     list_file.write("%s %s %s %s %s\n" % (label-1, box[0], box[1], box[2], box[3]))
            #     # print line
            #     # print label
            #     print(label-1, box[0], box[1], box[2], box[3])
            # elif label < 10:
            #     list_file.write("%s %s %s %s %s\n" % (label-2, box[0], box[1], box[2], box[3]))
            #     # print line
            #     # print label
            #     print(label-2, box[0], box[1], box[2], box[3])
            # else:
            #     list_file.write("%s %s %s %s %s\n" % (label-3, box[0], box[1], box[2], box[3]))
            #     # print line
            #     # print label
            #     print(label-3, box[0], box[1], box[2], box[3])
        list_file.close()
        origin_file.close()
    train_file.close()

def train_val():
    train_file = open('train_val.txt', 'w')

    for i in os.listdir("/home/yuanjun/train_data/segment_data/images/train_val"):
        if i.find("txt") != -1:
            continue
        train_file.write("/home/malin/code/darknet/segment_data/segment_data/images/train_val/%s\n" % i)
        list_file = open('/home/yuanjun/train_data/segment_data/labels/train_val/%s.txt'% i.split(".")[0], 'w')
        print("segment_data/label/%s.txt" % i.split(".")[0])
        origin_file = open("/home/yuanjun/train_data/segment_data/label_val/%s.txt" % i.split(".")[0], "r")
        lines = origin_file.readlines()
        for line in lines:
            # print "##########################################################################"
            a = line.split(" ")
            box = convert([640.0, 480.0], [float(a[4]), float(a[5]), float(a[6]), float(a[7])])
            # label = int(a[0].split("_")[-1])
            print(label_dict[a[0]])
            list_file.write("%s %s %s %s %s\n" % (label_dict[a[0]], box[0], box[1], box[2], box[3]))
            # if label < 4:
            #     list_file.write("%s %s %s %s %s\n" % (label-1, box[0], box[1], box[2], box[3]))
            #     # print line
            #     # print label
            #     print(label-1, box[0], box[1], box[2], box[3])
            # elif label < 10:
            #     list_file.write("%s %s %s %s %s\n" % (label-2, box[0], box[1], box[2], box[3]))
            #     # print line
            #     # print label
            #     print(label-2, box[0], box[1], box[2], box[3])
            # else:
            #     list_file.write("%s %s %s %s %s\n" % (label-3, box[0], box[1], box[2], box[3]))
            #     # print line
            #     # print label
            #     print(label-3, box[0], box[1], box[2], box[3])
        list_file.close()
        origin_file.close()
    train_file.close()

train()
train_val()