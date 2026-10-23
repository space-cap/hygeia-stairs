# 12. 인쇄용 하이지아 전단지·안내문 디자인 & 텍스트 템플릿

> **경쟁사(호호계단청소) 전단지를 압도하는 하이지아 실전 전단지 시안**
> 이 문서는 동네 인쇄소, 성원애드피아, 오프린트미 등에 그대로 맡기거나, A4 프린터로 즉시 출력하여 반으로 접어(A5) 사용할 수 있는 **인쇄 규격 맞춤 텍스트 및 HTML 인쇄용 코드**를 포함합니다.

---

## 1. 전단지 기획 개요

- **판형**: A5 (148mm × 210mm) 또는 A4 단면
- **배포 방식**: 대치동 빌라 우편함 투입, 현관 인터폰 옆 클립 거치, 1층 게시판 허락 후 부착
- **핵심 메시지**:
  1. *"물 뿌리고 미끄러운 옛날 청소는 그만!"* (경쟁사 카피 흡수 및 업그레이드)
  2. *"출근길(오전 7시 이전)에 호텔처럼 반짝이는 계단"* (새벽 무소음 청소 강조)
  3. *"청소 후 카카오톡 전/후 사진 안심 보고"* (경쟁사가 흉내 내지 못하는 증빙 차별화)
  4. *"영업배상책임보험 1억 원 가입 & 대치동 대표 직접 관리"* (신뢰성)

---

## 2. 전단지 텍스트 레이아웃 (인쇄 원고용)

```
[상단 헤드라인]
물 뿌리고 미끄러운 옛날 계단 청소는 이제 그만!
출근길에 기분 좋게 마주치는 호텔 같은 계단실

[브랜드명]
하이지아(Hygeia) 프리미엄 계단청소
- 대치동 본점 직영 관리 -

[하이지아만의 4대 안심 약속]
1. [카톡 안심 보고] 청소 전/후 비교 사진을 매회 카카오톡으로 전송해 드립니다.
2. [무소음 새벽 케어] 모터 소음 없는 독일식 정전기 포집 기술로 출근 전에 뽀송하게 완료!
3. [1억 배상보험 가입] 시설물 파손 및 보행 미끄럼 사고 100% 안심 보장
4. [대치동 대표 직접 관리] 외주 알바 없이 4년 경력 베테랑 대표가 직접 꼼꼼히 청소합니다.

──────────────────────────────────────────────────────────
[대치동 실속 관리 요금표 (4~5층 기준)]
──────────────────────────────────────────────────────────
구분           방문 주기        월 관리비       주요 서비스
──────────────────────────────────────────────────────────
빌라/다세대     주 1회 (월 4회)  월  70,000원~   계단/복도/창틀/로비/우편함/분리수거
(4~5층, 8세대)  주 2회 (월 8회)  월 130,000원~   주 2회 쾌적 케어 + 현관 유리 코팅
──────────────────────────────────────────────────────────
상가/근린빌딩   주 1회 (월 4회)  월 100,000원~   공용화장실 점검 + 계단실/로비
(4~5층 규모)    주 2회 (월 8회)  월 180,000원~   출근 전 새벽 완결 + 쓰레기 배출
──────────────────────────────────────────────────────────

[상세 청소 범위]
- 현관 로비 및 공동현관 유리문 손자국·유분 제거 코팅
- 전 층 계단실 및 복도 바닥 먼지 포집 & 극세사 중성 살균 세정
- 계단 난간 손잡이, 창틀 먼지, 우편함 스티커/광고물 완벽 제거
- 1층 주차장 바닥 꽁초·쓰레기 정리 및 분리수거대 정돈
- 벽면 거미줄 제거 및 센서등 먼지 케어

──────────────────────────────────────────────────────────
★ 대치동 오픈 기념 특별 이벤트 ★
"백 마디 말보다 한 번의 깨끗함을 눈으로 보여드립니다."
[1개 층 무료 시범 청소 + 전/후 사진]을 무료로 체험해 보세요!
(비용 부담 없이 결과만 보시고 결정하시면 됩니다.)
──────────────────────────────────────────────────────────

[상담 및 신청 문의]
대표 직통: 010-XXXX-XXXX (24시간 문자/카톡 접수 가능)
카카오톡 채널: "하이지아 계단청소" 검색
주소: 서울시 강남구 대치동
```

---

## 3. 웹 브라우저 인쇄용 HTML/CSS 소스코드

> **생성된 인쇄용 파일 바로가기**: [flier.html](file:///h:/lee/hygeia-stairs/print/flier.html)  
> 브라우저(Chrome/Edge)에서 위 파일을 더블 클릭하여 연 뒤, 상단의 **[🖨️ A4 즉시 인쇄]** 버튼을 누르거나 `Ctrl + P`를 누르면 여백 없이 완벽한 A4 규격으로 출력됩니다. (인쇄 옵션에서 **'배경 그래픽 포함'** 체크 권장)

아래는 해당 파일의 원본 소스코드입니다:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>하이지아 계단청소 전단지</title>
  <style>
    @page { size: A4 portrait; margin: 12mm; }
    body {
      font-family: 'Pretendard', 'Malgun Gothic', sans-serif;
      color: #1e293b;
      margin: 0;
      padding: 0;
      background-color: #ffffff;
      -webkit-print-color-adjust: exact;
    }
    .flier-container {
      border: 3px solid #0f766e;
      border-radius: 12px;
      padding: 24px;
      box-sizing: border-box;
      height: 100%;
    }
    .header { text-align: center; border-bottom: 2px dashed #cbd5e1; padding-bottom: 16px; }
    .sub-badge {
      display: inline-block;
      background: #f0fdfa;
      color: #0f766e;
      padding: 4px 12px;
      border-radius: 20px;
      font-weight: bold;
      font-size: 14px;
      margin-bottom: 6px;
    }
    .main-title { font-size: 28px; font-weight: 800; color: #0f766e; margin: 4px 0; }
    .hero-copy { font-size: 16px; color: #475569; margin: 0; }
    
    .promises {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin: 18px 0;
    }
    .promise-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 4px solid #0f766e;
      padding: 10px 12px;
      border-radius: 6px;
    }
    .promise-card strong { font-size: 14px; color: #0f766e; display: block; margin-bottom: 4px; }
    .promise-card span { font-size: 12px; color: #334155; line-height: 1.4; }

    .price-table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 13px; }
    .price-table th { background: #0f766e; color: #ffffff; padding: 8px; text-align: center; }
    .price-table td { border: 1px solid #cbd5e1; padding: 8px; text-align: center; }
    .price-table td.highlight { font-weight: bold; color: #0f766e; font-size: 14px; }

    .scope-box {
      background: #f1f5f9;
      padding: 12px;
      border-radius: 8px;
      font-size: 12px;
      line-height: 1.6;
      margin-bottom: 16px;
    }
    .scope-box strong { color: #0f766e; }

    .cta-event {
      background: #fef3c7;
      border: 2px solid #f59e0b;
      border-radius: 8px;
      padding: 12px;
      text-align: center;
      margin-bottom: 16px;
    }
    .cta-event h3 { margin: 0 0 4px; color: #b45309; font-size: 16px; }
    .cta-event p { margin: 0; font-size: 13px; color: #78350f; font-weight: bold; }

    .footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #0f766e;
      color: #ffffff;
      padding: 12px 18px;
      border-radius: 8px;
    }
    .footer-left { font-size: 13px; }
    .footer-phone { font-size: 22px; font-weight: 800; letter-spacing: 1px; color: #fef08a; }
  </style>
</head>
<body>
  <div class="flier-container">
    <div class="header">
      <div class="sub-badge">물 뿌리는 미끄러운 옛날 청소는 이제 그만!</div>
      <h1 class="main-title">하이지아(Hygeia) 프리미엄 계단청소</h1>
      <p class="hero-copy">출근길에 기분 좋게 마주치는 호텔 같은 대치동 계단실</p>
    </div>

    <div class="promises">
      <div class="promise-card">
        <strong>1. 카톡 전/후 사진 보고</strong>
        <span>청소 완료 즉시 4컷 전후 사진을 임대인 휴대폰으로 투명하게 전송합니다.</span>
      </div>
      <div class="promise-card">
        <strong>2. 새벽 무소음 케어</strong>
        <span>모터 진동 없는 정전기 포집 기술로 입주민 출근 전에 뽀송하게 끝냅니다.</span>
      </div>
      <div class="promise-card">
        <strong>3. 1억 원 영업배상보험</strong>
        <span>시설 파손 및 보행 미끄럼 사고에 대비해 현대해상/삼성화재 1억 보험 가입.</span>
      </div>
      <div class="promise-card">
        <strong>4. 대치동 주민 대표 직접 관리</strong>
        <span>하청이나 초보 알바 없이 4년 경력의 대표가 100% 책임 시공합니다.</span>
      </div>
    </div>

    <table class="price-table">
      <thead>
        <tr>
          <th>건물 유형</th>
          <th>방문 주기</th>
          <th>월 관리비</th>
          <th>관리 내용</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td rowspan="2"><b>빌라 / 다세대</b><br>(4~5층, 8세대 기준)</td>
          <td>주 1회 (월 4회)</td>
          <td class="highlight">월 7만 ~ 9만 원</td>
          <td>계단, 복도, 창틀, 로비, 우편함, 분리수거</td>
        </tr>
        <tr>
          <td>주 2회 (월 8회)</td>
          <td class="highlight">월 13만 ~ 16만 원</td>
          <td>주 2회 호텔식 광택 케어 + 현관 유리 발수코팅</td>
        </tr>
        <tr>
          <td rowspan="2"><b>상가 / 근린빌딩</b><br>(4~5층 규모)</td>
          <td>주 1회 (월 4회)</td>
          <td class="highlight">월 10만 ~ 12만 원</td>
          <td>공용화장실 점검 + 계단실 바닥 + 로비</td>
        </tr>
        <tr>
          <td>주 2회 (월 8회)</td>
          <td class="highlight">월 18만 ~ 22만 원</td>
          <td>출근 전 새벽 완결 + 화장실 세정 + 쓰레기 배출</td>
        </tr>
      </tbody>
    </table>

    <div class="scope-box">
      <strong>[청소 범위]</strong> 전 층 계단·복도 먼지 포집 & 살균 세정 / 손잡이 난간 소독 / 창틀 먼지 / 공동현관 유리문 손자국 코팅 / 우편함 전단지 스티커 제거 / 주차장 꽁초·낙엽 청소 / 분리수거함 정리
    </div>

    <div class="cta-event">
      <h3>★ 대치동 오픈 기념: 1개 층 무료 시범 청소 이벤트 ★</h3>
      <p>"비용 부담 없이 결과만 직접 눈으로 확인하시고 결정하세요!"</p>
    </div>

    <div class="footer">
      <div class="footer-left">
        <div>하이지아(Hygeia) 대치본점</div>
        <div style="font-size:11px; opacity:0.8;">서울 강남구 대치동 직영 관리 | 사업자 등록 완료</div>
      </div>
      <div class="footer-phone">
        상담문의: 010-XXXX-XXXX
      </div>
    </div>
  </div>
</body>
</html>
```

---

## 4. 현관문 부착용 초소형 포스트잇/스티커 문구 (초간단 버전)

A4 전단지 외에 현관 도어락 부근에 가볍게 붙이거나 우편함 전면에 꽂는 명함 사이즈 문구입니다:

> **[하이지아 계단청소]**
> *"계단 청소 상태가 마음에 안 드시나요?"*
> - 매주 청소 전/후 사진 카톡 보고
> - 물기 없이 보송한 무소음 새벽 케어
> - 빌라 주 1회 월 7만 원부터!
> **무료 1회 시범 청소 신청: 010-XXXX-XXXX**
