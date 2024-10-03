# 도메인

## 원칙
* 설계 레벨
  * 자동화된 작업은 언젠가 수작업이 반드시 필요하다.
  * 중요한 일에는 언제나 승인이 필요하다.
  * 데이터 타입으로 '임시'가 필요할 거다.
  * 데이터는 쪼개질 수도, 합쳐질 수도 있다.
  * best practice는 항상 존재한다.
* 구현 레벨
  * 언제나 운영을 생각하라.
    * 유저가 할 수 있으면 관리자도 할 수 있어야 한다.
      * 회원생성, 회원탈퇴 등
    * 1 and n
      * 원하는 수만큼 선택해서 일괄 회원탈퇴 등
  * serial and parallel
    * 성능 관련

## 목록
* APP: APPlication
* BCI: Business Core Infrastructure
* BCM: Business Common Module
* CRM: Customer Relationship Managment
* SCM: Supply Chaing Management
* LDM: Logistics and Distribution Management
* CMA: Cost and Management Accounting
* FRM: Financial Reporting Management

##  APP
* APP_Member
* APP_User
* APP_Organization
* APP_Organization_User_Map
* APP_Authority, APP_Role, APP_UserRole, APP_UserAuthority
* APP_APIRequest, APP_ServiceTransaction

* APP_Notification

* APP_Calendar

* APP_Service

* APP_Workflow
  * 기능 자동화
  * BCI_BPO에서 관리하지 않는 이유는 비즈니스 외의 고객 대상 서비스 도메인에서의 활용도 염두함.
  * APP
  * APP
  * APP

* APP_File

* APP_Log

* APP_Code
* APP_CodeSet

## BCI
* 중요: APP과 BCI 간의 통신은 별도로 기록하지 않고 APP에서 관리하는 로그로만 추적함.

* BCI_RPA

* BCI_BTM: Business Transaction Management
  * 주요 거래를 중심으로 추적.
* BCI_BPO: Business Process Orchestration
  * 정형화된 정의가 존재함.

* 참고 표준
  * BPMN(Business Process Model Notation)
  * CMMN(Case Mangement Model Notation)
  * DMN(Decision Model and Notation)

### 9월 22일 이전
* BCI_Master
  * domain and type
* BCI_MasterHistory
* BCI_Transaction
  * domain, transaction_type
  * '확정됨'과 '취소됨', '정정됨'만 추적
  * subtype transaction들이 가져야할 status
    * 생성중, 생섬됨 / createing, created
    * 수정중, 수정됨 / modifing, modified
    * 확정중, 확정됨 / confirming, confirmed
    * 정정중, 정정됨 / correcting, corrected
    * 취소중, 취소됨 / cancelling, cancelled
* BCI_TransactionObject
* BCI_TransactionObject_Hierarchy
* BIC_TransactionMapping
  * Transaction들간의 관계 데이터
  * 순환 참조 방지 필요

* BCI_Process
  * 최초 Transaction ID가 Process ID가 sql에서 BCI_Process 참조없이 트리 탐색 가능
* BCI_ProcessTransaction
  * Transaction에 next_process_id 필드를 정의해야할 듯.

## BCM
* BCM_Approval
* BCM_Approver

* BCM_Material
  * subtype
    * BCM_Product
    * BCM_Service
  * SCM, CRM, LDM

* BCM_Price
* BCM_Quotation
* BCM_Order
* BCM_OrderLine
  * 품목 그룹과 개별 품목의 계층적 구조 지향
  * 할인이나 세금 코드는 필드로 관리
* BCM_Invoice
* BCM_Payment
* BCM_Settlement

* BCM_CLM

## LDM
* LDM_Shipment

## CRM
* CRM_Customer
* CRM_Manager

* CRM_SalesQuotation
* CRM_SalesOrder
* CRM_Sales

* CRM_Reservation
* CRM_ServiceDelivery
* CRM_Coupon
* CRM_CustomerCoupon

* CRM_Campaign

## SCM
* SCM_Supplier

* SCM_RequestForQuotation (구현 후순위)
* SCM_PurchaseQuotation
* SCM_PurchaseQuotationLine
* SCM_PurchaseQuotation_Raw
  * 증빙자료(파일) 또는 링크
* SCM_PurchaseQuotationLine_Raw
* SCM_PurchaseRequisition
* SCM_PurchaseOrder
* SCM_PurchaseOrderLine
* SCM_PurchaseOrder_Raw
  * 증빙자료(파일) 또는 링크
* SCM_PurchaseOrderLine_Raw

## CMA
* 현금흐름 분석을 제외하고는 아직은 별로 쓸모가 없는 듯.

* CMA_CashFlow
* CMA_CashFlow_Scenario

* CMA_Performance
* CMA_PerformanceAggregation
  * 일, 주, 월별 집계

* KPI 관리

* CMA_Budget
* CMA_BudgetItems
  * 위계성 데이터

## FRM
* FRM_Journal
* FRM_JournalLine
* FRM_Ledger
* FRM_Voucher - 전표
* FRM_Settlement - 결산

* FRM_BankAccount
  * Master 데이터임.
* FRM_BankTransaction
* FRM_BankTransaction_Manual
* FRM_BankTransaction_Staging
* FRM_BankTransaction_Map
  * 표준 데이터, 수기 기록, 원본 첨부, 인터페이스된 데이터 간의 매핑
* FRM_BankTransaction_Raw_[은행명 또는 계좌번호]
* FRM_BankTransaction_Interface_[은행명 또는 계좌번호]

* FRM_VATInvoice_Raw

# 도메인 24.09.16

##  목록
* APP: 앱 내에서
  * 포함되는 테이블: Member, User, Organization, Authority, Role 등
* CRM: 고객관리, 판매, 서비스 관리 등
* SCM: 구매, 자재, 생산 등
  * PurchaseOrder, Material 등
* CMA: 원가관리회계, 예상현금흐름분석, 예상산출세액 등 의사결정을 위한 회계 관련 테이블
  * BankTransaction, CashFlow
* FRM: 재무보고
  * Journal, JournalItem 등
* LDM: 물류 및 유통
* BCM:

## APP
* APP_Member
* APP_User
* APP_Organization
* APP_Organization_User_Map
* APP_Authority, APP_Role, APP_UserRole, APP_UserAuthority

* 결재
  * APP_Approval 결재
  * APP_ApprovalHistory 결재이력
  * APP_Approver 결재자
  * APP_ApproverHistory 결재자 이력

## SYS
* SYS_APIRequest - 컨트롤러 레이어
* SYS_Transaction - 서비스, 리포지토리 레이어

## BCS: 다른 설계

* PO

## BCS: Business Core System
BCS는 금액적인 부분뿐만 아니라 행정(CS, 물류, 기타 서비스 로직 등) 처리까지 포괄하는 개념.

* BCS_Master - 원장성 데이터
* BCS_MasterHistory - 이력데이터
* BCS_Transaction - 원장성 데이터
  * status
    * 생성중, 생성됨
    * 수정중, 수정됨
    * 발행중, 발행됨
    * 취소중, 취소됨
    * 삭제중, 삭제됨
  * type
    * 금전적 거래
      * 목록: 판매, 구매, 배송, 환불, 교환, 결재, 계좌, 카드, pg, 정산, 지출
    * 비금전적 거래
      * 목록: Demand,
* BCS_TransactionHistory - 이력 데이터
* BCS_Process
  * History와 다른 개념.
  * BCS_Process_Transaction_Map
  * 종결 또는 흡수

* BCS_Contract
  * BCS_Contract_Transaction_Map

### 예시 1
* 판매 주문을 확정하고 결재가 아직 안 된 경우
  * 판매거래 SO_01은 확정완료
  * 결재거래 PY_01은 생성완료
* 임대차계약
  * 보증금 및 기타 임차료 지불 현금유출 COF 생성완료(예정)
  * 입금될 때마다 결제거래 PY_n 확정완료
* 구매 주문을 작성해서 거래처에 요청한 경우
  * 구매거래 PO_01 확정중, 확정완료

### 예시 2
* 판매주문 PO_01을 교환 처리할 경우
  1. BO_01 취소요청, 취소완료
  2. BO_01 수정요청, 수정완료 (PO_01 -> PO_02)
  3. BO_01 확정요청, 확정완료 (PO_02)
* 취소 요청을 취소(철회)하는 경우

### 결론
어느 주문을 취소하고, 취소한 걸 또 철회했는지에 대한 관심사는 원칙적으로 CRM에 있다.
**취소의 연쇄는 BCS_Process로 관리함이 옳다.**

##  CRM
* CRM_Customer
* CRM_CustomerDetail
* CRM_CustomerReward
* CRM_Manager
* CRM_SalesItem
  * CRM_SalesProduct
  * CRM_SalesService
* CRM_SalesOrder (취소주문 포함)
* CRM_SalesPrice
* CRM_SalesCoupon

##  SCM
* SCM_Vendor
* SCM_PurchaseOrder

##  CMA
Cost and Management Accounting
* Cost
* BankAccount

##  FRM
Financial Reporting Management
* Journal 분개
* HRM

# 도메인(~24.09.14)
* 서비스 도메인
  * 계정/사용자 User
    * personal, business, admin
  * 조직 Organization
    * 추후에 내부적으로 결재나 내부 권한 등이 필요할 수 있음.
  * 권한 Authority
  * 회원 Member (계약 단위)
    * consumer, supplier
    * personal, business
  * 상품 Product
  * 재고 Inventory
  * 주문 Order
  * 결재 Payment
  * 정산 Settlement
  * 배송 Shipment
  * 커뮤니티 Community
    * 게시판, 댓글, 팔로우, 그룹 및 SNS 기능...
  * CRM
    * 공지사항
    * 고객센터
      * FAQ
      * 문의
      * 기타 채널
  * 프로모션
    * 쿠폰 Coupon
    * 이밴트 Event
      * 이밴트 별 할인, 증정, 기타 혜택 정책
      * 상품, 브랜드
* 시스템 도메인
  * 마케팅 (퍼널 Funnel, AARRR)
  * 보안
    * sonarqube를 통한 SAST 적용
    * OWASP
    * 참고
      * TOSS SLASH 23

