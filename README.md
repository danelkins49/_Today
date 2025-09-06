---
title: Daily Workflow Logs
owner: Dan Elkins
date: 2025-09-06
status: Active
---

# 🗂️ Daily Workflow Logs

Welcome to the **Daily Workflow Logs** repo.  
This repository is where I document everything I do each day:  
tasks, meetings, learnings, experiments, and progress.

---

## 📖 Purpose
- Create a **daily habit** of documenting work and learning.  
- Track progress over time with clean Git history.  
- Build a **Single Source of Truth (SSOT)** for all activities.  
- Enable automation in the future (summaries, dashboards, reports).  

---

## 📂 Repo Structure

```
/logs/              # All daily log files stored here
   YYYY-MM-DD.md    # Example daily log file
README.md           # This file — guide, template, and index
```

---

## 📝 How to Use

1. Each evening, run the script (or manually copy) to generate a new daily log.  
2. Logs are stored in `/logs/` with the filename format:  
   ```
   YYYY-MM-DD.md
   ```
3. Each log uses the template below (with front matter).  
4. Commit the log file to Git at the end of the day.  

---

## 🧩 Daily Log Template

```markdown
---
title: Daily Log
owner: Dan Elkins
date: YYYY-MM-DD
status: Draft
---

# Daily Log

## Date
[Day, Month Day, Year]

---

## Plan
- [ ] ...

---

## Meetings
- ...

---

## Log
- ...

---

## Review
**Highlights**
- ...

**Roadblocks**
- ...

**Next Steps**
- ...

---

## Notes
- ...
```

---

## 📅 Index of Logs

This section links to all existing logs in `/logs/`.

- [2025-09-06](logs/2025-09-06.md)

(Add each new day here or automate the index generation.)

---

## ⚙️ Automation Plan

The next step is to create a script (`newlog.sh`) that will:  
1. Generate a new markdown file inside `/logs/` using today’s (or tomorrow’s) date.  
2. Insert the template automatically.  
3. Append the new file to the **Index of Logs** in this `README.md`.

---
