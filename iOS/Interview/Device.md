# 실제 디바이스가 없을 경우 개발 환경에서 할 수 있는 것과 없는 것을 설명하시오.

## 할 수 있는 것

할 수 없는 것을 제외한 대부분의 동작

## 할 수 없는 것

- 카메라 활용
- gps
- 자이로 센서

---

## 할 수 있는 것

- 페이스 iD → 시뮬레이터의 메뉴상에서 인식됨/안됨 처리 가능
- potraint
- landscape

## 할 수 없는 것

- 블루투스
- 책상에 엎거나 올려놓은 상태 → faceup, facedown
- 모션 인식(가속계, 자이로스코프)
- 오디오 및 비디오 입력(카메라, 마이크)
- 근접 센서
- 기압계
- 주변 조도 센서

### API

- Apple 푸시 알림 수신 및 전송
- 사진, 연락처, 일정관리 및 주의사항에 대한 개인 정보 경고
- UIBackgroundModes Key
- 핸드오프 지원

### Framework

- 외부 액세서리
- IOSurface
- Media Player
- Message UI
- UIVideoEditorController 클래스
- Metal, MetalKit 및 Metal Performance Shaders 프레임워크

### 참고 자료

[Testing and Debugging in Simulator](https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/iOS_Simulator_Guide/TestingontheiOSSimulator/TestingontheiOSSimulator.html)