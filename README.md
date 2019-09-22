# target-detection-crop
crop your dataset and drow the frame
本次数据集为布匹检测数据集，原图大小为2446，1000，对其进行裁剪，裁剪成两半
train1为存放json与图片的文件夹
train1:
      ___Annotations
      ___defect_Images
      ___normal_Images
      ___READEME.md
train1_crop:
           ___0asdfaseff.jpg
           .....
train1_crop是用来存放裁剪后图片的
train1_crop.json是用来保存图片名称，类别，bbox的文件
只需修改code里面的路径信息便可运行，如果是其他数据集需要修改下610根跟1836这两个数值，具体情况具体分析。
