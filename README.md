# 🧠 Django Lecture 8 Summary

**Topics Covered:**  
- ⚡ Django Signals  
- 🛠️ Custom Management Commands  
- 📦 Task Logic

---

## ⚡ 1. Django Signals

Django signals let your app respond to events automatically, like when a model is saved or deleted.

🔄 Typical use cases:
- 📧 Send a welcome email after user creation  
- 🗑️ Delete a file when a user is deleted  

---

## 🛠️ 2. Management Commands

Custom management commands are CLI tools you run with `python manage.py`. They're great for automating repetitive tasks.

🧰 Examples:
- 👥 Create multiple users
- 📊 Generate reports
- 🧹 Clean up stale data

---

## 📦 3. Tasks

Tasks are reusable functions that contain your app's business logic.  
They can be triggered from views, signals, or commands.

🔧 Purpose:
- Separate concerns  
- Reuse logic across the project  
- Improve code structure  

---

## 🎯 Goal

Gain practical knowledge on how to:  
- React to system events using signals  
- Build custom automation with commands  
- Organize your logic into clean, reusable tasks
