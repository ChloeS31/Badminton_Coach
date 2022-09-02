docker run -it --gpus all --ipc=host --name yolov5 -p 8888:8888 \
  -v /share/airiss/split_data/:/airiss \
  -v ~/AlphaPose/detector/yolo:/data/detector \
  -v ~/yolov5/result:/usr/src/app/result \
  yolo:v5 bash
