# Functional Specification Document

## Release Management Portal (RMP)

---

## Document Properties

| Property | Value |
|---|---|
| Document Title | Functional Specification Document — Release Management Portal (RMP) |
| Project | Release Management Portal (RMP) — Self-Service Release Slot Booking Portal / App |
| Version | 1.1 (Draft) |
| Date | 10 July 2026 |
| Prepared By | Business Analyst |
| Status | Draft — Pending Client Review (Discovery Gaps Open — see Sections 4 & 5) |

---

## Table of Contents

1. [Introduction](#1-introduction)
   - 1.1 [Purpose](#11-purpose)
   - 1.2 [Problem Statement](#12-problem-statement)
   - 1.3 [Business Objective](#13-business-objective)
   - 1.4 [Proposed Solution](#14-proposed-solution)
   - 1.5 [Expected Benefits](#15-expected-benefits)
   - 1.6 [Document Conventions](#16-document-conventions)
2. [Scope](#2-scope)
   - 2.1 [In Scope](#21-in-scope)
   - 2.2 [Out of Scope](#22-out-of-scope)
3. [Project Drivers](#3-project-drivers)
4. [Dependencies](#4-dependencies)
5. [Assumptions & Constraints](#5-assumptions--constraints)
   - 5.1 [Assumptions](#51-assumptions)
   - 5.2 [Constraints](#52-constraints)
6. [Functional Requirements](#6-functional-requirements)
   - UC-00 [User Login](#uc-00-user-login)
   - UC-01 [View Release Calendar & Slot Availability](#uc-01-view-release-calendar--slot-availability)
   - UC-02 [Book a Release Slot — Wizard Step 1: Details & Resources](#uc-02-book-a-release-slot--wizard-step-1-details--resources)
   - UC-03 [Complete PM Pre-Scheduling Checklist — Wizard Step 2](#uc-03-complete-pm-pre-scheduling-checklist--wizard-step-2)
   - UC-04 [Submit Request & Auto-Conflict Validation — Wizard Step 3](#uc-04-submit-request--auto-conflict-validation--wizard-step-3)
   - UC-05 [5-Stage Sequential Approval Workflow](#uc-05-5-stage-sequential-approval-workflow)
   - UC-06 [Reject / Cancel Release Request (Release Manager)](#uc-06-reject--cancel-release-request-release-manager)
   - UC-07 [Self-Cancel Booked Slot (PM/Team)](#uc-07-self-cancel-booked-slot-pmteam)
   - UC-08 [Admin Blackout Override Management](#uc-08-admin-blackout-override-management)
   - UC-09 [Automated Stakeholder Confirmation Notification](#uc-09-automated-stakeholder-confirmation-notification)
7. [Non-Functional Requirement](#7-non-functional-requirement)
8. [Notifications Reference](#8-notifications-reference)
9. [Revision History](#9-revision-history)

---

## 1. Introduction

### 1.1 Purpose

This Functional Specification Document (FSD) defines the detailed functional and non-functional behaviour of the Release Management Portal (RMP), based on the approved PRD and the discovery discussions held with the client stakeholder to date. It translates the business requirements into structured use cases, screen and interaction expectations, business rules, and notification behaviour that engineering, QA, and design teams will use to build and test the system. This document is intended for the Development Team, QA Team, UX/UI Designers, Project Management, and the client-side business stakeholders (Release Manager, Engineering Managers, Product Owners, and the QA Manager) who will validate that the specified behaviour matches their operational needs.

### 1.2 Problem Statement

In an enterprise with 200+ technical members operating across isolated project silos, release slot booking is currently managed entirely manually — through email trails, phone calls, and instant messages — with no cross-project visibility into sprints or planned release dates. The Release Manager must manually cross-check spreadsheets to avoid scheduling collisions. This manual process results in scheduling bottlenecks, human error, double-booking of shared resources (DevOps/SRE engineers), and delayed deployments.

### 1.3 Business Objective

To provide a single source of truth for release scheduling that eliminates manual coordination overhead, prevents slot and shared-resource collisions automatically, enforces release readiness through a mandatory checklist, and routes every release through a consistent, auditable digital approval chain — while preserving project-level privacy across siloed teams. The stakeholder-articulated success measure is to automate approximately 90% of the coordination effort currently performed manually by the Release Manager, while retaining a small residual (~10%) of manual coordination for edge cases.

### 1.4 Proposed Solution

The Release Management Portal (RMP) is a self-service, calendar-based Release Slot Booking Portal (with web and mobile compatibility) that allows Project Managers to book fixed 2-hour release slots, complete a mandatory pre-scheduling readiness checklist, and route the request through a 5-stage sequential digital approval chain (QA → Engineering Manager → Product/Business → DevOps/SRE → Release Manager). The system automatically blocks slot collisions and shared-resource double-booking, maintains blind availability status to protect project privacy, allows the Release Manager to apply admin blackout overrides, and triggers an automated confirmation notification once a release is fully approved.

### 1.5 Expected Benefits

- Elimination of manual, error-prone spreadsheet-based slot tracking and email/phone coordination.
- Automatic prevention of double-booked shared DevOps/SRE resources.
- Consistent enforcement of release-readiness documentation (Release Notes, Deployment Steps, Handover) before a request can proceed.
- A fully sequential, auditable 5-stage approval trail with no possibility of stage-skipping.
- Reduction of manual coordination effort by an estimated ~90%, per stakeholder-stated target.
- A single, self-service system usable across both web and mobile, reducing dependency on ad-hoc communication channels.
- Faster, more predictable release scheduling with fewer last-minute collisions and delayed deployments.

### 1.6 Document Conventions

| Abbreviation | Definition |
|---|---|
| PRD | Product Requirement Document |
| FSD | Functional Specification Document |
| BRD | Business Requirement Document |
| RMP | Release Management Portal |
| PM | Project Manager |
| TL | Technical Lead |
| EM | Engineering Manager |
| PO | Product Owner |
| QA | Quality Assurance |
| SRE | Site Reliability Engineer |
| RM | Release Manager |
| SA | Super Admin |
| IST | Indian Standard Time |
| MVP | Minimum Viable Product |
| NFR | Non-Functional Requirement |
| SSO | Single Sign-On |
| API | Application Programming Interface |
| UC | Use Case |
| BR | Business Rule |
| AF | Alternative Flow |

---

## 2. Scope

### 2.1 In Scope

- Self-service release calendar with fixed, non-overlapping 2-hour slot windows.
- Blind availability status ("Unavailable") visible to all users; project-level detail remains private.
- Automated slot collision blocking (no two projects can book the identical window).
- Shared Resource Guardrail preventing double-booking of DevOps/SRE engineers across projects.
- 3-step Release Scheduling Wizard: Details & Resources → PM Checklist & Uploads → Auto-Conflict Check & Route.
- Mandatory PM Pre-Scheduling Checklist (Release Notes, Deployment Steps, Handover to DevOps confirmation).
- 5-Stage Sequential Digital Approval Workflow (QA → EM → Product/Business → DevOps/SRE → Release Manager).
- Strict order enforcement and immutability once "Approved & Scheduled."
- Release Manager–driven rejection/cancellation flow with mandatory reason capture.
- PM/team self-cancellation of their own booked slot with mandatory reason capture.
- Admin (Release Manager) blackout override management (days, hour blocks, weekends, "No-Deploy Fridays," holidays).
- Automated stakeholder confirmation notification upon final Stage 5 approval.
- Dynamic, permission-driven role and access model, DB-configured (not hardcoded in UI).
- Web and mobile compatibility.
- User login via email address and password (no self-service sign-up; accounts are pre-provisioned).

### 2.2 Out of Scope

- SSO / enterprise Active Directory authentication integration (desired future enhancement — not committed for MVP).
- Vendor/external organisation onboarding (e.g., third-party vendor PMs) into the RMP ecosystem.
- Slack/Teams communication webhooks and automated chat DM notifications (Phase 2).
- Automated Resource Recommendation Engine (suggesting alternate slots/backup engineers) (Phase 2).
- Enterprise Bottleneck Dashboard / approval-stage analytics reporting (Phase 2).
- AI-Powered Document Validation (LLM-based parsing of handover documents) (Phase 2).
- System-level tracking of the content/outcome of the offline DevOps/SRE handover meeting (tracked only via checkbox in MVP).
- Individual confirmation capture from every squad member post-approval (accountability rests with the Release Manager).
- Multi-timezone display/conversion beyond IST (unless vendor onboarding scope is later approved).

---

## 3. Project Drivers

- **Operational inefficiency:** 100% manual slot booking via email/phone/IM across 200+ technical staff is unsustainable at current organisational scale.
- **Risk of collision and error:** Manual spreadsheet cross-checking is prone to human error, resulting in double-booked shared resources and delayed deployments.
- **Lack of visibility:** Isolated project silos have zero cross-project visibility into release schedules, increasing the risk of resource contention.
- **Governance gap:** No consistent, enforced readiness checklist or sequential sign-off currently exists prior to deployment, increasing release risk.
- **Stakeholder-driven efficiency target:** The client sponsor has set an explicit goal of automating ~90% of current manual coordination effort.
- **Organisational cross-training initiative:** The client has framed this rollout partly as an opportunity for cross-project teams to align on a standard release process.

---

## 4. Dependencies

| # | Dependency (System/Team) | Description | Owner |
|---|---|---|---|
| 1 | Shared Enterprise Resource Database | Source of truth for DevOps/SRE engineer identities and real-time availability; required for Shared Resource Guardrail logic. | Client IT / Enterprise Architecture (TBD) |
| 2 | Email Delivery Service | Required to dispatch the automated Stage 5 stakeholder confirmation email and other notification templates. | Client IT / DevOps |
| 3 | CI/CD or Build Tracking System | Potential source for the "Build Version" field referenced in confirmation notifications; data-entry point still unconfirmed. | Client Engineering / DevOps |
| 4 | Project Master / Onboarding Process | Existing or to-be-defined process for how new project silos are added to RMP. | Manoj Singh / PMO |
| 5 | Enterprise IAM / Directory System (Future) | Required only if/when SSO integration is approved for a future phase. | Client IT Security (TBD) |
| 6 | Downstream Approver Personas (QA Manager, EM, Product Owner, DevOps/SRE Lead) | Validation and sign-off required on their respective stage-specific approval requirements before FSD is finalised. | Manoj Singh / Respective Leads |
| 7 | Hosting / Infrastructure Environment | Confirmation of cloud/on-prem environment (Azure referenced informally) for deployment target and access provisioning. | Client IT / DevOps |

---

## 5. Assumptions & Constraints

### 5.1 Assumptions

- All bookable slots are assumed to operate within IST for MVP; no multi-timezone conversion is required unless vendor onboarding scope is later approved.
- The Release Manager's manual email/offline coordination is assumed sufficient to cover approver unavailability, in the absence of a formal delegation mechanism.
- The offline DevOps/SRE handover meeting is assumed to require no system-level content audit — a checkbox confirmation from the PM is assumed sufficient for MVP governance.
- Simple email/password authentication is assumed acceptable for MVP despite the stakeholder's own acknowledgment that SSO is ultimately needed.
- It is assumed that role and permission definitions can be fully managed via backend/DB configuration without a dedicated admin UI for MVP.
- It is assumed that "90% time saved" is an acceptable qualitative target without a formally defined baseline measurement methodology, pending further clarification.
- It is assumed Azure (referenced informally in discovery) is a representative, not necessarily final, confirmed deployment target environment.

### 5.2 Constraints

- The exact definition of "India Business Hours" is currently contradictory between two statements given by the stakeholder (10 AM–8 PM general business hours vs. 5–9 AM/5 PM stated deployment windows) and **must be resolved before Module 1 (slot engine) can be finalised in build.**
- The structure and size of the Shared DevOps/SRE resource pool has not yet been defined, constraining finalisation of Module 2 (Shared Resource Guardrail) logic.
- Minimum slot booking duration (30 minutes vs. 1 hour) remains undecided.
- No non-functional requirements (performance, concurrency, uptime, security, audit/compliance, data retention) have been confirmed to date; NFRs in Section 7 are provided at a high level only and require validation.
- No committed delivery timeline, phased rollout plan, or resourcing confirmation exists as of this document's drafting.

---

## 6. Functional Requirements

Each use case below follows a standard two-column format: a label column identifying the use case attribute, and a content column describing it in full.

---

### UC-00: User Login

| Attribute | Details |
|---|---|
| **Use Case ID** | UC-00 |
| **Use Case Name** | User Login |
| **Description** | Allows a registered user to authenticate into RMP using their enterprise email address and password. There is no self-service sign-up option — all user accounts are provisioned by an administrator/backend process ahead of time. |
| **Actors** | Primary: Project Manager, Technical Lead, QA, Shared DevOps, SRE, Engineering Manager, Product Owner, Release Manager (Global Admin).<br>Secondary: System (Authentication Engine). |
| **Pre-Conditions** | - User has a pre-provisioned account (email address and password) already set up in RMP by an administrator; no self-registration exists.<br>- User has access to the RMP login page (web or mobile). |
| **Post-Conditions** | - On success: user is authenticated and redirected to the Release Calendar (UC-01), with access scoped to their assigned role/permissions.<br>- On failure: user remains on the login screen with an appropriate error message and is not granted access. |
| **Basic Flow** | 1. User navigates to the RMP login screen (web or mobile).<br>2. User enters their registered email address.<br>3. User enters their password.<br>4. User clicks "Log In."<br>5. System validates the email/password combination against stored credentials.<br>6. On successful validation, system creates an authenticated session and redirects the user to the Release Calendar (UC-01), applying role-based permissions per the DB-configured role model. |
| **Alternative Flows** | **AF-01:** User enters an incorrect email address or password → system displays a generic "Invalid email or password" error without indicating which field was incorrect, and the user remains on the login screen.<br>**AF-02:** User attempts to log in with an email address that has no corresponding account → system displays the same generic "Invalid email or password" error (no account-existence disclosure).<br>**AF-03:** User forgets their password → user selects "Forgot Password" to initiate a password-reset flow (see BR-03).<br>**AF-04:** User exceeds a defined number of consecutive failed login attempts → account is temporarily locked and the user is shown a lockout message (exact threshold and lockout duration to be confirmed — see Section 5.2 Constraints). |
| **Screen Annotations** | Login screen with RMP branding/logo, two input fields ("Email Address," "Password" — masked), a "Log In" button, and a "Forgot Password?" link beneath the form. Inline validation messaging appears below the form on failed attempts. |
| **Link/Button Annotations** | "Log In" button → submits credentials for validation; disabled while a request is in progress to prevent duplicate submission. "Forgot Password?" link → routes to the password-reset flow. No "Sign Up" or "Create Account" link is present anywhere on the screen. |
| **Business Rules** | **BR-01:** Authentication for MVP is limited to email address and password only; no SSO/Active Directory integration is included (see Section 2.2 Out of Scope).<br>**BR-02:** No self-service sign-up/registration capability exists in RMP; all accounts must be provisioned by an administrator or backend process ahead of time.<br>**BR-03:** A "Forgot Password" mechanism must be available to allow users to reset a forgotten password via a secure reset link sent to their registered email address.<br>**BR-04:** Passwords must be stored securely (hashed) and never displayed or transmitted in plain text, per the security NFR in Section 7.<br>**BR-05:** Failed login attempts must not reveal whether the entered email address corresponds to an existing account, to avoid account enumeration. |

---

### UC-01: View Release Calendar & Slot Availability

| Attribute | Details |
|---|---|
| **Use Case ID** | UC-01 |
| **Use Case Name** | View Release Calendar & Slot Availability |
| **Description** | Allows any authenticated user to view the release calendar grid showing fixed 2-hour slots, with slots booked by other project silos displayed as "Unavailable" without exposing project-level detail. |
| **Actors** | Primary: Project Manager, Technical Lead, QA, Shared DevOps, SRE, Engineering Manager, Product Owner, Release Manager.<br>Secondary: System (Calendar Engine). |
| **Pre-Conditions** | - User has successfully logged in (UC-00).<br>- User has an assigned role with calendar-view permission. |
| **Post-Conditions** | - User has visibility of all bookable, booked, and blacked-out slots for the visible date range.<br>- No project-identifying information is disclosed for slots booked by other silos. |
| **Basic Flow** | 1. User logs into RMP.<br>2. User navigates to the Release Calendar screen.<br>3. System renders the calendar grid with fixed 2-hour slot columns/rows per day.<br>4. System marks each slot as "Available," "Unavailable" (booked by any project), or "Blacked Out" (admin override).<br>5. User may filter/scroll the calendar by date range. |
| **Alternative Flows** | **AF-01:** No slots are configured for the selected date range → system displays an empty-state message.<br>**AF-02:** Selected date range falls entirely within an admin blackout period → all slots display as "Unavailable" with a distinct blackout visual indicator. |
| **Screen Annotations** | Calendar grid view with day/date headers across the top, 2-hour slot rows down the side. Each cell is colour-coded: green = Available, grey = Unavailable, red/hatched = Blackout. No project name or squad detail appears on Unavailable cells. |
| **Link/Button Annotations** | "Book a Slot" button (visible on Available cells) → launches UC-02 wizard. Date range navigation arrows → shifts the visible calendar window. Legend toggle → shows/hides colour-key explanation. |
| **Business Rules** | **BR-01:** Slot status must be shown identically to all authenticated users regardless of role (blind visibility) for MVP — no privileged "unblinded" view exists.<br>**BR-02:** Admin blackout overrides must propagate instantly across all project views once applied. |

---

### UC-02: Book a Release Slot — Wizard Step 1: Details & Resources

| Attribute | Details |
|---|---|
| **Use Case ID** | UC-02 |
| **Use Case Name** | Book a Release Slot — Wizard Step 1: Details & Resources |
| **Description** | Allows a PM to select a Project ID, choose an available 2-hour slot, and assign named squad members (PM, Dev/TL, QA, Shared DevOps, SRE) to begin a booking request. |
| **Actors** | Primary: Project Manager.<br>Secondary: System (Collision & Shared Resource Guardrail Engine). |
| **Pre-Conditions** | - PM is authenticated and has booking permission.<br>- At least one "Available" slot exists in the calendar. |
| **Post-Conditions** | - Slot, project, and squad details are captured in a draft (unsubmitted) request.<br>- PM proceeds to Wizard Step 2 (UC-03). |
| **Basic Flow** | 1. PM clicks "Book a Slot" from the calendar (UC-01).<br>2. PM selects their Project ID from a dropdown.<br>3. PM selects an available 2-hour time block.<br>4. PM assigns names to mandatory squad fields: PM, Dev/TL, QA, Shared DevOps, SRE.<br>5. System checks real-time availability of the selected Shared DevOps/SRE engineer for that window.<br>6. PM clicks "Next" to proceed to Step 2. |
| **Alternative Flows** | **AF-01:** Selected shared engineer (DevOps/SRE) is already committed to another project in that window → field displays "Unavailable" and blocks progression until an alternate is chosen.<br>**AF-02:** PM attempts to select a slot beyond the maximum of 2 bookable slots/day for their project → system blocks selection and prompts for admin approval routing.<br>**AF-03:** PM navigates away without completing Step 1 → draft is discarded (not persisted). |
| **Screen Annotations** | Step 1 of 3 wizard header with progress indicator. Form fields: Project ID (dropdown), Date & Slot picker (calendar widget), Squad Assignment fields (5 named-entry fields with role labels). Inline availability indicator next to Shared DevOps/SRE fields. |
| **Link/Button Annotations** | "Next" button → validates Step 1 fields and advances to Step 2; disabled until all mandatory fields are completed and shared resources show "Available." "Cancel" link → discards the draft and returns to the calendar. |
| **Business Rules** | **BR-01:** A project may book a maximum of 2 slots per day; exceptions require Release Manager/admin approval.<br>**BR-02:** A shared DevOps/SRE engineer already committed to any project during a given window must display as "Unavailable" to all other projects for that same window.<br>**BR-03:** Minimum slot booking duration is currently unconfirmed (30 minutes vs. 1 hour) — pending clarification (see Section 5.2). |

---

### UC-03: Complete PM Pre-Scheduling Checklist — Wizard Step 2

| Attribute | Details |
|---|---|
| **Use Case ID** | UC-03 |
| **Use Case Name** | Complete PM Pre-Scheduling Checklist — Wizard Step 2 |
| **Description** | Requires the PM to upload Release Notes and Deployment Steps documents, and confirm (via checkbox) that Handover to DevOps/SRE has taken place offline, before the request can be submitted. |
| **Actors** | Primary: Project Manager.<br>Secondary: System (Checklist Gatekeeper Engine). |
| **Pre-Conditions** | - Wizard Step 1 (UC-02) has been completed successfully. |
| **Post-Conditions** | - All 3 mandatory checklist items are complete.<br>- "Submit Request" action becomes available, allowing progression to Step 3 (UC-04). |
| **Basic Flow** | 1. PM uploads the Release Notes document (predefined template).<br>2. PM uploads the Deployment Steps document (predefined template for DevOps execution).<br>3. PM ticks the "Handover to DevOps/SRE Completed" checkbox, confirming the offline handover meeting has occurred.<br>4. System validates all 3 items are complete.<br>5. "Submit Request" button becomes enabled. |
| **Alternative Flows** | **AF-01:** PM attempts to proceed with one or more items incomplete → "Submit Request" remains disabled with inline validation messaging indicating missing items.<br>**AF-02:** PM uploads a file in an unsupported format/size → system rejects the upload with an error message and prompts re-upload. |
| **Screen Annotations** | Step 2 of 3 wizard header. Two file-upload widgets (Release Notes, Deployment Steps) each showing filename and upload status once complete. One checkbox item: "Handover to DevOps/SRE Completed" with helper text describing the offline meeting requirement. |
| **Link/Button Annotations** | "Upload" buttons per document field → opens file picker. "Back" button → returns to Step 1 retaining entered data. "Submit Request" button → disabled until all 3 checklist items are complete; once enabled, advances to Step 3 (UC-04). |
| **Business Rules** | **BR-01:** Exactly 3 mandatory checklist items must be completed: Release Notes upload, Deployment Steps upload, and Handover-to-DevOps checkbox confirmation.<br>**BR-02:** "Submit Request" must remain disabled until all 3 items are satisfied — no partial submission is permitted.<br>**BR-03:** The Handover-to-DevOps meeting itself occurs offline and is not tracked by the system beyond the checkbox confirmation. |

---

### UC-04: Submit Request & Auto-Conflict Validation — Wizard Step 3

| Attribute | Details |
|---|---|
| **Use Case ID** | UC-04 |
| **Use Case Name** | Submit Request & Auto-Conflict Validation — Wizard Step 3 |
| **Description** | Final validation step where the system re-checks slot and shared-resource availability at the point of submission and, if clear, locks the schedule and routes the request into the QA Signoff queue. |
| **Actors** | Primary: Project Manager.<br>Secondary: System (Collision Detection & Workflow Routing Engine). |
| **Pre-Conditions** | - Wizard Steps 1 and 2 (UC-02, UC-03) are complete. |
| **Post-Conditions** | - On success: slot and shared resources are locked; request status is set to "Pending QA Approval."<br>- On failure: transaction is aborted and rolled back; no partial data is persisted. |
| **Basic Flow** | 1. PM clicks "Submit Request" at the end of Step 2.<br>2. System re-validates slot availability and shared-resource availability at the moment of submission.<br>3. If no conflict exists, system locks the slot and shared-resource assignments.<br>4. System sets request status to "Pending QA Approval" and routes it to the QA Signoff queue (UC-05, Stage 1).<br>5. System displays a confirmation screen to the PM with the request reference. |
| **Alternative Flows** | **AF-01:** A concurrent write request for the same slot/environment target is detected → transaction aborts and rolls back; PM is shown an error and returned to Step 1 to re-select a slot.<br>**AF-02:** Shared resource becomes unavailable between Step 1 selection and final submission (race condition) → transaction aborts and rolls back with an explanatory message. |
| **Screen Annotations** | Step 3 of 3 wizard header showing a summary review of all entered details (Project ID, slot, squad, uploaded documents, checklist status). Confirmation screen post-submission shows request reference number and current status ("Pending QA Approval"). |
| **Link/Button Annotations** | "Submit Request" button → triggers final validation and routing; disabled during processing to prevent duplicate submission. "Back" button → returns to Step 2 for corrections (only available before submission completes). |
| **Business Rules** | **BR-01:** The booking logic must enforce absolute mathematical isolation on time blocks — any overlap during a concurrent write must abort and roll back the transaction.<br>**BR-02:** A successfully submitted request must route directly to "Pending QA Approval" (Stage 1) with no possibility of skipping stages. |

---

### UC-05: 5-Stage Sequential Approval Workflow

| Attribute | Details |
|---|---|
| **Use Case ID** | UC-05 |
| **Use Case Name** | 5-Stage Sequential Approval Workflow |
| **Description** | Routes a submitted request through five sequential sign-off stages — QA, Engineering Manager, Product/Business, DevOps/SRE, and Release Manager — with strict order enforcement, culminating in "Approved & Scheduled" status. |
| **Actors** | Primary: QA Manager, Engineering Manager, Product Owner, Shared DevOps/SRE representative, Release Manager.<br>Secondary: System (Workflow State Machine). |
| **Pre-Conditions** | - Request has been successfully submitted (UC-04) and is in "Pending QA Approval" status. |
| **Post-Conditions** | - Request reaches "Approved & Scheduled" status and becomes read-only.<br>- Automated stakeholder confirmation notification is triggered (UC-09). |
| **Basic Flow** | 1. QA Manager reviews test logs and clicks "Approve" → status moves to "Pending EM Approval."<br>2. Engineering Manager reviews code metrics and clicks "Approve" → status moves to "Pending Product Approval."<br>3. Product Owner checks business readiness and clicks "Approve" → status moves to "Pending DevOps/SRE Approval."<br>4. DevOps/SRE representative verifies runbook/environment metrics and clicks "Approve" → status moves to "Pending Release Manager Approval."<br>5. Release Manager reviews global environment sanity and clicks "Approve" → status transitions to "Approved & Scheduled" (final state). |
| **Alternative Flows** | **AF-01:** Any approver clicks "Reject" at their stage → routes to UC-06 (Reject/Cancel Release Request).<br>**AF-02:** An approval action is attempted out of sequence (e.g., EM attempts to approve before QA) → system rejects the update and returns an order-violation error.<br>**AF-03:** Designated approver is unavailable → Release Manager manually coordinates via email/offline channels and holds override authority to progress or close the request. |
| **Screen Annotations** | Approval Queue screen per role, listing pending requests assigned to that stage with Project ID, slot, and squad summary. Request Detail screen shows full checklist documents, squad assignment, and current stage in a visual 5-step progress tracker. |
| **Link/Button Annotations** | "Approve" button → advances the request to the next sequential stage. "Reject" button → routes to the Release Manager cancellation flow (UC-06). "View Documents" link → opens uploaded Release Notes/Deployment Steps for review. |
| **Business Rules** | **BR-01:** The backend must reject an approval update if the preceding sign-off in the 5-stage sequence is missing or out of order.<br>**BR-02:** Once a request reaches "Approved & Scheduled," all fields become strictly read-only.<br>**BR-03:** No formal backup/delegate-approver mechanism exists in MVP; the Release Manager holds ultimate override authority to resolve stuck approvals.<br>**BR-04:** Individual confirmation from every squad member is not required post-approval; accountability for final readiness rests with the Release Manager. |

---

### UC-06: Reject / Cancel Release Request (Release Manager)

| Attribute | Details |
|---|---|
| **Use Case ID** | UC-06 |
| **Use Case Name** | Reject / Cancel Release Request (Release Manager) |
| **Description** | When any approver rejects a request at their stage, the Release Manager reviews the rejection and performs the cancellation, deleting the entry, freeing the slot, and capturing a mandatory reason. |
| **Actors** | Primary: Release Manager.<br>Secondary: QA Manager, Engineering Manager, Product Owner, DevOps/SRE (as rejection initiators); System. |
| **Pre-Conditions** | - A request exists in any "Pending [Stage] Approval" status.<br>- An approver has clicked "Reject" at their stage. |
| **Post-Conditions** | - Request entry is deleted from the active pipeline.<br>- The associated slot and shared resources are freed and return to the open bookable pool. |
| **Basic Flow** | 1. An approver (QA/EM/Product/DevOps-SRE) clicks "Reject" at their respective stage, entering a reason/comment.<br>2. Release Manager is notified of the rejection.<br>3. Release Manager reviews the rejection reason and any team input.<br>4. Release Manager clicks "Cancel Release," entering/confirming a mandatory reason.<br>5. System deletes the request entry and frees the slot and shared-resource commitments. |
| **Alternative Flows** | **AF-01:** Release Manager determines the rejection was raised in error and coordinates offline with the rejecting approver to have them re-approve instead of cancelling (manual, outside system flow).<br>**AF-02:** Multiple stages report conflicting readiness signals (e.g., one team says available, another says not) → Release Manager manually resolves via offline coordination before deciding whether to cancel. |
| **Screen Annotations** | Rejection Review screen showing the rejecting stage, rejection reason/comment, and full request detail. "Cancel Release" confirmation modal requiring a mandatory reason field before final deletion. |
| **Link/Button Annotations** | "Reject" button (approver-facing) → prompts mandatory reason entry, then routes to Release Manager. "Cancel Release" button (Release Manager-facing) → opens confirmation modal; on confirmation, permanently deletes the request and frees the slot. |
| **Business Rules** | **BR-01:** A rejection at any stage does not auto-delete the request; only the Release Manager can perform the "Cancel Release" action that deletes it.<br>**BR-02:** A reason/comment is mandatory when rejecting or cancelling a request.<br>**BR-03:** Cancelling a request immediately frees the associated slot and shared-resource commitments back into the open pool. |

---

### UC-07: Self-Cancel Booked Slot (PM/Team)

| Attribute | Details |
|---|---|
| **Use Case ID** | UC-07 |
| **Use Case Name** | Self-Cancel Booked Slot (PM/Team) |
| **Description** | Allows the PM/team that booked a slot to voluntarily cancel their own request prior to full approval, with a mandatory reason. |
| **Actors** | Primary: Project Manager.<br>Secondary: System. |
| **Pre-Conditions** | - Request exists in any "Pending [Stage] Approval" status (not yet "Approved & Scheduled"). |
| **Post-Conditions** | - Request is cancelled and removed from the approval pipeline.<br>- Slot and shared resources are freed back to the open pool. |
| **Basic Flow** | 1. PM navigates to "My Bookings" and selects the active request.<br>2. PM clicks "Cancel My Booking."<br>3. System prompts for a mandatory cancellation reason.<br>4. PM confirms cancellation.<br>5. System deletes the request and frees the slot/resources. |
| **Alternative Flows** | **AF-01:** PM attempts to cancel a request already in "Approved & Scheduled" (read-only) status → action is blocked; PM is directed to contact the Release Manager. |
| **Screen Annotations** | "My Bookings" list screen showing all requests raised by the PM with current status. Cancellation confirmation modal with a mandatory free-text reason field. |
| **Link/Button Annotations** | "Cancel My Booking" button → visible only on requests not yet in "Approved & Scheduled" status; opens confirmation modal requiring reason entry before finalising. |
| **Business Rules** | **BR-01:** Self-cancellation is only permitted prior to "Approved & Scheduled" status; once locked, only the Release Manager can act.<br>**BR-02:** A mandatory reason/comment must be captured for every self-cancellation. |

---

### UC-08: Admin Blackout Override Management

| Attribute | Details |
|---|---|
| **Use Case ID** | UC-08 |
| **Use Case Name** | Admin Blackout Override Management |
| **Description** | Allows the Release Manager (Global Admin) to lock and flag specific days, hour blocks, or entire weekends as "Unavailable" from an admin control panel, instantly blocking normal project scheduling. |
| **Actors** | Primary: Release Manager (Global Admin).<br>Secondary: System. |
| **Pre-Conditions** | - User holds Release Manager/Global Admin permission. |
| **Post-Conditions** | - Specified days/hours/weekends are flagged "Unavailable" across all project calendar views instantly. |
| **Basic Flow** | 1. Release Manager navigates to the Admin Control Panel.<br>2. Release Manager selects date(s), specific hour block(s), or recurring pattern (e.g., "No-Deploy Fridays").<br>3. Release Manager enters a reason/label (e.g., holiday, high-load window, corporate event).<br>4. Release Manager saves the blackout rule.<br>5. System instantly marks the affected slots "Unavailable" across all siloed project calendar views. |
| **Alternative Flows** | **AF-01:** Blackout is applied to a date/time already holding an approved booking → conflict is flagged for manual Release Manager resolution (handling approach to be confirmed — see Section 5.2 constraints). |
| **Screen Annotations** | Admin Control Panel with a date/time-range picker, recurrence pattern selector, and free-text reason/label field. List view of currently active blackout rules with edit/delete controls. |
| **Link/Button Annotations** | "Add Blackout Rule" button → opens the creation form. "Save" button → commits the rule and triggers instant propagation. "Delete" icon (per rule row) → removes an existing blackout, restoring normal bookability. |
| **Business Rules** | **BR-01:** Only the Release Manager/Global Admin role may create, edit, or delete blackout overrides.<br>**BR-02:** Blackout overrides must propagate instantly and identically across all siloed project calendar views. |

---

### UC-09: Automated Stakeholder Confirmation Notification

| Attribute | Details |
|---|---|
| **Use Case ID** | UC-09 |
| **Use Case Name** | Automated Stakeholder Confirmation Notification |
| **Description** | Upon final Stage 5 (Release Manager) approval, the system automatically triggers a confirmation email to all involved stakeholders serving as the official deployment pass. |
| **Actors** | Primary: System (Notification Engine).<br>Secondary: PM, TL, QA, Shared DevOps, SRE, Engineering Manager, Product Owner, Release Manager (as recipients). |
| **Pre-Conditions** | - Request has reached "Approved & Scheduled" status via UC-05. |
| **Post-Conditions** | - Confirmation email is dispatched to all stakeholders with complete execution details. |
| **Basic Flow** | 1. Release Manager approves at Stage 5.<br>2. System detects the transition to "Approved & Scheduled."<br>3. System compiles confirmed Date/Time (IST), Project ID, Build Version, Triage Squad names, and links to Release Notes and SRE Handover runbook.<br>4. System dispatches the confirmation email to all stakeholders (see Section 8 for recipient/template detail). |
| **Alternative Flows** | **AF-01:** Build Version field is not populated at the time of approval → system sends the notification with a placeholder/blank Build Version field (data-entry point for this field is unconfirmed — see Section 5.2).<br>**AF-02:** Email delivery fails → system logs the failure for Release Manager visibility (retry behaviour to be defined during technical design). |
| **Screen Annotations** | No dedicated screen; confirmation banner shown to the Release Manager immediately after approval indicating "Confirmation notification sent." Request Detail screen shows a notification log entry. |
| **Link/Button Annotations** | Not applicable (system-triggered, no user-initiated button for this use case). |
| **Business Rules** | **BR-01:** The confirmation notification must be triggered automatically and immediately upon final Stage 5 approval — no manual send action is required.<br>**BR-02:** The notification must include, at minimum: confirmed Date/Time (IST), Project ID, Build Version, Triage Squad names, and links to Release Notes and SRE Handover runbook. |

---

## 7. Non-Functional Requirement

- **Availability:** The system should target high availability during India business hours at minimum; exact uptime SLA to be confirmed (currently unconfirmed — see Discovery Gaps).
- **Performance:** Calendar and approval-queue screens should load within acceptable enterprise-grade response times under expected concurrent user load (concurrency targets unconfirmed).
- **Concurrency Integrity:** The system must enforce atomic, transactional slot-booking to guarantee no two projects can ever successfully book the same window, even under simultaneous submission.
- **Security:** All user credentials (email/password) must be securely stored (hashed) and transmitted over encrypted channels (HTTPS/TLS).
- **Auditability:** All approval actions, rejections, and cancellations should be logged with timestamp and actor identity, even though a formal audit-trail requirement has not yet been explicitly confirmed by the stakeholder.
- **Scalability:** The system should be architected to scale across 200+ technical users and a growing number of project silos without redesign.
- **Compatibility:** The application must be usable across both web and mobile form factors.
- **Data Retention:** Retention policy for cancelled/deleted requests and uploaded documents is currently unconfirmed and should be defined during technical design.
- **Extensibility:** The role/permission model and notification framework should be designed to accommodate Phase 2 features (SSO, Slack/Teams webhooks, AI document validation, analytics dashboard) without major rework.

---

## 8. Notifications Reference

| # | Trigger Event | Channel | Recipient | Template (Message Text) |
|---|---|---|---|---|
| 1 | User requests a password reset ("Forgot Password") | Email | Requesting User | "Subject: Reset Your RMP Password. Body: We received a request to reset your password. Click the secure link below to set a new password: [Reset Link]. If you did not request this, please ignore this email." |
| 2 | Account temporarily locked after repeated failed login attempts | Email | Affected User | "Subject: RMP Account Temporarily Locked. Body: Your account has been temporarily locked due to multiple failed login attempts. Please try again after [Lockout Duration] or reset your password." |
| 3 | Request submitted and routed to QA (Stage 1) | In-App/Push | PM (confirmation), QA Manager (action required) | "Your release request for [Project ID] on [Date/Slot] has been submitted and is now Pending QA Approval." |
| 4 | QA approves (Stage 1 → 2) | Email | Engineering Manager | "Subject: Action Required — Release [Project ID] Pending Your Approval. Body: QA has signed off on the release scheduled for [Date/Slot]. Please review and approve/reject in RMP." |
| 5 | EM approves (Stage 2 → 3) | Email | Product Owner | "Subject: Action Required — Release [Project ID] Pending Product Approval. Body: Engineering has signed off on the release scheduled for [Date/Slot]. Please review business readiness and approve/reject in RMP." |
| 6 | Product Owner approves (Stage 3 → 4) | Email | Shared DevOps/SRE Representative | "Subject: Action Required — Release [Project ID] Pending DevOps/SRE Approval. Body: Product/Business has signed off on the release scheduled for [Date/Slot]. Please verify runbook and environment readiness in RMP." |
| 7 | DevOps/SRE approves (Stage 4 → 5) | Email | Release Manager | "Subject: Final Approval Required — Release [Project ID]. Body: DevOps/SRE has signed off on the release scheduled for [Date/Slot]. Your final approval is required to confirm scheduling." |
| 8 | Release Manager gives final approval (Stage 5 → Approved & Scheduled) | Email | All stakeholders: PM, TL, QA, Shared DevOps, SRE, EM, Product Owner, Release Manager | "Subject: Deployment Confirmed — [Project ID] \| [Date] [Time Slot IST]. Body: This release has been fully approved and scheduled. Date/Time: [Date, Time Slot IST]. Project ID: [Project ID]. Build Version: [Build Version]. Squad: PM [Name], TL [Name], QA [Name], DevOps [Name], SRE [Name]. Release Notes: [Link]. SRE Handover Runbook: [Link]. This email serves as the official deployment pass." |
| 9 | Approver rejects the request at any stage | Email | Release Manager, PM | "Subject: Release [Project ID] Rejected at [Stage Name]. Body: The release scheduled for [Date/Slot] has been rejected at the [Stage Name] stage. Reason: [Rejection Reason]. Release Manager review required." |
| 10 | Release Manager cancels/deletes the request | In-App/Push | PM, full squad (PM, TL, QA, DevOps, SRE) | "The release request for [Project ID] scheduled on [Date/Slot] has been cancelled by the Release Manager. Reason: [Cancellation Reason]. The slot is now available for rebooking." |
| 11 | PM self-cancels their own booking | In-App/Push | Full squad (PM, TL, QA, DevOps, SRE), any approvers who had already signed off | "[PM Name] has cancelled the release booking for [Project ID] on [Date/Slot]. Reason: [Cancellation Reason]." |
| 12 | Admin applies a new blackout override affecting an existing booking | Email | Release Manager, affected PM | "Subject: Blackout Conflict — [Project ID] Booking on [Date/Slot]. Body: A new admin blackout has been applied to a period overlapping your approved/pending release. Manual review is required." |
| 13 | Approval pending beyond expected time (future SLA/escalation feature — not yet confirmed for MVP) | Email / WhatsApp (channel TBD) | Pending Approver, Release Manager | "Reminder: Release [Project ID] has been Pending [Stage Name] Approval for [X hours/days]. Please action in RMP." — *Template placeholder pending SLA confirmation (see Section 5.2 Constraints).* |

*Note: SMS and WhatsApp channels are not currently confirmed requirements per discovery to date; Row 11 is included as a placeholder pending SLA/escalation scope confirmation, and should be validated with the client stakeholder before build.*

---

## 9. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | 10 July 2026 | Business Analyst | Initial draft FSD compiled from PRD, discovery call transcript, BA clarification query log, requirement classification matrix, and risk register. Pending resolution of open discovery gaps (business hours contradiction, shared resource pool structure, NFR confirmation) before formal sign-off. |
| 1.1 | 10 July 2026 | Business Analyst | Added UC-00 (User Login) covering email/password authentication with no self-service sign-up, including "Forgot Password" and account-lockout alternative flows. Updated In Scope (Section 2.1), UC-01 pre-conditions, and Notifications Reference (Section 8) accordingly. |

---

*Confidential — Internal Use Only | Release Management Portal (RMP)*
