# S-AI_Project
# RAMP (Roadmap for Aspiring Professionals)

**프로젝트 기간:** 2024-08-28 ~ 2024-08-30 (3일)

## 프로젝트 개요

이 프로젝트는 사용자의 진로 선택에 도움을 줄 수 있는 AI 기반의 진로 추천 서비스를 개발하는 것을 목표로 합니다. 커리어넷, 큐넷, 워크넷 등 OpenAPI를 활용하여 직업, 학과, 자격증 정보를 수집하고, 이를 AI 언어 모델에 적용하여 사용자 맞춤형 진로 정보를 제공합니다. 또한, 사용자가 오프라인 상태에서도 서비스를 사용할 수 있는 기능을 제공합니다.

## 프로젝트 목표

### 주요 목표
- **AI 기반 진로 추천 서비스 제공:** 사용자에게 적합한 진로를 추천하는 AI 기반 서비스 개발

### 세부 목표
1. **커리어넷, 워크넷 OpenAPI 활용 및 데이터 전처리**
   - 직업백과와 학과 정보, 전망 등의 정보하여 API를 활용하여 진로 정보를 수집하고 전처리
2. **언어 모델을 통한 데이터 가공 및 추천 서비스 제공**
   - 전처리된 데이터를 Ollama - phi3.5 또는 GPT-4o 언어 모델에 입력하여 사용자 맞춤형 진로 추천
3. **On-Device 기능 구현**
   - 사용자가 오프라인 상태에서도 진로 정보를 확인할 수 있는 기능 제공
4. **자격증 정보 추가**
   - 큐넷 OpenAPI를 활용해 관련 자격증 정보를 수집하고 진로 추천에 반영

## 사용된 모델 및 기술

- **주요 모델:**
  - Ollama - phi3.5 또는 GPT-4o
- **사용 기술:**
  1. **커리어넷 OpenAPI**
     - 직업 및 학과 정보를 수집하여 사용자 맞춤형 진로 추천
  2. **큐넷 OpenAPI**
     - 자격증 정보를 수집하여 진로 선택 시 참고 자료로 제공
  3. **워크넷 OpenAPI**
     - 직업의 특성 및 전망, 상세 정보 (자격/면허, 관련직업, 수행직무)
  4. **Flask**
     - 웹 애플리케이션 구축 및 클라이언트와의 데이터 통신을 위한 서버 구현
  5. **API 및 기술 추가 예정**

## 프로젝트 일정

### 1일차 (2024-08-28)
- **커리어넷 API 데이터 수집 및 전처리**
  - 박성현: 직업 및 학과 정보 수집
  - 박의준: 데이터 전처리 및 언어 모델 적용
  - 박재한: 기본적인 진로 추천 기능 개발

### 2일차 (2024-08-29)
- **웹 기반 서비스 구축 및 테스트**
  - 박성현: 사용자 인터페이스 설계 및 구현
  - 박의준: Flask를 활용한 웹 기반 API 구축
  - 박재한: 진로 추천 기능 테스트 및 개선

### 3일차 (2024-08-30)
- **큐넷 API 데이터 수집 및 통합**
  - 박성현, 박재한: 자격증 정보 수집 및 기존 추천 서비스에 통합
  - 박의준: 전체 서비스 테스트, 디버깅, 최종 결과물 도출

## 예상 결과물

- **진로 추천 AI 웹 서비스**
  - 직업, 학과, 자격증 정보를 포함한 맞춤형 진로 추천 기능
  - 사용자 친화적인 웹 인터페이스
  - 오프라인 기능을 포함한 On-Device 사용 가능

- **프로젝트 문서화 및 보고서**
  - API 활용 가이드 및 코드 설명
  - 언어 모델 적용 및 데이터 전처리 과정 설명
  - 프로젝트 실행 결과 및 향후 개선 방안 제시

---
