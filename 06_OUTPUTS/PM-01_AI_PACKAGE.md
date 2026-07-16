
==================================================

PROJECT NAME:
PMOS AI Framework

CURRENT PHASE:
Initiation

CURRENT ACTIVITY:
PM-01

ASSIGNED AGENT:
Planning Agent

==================================================

TEMPLATE DETAILS:

{'folder': 'PM-01_PROJECT_CHARTER', 'template': 'PROJECT_CHARTER_TEMPLATE.docx'}

==================================================

PROMPT:

# PM-01 : Project Charter Drafting

## Objective

Create the project charter.

## Inputs

- SOW
- BRD
- Client discussions

## Templates

- Project Charter Template

## AI Instructions

1. Review all available documents.
2. Identify stakeholders.
3. Capture milestones.
4. Generate the charter.

## Expected Output

- Project Charter document

==================================================

AVAILABLE DOCUMENTS:

- BRD.md
- FSD.md
- Meeting_Transcript.md
- SOW.pdf
- Sprint_Plan.xlsx
- PM_AI_Assistant_SOP_v1.0.pdf
- BRD.pdf
- Release Management Portal (RMP)_FSD.md
- Release Slot Booking Manager - Client Meeting - Transcript.md
- Action Trakcer.xlsx
- DEPENDECNY Tracker Template.xlsx
- MOM Template.docx
- Project Plan Template.xlsx
- Risk Register Template.xlsx

==================================================

DOCUMENT CONTENT:



===== BRD.md =====

Business Requirement Document

Project Name: PMOS AI Framework

Business Objective:

Build an AI-powered project management operating system.

Scope:

- Project initiation
- Planning
- Sprint management
- RAID management
- Status reporting

Success Criteria:

- Reduce PM effort by 40%.
- Automate documentation.
- Improve delivery visibility.

===== FSD.md =====

Functional Specification Document

Modules:

1. Context Loader
2. Prompt Engine
3. Template Engine
4. Agent Factory
5. Document Reader

Technology Stack:

- Python
- VS Code
- GitHub

Expected Output:

- Project Charter
- RAID Register
- Sprint Plan
- Weekly Status Report

===== Meeting_Transcript.md =====

# Client Meeting Transcript

Date: 16-Jul-2026

Participants:

- Manish Singh
- Client PM
- Development Lead

Discussion:

- Project duration will be five months.
- Sprint duration will be two weeks.
- UAT will be milestone-wise.
- Weekly governance meeting every Monday.
- Phase 1 scope approved.
- Phase 2 stories under review.

Action Items:

- Client to provide API details.
- Team to prepare project charter.

===== SOW.pdf =====

Statement of Work 
 
Client: Demo Client 
 
Duration: 
 
- Development: 5 months 
- UAT: 2 weeks 
- Hypercare: 2 weeks 
 
Deliverables: 
 
- Project Charter 
- RAID Register 
- Sprint Plan 
- Status Reports 
 
Governance: 
 
- Weekly review 
- Monthly steering committee 


===== Sprint_Plan.xlsx =====


--- SHEET: Sheet1 ---
('Sprint', 'Start Date', 'End Date', 'Stories')
('Sprint 1', datetime.datetime(2026, 7, 13, 0, 0), datetime.datetime(2026, 7, 24, 0, 0), 20)
('Sprint 2', datetime.datetime(2026, 7, 27, 0, 0), datetime.datetime(2026, 8, 7, 0, 0), 18)
('Sprint 3', datetime.datetime(2026, 8, 10, 0, 0), datetime.datetime(2026, 8, 21, 0, 0), 22)


===== PM_SOP\PM_AI_Assistant_SOP_v1.0.pdf =====

PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
        
STANDARD  OPERATING  PROCEDURE 
Project  Manager  AI  Assistant  Guide AI-Driven  PM  Workflow   |   51  Activities   |   Scrum,  Waterfall  &  Hybrid    Includes  Claude  Cowork  Automation  Commands   |   Powered  by  Claude  &  Copilot ---------------------------------------------------------------------- Version  1.0   |   Project  Management  Department  
Kellton   |   For  Internal  Use  Only   |   Confidential 
 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  1  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
HOW  TO  USE  THIS  GUIDE This  SOP  covers  51  PM  activities  (PM-01  to  PM-51)  across  5  SDLC  phases  +  Tools.  Every  prompt  follows  the  Template-First  approach  and  is  tagged  with  its  delivery  methodology:    [  BOTH  ]   Works  for  Scrum,  Waterfall,  and  Hybrid  delivery    [  SCRUM  ]   Specific  to  Scrum  /  Agile  ceremonies  and  workflows    [  WATERFALL  ]   Specific  to  Waterfall  phase-gate  delivery    [  COWORK  ]   Claude  Cowork  agent  command  --  paste  into  Claude  Cowork,  NOT  regular  Claude  chat   1.   Find  your  activity  by  SOP  ID  (PM-01  to  PM-51),  phase,  or  methodology  tag.  2.   For  every  prompt:  upload  your  template  FIRST  (Kellton  Standard  >  Client  >  PM  Custom).  3.   If  no  template  --  AI  generates  using  standard  industry  structure  and  flags  it  for  mapping.  4.   Fill  all  [PLACEHOLDERS]  in  the  prompt  before  running.  5.   For  COWORK  commands:  paste  into  Claude  Cowork  desktop  agent,  not  Claude  chat.  6.   Review  every  AI  output  before  sharing.  Save  artifact  +  update  PM  AI  SOP  Tracker.  
 
1.   Template-First  Approach  &  Priority  Order  
Every  PM  activity  in  this  SOP  follows  the  Template-First  approach.  Upload  your  template  before  running  any  
prompt.
 
AI
 
reads
 
the
 
template,
 
confirms
 
its
 
structure,
 
asks
 
clarifying
 
questions,
 
then
 
fills
 
it
 
with
 
your
 
project
 
data.
 
If
 
no
 
template
 
is
 
available,
 
AI
 
uses
 
a
 
standard
 
industry
 
structure.
 
Priority Template  Type When  to  Use Status 
1 
Kellton  Standard 
Default  for  all  projects.  Use  unless  client  or  contract  specifies  otherwise.  
MANDATORY
 
2 Client-Specific 
Client  provides  their  own  format.  Takes  priority  over  Kellton  Standard  once  received.  
MANDATORY
 
3 PM  Custom 
Neither  Kellton  nor  client  template  available.  Temporary  use  only  --  notify  PM  Lead.  
TEMP  ONLY
 
4 No  Template 
No  template  available  at  all.  AI  generates  using  standard  industry  structure.  
FALLBACK
 
 
[NOTE]   When  a  client  provides  their  template  mid-project,  update  all  previously  submitted  documents  to  the  client  format  on  the  next  delivery  cycle.  Inform  PM  Lead  and  update  the  Templates  folder. 
 
The  4-Step  Template-First  Conversation  Pattern  
[TEMPLATE-FIRST]   This  pattern  is  mandatory  for  every  document  generation  session  in  this  SOP. 
 Step 
Action What  to  Say  /  Do 
1 Upload 
Upload  your  template  (Kellton  >  Client  >  PM  Custom).  Say:  "I  am  uploading  our  [document]  template.  Read  it,  list  every  section  heading,  and  confirm  the  structure  before  generating  anything."  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  2  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
Step 
Action What  to  Say  /  Do 
2 AI  Confirms 
AI  lists  every  section  it  sees.  Verify  it  matches  your  template.  Point  out  any  discrepancies  before  proceeding.  
3 AI  Questions 
Say:  "Ask  me  all  the  questions  you  need  to  fill  this  template  accurately.  Number  them.  Wait  for  my  answers  before  generating  any  content."  
4 AI  Fills 
Say:  "Fill  the  template  section  by  section  using  only  what  I  have  provided.  For  any  section  you  cannot  complete,  write  [NEEDS  INPUT  --  reason]  instead  of  guessing."  
 
[IMPORTANT]   NO  TEMPLATE?  Tell  AI:  "I  do  not  have  a  template.  Generate  the  [document]  using  standard  industry  best-practice  structure.  Add  this  note  at  the  top:  [ACTION  REQUIRED:  Map  this  output  to  the  Kellton  standard  template  before  sharing  with  any  stakeholder.]" 
  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  3  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
2.   Table  of  Contents  --  All  51  Activities  (PM-01  to  PM-51)  
PM-01  to  PM-30:  Core  SOP  Tracker  activities.  PM-31  to  PM-51:  New  from  Prompt  Library.  Use  Ctrl+F  and  search  any  
SOP
 
ID
 
to
 
jump
 
directly
 
to
 
its
 
prompt.
 
SOP  ID 
Phase Activity Method Section Source 
PM-01 
Initiation
 Project  Charter  Drafting  BOTH
 Sec  3.1
 Tracker
 
PM-02 
Initiation
 Stakeholder  Identification  &  RACI  BOTH
 Sec  3.2
 Tracker
 
PM-03 
Initiation
 Business  Case  Summary  BOTH
 Sec  3.3
 Tracker
 
PM-04 
Initiation
 Kick-off  Meeting  Preparation  BOTH
 Sec  3.4
 Tracker
 
PM-05 
Planning
 
Requirement  Summary  &  Traceability  (RTM)  
BOTH
 Sec  4.1
 Tracker
 
PM-06 
Planning
 WBS  /  Milestone  Planning  BOTH
 Sec  4.2
 Tracker
 
PM-07 
Planning
 RAID  Log  Initialization  BOTH
 Sec  4.3
 Tracker
 
PM-08 
Planning
 Resource  Plan  &  Skill  Matrix  BOTH
 Sec  4.4
 Tracker
 
PM-09 
Planning
 Communication  Plan  BOTH
 Sec  4.5
 Tracker
 
PM-10 
Planning
 Project  Schedule  Baseline  BOTH
 Sec  4.6
 Tracker
 
PM-11 
Execution
 Sprint  Planning  SCRUM
 Sec  5.1
 Tracker
 
PM-12 
Execution
 MOM  Generation  BOTH
 Sec  5.2
 Tracker
 
PM-13 
Execution
 Client  Communication  Drafting  BOTH
 Sec  5.3
 Tracker
 
PM-14 
Execution
 Change  Request  Analysis  BOTH
 Sec  5.4
 Tracker
 
PM-15 
Execution
 Escalation  Drafting  BOTH
 Sec  5.5
 Tracker
 
PM-16 
Execution
 Action  Item  Tracking  BOTH
 Sec  5.6
 Tracker
 
PM-17 
Execution
 Defect  Triage  Summarization  BOTH
 Sec  5.7
 Tracker
 
PM-18 
Monitoring
 Weekly  Status  Report  (WSR)  BOTH
 Sec  6.1
 Tracker
 
PM-19 
Monitoring
 RAID  Management  (Weekly  Update)  BOTH
 Sec  6.2
 Tracker
 
PM-20 
Monitoring
 Executive  Dashboard  /  KPI  Summary  BOTH
 Sec  6.3
 Tracker
 
PM-21 
Monitoring
 Timeline  Impact  Analysis  BOTH
 Sec  6.4
 Tracker
 
PM-22 
Monitoring
 Budget  Tracking  &  Variance  Analysis  BOTH
 Sec  6.5
 Tracker
 
PM-23 
Monitoring
 Dependency  Tracking  BOTH
 Sec  6.6
 Tracker
 
PM-24 
Monitoring
 UAT  Tracking  &  Defect  Theme  Summary  BOTH
 Sec  6.7
 Tracker
 
PM-25 
Monitoring
 Stakeholder  Engagement  Pulse  BOTH
 Sec  6.8
 Tracker
 
PM-26 
Closure
 Delivery  Readiness  Review  BOTH
 Sec  7.1
 Tracker
 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  4  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
SOP  ID 
Phase Activity Method Section Source 
PM-27 
Closure
 Closure  Documentation  BOTH
 Sec  7.2
 Tracker
 
PM-28 
Closure
 Lessons  Learned  Workshop  BOTH
 Sec  7.3
 Tracker
 
PM-29 
Closure
 Knowledge  Base  Article  BOTH
 Sec  7.4
 Tracker
 
PM-30 
Closure
 Post-Implementation  Review  (PIR)  BOTH
 Sec  7.5
 Tracker
 
PM-31 
Planning
 Full  Project  Initialisation  --  Starter  Pack BOTH
 Sec  4.7
 Prompt  Lib
 
PM-32 
Planning
 RACI  Matrix  Generator  (Detailed) BOTH
 Sec  4.8
 Prompt  Lib
 
PM-33 
Execution
 Daily  Standup  Digest  &  DSR SCRUM
 Sec  5.8
 Prompt  Lib
 
PM-34 
Execution
 Sprint  Review  Summary SCRUM
 Sec  5.9
 Prompt  Lib
 
PM-35 
Execution
 Retrospective  Facilitation SCRUM
 Sec  5.10
 Prompt  Lib
 
PM-36 
Execution
 Waterfall  Phase  Gate  Checklist 
WATERFALL
 
Sec  5.11
 Prompt  Lib
 
PM-37 
Execution
 Delay  Notification  Email BOTH
 Sec  5.12
 Prompt  Lib
 
PM-38 
Execution
 Decision  Request  Email BOTH
 Sec  5.13
 Prompt  Lib
 
PM-39 
Execution
 Milestone  Achievement  Announcement BOTH
 Sec  5.14
 Prompt  Lib
 
PM-40 
Monitoring
 
SIT/UAT  Defect  Triage  --  Steering  Summary 
WATERFALL
 
Sec  6.9
 Prompt  Lib
 
PM-41 
Monitoring
 Monthly  Business  Review  (MBR) BOTH
 Sec  6.10
 Prompt  Lib
 
PM-42 
Monitoring
 RAID  Update  from  Weekly  Notes BOTH
 Sec  6.11
 Prompt  Lib
 
PM-43 
Monitoring
 Risk  Escalation  Email BOTH
 Sec  6.12
 Prompt  Lib
 
PM-44 
Monitoring
 Weekly  Risk  Review BOTH
 Sec  6.13
 Prompt  Lib
 
PM-45 
Monitoring
 Issue  Log  Entry  &  Resolution  Plan BOTH
 Sec  6.14
 Prompt  Lib
 
PM-46 
Closure
 Go-Live  Cutover  Checklist  &  Run  Book BOTH
 Sec  7.6
 Prompt  Lib
 
PM-47 
Closure
 Project  Closure  Report  (Formal) BOTH
 Sec  7.7
 Prompt  Lib
 
PM-48 
Tools  &  
Automation
 
Excel  Agent  --  RAID  Tracker  (Cowork) COWORK
 Sec  8.1
 Prompt  Lib
 
PM-49 
Tools  &  
Automation
 
PowerPoint  Agent  --  WSR/MBR  Deck  (Cowork) 
COWORK
 Sec  8.2
 Prompt  Lib
 
PM-50 
Tools  &  
Automation
 
Chrome  Agent  --  Jira/Azure  DevOps  Sync  (Cowork) 
COWORK
 Sec  8.3
 Prompt  Lib
 
PM-51 
Tools  &  
Automation
 
File  Management  --  SharePoint  Organisation  (Cowork) 
COWORK
 Sec  8.4
 Prompt  Lib
 
 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  5  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
[TIP]   PM-01  to  PM-30  (navy)  =  Core  SOP  Tracker  activities.  PM-31  to  PM-51  (purple)  =  New  from  Prompt  Library.  Scrum-only  and  Waterfall-only  activities  are  clearly  tagged. 
  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  6  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
PHASE  1   --   Initiation Project  start-up  activities  --  establishing  the  foundation  before  execution  begins. PM-01  Charter   |   PM-02  Stakeholders   |   PM-03  Business  Case   |   PM-04  Kick-off
 
 
PM-01   |   Project  Charter  Drafting  
[TEMPLATE-FIRST]   Upload:  Project  Charter  Template  +  SoW/Contract.  Add  discovery  notes  if  available. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Project  Charter  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Project  Charter  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Project
 
Purpose
 
&
 
Background
 *  
Objectives
 
&
 
Success
 
Criteria
 
(SMART)
 *  
Scope
 
--
 
In
 
Scope
 
/
 
Out
 
of
 
Scope
 *  
Key
 
Stakeholders
 
&
 
Roles
 *  
High-Level
 
Timeline
 
&
 
Milestones
 *  
Budget
 
Overview
 *  
Assumptions
 
&
 
Constraints
 *  
Top
 
Risks
 
with
 
Mitigation
 *  
Sign-off
 
Block
  
AI  Prompt  
PM-01   Project  Charter  Drafting   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  template  uploaded:  Fill  the  uploaded  template  exactly,  section  by  section.    -  IF  no  template:  Generate  using  standard  industry  Project  Charter  structure.      Add  note:  [ACTION:  Map  to  Kellton  standard  template  before  sharing.]   Upload  the  following  before  running  this  prompt:    1.  Project  Charter  Template  (Kellton  /  Client  /  PM  Custom)    2.  Statement  of  Work  (SoW)  /  Contract  /  MSA  --  primary  source  for  scope  and  budget    3.  Discovery  call  notes  /  pre-sales  brief  (if  available)   After  reading  the  uploaded  files,  confirm:    -  Project  name  and  client  identified    -  Key  deliverables  listed  in  the  SoW    -  Contractual  timeline  and  milestones  found    -  Budget  or  engagement  value  identified    -  Any  ambiguities  in  the  SoW  that  need  PM  clarification   PROJECT  CONTEXT:    -  Project  Sponsor:  [SPONSOR_NAME]  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  7  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
  -  Delivery  Model:  [Agile  /  Waterfall  /  Hybrid]    -  PM  Name:  [YOUR  NAME]    -  Scope  agreed  verbally  but  not  in  SoW:  [Describe  or  write  "None"]   Fill  the  Charter  template  using  the  SoW  as  the  primary  source:    1.  Project  Purpose  &  Background  --  from  SoW  background  section    2.  Objectives  &  Success  Criteria  --  SMART  format  from  SoW  deliverables    3.  Scope  --  In  Scope  (from  SoW);  Out  of  Scope  (infer  and  flag  assumptions)    4.  Key  Stakeholders  &  Roles  --  from  SoW  signatories  and  named  contacts    5.  High-Level  Timeline  &  Milestones  --  from  SoW  schedule  or  payment  milestones    6.  Budget  Overview  --  from  SoW  commercial  terms    7.  Key  Assumptions  &  Constraints  --  SoW  conditions,  limitations,  dependencies    8.  Top  3  Risks  with  Mitigation  --  based  on  SoW  complexity  and  delivery  model    9.  Sign-off  Block  --  PM  name,  sponsor  name,  date   Flag  missing  info  as  [NEEDS  INPUT  --  reason].  Do  not  invent  figures  not  in  uploaded  documents.  
 [EXAMPLE  OUTPUT]   Project  Charter  --  Objectives  Section 
Objectives  &  Success  Criteria OBJ-01:  Reduce  customer  onboarding  time  from  5  days  to  <24  hours  by  Q3  2025.         Success  Metric:  TAT  via  system  timestamp.  Target:  100%  within  24  hrs. OBJ-02:  Achieve  95%  CSAT  score  on  new  onboarding  flow  within  60  days  of  go-live.         Success  Metric:  Post-onboarding  survey.  Target:  >=95%. OBJ-03:  Zero  critical  defects  at  production  go-live.         Target:  0  Critical,  <3  High  at  go-live  sign-off.  [NEEDS  INPUT  --  Section  5  (Timeline)  requires  confirmed  milestone  dates  from  sponsor] 
 Role Who Responsibilities 
R  --  Responsible 
Project  Manager  Runs  AI  prompt,  reviews  output,  fills  gaps,  maps  to  template.  
A  --  Accountable 
Project  Sponsor  /  PM  Lead  
Reviews  and  approves  before  sharing  with  any  stakeholder.  
C  --  Consulted 
BA  /  Solution  Architect  Validates  scope  accuracy  and  technical  assumptions.  
I  --  Informed 
All  Stakeholders  Receive  approved  charter  as  project  baseline.  
 
PM-02   |   Stakeholder  Identification  &  RACI  Matrix  
[TEMPLATE-FIRST]   Upload:  Stakeholder  Register  template  +  any  org  chart  or  contacts  list. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Stakeholder  Register  &  RACI  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  8  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Stakeholder  Register  &  RACI  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Stakeholder
 
Name
 
and
 
Role
 *  
Department
 
/
 
Organisation
 *  
Interest
 
Level
 
(H/M/L)
 *  
Influence
 
Level
 
(H/M/L)
 *  
Engagement
 
Strategy
 *  
RACI
 
assignments
 
per
 
key
 
PM
 
activity
  
AI  Prompt  
PM-02   Stakeholder  Identification  &  RACI  Matrix   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  template  uploaded:  Fill  the  uploaded  Stakeholder  Register  and  RACI  template  exactly.    -  IF  no  template:  Use  standard  Stakeholder  Register  +  RACI  Matrix  industry  format.      Add  note:  [ACTION:  Map  to  Kellton  standard  template  before  sharing.]   PROJECT  DESCRIPTION:  [Paste  project  summary  or  charter  scope]  KNOWN  TEAM  /  STAKEHOLDERS:  [List  names  and  roles  you  already  know]   PM  ACTIVITIES  FOR  RACI:    Charter  Sign-off  |  Requirement  Sign-off  |  Sprint  Reviews  |  Status  Reporting    Change  Requests  |  UAT  Sign-off  |  Go-Live  Approval  |  Project  Closure   Flag  anyone  with  High  Interest  but  Low  Influence  --  dedicated  communication  strategy  needed.  Mark  all  gaps  as  [NEEDS  INPUT].  
 
PM-03   |   Business  Case  Summary  
[NOTE]   No  standard  Kellton  template.  AI  generates  structured  summary  using  industry  standard. 
AI  Prompt  
PM-03   Business  Case  Summary   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  template  uploaded:  Fill  it  exactly  from  the  feasibility  document.    -  IF  no  template:  Generate  using  standard  Business  Case  Summary  structure.      Add  note:  [ACTION:  Map  to  client-required  format  before  submission.]   SOURCE  DOCUMENT:  [Upload  feasibility  document  /  business  case  inputs]   Generate  a  Business  Case  Summary  with:  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  9  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
  1.  Problem  Statement  (2-3  sentences)    2.  Proposed  Solution  (brief  description)    3.  Key  Benefits  (quantified  --  cost  saving,  revenue,  efficiency)    4.  Investment  Required  (budget  range  +  resource  summary)    5.  Risk  if  Not  Done  (consequence  of  inaction)    6.  Recommended  Decision  (Proceed  /  Defer  /  Reject)  with  brief  rationale   Keep  to  1  page  maximum.  Plain  business  language.  No  jargon.  
 
PM-04   |   Kick-off  Meeting  Preparation  
[TEMPLATE-FIRST]   Upload:  Project  Charter  +  SoW/RFP  +  Contract/PO/MSA.  AI  synthesises  all  three  into  an  executive-level  kick-off  deck  outline  with  speaker  notes. 
AI  Prompt  
PM-04   Kick-off  Meeting  Preparation  --  Automated  Deck  Generation   [  BOTH  ]
 
Role:  You  are  a  Senior  Project  Manager  and  PMO  Lead.   TEMPLATE  INSTRUCTION:    -  IF  a  kick-off  deck  template  is  uploaded:  Use  its  slide  structure  exactly.    -  IF  no  template:  Generate  slide-by-slide  outline  using  the  standard  structure  below.      Add  note:  [ACTION:  Build  deck  in  PowerPoint  using  Kellton  standard  branding.]   Upload  before  running:    1.  Project  Charter  (Vision,  Objectives,  RACI)    2.  Statement  of  Work  /  RFP  (Scope,  Process,  Technical  Specs)    3.  Contract  /  PO  /  MSA  (Commercials,  Milestones,  Legal  constraints)   Instructions:    Source  Mapping:  For  every  slide  cite  the  source  document  and  section.    Audience  Logic:  C-suite  (Vision/Commercials)  and  Technical  Leads  (Sprints/Logic).   Output  Structure:    Slide  1:  Title  &  Branding  --  Client  Name  and  Project  Title  from  RFP  header    Slide  2:  Vision  &  Need  Statement  --  Why  /  what  problem  are  we  solving?    Slide  3:  Functional  Scope  --  Core  modules,  complex  integrations    Slide  4:  Process  Transformation  --  As-Is  vs  To-Be  from  SoW    Slide  5:  Delivery  Roadmap  --  Convert  project  duration  into  sprint  intervals;              align  milestones  with  payment  terms    Slide  6:  Project  Governance  (RACI)  --  Accountability  vs  Responsibility    Slide  7:  Risks  &  Mitigation  --  Top  3  risks  mentioned  or  implied    Slide  8:  Commercials  &  AMC  --  Total  value,  payment  milestones,  Hypercare    Slide  9:  Q&A  &  Next  Steps  --  Immediate  actions   Constraints:    -  Do  NOT  invent  dates  or  figures.  Label  missing  info  [NEEDS  INPUT  -  FROM  SPONSOR].    -  Max  6  bullet  points  per  slide.   Deliverable:  Slide-by-slide  outline  with  Speaker  Notes.  
  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  10  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
PHASE  2   --   Planning Detailed  planning  --  scope,  schedule,  resources,  risks,  and  communication. PM-05  RTM   |   PM-06  WBS   |   PM-07  RAID  Init   |   PM-08  Resource  Plan   |   PM-09  Comm  Plan   |   PM-10  Schedule   |   PM-31  Full  Init  Pack   |   PM-32  RACI  Generator
 
 
PM-05   |   Requirement  Summary  &  Traceability  (RTM)  
[TEMPLATE-FIRST]   Upload  your  template  before  running  this  prompt.  If  none,  AI  uses  industry  standard  structure. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Requirement  Summary  &  Traceability  (RTM)  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Requirement  Summary  &  Traceability  (RTM)  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Requirement
 
ID
 *  
Requirement
 
Description
 *  
Type
 
(Functional
 
/
 
Non-Functional)
 *  
Priority
 
(MoSCoW)
 *  
Source
 
Document
 *  
User
 
Story
 
/
 
Jira
 
ID
 *  
Test
 
Case
 
Reference
 *  
Status
 *  
Sign-off
 
Owner
  
AI  Prompt  
PM-05   Requirement  Summary  &  Traceability  (RTM)   [  BOTH  ]
 
You  are  a  senior  Project  Manager  and  Business  Analyst.   TEMPLATE  INSTRUCTION:    -  IF  RTM  template  uploaded:  Fill  the  uploaded  template  exactly  from  the  PRD/BRD.    -  IF  no  template:  Generate  using  standard  RTM  industry  format.      Add  note:  [ACTION:  Map  to  Kellton  RTM  template  before  sharing.]   UPLOADED  DOCUMENT:  Read  the  uploaded  PRD  /  BRD  /  workshop  notes  before  starting.   PROJECT:  [PROJECT_NAME]   INSTRUCTIONS:  Step  1  --  Extract  all  requirements  from  the  uploaded  document.  Step  2  --  Build  requirements  list:    ID  |  Description  |  Type  (F/NF)  |  Priority  (MoSCoW)  |  Source  (page/section)  Step  3  --  Fill  the  RTM:    Req  ID  |  Requirement  |  User  Story  /  Jira  ID  |  Test  Case  Ref  |  Status  Step  4  --  Flag:  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  11  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
  -  Ambiguous  requirements:  [AMBIGUOUS  --  reason]    -  No  user  story:  [GAP  --  NEEDS  USER  STORY]    -  Unclear  source:  [ASSUMED  --  clarify  with  BA]   ASSUMPTION  RULE:  List  all  assumptions  at  the  end:    #  |  Assumption  Made  |  Section  Referenced  |  Action  Needed  
 
PM-06   |   WBS  /  Milestone  Planning  
[TEMPLATE-FIRST]   Upload  your  template  before  running  this  prompt.  If  none,  AI  uses  industry  standard  structure. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  WBS  /  Milestone  Planning  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  WBS  /  Milestone  Planning  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
WBS
 
ID
 *  
Task
 
Name
 *  
Owner
 
Role
 *  
Estimated
 
Duration
 *  
Dependencies
 *  
Milestone
 
|
 
Date
 
|
 
Acceptance
 
Criteria
  
AI  Prompt  
PM-06   WBS  /  Milestone  Planning   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  WBS/Project  Plan  template  uploaded:  Fill  it  exactly  from  the  PRD/BRD.    -  IF  no  template:  Generate  using  standard  WBS  Level-3  industry  format.      Add  note:  [ACTION:  Import  into  MS  Project  /  Jira  /  project  tracking  tool.]   UPLOADED  DOCUMENT:  Read  the  uploaded  PRD  /  BRD  before  starting.    Extract:  scope,  features,  modules,  components,  phases,  milestones.   PROJECT:  [PROJECT_NAME]  Delivery  Model:  [Agile  /  Waterfall]   |   Duration:  [X  months]  Team:  [Roles  --  Dev,  QA,  BA,  UX,  DevOps  etc.]   Step  1  --  List  every  feature,  module,  deliverable  identified  from  the  document.  Step  2  --  Generate  WBS  to  Level  3:    Phase  >  Deliverable  >  Task    WBS  ID  |  Task  Name  |  Owner  Role  |  Est.  Duration  |  Dependencies  Step  3  --  Milestone  Plan:    Milestone  |  Description  |  Target  Date  |  Dependencies  |  Acceptance  Criteria  Step  4  --  Critical  Path:  List  3-5  critical  tasks  and  explain  why.  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  12  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
 ASSUMPTION  RULE:  Tag  inferred  scope  items  [ASSUMED  --  verify  with  PO].  Flag  unestimable  areas:  [NEEDS  ESTIMATE  --  reason].  
 
PM-07   |   RAID  Log  Initialization  
[TEMPLATE-FIRST]   Upload  your  template  before  running  this  prompt.  If  none,  AI  uses  industry  standard  structure. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  RAID  Log  Initialization  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  RAID  Log  Initialization  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Risks:
 
ID
 
|
 
Description
 
|
 
Prob
 
|
 
Impact
 
|
 
Priority
 
|
 
Mitigation
 
|
 
Owner
 
|
 
Status
 *  
Assumptions:
 
ID
 
|
 
Assumption
 
|
 
Source
 
|
 
Impact
 
if
 
Wrong
 
|
 
Validation
 
|
 
Owner
 *  
Issues:
 
ID
 
|
 
Description
 
|
 
Raised
 
By
 
|
 
Date
 
|
 
Impact
 
|
 
Resolution
 
|
 
Owner
 
|
 
Status
 *  
Dependencies:
 
ID
 
|
 
Dependency
 
|
 
Type
 
|
 
Required
 
By
 
|
 
Status
 
|
 
Risk
 
if
 
Delayed
  
AI  Prompt  
PM-07   RAID  Log  Initialization   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  RAID  Log  template  uploaded:  Populate  all  four  tabs/sections  from  the  PRD/BRD.    -  IF  no  template:  Generate  standard  RAID  Log  with  four  sections.      Add  note:  [ACTION:  Transfer  to  Kellton  RAID  Log  template.]   UPLOADED  DOCUMENT:  Read  the  uploaded  PRD  /  BRD  before  starting.    Extract:  dependencies,  integrations,  constraints,  assumptions,  risks,  compliance  requirements.   PROJECT  CONTEXT:    -  Project:  [PROJECT_NAME]  |  Domain:  [FinTech  /  Healthcare  /  Retail  etc.]    -  Delivery:  [Agile  /  Waterfall]  |  Team:  [X  members]  |  Timeline:  [X  months]    -  Additional  constraints:  [Any  not  covered  in  uploaded  document]   Step  1  --  Extract  stated  risks,  assumptions,  dependencies,  constraints  from  document.  Step  2  --  Add  industry-standard  risks  for  this  domain  and  tech  stack.  Step  3  --  Fill  all  four  RAID  sections  (min  5  entries  each).  Flag  top  3  critical  risks:  [CRITICAL]  Tag  all  inferred  entries:  [ASSUMED  --  section  X]  
 
PM-08   |   Resource  Plan  &  Skill  Matrix  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  13  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
[TEMPLATE-FIRST]   Upload  your  template  before  running  this  prompt.  If  none,  AI  uses  industry  standard  structure. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Resource  Plan  &  Skill  Matrix  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Resource  Plan  &  Skill  Matrix  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Name
 
|
 
Role
 
|
 
Phase
 
|
 
Sprint/Week
 
|
 
Allocated
 
%
 
|
 
Key
 
Tasks
 *  
Skill
 
|
 
Level
 
Needed
 
(1-5)
 
|
 
[Person]
 
|
 
...
 
|
 
Gap
 
(Y/N)
 *  
Planned
 
Leave
 
Impact
 *  
Resource
 
Risk
 
Summary
  
AI  Prompt  
PM-08   Resource  Plan  &  Skill  Matrix   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  Resource  Plan  template  uploaded:  Fill  it  from  the  uploaded  roster.    -  IF  no  template:  Generate  standard  Resource  Allocation  +  Skill  Matrix  format.      Add  note:  [ACTION:  Map  to  Kellton  resource  plan  template.]   UPLOADED  DOCUMENTS:    File  1  --  Team  roster  /  availability  sheet  (Excel  or  PDF)    File  2  (optional)  --  WBS  /  project  plan  for  task  mapping   PROJECT:  [PROJECT_NAME]  |  Duration:  [X  months]  |  Model:  [Agile  /  Waterfall]   Step  1  --  Extract  all  team  members,  roles,  availability  from  roster.  Step  2  --  Resource  Allocation  Plan:  Name  |  Role  |  Phase  |  Sprint/Week  |  Allocated  %  |  Tasks  Step  3  --  Skill  Matrix:  Skill  |  Level  Needed  |  [Person  1]  |  [Person  2]  |  Gap  (Y/N)  Step  4  --  Resource  Risk  Summary:  SPOFs,  over-allocation,  skill  gaps.  Step  5  --  Planned  Leave  Impact:  flag  any  leave  overlapping  critical  milestones.   ASSUMPTION  RULE:  Where  roster  data  is  missing,  mark  [ASSUMED  --  confirm  with  manager].  
 
PM-09   |   Communication  Plan  
[TEMPLATE-FIRST]   Upload  your  template  before  running  this  prompt.  If  none,  AI  uses  industry  standard  structure. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  14  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Communication  Plan  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Communication  Plan  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Audience
 
/
 
Stakeholder
 
Group
 *  
Communication
 
Type
 *  
Frequency
 *  
Format
 
/
 
Medium
 *  
Owner
 *  
Channel
 *  
Key
 
Content
 
/
 
Purpose
 *  
Escalation
 
Matrix
  
AI  Prompt  
PM-09   Communication  Plan   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  Communication  Plan  template  uploaded:  Fill  it  from  the  stakeholder  register.    -  IF  no  template:  Generate  standard  Communication  Plan  table  +  Escalation  Matrix.      Add  note:  [ACTION:  Map  to  Kellton  communication  plan  template.]   STAKEHOLDER  LIST:  [Paste  stakeholder  register  or  list  of  roles]  PROJECT:  [PROJECT_NAME]  |  Model:  [Agile  /  Waterfall]  |  Duration:  [X  months]  Key  Milestones:  [Sprint  Reviews,  UAT,  Go-Live,  SteerCo]   Fill  the  template  covering:    Daily  standups  |  Weekly  status  reports  |  Sprint  reviews    Fortnightly  SteerCo  updates  |  Client  email  cadence  |  Escalation  protocol   Escalation  Matrix:    Issue  Type  |  Level  1  |  Level  2  |  Level  3  |  Timeframe  to  Escalate  
 
PM-10   |   Project  Schedule  Baseline  
[TEMPLATE-FIRST]   Upload  your  template  before  running  this  prompt.  If  none,  AI  uses  industry  standard  structure. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Project  Schedule  Baseline  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Project  Schedule  Baseline  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  15  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
*  
Milestone
 
|
 
Planned
 
Date
 
|
 
Owner
 
|
 
Predecessors
 
|
 
Buffer
 
(days)
 *  
Sprint
 
#
 
|
 
Start
 
|
 
End
 
|
 
Goals
 
|
 
Team
 
Capacity
 
|
 
Deliverables
 *  
Dependency
 
Map:
 
Task
 
|
 
Depends
 
On
 
|
 
Type
 
|
 
Lag/Lead
 
|
 
Risk
  
AI  Prompt  
PM-10   Project  Schedule  Baseline   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  Schedule  /  Project  Plan  template  uploaded:  Fill  it  from  the  WBS.    -  IF  no  template:  Generate  standard  Schedule  Baseline  table  format.      Add  note:  [ACTION:  Import  into  MS  Project  /  Jira  /  agreed  tracking  tool.]   UPLOADED  DOCUMENTS:    File  1  --  AI-generated  WBS  with  effort  estimates  (from  PM-06  output)    File  2  (optional)  --  Team  roster  /  leave  calendar   PROJECT:  [PROJECT_NAME]  |  Start:  [DATE]  |  End:  [DATE]  |  Model:  [Agile  /  Waterfall]  Fixed  constraints:  [regulatory  deadlines,  client  events,  holidays]   Step  1  --  Extract  tasks,  durations,  dependencies  from  WBS.  Step  2  --  Build  Schedule  Baseline:  Milestone  |  Date  |  Owner  |  Predecessors  |  Buffer  Step  3  --  Sprint/Phase  Plan  (if  Agile):  Sprint  #  |  Dates  |  Goals  |  Capacity  |  Deliverables  Step  4  --  Dependency  Map:  Task  |  Depends  On  |  Type  (FS/SS/FF)  |  Lag  |  Risk  Step  5  --  Baseline  Summary:  total  duration,  risk  dates,  recommended  buffer.   Flag  any  milestone  with  <5  working  days  buffer:  [LOW  BUFFER  --  RISK]  ASSUMPTION  RULE:  Tag  estimated  durations  [ASSUMED  ESTIMATE  --  validate  with  tech  lead].  
 
PM-31   |   Full  Project  Initialisation  --  Starter  Pack  
[BOTH]   NEW  from  Prompt  Library  1.1.  Generates  complete  starter  pack:  Project  Plan  +  RAID  +  Resource  Tracker  +  RAG  Dashboard  in  one  session. 
AI  Prompt  
PM-31   Full  Project  Initialisation  --  Starter  Pack   [  BOTH  ]
 
You  are  an  expert  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  any  templates  uploaded  (project  plan,  RAID,  resource  tracker):  Fill  those  templates.    -  IF  no  templates:  Generate  all  four  artefacts  using  standard  industry  formats.      Add  note:  [ACTION:  Transfer  to  Kellton  standard  templates.]   Project  details:    -  Project  name:  [PROJECT  NAME]   |   Client:  [CLIENT  NAME]    -  Delivery  methodology:  [Scrum  /  Waterfall  /  Hybrid]    -  Project  type:  [Web  app  /  Mobile  app  /  API  integration  /  Legacy  migration]    -  Duration:  [X  months]   Start:  [DD-Mon-YYYY]   End:  [DD-Mon-YYYY]    -  Budget:  [AMOUNT]  (if  known)  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  16  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
  -  Team:  [N]  developers,  [N]  BAs,  [N]  QAs,  [N]  PMs    -  Key  milestones:  [MILESTONE  --  DATE,  one  per  line]    -  Known  risks:  [LIST  or  "none  identified  yet"]    -  Client  stakeholders:  [NAMES  &  ROLES]    -  Internal  stakeholders:  [NAMES  &  ROLES]   Generate  four  artefacts:    1.  Project  Plan:  WBS  phases,  tasks,  owners,  start/end  dates,  duration,       %  complete  (all  0%),  dependencies,  RAG  (all  Green).    2.  RAID  Tracker:  Risks  |  Actions  |  Issues  |  Dependencies  tabs  --       populated  with  known  items  from  above.    3.  Resource  Tracker:  each  team  member,  role,  %  allocation,  start/end  date.    4.  Project  Health  Dashboard:  RAG  indicators  for       Schedule  |  Budget  |  Scope  |  Resources  |  Quality  |  Risk   Use  DD-Mon-YYYY  date  format  throughout.  
 
PM-32   |   RACI  Matrix  Generator  (Detailed)  
[BOTH]   NEW  from  Prompt  Library  1.3.  Detailed  RACI  with  governance  gap  analysis. 
AI  Prompt  
PM-32   RACI  Matrix  Generator  (Detailed)   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  RACI  template  uploaded:  Fill  it  using  the  roles  and  activities  below.    -  IF  no  template:  Generate  standard  RACI  table  format  with  legend  and  gap  analysis.   Project:  [PROJECT  NAME]   Team  members  and  roles:    -  [NAME]  --  [ROLE  e.g.  Project  Manager]    -  [NAME]  --  [ROLE  e.g.  Business  Analyst]    -  [NAME]  --  [ROLE  e.g.  Tech  Lead]    -  [NAME]  --  [ROLE  e.g.  Developer]    -  [NAME]  --  [ROLE  e.g.  QA  Lead]    -  [NAME]  --  [ROLE  e.g.  Client  Sponsor]    -  [NAME]  --  [ROLE  e.g.  Steering  Committee]   Key  activities  (add  or  remove  as  needed):    Requirements  gathering,  Solution  design,  Development,  Code  review,  Testing  (SIT/UAT),    Defect  triage,  Status  reporting,  Risk  management,  Change  control,  Client  sign-off,    Deployment  approval,  Go-live  decision.   Format:  activities  as  rows,  team  members  as  columns.  Use  R,  A,  C,  I  notation.  Highlight  activities  with  no  Accountable  owner.  Add  legend  and  note  any  governance  gaps.  
  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  17  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
PHASE  3   --   Execution Day-to-day  delivery  --  sprints,  standups,  communications,  and  change  management. PM-11  Sprint  Plan   |   PM-12  MOM   |   PM-13  Client  Comms   |   PM-14  CR   |   PM-15  Escalation   |   PM-16  Actions   |   PM-17  Defect  Triage   |   PM-33  DSR   |   PM-34  Sprint  Review   |   PM-35  Retro   |   PM-36  Phase  Gate   |   PM-37  Delay  Email   |   PM-38  Decision  Email   |   PM-39  Milestone  Ann.
 
 
PM-11   |   Sprint  Planning  
[SCRUM]   Scrum-specific  activity. 
[TEMPLATE-FIRST]   Upload:  Backlog  export  (Jira/ADO)  +  Team  capacity/leave  calendar. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Sprint  Plan  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Sprint  Plan  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Sprint
 
Goal
 *  
Committed
 
Stories
 
(ID
 
|
 
Title
 
|
 
SP
 
|
 
Priority)
 *  
Team
 
Capacity
 
Table
 
(member
 
|
 
available
 
days
 
|
 
leave
 
|
 
SP
 
capacity)
 *  
Sprint
 
Risks
 *  
Definition
 
of
 
Done
  
AI  Prompt  
PM-11   Sprint  Planning   [  SCRUM  ]
 
You  are  a  senior  Project  Manager  and  Scrum  Master.   TEMPLATE  INSTRUCTION:    -  IF  sprint  plan  template  uploaded:  Fill  it  from  the  backlog  and  capacity  data.    -  IF  no  template:  Generate  standard  sprint  plan  format.      Add  note:  [ACTION:  Transfer  to  Kellton  sprint  plan  template.]   UPLOADED  DOCUMENTS:    File  1  --  Backlog  export  from  Jira  /  Azure  DevOps  (Excel  or  PDF)    File  2  (optional)  --  Team  capacity  /  leave  calendar   PROJECT:  [PROJECT_NAME]   |   Sprint  [X]  of  [Y]  Duration:  [1  /  2  weeks]   |   Start:  [DATE]   |   End:  [DATE]  Team  Velocity  (avg  last  3  sprints):  [X  story  points]  Sprint  Goal:  [What  this  sprint  must  achieve]   Step  1  --  Read  backlog.  List  all  candidate  stories  with  point  values.  Step  2  --  Read  capacity  file.  Calculate  actual  available  capacity:    [Working  days]  minus  [Leave  days]  =  Available  days  ->  Story  points  via  velocity  ratio.  Step  3  --  Recommend  sprint  commitment  (actual  capacity,  not  just  velocity):    Stories  by  feature/theme  |  Total  SP  |  Within  capacity?  Y/N  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  18  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
Step  4  --  Capacity  Table:  Member  |  Role  |  Available  Days  |  Leave  |  SP  Capacity  |  Assigned  SP  Step  5  --  Sprint  Risks:  unclear  ACs,  dependencies,  oversized  stories.  Step  6  --  Definition  of  Done  reminder.   ASSUMPTION  RULE:  Missing  capacity  ->  [ASSUMED  FULL  CAPACITY  --  confirm  with  member].  
 
PM-12   |   MOM  Generation  
[TEMPLATE-FIRST]   Upload:  MOM  template  +  meeting  recording/transcript  (any  format). 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Minutes  of  Meeting  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Minutes  of  Meeting  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Meeting
 
Title,
 
Date,
 
Attendees
 *  
Meeting
 
Objective
 *  
Key
 
Discussion
 
Points
 *  
Decisions
 
Made
 
(with
 
decision-maker)
 *  
Action
 
Items
 
(owner
 
|
 
due
 
date
 
|
 
priority)
 *  
Open
 
/
 
Parked
 
Topics
 *  
Next
 
Meeting
 
Date
 
and
 
Agenda
  
AI  Prompt  
PM-12   MOM  Generation   [  BOTH  ]
 
You  are  a  senior  Project  Manager  and  professional  note-taker.   TEMPLATE  INSTRUCTION:    -  IF  MOM  template  uploaded:  Fill  it  using  the  meeting  recording/transcript.    -  IF  no  template:  Generate  standard  MOM  format.      Add  note:  [ACTION:  Map  to  Kellton  MOM  template  before  distributing.]   UPLOADED  FILE:  Upload  the  meeting  file  before  running.    Accepted:  .txt  or  .docx  transcript  |  .mp4/.mp3/.wav  recording  |  Teams/Zoom  auto-transcript   MEETING  DETAILS:    -  Project:  [PROJECT_NAME]    -  Meeting  Type:  [Standup  /  Sprint  Review  /  Stakeholder  Sync  /  Client  Call  /  Kick-off]    -  Date:  [DATE]    -  Attendees:  [Confirm  against  calendar  invite  --  do  not  rely  solely  on  transcript]   Step  1  --  Read/transcribe  the  uploaded  file.  Clean  up  transcript  errors  first.  Step  2  --  Fill  the  MOM  template:    1.  Meeting  Objective  (one  sentence)    2.  Key  Discussion  Points  (factual  bullets  by  topic  --  no  editorialising)  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  19  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
  3.  Decisions  Made  (every  decision  with  the  decision-maker  named)    4.  Action  Items:  #  |  Action  |  Owner  |  Due  Date  |  Priority  (C/H/M/L)    5.  Open  /  Parked  Topics  (raised  but  not  resolved)    6.  Next  Meeting:  Date  |  Time  |  Carry-forward  agenda  items  Step  3  --  Every  "will  do"  or  commitment  in  the  transcript  =  action  item.   RULES:    -  Do  not  fabricate  anything  not  in  the  recording/transcript.    -  Unclear  name:  [NAME  UNCLEAR  --  verify  with  attendee  list]    -  Ambiguous  decision:  [DECISION  UNCLEAR  --  describe  ambiguity]   ASSUMPTION  RULE:  List  uncertain  transcript  sections:    #  |  Unclear  Section  |  Timestamp  |  Action  Needed  
 [EXAMPLE  OUTPUT]   MOM  --  Action  Items  Section 
4.  ACTION  ITEMS    #  |  Action                                |  Owner      |  Due  Date  |  Priority   01  |  Raise  CR  for  push  notifications       |  PM         |  25-Apr    |  High   02  |  Nominate  UAT  test  lead                |  Client  PO  |  05-May    |  High   03  |  Fix  API  timeout  bug  BUG-047           |  Dev  Lead   |  22-Apr    |  Critical   04  |  Share  updated  UAT  test  cases          |  QA  Lead    |  24-Apr    |  Medium  5.  OPEN  /  PARKED  ITEMS   *  Budget  approval  for  Phase  2  --  deferred  to  SteerCo  15-May   *  [UNCLEAR  --  VERIFY]  Data  retention  policy  --  transcript  unclear  at  42:15  
[IMPORTANT]   Always  verify  attendee  names  against  the  calendar  invite.  AI  transcription  tools  frequently  mishear  names. 
 
PM-13   |   Client  Communication  Drafting  
[TEMPLATE-FIRST]   Upload:  Client  communication  template  if  the  client  has  a  preferred  format. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Client  Communication  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Client  Communication  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Subject
 
Line
 *  
Salutation
 *  
Situation
 
Summary
 
(2-3
 
sentences)
 *  
Key
 
Updates
 
or
 
Decisions
 *  
Client
 
Actions
 
Required
 
with
 
Deadlines
 *  
Next
 
Steps
 *  
Sign-off
  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  20  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
AI  Prompt  
PM-13   Client  Communication  Drafting   [  BOTH  ]
 
You  are  a  senior  Project  Manager  at  Kellton  communicating  with  a  client.   TEMPLATE  INSTRUCTION:    -  IF  client  template  uploaded:  Use  its  exact  structure,  subject  line  format,  sign-off  style.    -  IF  no  template:  Use  standard  professional  email  format.      Add  note:  [ACTION:  Check  client  prefers  this  format  before  sending  regularly.]   CONTEXT:    -  Project:  [PROJECT_NAME]    -  Type:  [Weekly  Update  /  Delay  Notification  /  CR  Response  /  Escalation  /  Good  News]    -  Situation:  [2-3  sentences:  what  happened  and  what  needs  communicating]    -  Recipient:  [Client  Name,  Role]    -  Tone:  [Formal  /  Semi-formal]    -  Key  Points:      1.  [Point  1]      2.  [Point  2]      3.  [Client  action  required  with  deadline,  if  any]   Draft  with:  clear  subject  line  |  professional  greeting  |  situation  summary  (max  3  sentences)  |  key  updates  |  client  action  items  with  deadlines  |  solution-focused  closing.  Keep  to  200  words  or  fewer  unless  more  is  required.   ASSUMPTION  RULE:  Missing  details  ->  flag  [NEEDS  CLARIFICATION  --  reason]  inline.  PM  must  review  and  approve  before  sending.  
 
[IMPORTANT]   PM  MUST  review  and  approve  all  AI-drafted  client  communications.  Never  forward  AI  output  directly. 
 
PM-14   |   Change  Request  Analysis  
[TEMPLATE-FIRST]   Upload:  CR  template  +  current  project  plan/baseline  +  original  PRD/charter. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Change  Request  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Change  Request  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
CR
 
Reference
 
ID
 *  
Change
 
Description
 *  
Business
 
Justification
 *  
Scope
 
Impact
 *  
Timeline
 
Impact
 *  
Budget
 
Impact
 *  
Risk
 
Impact
 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  21  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
*  
Recommendation
 
(Approve/Reject/Defer)
 *  
Decision
 
Authority
 *  
Approval
 
Sign-off
 
Block
  
AI  Prompt  
PM-14   Change  Request  Analysis   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  CR  template  uploaded:  Fill  all  sections  from  the  uploaded  baseline  documents.    -  IF  no  template:  Generate  standard  CR  Impact  Assessment  format.      Add  note:  [ACTION:  Map  to  Kellton  CR  template  before  submitting.]   UPLOADED  DOCUMENTS:    File  1  --  Current  project  plan  /  schedule  baseline  (Excel  or  PDF)    File  2  (optional)  --  Original  PRD  /  BRD  or  charter    File  3  (optional)  --  Current  RAID  log   CR  DETAILS:    -  CR  Reference:  [CR-ID]   |   Raised  By:  [Name  /  Role]    -  Description:  [Plain  language  description]    -  Business  Justification:  [Why  is  this  being  requested?]   Step  1  --  Read  uploads.  Identify  current  scope,  timeline,  and  budget  baseline.  Step  2  --  Complete  CR  assessment:    1.  Scope  Impact  --  what  changes  vs  the  baseline    2.  Timeline  Impact  --  days/weeks  required;  milestones  affected    3.  Budget  Impact  --  additional  person-days  and  estimated  cost    4.  Risk  Impact  --  new  risks;  cross-reference  RAID  if  provided    5.  Recommendation  --  Approve  /  Reject  /  Defer  with  justification    6.  Decision  Authority  --  who  must  sign  off   Flag  if  this  CR  changes  any  signed  baseline  document.  ASSUMPTION  RULE:  Missing  data  ->  [ASSUMED  --  reason]  in  Assumptions  Log.  
 
PM-15   |   Escalation  Drafting  
[NOTE]   No  standard  Kellton  template.  AI  generates  professional  escalation  using  industry  standard  format. 
AI  Prompt  
PM-15   Escalation  Drafting   [  BOTH  ]
 
You  are  a  senior  Project  Manager  drafting  a  formal  escalation.   TEMPLATE  INSTRUCTION:    -  IF  escalation  template  uploaded:  Use  it  exactly.    -  IF  no  template:  Use  standard  escalation  email  format  (subject,  context,  impact,  resolution  ask,  deadline).   ESCALATION  CONTEXT:    -  Project:  [PROJECT_NAME]  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  22  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
  -  Type:  [Internal  /  Client  /  Vendor  /  Sponsor]    -  Issue:  [2-3  sentences  describing  the  issue]    -  Impact:  [Timeline  /  cost  /  quality  if  not  resolved]    -  Actions  Already  Taken:  [What  has  already  been  tried?]    -  Resolution  Needed  By:  [DATE]    -  Escalating  To:  [Name  /  Role]   Draft  with:    1.  Clear  factual  subject  line  (no  emotional  language)    2.  One-paragraph  situation  summary    3.  Impact  if  unresolved  (specific  --  dates,  costs,  deliverables)    4.  Specific  resolution  requested  (exact  action  needed)    5.  Proposed  next  steps  and  timeline    6.  Professional,  solution-focused  closing   Tone:  Firm,  factual,  professional.  Not  accusatory.  
 
PM-16   |   Action  Item  Tracking  
[NOTE]   No  standard  template.  Uses  MOM  action  items  section  or  project  tracking  tool  (Jira  /  MS  Planner). 
AI  Prompt  
PM-16   Action  Item  Tracking   [  BOTH  ]
 
You  are  a  senior  Project  Manager.  Extract  all  action  items  from  the  meeting  notes/transcript  and  format  as  a  structured  table.   TEMPLATE  INSTRUCTION:    -  IF  action  log  template  uploaded:  Fill  it  from  the  meeting  notes.    -  IF  no  template:  Generate  standard  action  items  table.   PROJECT:  [PROJECT_NAME]   |   Meeting  Date:  [DATE]  MEETING  NOTES  /  TRANSCRIPT:  [Paste  here  or  upload  file]   Extract  and  format:    |  #  |  Action  Description  |  Owner  |  Due  Date  |  Priority  (C/H/M/L)  |  Status  |   Rules:    -  Every  "will  do"  or  commitment  =  action  item.    -  No  named  owner:  [OWNER  TBD]   |   No  due  date:  [DATE  TBD]    -  Do  not  infer  actions  not  explicitly  mentioned.   After  the  table,  list  previous  meeting  actions  NOT  confirmed  complete  today:    [Paste  previous  action  log  here  if  available]  
 
PM-17   |   Defect  Triage  Summarization  
[NOTE]   No  standard  Kellton  template.  AI  generates  structured  analysis.  PM  shares  in  sprint  review  or  daily  defect  update. 
AI  Prompt  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  23  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
PM-17   Defect  Triage  Summarization   [  BOTH  ]
 
You  are  a  senior  Project  Manager  reviewing  sprint  defects.   TEMPLATE  INSTRUCTION:    -  IF  defect  summary  template  uploaded:  Fill  it  from  the  defect  export.    -  IF  no  template:  Generate  standard  defect  triage  summary  format.   UPLOADED  FILE:  Defect  export  (Jira/.xlsx/.csv  /  ADO  /  manual  defect  log)    Expected:  ID  |  Summary  |  Severity  |  Module  |  Status  |  Assigned  To  |  Date  Raised   PROJECT:  [PROJECT_NAME]   |   Sprint/Cycle:  [Sprint  X  /  UAT  Week  Y]   Step  1  --  Count  and  categorise  all  defects  from  the  uploaded  file.  Step  2  --  Generate:    1.  DEFECT  DASHBOARD:  Total  |  Critical  |  High  |  Medium  |  Low  |  Open  |  Resolved  |  Deferred    2.  MODULE  HOTSPOTS:  Top  3  modules  by  defect  count  with  %  of  total    3.  TRIAGE  RECOMMENDATIONS:  For  each  Critical/High  open  defect:       ID  |  Summary  |  Recommended  Action  |  Block  Sprint?  Y/N  |  Owner    4.  SPRINT  RISK:  Proceed  /  Partial  /  Block  --  with  rationale    5.  TEAM  UPDATE  (2  sentences  for  standup):  plain  English,  factual   ASSUMPTION  RULE:  Blank  severity/module  ->  [ASSUMED  --  verify  with  QA  lead].  
 
PM-33   |   Daily  Standup  Digest  &  DSR  
[BOTH]   NEW  from  Prompt  Library  2.2.  Converts  raw  standup  notes  into  a  structured  Daily  Status  Report  with  RAG. 
[SCRUM]   Scrum-specific  activity. 
AI  Prompt  
PM-33   Daily  Standup  Digest  &  DSR   [  SCRUM  ]
 
You  are  an  experienced  Project  Manager  and  Scrum  Master.   TEMPLATE  INSTRUCTION:    -  IF  DSR  template  uploaded:  Fill  it  from  the  standup  notes  below.    -  IF  no  template:  Generate  standard  Daily  Status  Report  format.   Project:  [PROJECT  NAME]   |   Date:  [DD-Mon-YYYY]   |   Sprint:  [N]   |   Day:  [X  of  10]  Prepared  by:  [PM  NAME]   Raw  standup  notes:  ---  [PASTE  STANDUP  NOTES  HERE  --  bullet  points,  Teams  chat  export,  or  voice  transcript]  ---   Generate  the  DSR:    1.  Yesterday's  accomplishments  (per  team  member,  consolidated)    2.  Today's  plan  (per  team  member)    3.  Blockers  /  impediments  --  flag  each  as  CRITICAL  /  HIGH  /  LOW    4.  Sprint  burndown  status  (estimate  remaining  points  if  inferable)    5.  RAG:  Overall  |  Schedule  |  Budget  |  Resources  |  Scope  |  Quality  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  24  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
  6.  Open  actions  (owner,  due  date)    7.  Items  requiring  PM  decision  or  client  input  today   Use  DD-Mon-YYYY  dates.  Professional  and  concise.  
 
PM-34   |   Sprint  Review  Summary  
[BOTH]   NEW  from  Prompt  Library  2.3.  End-of-sprint  summary  with  velocity  analysis  and  client  email. 
[SCRUM]   Scrum-specific  activity. 
AI  Prompt  
PM-34   Sprint  Review  Summary   [  SCRUM  ]
 
You  are  an  experienced  Project  Manager  and  Scrum  Master.   TEMPLATE  INSTRUCTION:    -  IF  sprint  review  template  uploaded:  Fill  it  with  the  data  below.    -  IF  no  template:  Generate  standard  Sprint  Review  Summary  format.   Project:  [PROJECT  NAME]   |   Sprint:  [N]   |   Period:  [DD-Mon-YYYY]  to  [DD-Mon-YYYY]  Sprint  goal:  [ORIGINAL  GOAL]   Committed  stories:  [ID]  [TITLE]  --  [POINTS]  pts   (repeat)  Completed  stories:  [ID]  [TITLE]  --  [POINTS]  pts  --  Demo:  [Yes/No]   (repeat)  Carried  forward:  [ID]  [TITLE]  --  [POINTS]  pts  --  Reason:  [REASON]   (repeat)   Velocity:  This  sprint  [X]  |  Previous  sprint  [Y]  |  Team  average  [Z]  Bugs:  Raised  [N]  |  Closed  [N]  |  Open  [N]  Demo  highlights:  [What  the  client  saw]  Stakeholder  feedback:  [Paste  or  write  "none  recorded"]   Generate:    1.  Sprint  Review  Summary  (1  page,  client-ready)    2.  Velocity  trend  narrative  (2-3  sentences)    3.  Carry-forward  risk  assessment    4.  Recommended  sprint  goal  for  Sprint  [N+1]    5.  Draft  email  to  client  summarising  the  sprint  outcome  
 
PM-35   |   Retrospective  Facilitation  
[BOTH]   NEW  from  Prompt  Library  2.4.  Generates  retro  questions,  structures  team  inputs  into  action  plan,  produces  team  memo. 
[SCRUM]   Scrum-specific  activity. 
AI  Prompt  
PM-35   Retrospective  Facilitation   [  SCRUM  ]
 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  25  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
You  are  an  experienced  Scrum  Master  and  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  retrospective  template  uploaded:  Use  its  structure  for  the  output.    -  IF  no  template:  Generate  standard  Keep/Drop/Try  retrospective  format.   Project:  [PROJECT  NAME]   |   Sprint:  [N]  Team  size:  [N]  members   |   Format:  [In-person  /  Remote]   |   Time:  [60  /  90  minutes]   Context:    -  What  went  well:  [PASTE  TEAM  INPUTS  or  "to  be  collected  in  session"]    -  What  could  improve:  [PASTE  TEAM  INPUTS  or  "to  be  collected  in  session"]    -  Actions  from  last  retro:  [LIST  ACTIONS  AND  STATUS]   Step  1:  Generate  5  open-ended  questions  per  category:    -  What  went  well  (Keep)    -  What  needs  improvement  (Drop  /  Change)    -  What  to  try  next  sprint  (Try)   Step  2  (if  inputs  provided):  Convert  raw  inputs  into:    -  Structured  What  Went  Well  list    -  Structured  Improvement  Areas  list    -  Prioritised  Action  Plan:  Action  |  Owner  |  Due  Date  |  Success  Metric   Step  3:  Draft  retrospective  summary  memo  to  share  with  the  team.  
 
PM-36   |   Waterfall  Phase  Gate  Checklist  
[BOTH]   NEW  from  Prompt  Library  3.1.  Phase-gate  Go/No-Go  for  Waterfall  delivery. 
[WATERFALL]   Waterfall-specific  activity. 
AI  Prompt  
PM-36   Waterfall  Phase  Gate  Checklist   [  WATERFALL  ]
 
You  are  an  experienced  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  phase  gate  checklist  template  uploaded:  Fill  it  with  the  status  data  below.    -  IF  no  template:  Generate  standard  Phase  Gate  Checklist  +  Go/No-Go  memo.   Project:  [PROJECT  NAME]  Phase:  [Requirements  /  Design  /  Build  /  SIT  /  UAT]  Planned  end:  [DD-Mon-YYYY]   |   Actual  end:  [DD-Mon-YYYY]   Deliverables  status:    -  BRD:  [Complete  /  In  Review  /  Draft  /  Not  Started]    -  FSD:  [STATUS]   |   NFR:  [STATUS]   |   Data  flow  /  process  maps:  [STATUS]    -  Client  sign-off:  [Yes  /  No  /  Pending]    -  Open  queries:  [N  open]  |  [N  closed]   Known  gaps  or  risks  at  phase  close:  [LIST  or  "none"]   Generate:  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  26  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
  1.  Phase  Gate  Checklist  with  RAG  per  deliverable    2.  Open  items:  Item  |  Owner  |  Due  Date  |  Impact  if  Delayed    3.  Go  /  No-Go  recommendation  with  rationale    4.  Phase  Gate  Meeting  agenda  (30  minutes)    5.  Phase  completion  memo  for  client  sign-off  
 
PM-37   |   Delay  Notification  Email  
[BOTH]   NEW  from  Prompt  Library  6.1.  Calm,  factual,  solution-focused  delay  notification. 
AI  Prompt  
PM-37   Delay  Notification  Email   [  BOTH  ]
 
You  are  a  senior  Project  Manager  at  Kellton.   TEMPLATE  INSTRUCTION:    -  IF  client  email  template  uploaded:  Use  its  structure  and  sign-off  style.    -  IF  no  template:  Use  standard  professional  delay  notification  format.   Project:  [PROJECT  NAME]   |   Date:  [DD-Mon-YYYY]  From:  [YOUR  NAME]   |   To:  [CLIENT  NAME  /  ROLE]   Delay  details:    -  What  is  delayed:  [MILESTONE  /  DELIVERABLE]    -  Original  planned  date:  [DD-Mon-YYYY]    -  New  forecast  date:  [DD-Mon-YYYY]    -  Delay  duration:  [N  days  /  weeks]   Root  cause:  [Explain  clearly]  Downstream  impact:  [Milestones,  budget,  resources  affected]  Recovery  actions  already  taken:  [What  has  been  done]  Client  action  needed:  [Approval  to  adjust  date  /  No  action  required]   Tone:  calm,  factual,  solution-focused.  Take  ownership  without  excessive  apology.  One  clear  ask  at  the  end.  Subject  line  references  project  and  specific  milestone.  
 
PM-38   |   Decision  Request  Email  
[BOTH]   NEW  from  Prompt  Library  6.2.  Structured  decision  request  with  options  and  firm  deadline. 
AI  Prompt  
PM-38   Decision  Request  Email   [  BOTH  ]
 
You  are  a  senior  Project  Manager  at  Kellton.   TEMPLATE  INSTRUCTION:    -  IF  client  email  template  uploaded:  Use  its  structure.    -  IF  no  template:  Use  standard  decision  request  email  format.   Project:  [PROJECT  NAME]   |   Date:  [DD-Mon-YYYY]  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  27  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
From:  [YOUR  NAME]   |   To:  [STAKEHOLDER  NAME  /  ROLE]  Decision  deadline:  [DD-Mon-YYYY]  --  why  this  date  matters:  [explain]   Context:  [Background  leading  to  this  decision  point]  Decision  required:  [One  clear  question  the  person  must  answer]   Options:    Option  1:  [DESCRIPTION]  --  Implication:  [COST  /  TIME  /  QUALITY  impact]    Option  2:  [DESCRIPTION]  --  Implication:  [...]    Option  3  (if  applicable):  [DESCRIPTION]  --  Implication:  [...]   Recommendation:  [Your  recommended  option  +  1-2  sentence  rationale]  Default  if  no  decision  by  [DATE]:  [What  happens  by  default  --  be  specific]   Keep  to  one  page.  Professional,  clear,  firm  on  deadline  but  not  pressuring.  
 
PM-39   |   Milestone  Achievement  Announcement  
[BOTH]   NEW  from  Prompt  Library  6.3.  Two  versions:  internal  (celebratory)  +  client-facing  (professional). 
AI  Prompt  
PM-39   Milestone  Achievement  Announcement   [  BOTH  ]
 
You  are  a  senior  Project  Manager  at  Kellton.   TEMPLATE  INSTRUCTION:    -  IF  announcement  template  uploaded:  Use  it  for  both  versions.    -  IF  no  template:  Generate  two  versions  as  specified.   Project:  [PROJECT  NAME]   |   Date:  [DD-Mon-YYYY]  Milestone  achieved:  [MILESTONE  NAME]  Planned  date:  [DD-Mon-YYYY]   |   Actual  date:  [DD-Mon-YYYY]   What  was  delivered:  [Plain  business  language  --  no  jargon]  Business  value:  [Why  this  matters  to  the  business  /  client]  Team  members  to  recognise:  [Names  and  specific  contributions]  What  comes  next:  [Next  milestone  /  phase  --  planned  date]   Generate  two  versions:    Version  A  --  Internal  team  email:  warm,  celebratory,  150  words  max    Version  B  --  Client-facing  email:  professional,  business-focused,  200  words  max   Both  end  with  forward  momentum  --  what  happens  next,  not  just  what  was  achieved.  
  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  28  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
PHASE  4   --   Monitoring  &  Control Ongoing  governance  --  status,  risks,  budget,  timeline,  and  stakeholder  health. PM-18  WSR   |   PM-19  RAID  Update   |   PM-20  KPI  Dashboard   |   PM-21  Timeline  Impact   |   PM-22  Budget   |   PM-23  Dependencies   |   PM-24  UAT   |   PM-25  Stakeholder  Pulse   |   PM-40  SIT/UAT  Steering   |   PM-41  MBR   |   PM-42  RAID  from  Notes   |   PM-43  Risk  Escalation   |   PM-44  Risk  Review   |   PM-45  Issue  Log
 
 
PM-18   |   Weekly  Status  Report  (WSR)  
[TEMPLATE-FIRST]   Upload:  WSR  template  +  sprint  data  export  +  budget  actuals  +  RAID  log  +  previous  WSR. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Weekly  Status  Report  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Weekly  Status  Report  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Reporting
 
Period
 
and
 
RAG
 
Status
 *  
Executive
 
Summary
 
(3
 
sentences)
 *  
Progress
 
This
 
Week
 *  
Key
 
Metrics:
 
Sprint
 
Velocity
 
|
 
Budget
 
|
 
Timeline
 
|
 
Quality
 *  
Risks
 
&
 
Issues
 
Update
 *  
Decisions
 
&
 
Action
 
Items
 *  
Next
 
Week
 
Plan
 *  
Client
 
Actions
 
Required
  
AI  Prompt  
PM-18   Weekly  Status  Report  (WSR)   [  BOTH  ]
 
You  are  a  senior  Project  Manager  at  Kellton.   TEMPLATE  INSTRUCTION:    -  IF  WSR  template  uploaded:  Fill  all  sections  from  the  uploaded  data  files.    -  IF  no  template:  Generate  standard  WSR  format.      Add  note:  [ACTION:  Map  to  Kellton  WSR  template  before  sending.]   UPLOADED  DOCUMENTS  (upload  one  or  more):    File  1  --  Sprint  board  /  Jira  export  (Excel  or  PDF):  stories,  velocity,  blockers    File  2  (optional)  --  Budget  actuals  sheet  (Excel):  planned  vs  actual  spend    File  3  (optional)  --  RAID  log  (Excel):  current  risks  and  issues    File  4  (optional)  --  Previous  WSR:  carry  forward  open  actions   REPORTING  PERIOD:  [Week  of  DD-MMM-YYYY]  PROJECT:  [PROJECT_NAME]   |   CLIENT:  [CLIENT_NAME]  OVERALL  RAG:  [Red  /  Amber  /  Green]   |   RAG  REASON:  [One  sentence]   Step  1  --  Extract  sprint  progress  from  uploaded  sprint  data.  Step  2  --  Extract  budget  figures  from  actuals  sheet  (if  provided).  Step  3  --  Extract  top  3  active  risks/issues  from  RAID  log  (if  provided).  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  29  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
Step  4  --  Fill  WSR  template:    1.  Executive  Summary  (3  sentences  max  --  RAG,  progress,  key  message)    2.  Progress  This  Week  (from  sprint  data)    3.  Key  Metrics:  Sprint  Velocity  |  Budget  Utilisation  |  Timeline  |  Open  Defects    4.  Risks  &  Issues  Update  (from  RAID)    5.  Decisions  &  Action  Items    6.  Next  Week  Plan    7.  Client  Actions  Required  (overdue  or  upcoming  --  be  explicit)   For  every  figure,  note  the  source  file  in  brackets.  Missing  data:  [DATA  PENDING  --  source  needed].  ASSUMPTION  RULE:  Estimated  figures  ->  [ASSUMED  --  validate]  in  Assumptions  Log.  
 [EXAMPLE  OUTPUT]   WSR  --  Executive  Summary 
REPORTING  PERIOD:  Week  of  12-May-2025 PROJECT:  Customer  Onboarding  Portal   |   CLIENT:  XYZ  Corp   |   RAG:  AMBER  EXECUTIVE  SUMMARY Sprint  4  is  at  68%  completion  (34  of  50  SP)  with  the  KYC  API  blocker  (R-01)  under active  management  --  dev  team  applying  vendor  patch  by  16-May.  Timeline  remains  on track  for  the  15-June  UAT  start;  budget  healthy  at  74%  utilised  vs  76%  elapsed. One  overdue  client  action:  UAT  Test  Lead  nomination  (was  due  05-May  --  see  Section  7). 
 
PM-19   |   RAID  Management  (Weekly  Update)  
[TEMPLATE-FIRST]   Upload:  Current  RAID  Log  (Excel  or  PDF).  AI  updates  in  place  --  never  deletes  entries. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  RAID  Log  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  RAID  Log  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Risks:
 
ID
 
|
 
Description
 
|
 
Prob
 
|
 
Impact
 
|
 
Priority
 
|
 
Mitigation
 
|
 
Owner
 
|
 
Status
 *  
Assumptions:
 
ID
 
|
 
Assumption
 
|
 
Impact
 
if
 
Wrong
 
|
 
Validation
 
|
 
Owner
 *  
Issues:
 
ID
 
|
 
Description
 
|
 
Impact
 
|
 
Resolution
 
|
 
Owner
 
|
 
Status
 *  
Dependencies:
 
ID
 
|
 
Dependency
 
|
 
Type
 
|
 
Required
 
By
 
|
 
Status
 
|
 
Risk
 
if
 
Delayed
  
AI  Prompt  
PM-19   RAID  Management  --  Weekly  Update   [  BOTH  ]
 
You  are  a  senior  Project  Manager  doing  a  weekly  RAID  review.   TEMPLATE  INSTRUCTION:    -  IF  RAID  log  uploaded:  Update  it  in  place.  Do  not  delete  any  existing  entries.    -  IF  no  RAID  log  uploaded:  Generate  a  new  RAID  log  using  standard  format.   
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  30  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
UPLOADED  FILE:  Current  RAID  Log  (Excel  or  PDF)   PROJECT:  [PROJECT_NAME]   |   Week  of:  [DATE]   THIS  WEEK'S  UPDATES:    New  Risks:  [Describe  or  "None"]    Risk  Status  Changes:  [Probability  /  impact  /  status  changes?]    New  Issues:  [From  standups,  client  calls,  escalations]    Issues  Resolved:  [Any  closed  this  week?]    Assumption  Validations:  [Confirmed  or  disproved?]    Dependency  Updates:  [Completed,  delayed,  or  newly  at  risk?]   Step  1  --  Read  uploaded  RAID  log.  List  all  current  open  items  per  section.  Step  2  --  Apply  updates:    -  Update  existing  entries  (status,  mitigation,  owner  changes)    -  Add  new  entries  with  today's  date    -  Close  resolved  items  (Status  =  Closed  --  do  not  delete)  Step  3  --  Flag  top  3  open  risks  for  this  week's  WSR.  Step  4  --  List  RAID  items  requiring  client  or  sponsor  action.   ASSUMPTION  RULE:  Incomplete  entries  ->  [INCOMPLETE  --  action  needed]  in  Assumptions  Log.  
 
PM-20   |   Executive  Dashboard  /  KPI  Summary  
[TEMPLATE-FIRST]   Upload:  sprint  data  +  budget  actuals  +  defect  log  +  previous  dashboard. 
[NOTE]   No  standard  Kellton  template.  Uses  Power  BI  +  Copilot  or  client-agreed  format.  AI  generates  KPI  narrative  for  governance  packs. 
AI  Prompt  
PM-20   Executive  Dashboard  /  KPI  Summary   [  BOTH  ]
 
You  are  a  senior  Project  Manager  preparing  a  weekly  executive  KPI  summary.   TEMPLATE  INSTRUCTION:    -  IF  dashboard  template  uploaded:  Fill  all  KPI  cells  from  the  uploaded  data  files.    -  IF  no  template:  Generate  standard  KPI  Summary  table.      Add  note:  [ACTION:  Map  to  client/Kellton  dashboard  format.]   UPLOADED  DOCUMENTS:    File  1  --  Sprint  board  /  Jira  export:  velocity  and  completion  data    File  2  (optional)  --  Budget  actuals  (Excel):  planned  vs  actual  spend    File  3  (optional)  --  Defect  log  (Excel):  quality  metrics    File  4  (optional)  --  Previous  KPI  dashboard:  for  trend  comparison   PROJECT:  [PROJECT_NAME]   |   Week  of:  [DATE]   Step  1  --  Extract  all  KPI  data  from  uploaded  files.  Step  2  --  Generate:    1.  EXECUTIVE  SUMMARY  (4  bullets  --  Schedule,  Budget,  Quality,  Risks)    2.  KPI  TABLE:  KPI  |  This  Week  |  Last  Week  |  Trend  |  RAG  |  Source  File    3.  TOP  3  ITEMS  NEEDING  SPONSOR  /  CLIENT  ATTENTION  (specific)    4.  FORECAST:  Will  project  hit  [MILESTONE]  by  [DATE]?    5.  AI  ADOPTION  METRICS:  Activities  completed  with  AI  |  Estimated  time  saved  (hrs)   
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  31  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
Language  suitable  for  non-technical  sponsor  audience.  Missing  data:  [DATA  NOT  PROVIDED  --  source  needed].  ASSUMPTION  RULE:  List  all  gaps  in  Assumptions  Log.  
 
PM-21   |   Timeline  Impact  Analysis  
[TEMPLATE-FIRST]   Upload:  Current  project  plan/schedule  baseline  +  RAID  log. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Delay  Impact  Report  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Delay  Impact  Report  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Impact
 
Summary
 
(revised
 
milestone
 
dates
 
vs
 
baseline)
 *  
Root
 
Cause
 
Analysis
 
(5-Why)
 *  
Recovery
 
Option
 
A
 
--
 
Crashing
 *  
Recovery
 
Option
 
B
 
--
 
Fast-tracking
 *  
Recovery
 
Option
 
C
 
--
 
Scope
 
Reduction
 *  
Recommended
 
Option
 
with
 
Justification
 *  
Client
 
Communication
 
Draft
 
(3
 
sentences)
  
AI  Prompt  
PM-21   Timeline  Impact  Analysis   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  delay  impact  template  uploaded:  Fill  it  from  the  project  plan  and  delay  details.    -  IF  no  template:  Generate  standard  Delay  Impact  Report  format.   UPLOADED  DOCUMENTS:    File  1  --  Current  project  plan  /  schedule  baseline  (Excel,  PDF,  or  .mpp  export)    File  2  (optional)  --  RAID  log:  check  if  this  delay  is  linked  to  a  known  risk   DELAY  DETAILS:    -  Root  Cause:  [What  caused  the  delay]    -  Estimated  Delay:  [X  days  /  weeks]    -  Affected  Milestone:  [Which  milestone?]    -  Client  verbally  informed?  [Y  /  N]    -  Maximum  acceptable  revised  go-live  (client  constraint):  [DATE  or  Unknown]   Step  1  --  Read  uploaded  plan.  Identify  current  baseline  for  all  milestones.  Step  2  --  Calculate  exact  impact  on  every  downstream  milestone.  Step  3  --  Fill  Delay  Impact  Report:    1.  Impact  Summary  --  revised  dates  vs  baseline  (table  format)    2.  Root  Cause  --  5-Why  summary    3.  Recovery  Options:       Option  A:  Crashing  --  effort,  cost,  risk  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  32  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
     Option  B:  Fast-tracking  --  what  can  run  concurrently       Option  C:  Scope  reduction  --  what  can  defer  to  Phase  2    4.  Recommended  option  with  justification    5.  Client  communication  draft  (3  sentences  --  factual,  solution-focused)   ASSUMPTION  RULE:  Where  plan  lacks  detail  ->  [ASSUMED  --  validate  with  tech  lead].  
 
PM-22   |   Budget  Tracking  &  Variance  Analysis  
[TEMPLATE-FIRST]   Upload:  Budget  actuals  sheet  (Excel/PDF)  --  invoices,  timesheets,  or  finance  reports. 
[NOTE]   No  standard  Kellton  template  --  uses  project  financial  tracker  in  Excel  or  agreed  finance  tool. 
AI  Prompt  
PM-22   Budget  Tracking  &  Variance  Analysis   [  BOTH  ]
 
You  are  a  senior  Project  Manager  reviewing  weekly  budget  actuals.   TEMPLATE  INSTRUCTION:    -  IF  budget  tracking  template  uploaded:  Fill  it  from  the  uploaded  actuals  file.    -  IF  no  template:  Generate  standard  Budget  Variance  Analysis  format.   UPLOADED  FILE:  Budget  actuals  (Excel  or  PDF)    Expected:  Category  |  Planned  Cost  |  Actual  Cost  |  Variance  |  Period    Also  accepted:  invoice  exports,  timesheet  summaries,  finance  reports   PROJECT:  [PROJECT_NAME]   |   Week  of:  [DATE]  Contract  Value:  [TOTAL  BUDGET]   |   Billing  Model:  [Fixed  Price  /  T&M  /  Milestone]   Step  1  --  Extract  all  planned  vs  actual  figures  by  category.  Step  2  --  Generate:    1.  VARIANCE  TABLE:  Category  |  Planned  |  Actual  |  Variance  (value)  |  Variance  (%)  |  RAG  |  Reason    2.  OVERALL  BUDGET  HEALTH:  RAG  with  justification    3.  BURN  RATE:  %  budget  used  vs  %  timeline  elapsed.  Will  budget  last?    4.  FORECAST  TO  COMPLETION  (EAC):  Projected  final  cost  at  current  burn  rate    5.  RISK  FLAGS:  Categories  trending  towards  overrun    6.  RECOMMENDATIONS:  Specific  actions  to  bring  back  on  track    7.  NARRATIVE  (3  sentences  for  WSR):  plain  English  summary   ASSUMPTION  RULE:  Incomplete  data  ->  [ASSUMED  --  verify  with  Finance].  
 
PM-23   |   Dependency  Tracking  
[TEMPLATE-FIRST]   Upload:  PRD/BRD  (for  initial  extraction)  +  RAID  log  (Dependencies  tab)  +  Delivery  Plan. 
[NOTE]   No  standard  Kellton  template  --  tracked  within  RAID  Log  (Dependencies  tab)  or  project  schedule. 
AI  Prompt  
PM-23   Dependency  Tracking   [  BOTH  ]
 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  33  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  dependency  tracking  template  uploaded:  Fill  it  from  the  uploaded  documents.    -  IF  no  template:  Generate  standard  Dependency  Log  format.   UPLOADED  DOCUMENTS:    File  1  --  Approved  PRD  /  BRD:  to  extract  all  dependencies  at  project  start    File  2  --  Current  RAID  Log  (Dependencies  tab):  existing  tracked  dependencies    File  3  (optional)  --  Delivery  Plan  /  WBS:  for  schedule  context   PROJECT:  [PROJECT_NAME]   |   Week  of:  [DATE]   FOR  INITIAL  EXTRACTION  from  PRD/BRD:    ID  |  Dependency  |  Source  (PRD  Section)  |  Type  (Internal/External/Third-party)    |  Required  By  (milestone)  |  Owner  |  Risk  if  Delayed   FOR  WEEKLY  UPDATE:    THIS  WEEK'S  CHANGES:  [Completions,  new  blockers,  delays  --  or  "None"]   Generate:    1.  DEPENDENCY  STATUS:  Total  |  On  Track  |  At  Risk  |  Blocked  |  Completed  |  New    2.  AT-RISK  /  BLOCKED:       ID  |  Description  |  Root  Cause  |  Delivery  Plan  Impact  |  Action  |  Escalation?  |  By  When?    3.  NEW  DEPENDENCIES  IDENTIFIED  THIS  WEEK    4.  ACTIONS  REQUIRED:  follow-ups,  owner,  deadline    5.  RISK  NARRATIVE  (2  sentences  for  WSR)  
 
PM-24   |   UAT  Tracking  &  Defect  Theme  Summary  
[TEMPLATE-FIRST]   Upload:  UAT  defect  log  (Jira/ADO  export  or  manual  log)  +  UAT  Summary  template. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  UAT  Defect  Summary  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  UAT  Defect  Summary  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Defect
 
Dashboard
 
(totals
 
by
 
severity)
 *  
Theme
 
Analysis
 
by
 
module/feature
 *  
Trend
 
Analysis
 
(day-on-day)
 *  
Go-Live
 
Risk
 
Assessment
 *  
Client
 
Update
 
Paragraph
  
AI  Prompt  
PM-24   UAT  Tracking  &  Defect  Theme  Summary   [  BOTH  ]
 
You  are  a  senior  Project  Manager  overseeing  UAT.  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  34  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
 TEMPLATE  INSTRUCTION:    -  IF  UAT  summary  template  uploaded:  Fill  it  from  the  defect  log.    -  IF  no  template:  Generate  standard  UAT  Defect  Summary  format.   UPLOADED  FILE:  UAT  defect  log  (Excel,  CSV,  or  PDF  from  Jira  /  test  tool)    Expected:  ID  |  Summary  |  Severity  |  Module  |  Status  |  Date  Raised  |  Date  Resolved   PROJECT:  [PROJECT_NAME]  UAT  Period:  [Start]  to  [Today]   |   Planned  Go-Live:  [DATE]   |   Days  Remaining:  [X]   Step  1  --  Extract  and  categorise  all  defects  from  uploaded  file.  Step  2  --  Fill  the  UAT  summary:    1.  DEFECT  DASHBOARD:  Total  |  Critical  |  High  |  Medium  |  Low  |  Open  |  In  Progress  |  Resolved    2.  THEME  ANALYSIS:  Top  3  modules  |  Count  |  Trend  |  Severity  breakdown    3.  TREND:  New  defects  rising,  stable,  or  falling?  (extract  count  by  date)    4.  GO-LIVE  RISK:       Proceed  /  Delay  /  Conditional  Go-Live       If  Conditional:  exact  conditions  to  be  met  before  go-live    5.  CLIENT  UPDATE  (3  sentences  for  daily  UAT  email):  factual,  plain  English,  no  alarm   ASSUMPTION  RULE:  Blank  severity/module  ->  [ASSUMED  --  verify  with  QA  lead].  
 
PM-25   |   Stakeholder  Engagement  Pulse  
[NOTE]   No  standard  Kellton  template.  AI  drafts  pulse  survey  and  summarises  responses. 
AI  Prompt  
PM-25   Stakeholder  Engagement  Pulse   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  stakeholder  pulse  template  uploaded:  Use  it  for  the  survey  and  summary.    -  IF  no  template:  Generate  standard  5-question  pulse  survey  +  response  summary  format.   TASK  1  --  DRAFT  PULSE  SURVEY:  Project:  [PROJECT_NAME]   |   Period:  [Biweek  dates]  Stakeholder  Group:  [Client  /  Internal  Team  /  Sponsor]   Draft  5-question  pulse  check  covering:    -  Overall  project  confidence  (RAG  from  their  perspective)    -  Communication  effectiveness    -  Concern  or  risk  they  want  to  flag    -  Support  needed  from  PM    -  One  thing  going  well  Max  10  words  per  question.  Use  1-5  scale  or  single-choice  where  possible.   TASK  2  --  SUMMARISE  RESPONSES  (paste  responses  when  received):  RESPONSES:  [Paste  here]   Summarise:    1.  Overall  sentiment  (Positive  /  Neutral  /  Negative)  with  evidence    2.  Top  3  themes  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  35  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
  3.  Red  flags  needing  immediate  PM  action    4.  Recommended  follow-up  actions  
 
PM-40   |   SIT/UAT  Defect  Triage  --  Steering  Summary  
[BOTH]   NEW  from  Prompt  Library  3.2.  Steering-committee  defect  summary  with  entry/exit  criteria  assessment. 
[WATERFALL]   Waterfall-specific  activity. 
AI  Prompt  
PM-40   SIT/UAT  Defect  Triage  --  Steering  Summary   [  WATERFALL  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  steering  committee  report  template  uploaded:  Fill  it  with  the  defect  data  below.    -  IF  no  template:  Generate  standard  Steering  Defect  Triage  Summary  format.   Project:  [PROJECT  NAME]   |   Phase:  [SIT  /  UAT]  Report  date:  [DD-Mon-YYYY]   |   Testing  window:  [DATE]  to  [DATE]   Defect  summary:    Critical  (P1):  [N]  open,  [N]  closed   |   High  (P2):  [N]  open,  [N]  closed    Medium  (P3):  [N]  open,  [N]  closed   |   Low  (P4):  [N]  open,  [N]  closed   |   Re-opened:  [N]   Top  5  open  defects  needing  PM  attention:    [ID]  |  [TITLE]  |  [SEVERITY]  |  [OWNER]  |  [TARGET  FIX  DATE]   (repeat)   Testing  progress:    Planned:  [N]   |   Executed:  [N]   |   Passed:  [N]   |   Failed:  [N]   |   Blocked:  [N]    %  complete:  [X%]   |   Blockers:  [LIST  or  "none"]   Generate:    1.  Defect  dashboard  (RAG  by  severity)    2.  Risk  narrative  --  is  the  defect  profile  acceptable  for  go-live?    3.  Top  3  critical  path  defects  +  recommended  resolution  actions    4.  Entry/exit  criteria  assessment  for  this  testing  phase    5.  Client-facing  defect  summary  email  (non-technical  language)  
 
PM-41   |   Monthly  Business  Review  (MBR)  
[BOTH]   NEW  from  Prompt  Library  4.2.  Full  8-slide  MBR  deck  content  for  steering  committee. 
[TEMPLATE-FIRST]   Upload:  MBR  slide  template  +  milestone  tracker  +  budget  actuals  +  RAID  log. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Monthly  Business  Review  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  36  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Monthly  Business  Review  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Slide
 
1:
 
Title
 
+
 
Project
 
Health
 
Dashboard
 *  
Slide
 
2:
 
Executive
 
Summary
 *  
Slide
 
3:
 
Milestone
 
Tracker
 *  
Slide
 
4:
 
Financial
 
Summary
 *  
Slide
 
5:
 
RAID
 
Summary
 *  
Slide
 
6:
 
Resource
 
Overview
 *  
Slide
 
7:
 
Decisions
 
Required
 *  
Slide
 
8:
 
Next
 
30
 
Days
 
Roadmap
  
AI  Prompt  
PM-41   Monthly  Business  Review  (MBR)   [  BOTH  ]
 
You  are  a  senior  Project  Manager  preparing  for  a  Monthly  Business  Review.   TEMPLATE  INSTRUCTION:    -  IF  MBR  template  uploaded:  Fill  all  slides  from  the  data  below.    -  IF  no  template:  Generate  8-slide  MBR  content  using  standard  format.      Add  note:  [ACTION:  Build  in  PowerPoint  using  Kellton/client  MBR  template.]   Project:  [PROJECT  NAME]   |   PM:  [YOUR  NAME]  MBR  Date:  [DD-Mon-YYYY]   |   Audience:  [Steering  Committee  /  C-Suite  /  Client  Sponsor]  Month:  [MONTH  YEAR]   Month  summary:  [Key  events,  decisions,  accomplishments]   Milestone  tracker:  [MILESTONE  |  Planned  DATE  |  Actual/Forecast  DATE  |  RAG  |  Comment]   Financials:    Total  budget:  [AMOUNT]   |   Consumed  to  date:  [AMOUNT]  ([X%])    Remaining:  [AMOUNT]   |   Forecast  at  completion:  [AMOUNT]   |   Variance:  [AMOUNT/%]   RAID:  Risks  [N]  open  /  [N]  new  /  [N]  closed   |   Actions  [N]  open  /  [N]  overdue        Issues  [N]  open  /  [N]  critical   |   Dependencies  [N]  outstanding   Resources:  [ROLE  |  NAME  |  %  allocation  |  Status]   Next  30  days:  [Key  activities,  milestones,  decisions  due]  Decisions  needed  from  steering:  [LIST  or  "none"]   Generate  slide-by-slide  content  (8  slides)  with  speaker  notes.  
 
PM-42   |   RAID  Update  from  Weekly  Notes  
[BOTH]   NEW  from  Prompt  Library  5.1.  Converts  raw  meeting  notes  or  email  threads  into  structured  RAID  entries. 
AI  Prompt  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  37  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
PM-42   RAID  Update  from  Weekly  Notes   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  RAID  log  template  uploaded:  Add  new  entries  directly  into  the  correct  sections.    -  IF  no  template:  Generate  new  RAID  entries  in  standard  format  ready  for  copy-paste.   Project:  [PROJECT  NAME]   |   Date:  [DD-Mon-YYYY]   Raw  notes  /  meeting  minutes:  ---  [PASTE  WEEKLY  NOTES,  MEETING  MINUTES,  OR  EMAIL  THREADS  HERE]  ---   Classify  each  item  as:  Risk  /  Action  /  Issue  /  Dependency   For  Risks:    Risk  ID  (R-XXX)  |  Description  |  Category  |  Likelihood  (1-5)  |  Impact  (1-5)    |  Risk  Score  (LxI)  |  RAG  |  Mitigation  |  Owner  |  Review  Date   For  Actions:    Action  ID  (A-XXX)  |  Description  |  Owner  |  Due  Date  |  Priority  |  Status   For  Issues:    Issue  ID  (I-XXX)  |  Description  |  Severity  (Critical/High/Med/Low)    |  Impact  |  Resolution  Plan  |  Owner  |  Target  Close  Date   For  Dependencies:    Dep  ID  (D-XXX)  |  Description  |  Type  (Internal/External)  |  Depends  On  |  Due  Date  |  Status   Also  flag:    -  Any  previously  Amber  items  now  turning  Red    -  Any  overdue  actions  requiring  escalation  
 
PM-43   |   Risk  Escalation  Email  
[BOTH]   NEW  from  Prompt  Library  5.2.  Formal  Red-risk  escalation  to  steering  committee  with  decision  request. 
AI  Prompt  
PM-43   Risk  Escalation  Email   [  BOTH  ]
 
You  are  a  senior  Project  Manager  at  Kellton.   TEMPLATE  INSTRUCTION:    -  IF  escalation  email  template  uploaded:  Use  its  structure  and  sign-off  style.    -  IF  no  template:  Use  standard  risk  escalation  email  format.   Project:  [PROJECT  NAME]   |   From:  [YOUR  NAME]   |   To:  [STEERING  /  SPONSOR]  Date:  [DD-Mon-YYYY]   |   Current  RAG:  Red   Risk  /  Issue  description:  [Plain  language  --  what  is  broken  or  at  risk]  Business  impact  if  unresolved:  [Schedule  /  Budget  /  Quality  /  Scope  impact]  Decision  needed  by:  [DD-Mon-YYYY]   |   Why  this  date:  [Explain]  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  38  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
 Options:    Option  A:  [DESCRIPTION]  --  Pros:  [X]   Cons:  [Y]    Option  B:  [DESCRIPTION]  --  Pros:  [X]   Cons:  [Y]   Recommended  option:  [A  /  B  /  Other  +  rationale]  Decision  required:  [Exactly  what  the  stakeholder  must  decide  or  approve]   Draft:  concise  escalation  email  (max  300  words).  Subject  line:  clear  and  urgent  without  being  alarmist.  End  with  specific  call  to  action  and  deadline.  
 
PM-44   |   Weekly  Risk  Review  
[BOTH]   NEW  from  Prompt  Library  5.3.  Assesses  risk  register  week-on-week,  outputs  updated  register  +  WSR  paragraph. 
AI  Prompt  
PM-44   Weekly  Risk  Review   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  risk  register  template  uploaded:  Update  it  in  place  from  the  week's  events.    -  IF  no  template:  Generate  revised  risk  register  in  standard  format.   Project:  [PROJECT  NAME]   |   Review  date:  [DD-Mon-YYYY]   |   Sprint/Week:  [N]   Current  risk  register:    [Risk  ID  |  Description  |  Current  RAG  |  Likelihood  |  Impact  |  Mitigation  |  Owner]   This  week's  events  that  may  affect  risks:    [E.g.  "BA  left  the  team",  "client  delayed  sign-off  by  2  weeks",  "new  requirement  added"]   For  each  existing  risk:    1.  Assess  whether  likelihood  or  impact  changed  based  on  this  week's  events    2.  Recommend  new  RAG  status  with  rationale  if  changing    3.  Note  if  mitigation  plan  needs  updating   Identify  NEW  risks  introduced  this  week  based  on  the  events  described.   Output:    -  Revised  risk  register  table    -  Risk  summary  paragraph  for  this  week's  WSR  
 
PM-45   |   Issue  Log  Entry  &  Resolution  Plan  
[BOTH]   NEW  from  Prompt  Library  7.2.  Formal  issue  log  entry  with  5-Why  root  cause  and  resolution  options. 
AI  Prompt  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  39  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
PM-45   Issue  Log  Entry  &  Resolution  Plan   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  issue  log  template  uploaded:  Add  this  entry  to  it  in  the  correct  format.    -  IF  no  template:  Generate  standard  Issue  Log  entry  +  Resolution  Plan.   Project:  [PROJECT  NAME]   |   Date  raised:  [DD-Mon-YYYY]   |   Raised  by:  [NAME]   Issue  description:  [What  is  broken  or  blocked  and  how  it  was  discovered]  Severity:  [Critical  /  High  /  Medium  /  Low]  Business  impact:  [Effect  on  project  or  client  operations]  Affected  area:  [Integration  /  UI  /  Performance  /  Data  /  Security  /  Process]  What  has  already  been  tried:  [Steps  taken  or  "investigation  not  started"]  Constraints:  [E.g.  "Cannot  deploy  until  release  window  DD-Mon-YYYY"]   Generate:    1.  Issue  Log  entry:  ID  |  Date  |  Description  |  Severity  |  Impact  |  Status  |  Owner    2.  Root  cause  analysis  (5-Whys  or  fishbone  --  choose  most  appropriate)    3.  Resolution  options  with  effort  estimate  and  trade-offs    4.  Recommended  resolution  path  with  owner  and  target  close  date    5.  Client  communication  paragraph  (for  WSR  or  direct  email)  
  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  40  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
PHASE  5   --   Closure Project  wrap-up  --  delivery,  documentation,  knowledge  transfer,  and  formal  closure. PM-26  Readiness   |   PM-27  Closure  Doc   |   PM-28  Lessons  Learned   |   PM-29  Knowledge  Base   |   PM-30  PIR   |   PM-46  Cutover  Runbook   |   PM-47  Closure  Report
 
 
PM-26   |   Delivery  Readiness  Review  
[TEMPLATE-FIRST]   Upload:  Go-Live  Readiness  Checklist  template  +  UAT  sign-off  report  +  test  reports. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Go-Live  Readiness  Checklist  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Go-Live  Readiness  Checklist  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Technical
 
Readiness
 
checks
 *  
UAT
 
Readiness
 
(defect
 
status,
 
sign-off)
 *  
Operations
 
&
 
Support
 
Readiness
 *  
Communication
 
&
 
Training
 
Readiness
 *  
Go
 
/
 
No-Go
 
Recommendation
 *  
Hypercare
 
Plan
 
(48
 
hrs
 
|
 
Week
 
1
 
|
 
Week
 
2-4)
  
AI  Prompt  
PM-26   Delivery  Readiness  Review   [  BOTH  ]
 
You  are  a  senior  Project  Manager  preparing  for  go-live.   TEMPLATE  INSTRUCTION:    -  IF  readiness  checklist  template  uploaded:  Fill  all  items  from  the  uploaded  reports.    -  IF  no  template:  Generate  standard  Go-Live  Readiness  Checklist  +  Go/No-Go  format.   UPLOADED  DOCUMENTS:    File  1  --  UAT  sign-off  report  or  defect  closure  report  (Excel/PDF)    File  2  (optional)  --  Performance  /  security  test  report  (PDF)    File  3  (optional)  --  Readiness  Checklist  template  (if  available)   PROJECT:  [PROJECT_NAME]   |   GO-LIVE  DATE:  [DATE]   STATUS  INPUTS:    -  Training:  [Client  team  trained?  Y/N]    -  Data  Migration:  [Status]    -  Rollback  Plan:  [Documented  and  tested?  Y/N]    -  Hypercare  Support:  [Plan  in  place?  Y/N]    -  Sign-offs  Received:  [List  who  has  signed  off]   Step  1  --  Read  uploaded  reports.  Extract  UAT  and  performance  testing  status.  Step  2  --  Fill  readiness  checklist:    Check  Item  |  Status  (OK  /  Warning  /  Blocked)  |  Evidence  Source  |  Owner  |  Notes  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  41  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
  Group  by:  Technical  |  UAT  |  Operations  |  Communication  &  Training  Step  3  --  Go  /  No-Go  Recommendation:    If  Go:  confirm  all  blockers  resolved.    If  No-Go:  list  exact  conditions  to  meet  with  owner  and  target  date.  Step  4  --  Hypercare  Plan:  First  48  hrs  |  Week  1  |  Week  2-4  |  Escalation  path.   Every  BLOCKER:  [BLOCKER  --  must  resolve  before  go-live].  ASSUMPTION  RULE:  Unconfirmed  items  ->  [UNVERIFIED  --  source  document  needed].  
 
PM-27   |   Closure  Documentation  
[TEMPLATE-FIRST]   Upload:  Project  Closure  template  +  original  Charter  +  UAT  acceptance  evidence  +  final  budget  actuals. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Project  Closure  Document  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Project  Closure  Document  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Project
 
Summary
 *  
Objectives
 
Achievement
 
(Met/Partial/Not
 
Met)
 *  
Final
 
Scope
 
vs
 
Baseline
 *  
Final
 
Budget
 
vs
 
Baseline
 *  
Final
 
Timeline
 
vs
 
Baseline
 *  
Deliverables
 
Sign-off
 
Status
 *  
Outstanding
 
Items
 
/
 
Handover
 
Notes
 *  
Formal
 
Closure
 
Statement
 
and
 
Sign-off
  
AI  Prompt  
PM-27   Closure  Documentation   [  BOTH  ]
 
You  are  a  senior  Project  Manager  preparing  formal  project  closure.   TEMPLATE  INSTRUCTION:    -  IF  closure  document  template  uploaded:  Fill  all  sections  from  the  uploaded  files.    -  IF  no  template:  Generate  standard  Project  Closure  Document  format.   UPLOADED  DOCUMENTS:    File  1  --  Original  Project  Charter  (PDF  or  Word):  original  objectives  and  baseline    File  2  (optional)  --  Final  delivery  sign-off  or  UAT  acceptance  (PDF)    File  3  (optional)  --  Final  budget  actuals  (Excel)   PROJECT:  [PROJECT_NAME]   |   Go-Live:  [DATE]   |   Closure  Date:  [DATE]   ADDITIONAL  INPUTS:    -  Outstanding  Items  /  Handover:  [Deferred  to  support  or  Phase  2]    -  Client  Sign-off:  [Received  /  Pending  from  whom]  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  42  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
 Step  1  --  Read  charter.  Extract  original  objectives,  scope,  budget  baseline.  Step  2  --  Fill  closure  document:    1.  Project  Summary    2.  Objectives  Achievement:  each  charter  objective  --  Met  /  Partially  Met  /  Not  Met  +  evidence    3.  Final  Scope  vs  Baseline  (from  charter)    4.  Final  Budget  vs  Baseline  (from  actuals)    5.  Final  Timeline  vs  Baseline    6.  Deliverables  Sign-off  (from  acceptance  evidence)    7.  Outstanding  Items  /  Handover  Notes    8.  Formal  Closure  Statement  with  sign-off  block   ASSUMPTION  RULE:  Missing  data  ->  [NEEDS  INPUT  --  reason]  in  Assumptions  Log.  
 
PM-28   |   Lessons  Learned  Workshop  
[TEMPLATE-FIRST]   Upload:  Lessons  Learned  template  +  resolved  RAID  log  +  sprint  retro  MOMs  +  CSAT  results. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Lessons  Learned  Report  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Lessons  Learned  Report  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
What
 
Went
 
Well
 
(min
 
5
 
with
 
evidence)
 *  
What
 
Could
 
Be
 
Improved
 
(min
 
5
 
with
 
root
 
cause)
 *  
Process
 
Improvements
 
Recommended
 *  
AI
 
Tool
 
Effectiveness
 
Assessment
 *  
Team
 
Recognition
  
AI  Prompt  
PM-28   Lessons  Learned  Workshop  Preparation   [  BOTH  ]
 
You  are  a  senior  Project  Manager  preparing  a  Lessons  Learned  session.   TEMPLATE  INSTRUCTION:    -  IF  lessons  learned  template  uploaded:  Fill  it  from  the  uploaded  artifacts.    -  IF  no  template:  Generate  standard  Lessons  Learned  Report  format.      Format  as  facilitator  guide  with  workshop  discussion  prompts.   UPLOADED  DOCUMENTS:    File  1  --  Resolved  RAID  log  (Excel/PDF):  closed  risks,  issues,  validated  assumptions    File  2  (optional)  --  Sprint  Retrospective  MOMs  (Word/PDF)    File  3  (optional)  --  Client  satisfaction  survey  results  (PDF/Excel)    File  4  (optional)  --  CR  log  (Excel):  all  change  requests  with  outcomes   PROJECT:  [PROJECT_NAME]   |   Duration:  [X  months]   |   Team  Size:  [X]  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  43  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
 Step  1  --  Read  all  uploaded  documents.  Extract  evidence  for  what  worked  and  what  did  not.  Step  2  --  Fill  Lessons  Learned  template:    1.  WHAT  WENT  WELL  (min  5)  --  specific  evidence  from  uploaded  documents    2.  WHAT  COULD  BE  IMPROVED  (min  5)  --  root  cause  +  recommended  fix    3.  PROCESS  IMPROVEMENTS  --  specific  changes  to  PM  processes,  tools,  or  templates    4.  AI  TOOL  EFFECTIVENESS:       -  Activities  saving  most  time  (from  Tracker)       -  Activities  requiring  most  rework  and  why       -  Recommended  prompt  improvements  for  next  project    5.  TEAM  RECOGNITION  --  achievements  and  contributions  (from  MOMs  if  available)  Step  3  --  Add  workshop  discussion  prompts  for  each  section.   ASSUMPTION  RULE:  Incomplete  documents  ->  [INSUFFICIENT  DATA  --  discuss  in  workshop].  
 
PM-29   |   Knowledge  Base  Article  
[NOTE]   No  standard  Kellton  KB  template.  AI  drafts  from  project  artifacts.  PM  reviews  and  uploads  to  Kellton  KB  /  Confluence. 
AI  Prompt  
PM-29   Knowledge  Base  Article   [  BOTH  ]
 
You  are  a  senior  Project  Manager  creating  a  Knowledge  Base  entry.   TEMPLATE  INSTRUCTION:    -  IF  KB  article  template  uploaded:  Fill  it  from  the  uploaded  project  artifacts.    -  IF  no  template:  Generate  standard  KB  Article  format  for  Kellton  KB  /  Confluence.   UPLOAD  (one  or  more):  Project  Charter  |  Lessons  Learned  report  |  RAID  Log  |  Notable  solutions   PROJECT:  [PROJECT_NAME]   |   Industry:  [DOMAIN]   |   Model:  [Agile/Waterfall]   Generate  KB  article:    1.  TITLE:  [Concise,  searchable  title]    2.  SUMMARY:  What  was  the  project  and  what  problem  did  it  solve?  (3  sentences)    3.  KEY  CHALLENGES  &  RESOLUTIONS:  Top  3-5  with  approach    4.  REUSABLE  ASSETS:  Templates,  prompts,  code  snippets,  or  processes  created    5.  AI  USAGE  HIGHLIGHTS:  AI-assisted  activities  that  worked  best    6.  LESSONS  FOR  FUTURE  PROJECTS:  Top  5  actionable  tips    7.  TAGS:  [Searchable  tags  for  KB  system]   Write  for  a  PM  audience  reading  6  months  from  now.  Specific,  not  generic.  
 
PM-30   |   Post-Implementation  Review  (PIR)  
[TEMPLATE-FIRST]   Upload:  PIR  template  +  original  Charter  +  post-live  incident  log  +  user  adoption  report  +  CSAT. 
TEMPLATE-FIRST  INSTRUCTION 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  44  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Post-Implementation  Review  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Post-Implementation  Review  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Executive
 
Summary
 *  
KPI
 
Scorecard
 
(Target
 
|
 
Actual
 
|
 
Met/Partial/Not
 
Met)
 *  
Technical
 
Performance
 *  
User
 
Adoption
 
&
 
Training
 
Effectiveness
 *  
Issue
 
&
 
Defect
 
Analysis
 
(post
 
go-live)
 *  
Lessons
 
Applied
 *  
Recommendations
 
for
 
Phase
 
2
 
/
 
Future
 *  
Formal
 
Closure
 
Statement
 
and
 
Sign-off
  
AI  Prompt  
PM-30   Post-Implementation  Review  (PIR)   [  BOTH  ]
 
You  are  a  senior  Project  Manager  drafting  a  PIR  30  days  after  go-live.   TEMPLATE  INSTRUCTION:    -  IF  PIR  template  uploaded:  Fill  all  sections  from  the  uploaded  data  files.    -  IF  no  template:  Generate  standard  PIR  format.   UPLOADED  DOCUMENTS:    File  1  --  Original  Project  Charter:  original  objectives  and  KPIs    File  2  (optional)  --  Post-live  incident  /  defect  log  (Excel)    File  3  (optional)  --  User  adoption  report  or  system  analytics  (Excel/PDF)    File  4  (optional)  --  Client  satisfaction  survey  (PDF/Excel)   PROJECT:  [PROJECT_NAME]   |   Go-Live:  [DATE]   |   PIR  Date:  [DATE]   ADDITIONAL  INPUTS:    -  System  Stability:  [Uptime  %,  incident  summary  if  not  in  uploaded  file]    -  Client  Satisfaction:  [CSAT  or  qualitative  feedback  if  not  in  uploaded  file]    -  Hypercare  Issues:  [Key  support  issues  and  resolutions]   Step  1  --  Read  charter.  Extract  original  objectives  and  success  KPIs.  Step  2  --  Read  post-live  data.  Extract  actual  performance  against  each  KPI.  Step  3  --  Fill  PIR  template:    1.  Executive  Summary  --  achievement  vs  charter  objectives    2.  KPI  Scorecard:  Original  Target  |  Actual  (from  data)  |  Met  /  Partial  /  Not  Met    3.  Technical  Performance  --  stability,  incidents,  metrics    4.  User  Adoption  --  usage  stats,  training  effectiveness,  blockers    5.  Issue  &  Defect  Analysis  --  post  go-live  trends    6.  Lessons  Applied  from  Previous  Projects    7.  Phase  2  /  Future  Recommendations  (specific,  actionable)    8.  Formal  Closure  Statement  with  sign-off  block   ASSUMPTION  RULE:  Missing  KPI  data  ->  [DATA  NOT  AVAILABLE  --  manual  input  needed].  
 
PM-46   |   Go-Live  Cutover  Checklist  &  Run  Book  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  45  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
[BOTH]   NEW  from  Prompt  Library  3.3.  Timed  cutover  runbook  with  rollback  plan  and  hypercare  schedule. 
[TEMPLATE-FIRST]   Upload:  Cutover  runbook  template  if  available. 
AI  Prompt  
PM-46   Go-Live  Cutover  Checklist  &  Run  Book   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  cutover  runbook  template  uploaded:  Fill  it  with  the  data  below.    -  IF  no  template:  Generate  standard  Cutover  Run  Book  format.   Project:  [PROJECT  NAME]  Go-live  date:  [DD-Mon-YYYY]   |   Cutover  window:  [HH:MM]  to  [HH:MM]  [TIMEZONE]  Environment:  [Production  /  Cloud  region  /  On-premise]   Components  being  deployed:  [Front-end  UI  /  REST  API  /  Database  migration  /  Integration  layer]   Key  contacts  during  cutover:    Tech  Lead:  [NAME]  --  [CONTACT]   |   DBA:  [NAME]  --  [CONTACT]    Infrastructure:  [NAME]  --  [CONTACT]   |   Client  IT:  [NAME]  --  [CONTACT]    PM:  [NAME]  --  [CONTACT]   Rollback  criteria  (go-back  decision  if):    [E.g.  P1  defect  found  post-deployment  /  Data  migration  >5%  error  rate]   Generate:    1.  Pre-cutover  checklist  (T-5  days,  T-2  days,  T-1  day,  T-4  hours)    2.  Cutover  run  book  (timed  step-by-step  with  owner)    3.  Go/No-Go  sign-off  gate  criteria    4.  Post-go-live  monitoring  checklist  (first  24  hours,  first  week)    5.  Rollback  procedure  outline    6.  Hypercare  support  plan  (first  [2  /  4]  weeks)  
 
PM-47   |   Project  Closure  Report  (Formal)  
[BOTH]   NEW  from  Prompt  Library  8.2.  Formal  closure  report  for  client  and  internal  sponsor  sign-off. 
[TEMPLATE-FIRST]   Upload:  Project  Closure  Report  template  +  Charter  +  UAT  acceptance  +  budget  actuals. 
TEMPLATE-FIRST  INSTRUCTION 
WITH  TEMPLATE   --  IF  YOU  HAVE  A  TEMPLATE:  Upload  it  now  (Kellton  Standard  >  Client  Template  >  PM  Custom,  in  that  priority). WITH  TEMPLATE   --  Say:  "I  am  uploading  our  Project  Closure  Report  template.  Read  it,  list  every  section,  then  wait  for  my  project  data  before  filling  anything." NO  TEMPLATE   --  IF  NO  TEMPLATE  IS  AVAILABLE:  AI  will  generate  output  using  the  standard  industry  structure  below. NO  TEMPLATE   --  Say:  "I  do  not  have  a  template.  Generate  the  Project  Closure  Report  using  standard  industry  best-practice  structure.  Add  a  note  at  the  top:  [ACTION:  Copy  to  standard  template  before  sharing  with  stakeholders.]" 
Standard  sections  AI  should  identify  in  this  template:
 *  
Executive
 
Summary
 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  46  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
*  
Project
 
Objectives
 
(Achieved/Partial/Not
 
Achieved)
 *  
Delivery
 
Performance
 
(scope,
 
time,
 
budget,
 
quality)
 *  
RAID
 
Closure
 
Summary
 *  
Open
 
Items
 
and
 
Transition
 
Plan
 *  
Lessons
 
Learned
 
Headline
 *  
Sign-off
 
Section
 
(PM,
 
Client,
 
Sponsor)
 *  
Recommendations
 
for
 
Hypercare
 
/
 
Support
 
Period
  
AI  Prompt  
PM-47   Project  Closure  Report  (Formal)   [  BOTH  ]
 
You  are  a  senior  Project  Manager.   TEMPLATE  INSTRUCTION:    -  IF  closure  report  template  uploaded:  Fill  all  sections  from  the  data  below.    -  IF  no  template:  Generate  standard  formal  Project  Closure  Report.   Project:  [PROJECT  NAME]   |   PM:  [YOUR  NAME]  Start:  [DD-Mon-YYYY]   |   End:  [DD-Mon-YYYY]   |   Duration:  [X  months]  Client:  [CLIENT  NAME]   |   Internal  Sponsor:  [NAME]   Delivery  summary:    -  Original  scope:  [DESCRIBE]   |   Final  delivered  scope:  [DESCRIBE]    -  Scope  changes:  [N  CRs,  approx  X  days  /  Y  cost]    -  Timeline:  Planned  go-live  [DATE]  --  Actual  [DATE]  --  Variance:  [N  days  /  on  time]    -  Budget:  Planned  [AMOUNT]  --  Actual  [AMOUNT]  --  Variance:  [AMOUNT  /  %]   Quality:  Total  defects  in  testing:  [N]   |   Critical  at  go-live:  [N]   |   Outstanding:  [N]  UAT  sign-off  received:  [Yes  /  No  /  Conditional]   Open  items  at  closure:  [LIST  or  "none"]  Client  satisfaction:  [PASTE  FEEDBACK  /  SCORE  or  "formal  survey  pending"]   Generate  formal  closure  report:    1.  Executive  Summary    2.  Project  Objectives  --  Achieved  /  Partially  /  Not  Achieved    3.  Delivery  Performance  (scope,  time,  budget,  quality)    4.  RAID  closure  summary    5.  Open  items  and  transition  plan    6.  Lessons  Learned  headline  (link  to  full  document)    7.  Sign-off  section  (PM,  Client,  Internal  Sponsor)    8.  Recommendations  for  support  /  hypercare  period  
  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  47  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
PHASE  6   --   Tools  &  Automation  (Claude  Cowork) Automation  commands  --  paste  into  Claude  Cowork  desktop  agent,  NOT  regular  Claude  chat. PM-48  Excel  RAID   |   PM-49  PPT  Deck   |   PM-50  Jira  Sync   |   PM-51  SharePoint
 
 
[IMPORTANT]   IMPORTANT:  All  prompts  in  this  section  are  Claude  Cowork  commands.  Paste  them  into  the  Claude  Cowork  desktop  automation  agent,  NOT  into  Claude.ai  chat  or  Copilot. 
 
PM-48   |   Excel  Agent  --  RAID  Tracker  Creation  
[CLAUDE  COWORK  COMMAND]   Claude  Cowork  command.  Creates  a  fully  formatted,  conditional-formatted  RAID  tracker  Excel  file  from  scratch. 
Cowork  Command  
PM-48   Excel  Agent  --  RAID  Tracker  Creation   [  COWORK  ]
 
COWORK  --  EXCEL  AGENT  Create  a  new  project  RAID  tracker  for  [PROJECT  NAME]  with  the  following  tabs:    1.  Dashboard  --  RAG  summary  counts  for  each  RAID  category   2.  Risks  --  ID  |  Category  |  Description  |  Likelihood  (1-5)  |  Impact  (1-5)               |  Score  |  RAG  |  Mitigation  |  Owner  |  Review  Date  |  Status   3.  Actions  --  ID  |  Description  |  Owner  |  Raised  Date  |  Due  Date                |  Priority  |  Status  |  Notes   4.  Issues  --  ID  |  Description  |  Severity  |  Impact  |  Raised  By  |  Date  Raised               |  Owner  |  Target  Close  |  Status  |  Resolution   5.  Dependencies  --  ID  |  Description  |  Type  |  Depends  On  |  Due  Date                     |  Status  |  Risk  if  Delayed  |  Owner  Apply:   -  Conditional  formatting:  Red  fill  for  Red  RAG,  Amber  for  Amber,  Green  for  Green   -  Data  validation  dropdowns  on  Status,  RAG,  Priority,  Severity  columns   -  Freeze  panes  on  row  1  of  each  tab   -  Auto-filter  on  all  columns   -  Bold  headers  with  navy  (#003366)  fill  and  white  text  Save  as:  [PROJECT  NAME]_RAID_Tracker_v1.0_[DD-Mon-YYYY].xlsx 
 
PM-49   |   PowerPoint  Agent  --  WSR  /  MBR  Deck  
[CLAUDE  COWORK  COMMAND]   Claude  Cowork  command.  Creates  a  formatted  WSR  or  MBR  PowerPoint  deck  with  Kellton  navy/gold  branding. 
Cowork  Command  
PM-49   PowerPoint  Agent  --  WSR/MBR  Deck   [  COWORK  ]
 
COWORK  --  POWERPOINT  AGENT  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  48  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
Create  a  Weekly  Status  Report  slide  deck  for  [PROJECT  NAME]. Week  ending:  [DD-Mon-YYYY]  Design:  Navy  (#003366)  header  bars,  white  content  area,  gold  (#F5A623)  accents. Every  slide:  project  name  top-left,  date  and  page  number  bottom-right.    Slide  1  --  Title:  "[PROJECT  NAME]  Weekly  Status  Report  --  Week  ending  [DATE]"   Slide  2  --  Project  Health  Dashboard:  6-cell  RAG  grid              (Schedule  |  Budget  |  Scope  |  Resources  |  Quality  |  Risk)   Slide  3  --  Week  Summary:  highlights  (max  6  bullets)   Slide  4  --  Milestone  Tracker:  Milestone  |  Planned  |  Forecast  |  Status  |  RAG   Slide  5  --  RAID  Summary:  Category  |  Open  |  New  |  Closed  |  Critical   Slide  6  --  Decisions  Required:  Decision  |  Owner  |  Deadline  |  Consequence   Slide  7  --  Next  2  Weeks:  upcoming  activities  Populate  with  this  data:   [PASTE  WSR  DATA  HERE  or  reference  the  WSR  document  already  generated  by  PM-18]  Save  as:  [PROJECT  NAME]_WSR_[DD-Mon-YYYY].pptx 
 
PM-50   |   Chrome  Agent  --  Jira  /  Azure  DevOps  Sync  
[CLAUDE  COWORK  COMMAND]   Claude  Cowork  command.  Pulls  live  sprint  and  defect  data  from  Jira  or  Azure  DevOps  for  DSR  or  WSR. 
Cowork  Command  
PM-50   Chrome  Agent  --  Jira/Azure  DevOps  Sync   [  COWORK  ]
 
COWORK  --  CHROME  AGENT  Navigate  to  our  Jira  board  at  [URL]  and  log  in  using  my  saved  credentials. Pull  the  following  and  format  for  the  DSR:    1.  Stories  in  "In  Progress":      Story  ID  |  Title  |  Assignee  |  Story  Points  |  Days  in  current  status   2.  Stories  in  "Blocked"  or  "Impediment":      Same  fields  plus  Blocker  description   3.  Stories  moved  to  "Done"  in  the  last  24  hours:      Story  ID  |  Title  |  Points   4.  Sprint  burndown:  total  points  committed  vs  points  remaining  After  pulling  the  data,  open  a  new  Claude  chat. Paste  the  data  and  say:   "Generate  today's  DSR  for  [PROJECT  NAME]  using  this  Jira  data."  Or  paste  directly  into  PM-33  (Daily  Standup  Digest  &  DSR)  prompt. 
 
PM-51   |   File  Management  --  SharePoint  Organisation  
[CLAUDE  COWORK  COMMAND]   Claude  Cowork  command.  Organises  the  project  SharePoint  folder  and  renames  files  to  Kellton  naming  convention. 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  49  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
Cowork  Command  
PM-51   File  Management  --  SharePoint  Organisation   [  COWORK  ]
 
COWORK  --  FILE  MANAGEMENT  Organise  the  project  folder  at  [FOLDER  PATH  /  SHAREPOINT  URL]:  1.  Create  folder  structure  (if  not  already  exists):    /[PROJECT  NAME]/      /01_Project_Management/   /DSR/   /WSR/   /MBR/      /02_RAID_and_Risk/      /03_Change_Requests/      /04_Requirements/      /05_Design/      /06_Testing/      /07_Closure/  2.  Move  files  to  correct  folders:    Files  with  "DSR"  or  "Daily"  in  name     -->  /DSR/    Files  with  "WSR"  or  "Weekly"  in  name    -->  /WSR/    Files  with  "RAID"  or  "Risk"  in  name     -->  /02_RAID_and_Risk/    Files  with  "CR"  or  "Change"  in  name     -->  /03_Change_Requests/  3.  Rename  files  not  following  convention  to:    [PROJECT]_[DOCTYPE]_v[VERSION]_[DD-Mon-YYYY].[EXT]  Report  back:  list  of  files  moved  +  any  that  could  not  be  auto-categorised. 
  
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  50  of  51
 
PM  AI  Assistant  SOP  v1.0   |   51  Activities  (PM-01  to  PM-51)   |   Scrum  &  Waterfall   |   Kellton  Confidential
 
Appendix  A  --  Template  Storage  &  Governance  
Template  Type Storage  Location Naming  Convention 
Update  Owner 
Review  Cycle 
Kellton  Standard 
SharePoint  >  PM  Templates  >  Kellton  Standard  
[DocType]_Kellton_Std_vX.X.docx  
PM  Lead  
Quarterly  
Client-Specific 
SharePoint  >  PM  Templates  >  Client  >  [Client  Name]  
[Client]_[DocType]_vX.X.docx  
Assigned  PM  
Per  client  update  
PM  Custom  (Temp) PM  personal  SharePoint  folder  
[PM]_[DocType]_[Project]_vX.X.docx  
Individual  PM  
After  project  closure  
 
[TIP]   When  a  PM  creates  a  significantly  improved  template,  submit  to  PM  Lead  for  review.  If  approved,  it  replaces  the  Kellton  Standard  version  for  all  future  projects. 
 
Appendix  B  --  Methodology  Coverage  Summary  
Phase Activity  (SOP  ID) BOTH 
SCRUM  Only 
WATERFALL  Only 
Initiation PM-01  to  PM-04  All  4  --  --  
Planning PM-05  to  PM-10,  PM-31  to  PM-32  All  8  --  --  
Execution PM-11  to  PM-17,  PM-33  to  PM-39  11  activities  
PM-11,  PM-33,  PM-34,  PM-35  
PM-36  
Monitoring PM-18  to  PM-25,  PM-40  to  PM-45  13  activities  --  PM-40  
Closure PM-26  to  PM-30,  PM-46  to  PM-47  All  7  --  --  
Tools PM-48  to  PM-51  All  4  (Cowork)  --  --  
TOTAL 51  activities  45  4  2  
 Companion  tool:  PM  AI  SOP  Compliance  Tracker  (PM_AI_SOP_Tracker_v3.1.xlsx) --  log  Compliance  Status,  AI  Maturity,  
Time
 
Saved,
 
and
 
Evidence
 
artifact
 
for
 
PM-01
 
to
 
PM-30.
 Prompt  Library:  PM  AI  Prompt  Library  v1.0 --  source  document  for  PM-31  to  PM-51.  Keep  in  SharePoint  >  PM  Templates  
folder
 
alongside
 
this
 
SOP.
 
Project  Management  Department   |   AI-Assisted  PM  SOP  v1.0   |   Page  51  of  51
 


===== SAMPLE_PROJECTS\BRD.pdf =====

DeploySlot   Product  Requirement  Document  
 
1.  High-Level  Business  Context  &  Objective  
 Target  Audience  
Release  Managers,  Engineering  Managers  (EMs),  Product  Owners  (POs),  QA  Manager  and  a  triage  squad  
consisting
 
of
 
a
 
Project
 
Manager
 
(PM),
 
TL,
 
QA,
 
Shared
 
DevOps,
 
and
 
an
 
SRE.
 
The  Problem  
In  an  enterprise  with  200+  technical  members,  teams  operate  in  isolated  project  silos  with  zero  
cross-project
 
visibility
 
into
 
sprints
 
or
 
planned
 
release
 
dates.
 
Currently,
 
all
 
slot
 
booking
 
happens
 
manually
 
through
 
chaotic
 
email
 
trails,
 
phone
 
calls,
 
and
 
instant
 
messages.
 
The
 
Release
 
Manager
 
must
 
manually
 
check
 
spreadsheets
 
to
 
prevent
 
collisions.
 
This
 
manual
 
process
 
causes
 
scheduling
 
bottlenecks,
 
human
 
error,
 
double-booked
 
shared
 
resources
 
(DevOps/SRE),
 
and
 
delayed
 
deployments.
 
The  MVP  Solution   
A  streamlined  Self-Service  Release  Slot  Booking  Portal  or  Mobile  App.  This  focused  MVP  provides  a  
single
 
source
 
of
 
truth
 
for
 
scheduling.
 
It
 
replaces
 
emails
 
and
 
phone
 
calls
 
with
 
a
 
self-service
 
calendar
 
grid
 
that
 
automatically
 
blocks
 
slot
 
collisions,
 
checks
 
the
 
availability
 
of
 
shared
 
resources,
 
enforces
 
a
 
mandatory
 
PM
 
readiness
 
checklist,
 
and
 
handles
 
an
 
automated
 
5-stage
 
digital
 
approval
 
chain
 
right
 
inside
 
the
 
application.
 
2.  System  Structure  &  Simplified  Resource  Matrix  
The  application  handles  a  flat  multi-project  list  while  maintaining  blind  slot  status  visibility  to  respect  
project
 
privacy.
 
Resource  Mapping  ●  Dedicated  Team:  Project  Manager  (PM),  Technical  Lead,  QA  Lead.  ●  Shared  Enterprise  Pool:  Shared  DevOps  Engineer,  Site  Reliability  Engineer  (SRE).  
3.  Core  Modules  &  Feature  Requirements  
Module  1:  Automated  Self-Service  Slot  Engine  ●  Fixed  Time  Slots:  The  calendar  divides  the  day  into  distinct,  non-overlapping  2-hour  windows  
based
 
on
 
India
 
Business
 
Hours.
 
●  Blind  Availability  Status:  When  a  user  views  the  calendar,  slots  booked  by  other  project  silos  
simply
 
display
 
as
 
"Unavailable."
 
 ●  Automated  Collision  Block:  The  backend  prevents  any  two  projects  from  successfully  booking  the  
exact
 
same
 
time
 
slot
 
window.
 
Module  2:  Shared  Resource  Guardrail  
The  portal  blocks  form  submission  unless  a  unique  engineer  is  assigned  to  the  shared  roles.  
●  The  system  evaluates  the  shared  enterprise  database.  If  DevOps_Engineer_A  or  SRE_A  is  already  
assigned
 
to
 
an
 
active
 
slot
 
during
 
that
 
2-hour
 
window,
 
the
 
portal
 
marks
 
them
 
as
 
"Unavailable"
 
for
 
any
 
other
 
project
 
attempting
 
a
 
booking.
 
Module  3:  PM  Pre-Scheduling  Checklist  Gatekeeper  
Before  a  Project  Manager  can  submit  the  form  and  route  it  to  the  approval  queue,  they  must  explicitly  
interact
 
with
 
a
 
Mandatory
 
Readiness
 
Checklist
 
inside
 
the
 
wizard
 
interface:
 
●  Release  Notes  Upload:  PM  must  upload  a  predefined  template  detailing  user-facing  changes  and  
bug
 
fixes.
 ●  Deployment  Steps:  PM  must  upload  a  predefined  template  for  Devops  to  execute  during  
deployment.
 ●  Handover  to  DevOps/SRE:  PM  must  upload  the  technical  deployment  runbook  document  
containing
 
rollback
 
paths
 
and
 
alert
 
thresholds.
 ●  Enforcement:  The  "Submit  Request"  button  remains  completely  disabled  until  both  files  are  
uploaded
 
and
 
both
 
checkboxes
 
are
 
checked.
 
Module  4:  5-Stage  Sequential  Approval  Workflow  
Once  the  PM  submits  the  checklist-validated  request,  it  enters  a  structured  status  lifecycle.  The  release  
cannot
 
jump
 
stages;
 
it
 
must
 
pass
 
through
 
each
 
sign-off
 
sequentially:
 
[Pending  QA  Approval]  ──►  [Pending  EM  Approval]  ──►  [Pending  Product  Approval]  ──►  [Pending  
DevOps/SRE]
 
──►
 
[Pending
 
Release
 
Mgr]
 
──►
 
[Approved
 
&
 
Scheduled]
 
1.  Stage  1:  QA  Signoff:  The  dedicated  QA  Manager  reviews  test  logs  and  clicks  "Approve"  ->  moves  
to
 
Pending
 
EM
 
Approval.
 2.  Stage  2:  EM  Signoff:  The  project's  Engineering  Manager  reviews  code  metrics  and  clicks  
"Approve"
 
->
 
moves
 
to
 
Pending
 
Product
 
Approval.
 3.  Stage  3:  Product/Business  Signoff:  The  Product  Owner  checks  business  readiness  and  clicks  
"Approve"
 
->
 
moves
 
to
 
Pending
 
DevOps/SRE
 
Approval.
 4.  Stage  4:  DevOps/SRE  Signoff:  The  shared  infrastructure  team  verifies  the  runbook  environment  
metrics
 
and
 
clicks
 
"Approve"
 
->
 
moves
 
to
 
Pending
 
Release
 
Manager
 
Approval.
 
5.  Stage  5:  Release  Manager  Final  Approval:  The  master  Release  Manager  reviews  global  
environment
 
sanity.
 
Clicking
 
"Approve"
 
transitions
 
the
 
window
 
to
 
its
 
final
 
execution
 
state:
 
Approved
 
&
 
Scheduled.
 
4.  Step-by-Step  Release  Scheduling  Wizard  
 
[Step  1:  Details  &  Resources]  ──►  [Step  2:  Mandatory  PM  Checklist  &  Uploads]  ──►  [Step  3:  
Auto-Conflict
 
Check
 
&
 
Route]
 
●  Step  1:  Parameters:  The  PM  selects  their  Project  ID,  picks  an  available  2-hour  time  block  on  the  
calendar,
 
and
 
assigns
 
names
 
to
 
the
 
mandatory
 
squad
 
fields
 
(PM,
 
Dev,
 
QA,
 
Shared
 
DevOps,
 
SRE).
 ●  Step  2:  PM  Checklist:  The  PM  uploads  the  Release  Notes  and  Handover  Documents,  then  ticks  
both
 
confirmation
 
checkboxes
 
to
 
unlock
 
the
 
form.
 ●  Step  3:  Submission  &  Validation:  The  system  evaluates  the  database  transaction.  If  clear,  it  locks  
the
 
resource
 
schedules
 
and
 
routes
 
the
 
release
 
directly
 
into
 
the
 
QA
 
Signoff
 
Queue
 
(Stage
 
1).
 
5.  MVP  Critical  Engineering  Rules   
1.  The  Slot  Collision  &  Overlap  Rule  
The  booking  logic  must  enforce  absolute  mathematical  isolation  on  time  blocks.  If  an  overlap  occurs  
during
 
a
 
concurrent
 
write
 
request
 
for
 
the
 
same
 
environment
 
target,
 
the
 
transaction
 
must
 
abort
 
and
 
roll
 
back
 
to
 
protect
 
calendar
 
integrity.
 
2.  Double-Booking  Constraint  
The  verification  engine  treats  shared  resources  globally.  If  an  SRE  or  DevOps  engineer  is  committed  to  
Project
 
X
 
from
 
7:00
 
AM
 
to
 
9:00
 
AM
 
IST,
 
any
 
parallel
 
submission
 
from
 
another
 
project
 
attempting
 
to
 
claim
 
their
 
time
 
within
 
those
 
exact
 
hours
 
must
 
fail
 
validation.
 
3.  State  Invariance  &  Immutability  ●  Order  Enforcement:  The  backend  database  must  reject  an  approval  update  if  the  preceding  
signature
 
in
 
the
 
5-stage
 
matrix
 
is
 
missing
 
or
 
out
 
of
 
sequence.
 ●  Locking:  Once  a  slot  transitions  to  "Approved  &  Scheduled",  all  fields  become  strictly  read-only.  
If
 
any
 
stage
 
clicks
 
"Reject",
 
the
 
user
 
must
 
click
 
"Cancel
 
Release,"
 
which
 
deletes
 
the
 
entry,
 
frees
 
up
 
the
 
slot
 
globally,
 
and
 
resets
 
the
 
process
 
back
 
to
 
the
 
open
 
pool.
 
3.  Admin  custom  Blackout  Overrides The  master  Release  Manager  (Global  Admin)  must  have  the  ability  to  explicitly  lock  and  flag  
specific
 
days,
 
specific
 
hour
 
blocks,
 
or
 
entire
 
weekends
 
as
 
"Unavailable"
 
directly
 
from
 
an
 
admin
 
control
 
panel.
 
This
 
override
 
must
 
instantly
 
block
 
normal
 
project
 
scheduling
 
for
 
scenarios
 
such
 
as
 
region-specific  business  hour  boundaries,  heavy  system  load  windows,  special  corporate  
occasions,
 
"No-Deploy
 
Fridays"
 
(to
 
prevent
 
weekend
 
incidents),
 
and
 
long
 
festive
 
holidays.
 
When
 
an
 
admin
 
blocks
 
these
 
windows,
 
they
 
must
 
immediately
 
show
 
as
 
"Unavailable"
 
across
 
all
 
siloed
 
project
 
views.
 
 
3.  Automated  Stakeholder  Confirmation  Notifications: Upon  final  Stage  5  approval  by  the  Release  Manager,  the  system  must  instantly  trigger  a  
comprehensive
 
confirmation
 
email
 
to
 
all
 
involved
 
stakeholders.
 
This
 
email
 
serves
 
as
 
the
 
official
 
deployment
 
pass
 
and
 
must
 
include
 
all
 
vital
 
execution
 
details:
 
the
 
confirmed
 
Date
 
and
 
Time
 
Slot
 
(IST),
 
Project
 
ID,
 
Build
 
Version,
 
assigned
 
Triage
 
Squad
 
names,
 
and
 
direct
 
links
 
to
 
the
 
view
 
Release
 
Notes
 
and
 
SRE
 
Handover
 
runbook.
 
 Future  Scope  —  Phase  2  Blueprint   
1.  Advanced  Automation  &  Integrations  
●  Communication  Webhooks  (Slack/Teams):  Automated  chat  notifications.  The  system  
automatically
 
pings
 
the
 
next
 
required
 
approver
 
via
 
chat
 
DM
 
when
 
a
 
release
 
arrives
 
in
 
their
 
queue
 
(e.g.,
 
"Hi
 
Release
 
Manager,
 
DevOps
 
has
 
signed
 
off.
 
Your
 
final
 
Stage
 
5
 
approval
 
is
 
required.").
 
2.  Intelligent  Conflict  Resolution  &  Analytics  
●  Automated  Resource  Recommendation  Engine:  If  a  desired  time  slot  is  unavailable  due  to  a  
shared
 
resource
 
conflict,
 
the
 
platform
 
will
 
suggest
 
alternative
 
open
 
windows
 
or
 
recommend
 
an
 
available
 
backup
 
DevOps
 
engineer.
 ●  Enterprise  Bottleneck  Dashboard:  A  reporting  metrics  interface  tailored  for  the  Release  Manager  
to
 
track
 
which
 
bottleneck
 
stages
 
(QA,
 
EM,
 
Product,
 
DevOps)
 
hold
 
up
 
approvals
 
the
 
longest
 
over
 
time.
 
3.  Advanced  Governance  &  Document  Processing  
●  AI-Powered  Document  Validation:  An  integrated  LLM  parser  will  scan  uploaded  SRE  Handover  
Checklists
 
in
 
real-time
 
to
 
verify
 
that
 
the
 
file
 
contains
 
actual
 
rollback
 
code
 
blocks,
 
valid
 
health
 
check
 
URLs,
 
and
 
active
 
contact
 
numbers,
 
automatically
 
rejecting
 
blank
 
documents.
 


===== SAMPLE_PROJECTS\Release Management Portal (RMP)_FSD.md =====

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


===== SAMPLE_PROJECTS\Release Slot Booking Manager - Client Meeting - Transcript.md =====

## **Release Slot Booking Manager \- Client Meeting \- 2026/07/10 10:31 IST \- Transcript**

# **Attendees**

Manoj Singh, Prabhjot Singh

# **Transcript**

Manoj Singh: as of now. Yes. Team was trying to change the requirement but he refused. No, we'll have to. So, let's start with the question. There are nine questions. Initially, the claw generated 26 questions out of which I think only nine are critical. So, this is a workshop. Okay. So don't mind take your mind help across we will ask you people to join that tell them we get because this is more like cross training also we will be recognizing everything it is not like everything will be notified but I don't

Manoj Singh: I want this to be this time everyone has to come out with something so that is my objective I'll ask you people or their people to come here or you people to go there explain them for 30 minutes strategy come back so that they can again come back to So as I said there were 26 questions then out of which nine are critical questions which I'm going to discuss. So first question is what exactly is the system roles for users let's say you have say release manager then super admin.

Manoj Singh: So there are two ways one for superm we can say SA release manager we can say RM. So is that good approach or do you want to define roles? I think let's make it dynamic. I don't want any UI to do that but let's permission driven roles. So let's define one role called engineering manager one is those are role we can create it right and just map it that in the database somewhere What is the permission of them right? So instead of I don't want to make it hardcoded because the dynamic is more UI but it has to be dynamic as a back end correct you just keep in the DB. So yeah now coming to the roles and all personas one is release manager one is engineering manager right one is product or someone business right and one is this guy and

Manoj Singh: Of course my team also. Next question is the unavailable slot blind to everyone including? No, we are discussing. So there are some queries.

Manoj Singh: So is the unavailable slot blind to everyone including release manager release manager will have the privilege to unavailable for let's be open for everyone it doesn't matter right so if it is unavailable so I just wanted to make it in future what we can do we can make it restrict right what release is going on right others it doesn't matter to them right so for now if

Manoj Singh: It is okay you make okay unavailable but release manager can have a information right can see who has the data and all right right so I think either it is open right doesn't matter let's say there are two project managers one is making the routine and I'm another project manager I can talk to him yeah just shift because I have some priority offline whatever right then he can shift for us other day right so let's be open doesn't matter it should be restricted the project information let's be understood So it is going to open for everyone. I'm I mean both the things. Okay. What are the exact start and end times or is it going to be So India business hours just consider around 10:00 a.m. to 10 to 8 or something. Right. So mostly the deployment slot will be starting from 5 to 9:00 a.m. Okay. And 5 in the evening.

Manoj Singh: No morning 5 to 8 two hours per slot and how many slots can be booked per day? I mean how many 5 to 7 7 to 9 accordingly you can imum two slot in a day maximum two slot but it depends right this guy football match is going on in night right India night right but Z5 is some of the audience they watch in day right so that depend right during this event you can request but the slot m Time period should be maximum two hours and it will be up to the admin to approve it And Minimum two releases. Minimum time 30 minutes 30 minutes or 1 hour.

### 00:05:00

Manoj Singh: But how does it matter because only the point is if it is extending beyond the time maybe some issue or role maybe they can that's a good point yes okay next question this is not making sense to me so I'll skip this describes three mandatory documents but the enforcement rule says both files both check boxes is it two or three uploads or how many check boxes should Total three. One is release Second is steps. What steps deops will exute. Right.

Manoj Singh: And third was can you open the document? Any other go down? Yeah, it's not QA em no document upload deployment step and hand over to devops. hand over right hand over. Okay. Yeah.

Manoj Singh: Any Three more question but we'll discuss that later. if the designated approver is not available, is there a backup delegate mechanism? The release manager will coordinate over email and he has ultimately rights to do that. On rejection, must the entire request be deleted or restarted from the scratch or once it is rejected there should be some reason, right? The release manager should cancel Release manager should be able to delete this slot, right?

Manoj Singh: For example, QA sign off is not there or engineering manager say no no we are not going today I mean there's no confidence on the team or whatever right so they can reject end of the day release manager can delete it release manager has all the rights to do that right and even if let's say one team has said okay they are available another is saying no we're not available then also the deployment won't but mostly I mean it doesn't happen because this is pre-cheduled right the ops engineer x name this guy will come and execute it because deployment is nothing.

Manoj Singh: It is not very straightforward because this guy should know the steps access rights whatever if they are deploying onto Azure there should be repo access there should be DB access all of them is required right before making anything right so it is needed and the same person should be there so I think question is confirmation not supposed to be required for every single person if approved the slot then I think that is release manager right release manager offline

Manoj Singh: they will do see right now they are doing 100% manual right now by the system they should be able to save 90% of time right 10% coordination that might be needed right right otherwise one team will say they're available and another say but no it is not 100% replacement of release manager it is just offload is work right nice right nice so 90% if we can make it automated then we are good okay one more question what do you want to develop web or

Manoj Singh: mobile doesn't matter to me any of I mention either web or mobile whatever compatibility means both au authentication mechanism should be there we have considered simple user ID and password it's like email id and password do email id password only do email ID password no issues token token I mean there are two questions one is ad or just normal that also I'm saying okay I mean which is okay username password is okay for

Manoj Singh: I have a question right do you want to ask that but idle requirement is maybe in future we should have edict because it should be authenticated within ecosystem maybe there are vendors but vendors can be onboarded right Indigo right Kelton is vendor right but let's say Kelton project project manager is raising request for production deployment right so they can be onboarded onto their ecosystem right exactly but I mean to be frank SSO is needed but for now if you wanted to go

### 00:10:00

Manoj Singh: with email address password which is I think if time permits we can try with the SSO also right so last time we were trying to add SS you didn't problem authenticator I know that anyway so I was having two questions one is key should we give any option to the PM or any team to cancel their reports cancel their slot yes of course we can right and for proper

Manoj Singh: There's a proper reason why we are canceling our just box whatever comment or whatever they wanted to and second was question that is saying three checklist should be there which is release notes deployment steps and hand over to DevOps. So the hand over to DevOps availability that will be offline or there will be a slot for devops.

Manoj Singh: that is a offline meeting between S devOps and all right so that is what the check box where okay hand head over is done that's all that is offline thinguling meeting who is available who is not available who will be part of that that is offline so there is a team right one person represent S they will be part of it they will ask lot of questions to technical team why we are doing how we are doing what are the new infra we are provisioning for this particular deployment is it are already there or not whatever Monitoring what should we monitor and during that window as well they do monitor okay if there is deviation in the API response time or something is failing or whatever right they do check all the progress is nothing nowhere there in only the fruit of sources PM who is going to providing that checklist that's it right basically this

Manoj Singh: This is K of release manager actually not project manager coordination can be done by project manager but end of the day release manager will make sure okay this is done then only they will provide final confirmation otherwise they will not but release manager doesn't have any further information that the maximum they are in the offline scheduled meeting release manager is part of it there is in the checklist as well they can say okay this There is a steps right? Mhm. So handover is needed is important Handover is also offline. Maybe whatever right we'll share the meeting with Thank you. recording is

### Meeting ended after 00:13:05 👋

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*



===== TEMPLATES\Action Trakcer.xlsx =====


--- SHEET: Sheet1 ---
('Action Item', 'Owner', 'Target', 'Status', 'Resolve Date', 'Comments')


===== TEMPLATES\DEPENDECNY Tracker Template.xlsx =====


--- SHEET: Sheet1 ---
('ID', 'Description', 'Date Identified', 'Owner', 'Expected Closure Date', 'Closed on', 'Status', 'Priority', 'Impact ', 'Mitigation')


===== TEMPLATES\MOM Template.docx =====


Skipped file type.


===== TEMPLATES\Project Plan Template.xlsx =====


--- SHEET: SPARTA-V1.0 ---
('Task', 'Status', 'Predecessors', 'Duration', 'Planned Start Date', 'Planned End Date', 'Owner', 'Actual End Date', 'Assigned ', 'Baseline Start', 'Baseline Finish', 'Variance', 'Budget', 'Actual', 'Budget Variance')

--- SHEET: Comments ---

--- SHEET: Summary ---
('Project Name',)
('Project Manager',)


===== TEMPLATES\Risk Register Template.xlsx =====


--- SHEET: Sheet1 ---
('ID', 'Description', 'Type', 'Date Identified', 'Owner', 'Target Resolution  Date', 'Closed on', 'Status', 'Priority', 'Impact ', 'Mitigation', 'Risk Trigger', 'Contingency Plan', 'Mitigation', 'Last Reviewed', 'Next Review Date', 'Escalation Level', 'Financial Impact', 'AI Recommendation', 'AI Confidence (%) ')


==================================================
