# 💊 건강기능식품 도우미 프로그램

> **🏆 글로벌융합학과 & 글로벌리더학과 융합 학술제 대상 수상작**

전자상거래 건강기능식품 광고 규제 대응을 위한 AI 솔루션입니다.

## 🏆 수상 경력

- **글로벌융합학과 & 글로벌리더학과 융합 학술제 대상**
- 전자상거래 건강기능식품 광고 규제 대응 AI 솔루션 부문
- 2024년 학술제 최우수 작품 선정

## 🚀 주요 기능

### 1. 🧾 OCR 기반 정확한 기능 안내
- 건강기능식품 이미지에서 성분 정보를 자동 추출
- 추출된 성분의 정확한 기능성 내용 제공
- OCR 기술을 활용한 자동화된 성분 분석

### 2. 🏷️ 마케팅 문구 생성
- 선택한 성분에 대한 적법한 마케팅 문구 자동 생성
- 규제 기준에 맞는 안전한 광고 문구 추천
- AI를 활용한 맞춤형 마케팅 문구 제안

### 3. 🚨 허위·과장 문구 판별
- 입력된 광고 문구의 적법성 검사
- 과장·허위 표현 자동 감지
- 규제 위반 위험 문구 경고 시스템

## 🛠️ 기술 스택

- **Frontend**: Streamlit
- **AI/ML**: Mistral AI API
- **OCR**: Naver Cloud Platform OCR API
- **Data Processing**: Pandas
- **Language**: Python 3.8+

## 📁 프로젝트 구조

```
글리_글융_학술제_3조_코드/
├── home.py                 # 메인 애플리케이션
├── functions/              # 핵심 기능 모듈
│   ├── ocr.py             # OCR 기반 성분 추출
│   ├── generator.py       # 마케팅 문구 생성
│   └── checker.py         # 허위·과장 문구 판별
├── utils/                  # 유틸리티 모듈
│   ├── openai_utils.py    # AI API 연동
│   └── prompt_utils.py    # 프롬프트 템플릿
├── data/                   # 데이터 파일
│   ├── 기능23_data.csv    # 기능성 원료 데이터
│   └── ingredient_db.csv  # 성분 데이터베이스
├── requirements.txt        # 의존성 패키지
├── .env.example           # 환경변수 예시
└── README.md              # 프로젝트 문서
```

## 🚀 설치 및 실행

### 1. 저장소 클론
```bash
git clone [repository-url]
cd 글리_글융_학술제_3조_코드
```

### 2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 환경변수 설정
```bash
cp .env.example .env
```

`.env` 파일을 열어 다음 API 키들을 설정하세요:
```
MISTRAL_API_KEY=your_mistral_api_key_here
OCR_SECRET_KEY=your_ocr_secret_key_here
```

### 5. 애플리케이션 실행
```bash
streamlit run home.py
```

## 🔑 API 키 설정

### Mistral AI API
1. [Mistral AI](https://console.mistral.ai/)에서 계정 생성
2. API 키 발급
3. `.env` 파일에 `MISTRAL_API_KEY` 설정

### Naver Cloud Platform OCR API
1. [Naver Cloud Platform](https://www.ncloud.com/)에서 계정 생성
2. OCR 서비스 신청 및 API 키 발급
3. `.env` 파일에 `OCR_SECRET_KEY` 설정

## 📊 데이터베이스

### 기능23_data.csv
- 건강기능식품의 기능성 원료 정보
- 성분별 기능성 내용, 표현 가능/불가능 사례 포함
- 총 23개 주요 성분 데이터

### ingredient_db.csv
- 확장된 성분 데이터베이스
- OCR 매칭을 위한 성분명과 기능성 내용
- 1,600+ 성분 정보 포함

## 🎯 사용 방법

### OCR 기반 성분 분석
1. 건강기능식품 이미지 업로드
2. "성분 추출 시작" 버튼 클릭
3. 자동으로 추출된 성분과 기능성 내용 확인

### 마케팅 문구 생성
1. 성분 선택
2. "문구 생성" 버튼 클릭
3. 규제 기준에 맞는 마케팅 문구 확인

### 허위·과장 문구 검사
1. 검사할 성분 선택
2. 광고 문구 입력
3. "검사 시작" 버튼 클릭
4. 문구의 적법성 검사 결과 확인

## ⚠️ 주의사항

- 생성된 마케팅 문구는 참고용이며, 최종 검토가 필요합니다
- OCR 정확도는 이미지 품질에 따라 달라질 수 있습니다

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.


## 📞 문의

프로젝트에 대한 문의사항이 있으시면 이슈를 생성해 주세요.

## 📈 프로젝트 성과

- **학술제 대상 수상**: 글로벌융합학과 & 글로벌리더학과 융합 학술제
- **실용성 인정**: 전자상거래 업계의 실제 문제 해결 솔루션
- **기술적 혁신**: OCR + AI를 활용한 자동화된 광고 문구 검수 시스템
- **규제 준수**: 건강기능식품 광고 규제 기준을 정확히 반영한 솔루션

---

**건강기능식품 도우미 프로그램** - 전자상거래 건강기능식품 광고 규제 대응 AI 솔루션

*글로벌융합학과 & 글로벌리더학과 융합 학술제 대상 수상작*
