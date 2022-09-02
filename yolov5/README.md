# README
- 이 디렉토리에 있는 파일을 yolov5 디렉토리에 넣는다.
- 이 문서는 현재 디렉토리가 `~/yolov5`라고 가정한다.

## docker-run.sh
- 호스트에서 도커 컨테이너 생성한다.
- 실행방법: `sudo sh ./docker-run.sh`

## Makefile
- 도커 컨테이너 내에서 명령을 쉽게 실행하기 위해 만들었다.
### How to use
- 훈련: `make start`