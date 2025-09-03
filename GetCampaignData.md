kpis:
  - "Accounts flagged correctly vs. benchmarks"
risk_level: "medium"
---

## Purpose
Define a repeatable process for pulling ad account performance data and comparing results against benchmarks.

## Scope
Applies to all active paid social ad accounts under Ads Maintenance.  

## Preconditions
- Access to Swydo
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
