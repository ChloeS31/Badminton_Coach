# README for airiss

## 준비
- `pretrained_models/simple_res50_256x192.pth`
- `cd AlphaPose`
- `mkdir -p data/airiss/annotations`
- `ln -s /share/airiss/split_data/val data/airiss/val`
- `ln -s /share/airiss/split_data/train data/airiss/train`
- `ln -s /share/airiss/split_data/train.json data/airiss/annotations/train.json`
- `ln -s /share/airiss/split_data/val.json data/airiss/annotations/val.json`

## update AlphaPose for airiss
AlphaPose 공식 저장소에서 clone한 디렉토리에 airiss 데이터를 훈련시킬 수 있도록 수정한 파일을 사용하기 위해 다음과 같이 한다.
1. `cd ~`
2. `wget https://github.com/m2b3k3/tennis/archive/refs/heads/main.zip`
3. `unzip tennis-main.zip`
4. `cp -r -f tennis-main/AlphaPose/* ~/AlphaPose`

## 실행
- `sh scripts/train.sh configs/airiss/resnet/simple.yaml airiss`