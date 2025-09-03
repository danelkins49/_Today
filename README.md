# Tuesday September 2, 2025

## Plan
- Get Ad Account Performance Data

From Dashboard Pull last 7 days (excluding today) of the following metrics
m1 Cost-per-lead
m2 Cost-per-click(all)
m3 Click-through-rate(all)
m4 Click-through-rate(link)
m5 Frequency

Determine if last 7 days is performing below performance benchmarks per the campaign audience (Decision branch?)****


b1 VET IUL : $20
b2 Veterans : $18
b3 First Responders : $15
b4 First Responder IUL : $16
b5 Trucker : $20
b6 Trucker IUL : $20
b7 FEX : $15
b8 General IUL : $15
b9 Mortgage : $15
b10 Nurse : $15
b11 Teachers : $15
b12 Construction/Contractor : $15
b13 Annuity: $35



Take note of all accounts that are high last 7 days....based off the benchmarks (Decison branch?)****


Pull last 3 days (excluding today) of the following metrics, for all accounts that are "high/benchmark" last 7 days
m1 Cost-per-lead
m2 Cost-per-click(all)
m3 Click-through-rate(all)
m4 Click-through-rate(link)
m5 Frequency



Pull today (excluding today) of the following metrics, for all accounts that are "high/benchmark" last 3 days
m1 Cost-per-lead
m2 Cost-per-click(all)
m3 Click-through-rate(all)
m4 Click-through-rate(link)
m5 Frequency


Send all accounts that are high today and/or last 3 days to account examination stage.


--------------------------------------------------------------------


kpis:
  - "Accounts flagged correctly vs. benchmarks"
risk_level: "medium"
---

## Purpose
Define a repeatable process for pulling ad account performance data and comparing results against benchmarks.

## Scope
Applies to all active paid social ad accounts under Ads Maintenance.  

## Preconditions
- Access to dashboard/reporting system
- Current benchmark list (see below)
- Ability to export 7-day, 3-day, and daily performance data

## Procedure

### Step 1 — Pull 7-day performance data
- From dashboard, pull the last **7 days (excluding today)** of the following metrics:
  - Cost per Lead (CPL)
  - Cost per Click (All)
  - CTR (All)
  - CTR (Link)
  - Frequency

### Step 2 — Compare to benchmarks
**Benchmarks (CPL):**
- VET IUL: $20  
- Veterans: $18  
- First Responders: $15  
- First Responder IUL: $16  
- Trucker: $20  
- Trucker IUL: $20  
- FEX: $15  
- General IUL: $15  
- Mortgage: $15  
- Nurse: $15  
- Teachers: $15  
- Construction/Contractor: $15  
- Annuity: $35  

**Decision Branch A**  
- If 7-day CPL ≤ benchmark → Mark account **Healthy**, end process for this account.  
- If 7-day CPL > benchmark → Mark account **High**, continue to Step 3.  

### Step 3 — Pull 3-day performance data
For all **High** accounts, pull the last **3 days (excluding today)** of metrics:  
- CPL, CPC (All), CTR (All), CTR (Link), Frequency  

**Decision Branch B**  
- If 3-day CPL ≤ benchmark → Mark account **Recovered**, end process for this account.  
- If 3-day CPL > benchmark → Continue to Step 4.  

### Step 4 — Pull 1-day performance data
For all accounts still **High** after 3 days, pull **Today (excluding today)** metrics:  
- CPL, CPC (All), CTR (All), CTR (Link), Frequency  

**Decision Branch C**  
- If 1-day CPL > benchmark → Escalate to **Account Examination Stage**.  
- Else → Mark account **Under Watch**, monitor next cycle.  
















--------------------------------------------------------------------

## Validation
- Accounts above benchmark are escalated properly.
- Healthy accounts are not escalated incorrectly.
- Escalation list delivered daily.

## Rollback / Escalation
- If data pull is incomplete, rerun export and recheck benchmarks.
- If escalation flagged in error, correct and reclassify account.

















































- Create Campaign
Navigate to ad account
Create new campaign with leads as objective and setup type "manual leads campaign"
Name the campaign with appropriate convention
Select campaign budget
Select the budget
Select Special Ads Category "Financial Products and Services"
Navigate to adset level
Name the adset
Select the appropriate facebook page
Select performance goal "maximize Number of leads"









Determine if last 3 days is performing below performance benchmarks per campaign audience ****(Decsion Branch)****









## Meetings
-

## Log
-

# Review
    - Highlights:
    - Roadblocks:
    - Next steps:


