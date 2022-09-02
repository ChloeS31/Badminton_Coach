# 눈치코치
aiffel 대전 2기 해커톤 3차 기업프로젝트

## 개요

### 아이템 소개
- 배드민턴 자세 교정 AI

### 개발 목적
많은 플랫폼에서 스스로 영상을 보며 따라할 수 있는 운동강의를 제공한다. 하지만 특히 구기종목에서는 자세가 중요하고, 이는 영상을 따라하기만 해서는 초보자가 정확한 자세를 배우기가 쉽지 않다.

이 플랫폼의 목적은 배드민턴을 처음 배우는 초보자들이나 아마추어 선수들이 스스로 자세를 확인하고, 플랫폼에서 제공하는 정확한 자세와 비교하여 자세 교정을 하는 것에 있다.

이에 따라 초보자나 아마추어 선수들은 코치를 만나지 않고도 개인이 원할 때 연습할 수 있으므로, 코치를 직접 만나서 배우는 만큼의 효율을 얻으면서, 이에 필요한 시간과 돈을 절감할 수 있다.

### 개발아이템의 독창성
1. 라켓까지 인식할 수 있다. 현재까지 공개된 데이터 중 라켓까지 인식할 수 있는 모델은 없다.

---

## 개발 및 연구 내용
### 개발 내용 상세
이 프로젝트는 배드민턴 치는 사람의 동작 이미지를 인식하여 전문가의 올바른 자세와 비교, 이용자의 자세를 교정해주는것을 목표로 한다.

학습 모델은 현재 발표된 Deep Pose, Open Pose 등의 다양한 human pose estimation 기술 중 회사에서 제공하는 데이터와 목표에 맞는 학습 모델을 선정한다.

데이터는 에이리스에서 제공하며, augmentation 등의 전처리를 진행한다. 특히 에이리스의 데이터는 다른 public data 와 달리 라켓 class 가 추가되어 있고, 라켓은 사람의 관절과는 다른 양상의 분포일것이므로, 이 class로 인한 추가적인 전처리에 대한 연구가 필요할 것으로 보인다.

**Augmentation**: **[imgaug](https://github.com/aleju/imgaug)를 이용하여 아래 항목을 수행**
- Gauss. Noise + Contrast + Sharpen
- Affine
- Crop + Pad
- Fliplr + Perspective

**Label:** 에이리스의 데이터는 다른 공개데이터와 달리 라켓이 추가 되어 있다. 이 라벨은 아래 이미지에 보이는 사람 관절 keypoint 에 추가해주어, 모델이 추가적인 관절로 인식하도록 한다.

### 개발 단계별 목표
1. Pose Estimtimation을 사용한 사람의 자세 및 라켓의 위치 학습기능
   1. 논문 및 레퍼런스를 참조하여 사용할 모델(deeppose 등)을 고르고 관련 베이스라인 찾기
   2. coco나 aihub에서 일반 베드민턴 유저데이터를 구해 같이 학습시키고(잘 안될경우 Test셋으로 활용) 그것을 데이터양에 따라 가중치 차이두기
   3. 에이리스에서 제공하는 학습용 데이터 파일 원하는 형태로 받아서 학습에 사용하도록 코드 준비(pandas나 tensor등)
   4. imgaug를 이용하여 데이터 증강(augmentation) 코드작성
   5. 베이스라인을 이용하여 정상적으로 학습이 진행되는지 확인
   6. 베이스라인을 기본으로 딥러닝모델 형성 및 학습하여 정확도 비교
   7. 에이리스에서 제공받은 학습데이터가 정답이므로 일반인 데이터를 보고 틀린 자세인 것을 구분하도록 결과값 구현

2. 결과 시각화
3. (차후구현)Regression을 사용한 전문가의 자세와 비교, 그 차이를 분석기능
   1. 에이리스에서 제공받은 데이터가 기술(드라이브,오버해드 등)별로 나눠져 있으므로 기술별로 인식가능한지 확인
   2. 일반인의 포즈가 얼마나 적합한지 퍼센트로 구현
4. (차후구현)프레임간 라켓의 움직임을 기준으로 스윙스피드 계산기능

---

## 레퍼런스
- [2D Human Pose Estimation](https://paperswithcode.com/task/2d-human-pose-estimation)
- [Human Pose Estimation Technology 2021 Guide](https://mobidev.biz/blog/human-pose-estimation-ai-personal-fitness-coach)
- [Introduction to Human Pose Estimation](http://dmqm.korea.ac.kr/activity/seminar/311)
- [MVIG-SJTU/AlphaPose](https://github.com/MVIG-SJTU/AlphaPose)
- [미디어파이프 BlazePose를 사용한 실시간신체추적](https://brunch.co.kr/@synabreu/95)
- [Multi-Instance Pose Networks: Rethinking Top-Down Pose Estimation](https://arxiv.org/pdf/2101.11223v3.pdf)
- [잘못된 운동 자세, AI 코치가 바르게 잡아드립니다](http://www.aitimes.com/news/articleView.html?idxno=141841)
