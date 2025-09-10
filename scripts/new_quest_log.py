#!/usr/bin/env python3
from datetime import date, timedelta
from pathlib import Path
import sys

print("[new_quest_log] Starting...", flush=True)

RESET_DOW = 1  # 0=Mon, 1=Tue, ... -> Tuesday reset
XP_GOAL = 70

SCRIPT_PATH = Path(__file__).resolve()
SCRIPTS_DIR = SCRIPT_PATH.parent
REPO_ROOT = SCRIPTS_DIR.parent
DEST_DIR = REPO_ROOT / "quest_logs"

print(f"[new_quest_log] Script path: {SCRIPT_PATH}", flush=True)
print(f"[new_quest_log] Repo root:   {REPO_ROOT}", flush=True)
print(f"[new_quest_log] Logs dir:    {DEST_DIR}", flush=True)

DEST_DIR.mkdir(parents=True, exist_ok=True)

today = date.today()
days_since_reset = (today.weekday() - RESET_DOW) % 7
reset_date = today - timedelta(days=days_since_reset)
end_date = reset_date + timedelta(days=6)
iso_week = reset_date.isocalendar().week

fname = f"quest_log_w{iso_week:02d}_{reset_date.isoformat()}.md"
fpath = DEST_DIR / fname

if fpath.exists():
    print(f"[new_quest_log] File already exists: {fpath}")
    print("[new_quest_log] No new file created.")
    sys.exit(0)

def month_label(d):
    m = d.strftime("%b")
    return "Sept" if m == "Sep" else m

def nice_range(a, b):
    if a.month == b.month and a.year == b.year:
        return f"{month_label(a)} {a.day}–{b.day}, {a.year}"
    elif a.year == b.year:
        return f"{month_label(a)} {a.day} – {month_label(b)} {b.day}, {a.year}"
    else:
        return f"{month_label(a)} {a.day}, {a.year} – {month_label(b)} {b.day}, {b.year}"

week_range = nice_range(reset_date, end_date)
day_names = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
ordered = [(reset_date + timedelta(days=i), day_names[(RESET_DOW + i) % 7]) for i in range(7)]

md = f"""---
title: Quest Log
week: {week_range}
xp_goal: {XP_GOAL}
---

# 🎮 Weekly Quest Log
**Week of:** {week_range}  
**XP Goal:** {XP_GOAL}  
**Result:** Level Up ✅ / ❌

---

## 📅 Daily Quests
"""

for d, name in ordered:
    md += f"""
### {name} ({d.isoformat()})
- [ ] Morning Lock-in (+10)
- [ ] Night Lock-in (+10)
- [ ] AI Quest (+5)
- [ ] Workout (+5)
- [ ] No Relapse (-5 if fail)

**XP Earned:** 0/{XP_GOAL}

---
"""

md += """
## 🧾 Weekly Summary
- **Total XP:** ___ / 70  
- **Level Up:** ✅ or ❌  
- **Loot Earned:** [Reward yourself if you hit 70 XP]  
- **Notes:** Wins, lessons, or adjustments for next week  
"""

fpath.write_text(md, encoding="utf-8")
print(f"[new_quest_log] Created: {fpath}")
print("[new_quest_log] Done.", flush=True)
