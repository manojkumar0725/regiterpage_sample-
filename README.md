# 🚀 Register & Login Project - Setup Guide

## 📁 Project Structure
```
auth_project/
├── app.py                  ← Flask main file
├── requirements.txt        ← Python packages
├── database_setup.sql      ← MySQL setup
├── templates/
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
└── static/
    ├── css/style.css
    └── js/main.js
```

---

## ✅ STEP 1 — Software Install பண்ணுங்க

### Python Install:
👉 https://python.org/downloads → Download → Install
(⚠️ "Add Python to PATH" checkbox tick பண்ணுங்க)

### MySQL Install:
👉 https://dev.mysql.com/downloads/installer/
- MySQL Installer download பண்ணுங்க
- Setup போது: Developer Default தேர்ந்தெடுக்கவும்
- Root password வைக்கவும் (நினைவில் வைக்கவும்!)

---

## ✅ STEP 2 — Project Folder Setup

1. `auth_project` folder எங்கே வேணும்னாலும் வைக்கவும்
   (Example: `C:\Users\YourName\auth_project`)

2. அந்த folder-ல் மேலே உள்ள எல்லா files-ம் இருக்கணும்

---

## ✅ STEP 3 — MySQL Database Setup

MySQL Workbench அல்லது Command Prompt திறக்கவும்:

```sql
-- Command Prompt-ல்:
mysql -u root -p
-- Password கொடுக்கவும்

-- பிறகு database_setup.sql-ல் உள்ள commands run பண்ணவும்:
source C:/Users/YourName/auth_project/database_setup.sql
```

அல்லது MySQL Workbench திறந்து `database_setup.sql` file open பண்ணி Run பண்ணவும்.

---

## ✅ STEP 4 — app.py-ல் Database Password மாற்றவும்

`app.py` file திறந்து இந்த part மாற்றவும்:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "உங்கள் MySQL password இங்கே",  # ← இதை மாற்றவும்
    "database": "auth_db"
}
```

---

## ✅ STEP 5 — Python Packages Install

Command Prompt / Terminal திறந்து:

```bash
cd C:\Users\YourName\auth_project

pip install -r requirements.txt
```

---

## ✅ STEP 6 — Project Run பண்ணுங்க

```bash
python app.py
```

இப்படி காட்டும்:
```
 * Running on http://0.0.0.0:5000
 * Running on http://192.168.x.x:5000
```

---

## ✅ STEP 7 — Browser-ல் திறக்கவும்

### Laptop-ல்:
👉 http://localhost:5000

### Mobile-ல் (same WiFi-ல் இருக்கணும்):
1. Laptop-ல் Command Prompt திறந்து `ipconfig` type பண்ணவும்
2. "IPv4 Address" பார்க்கவும் (Example: 192.168.1.5)
3. Mobile browser-ல்: http://192.168.1.5:5000

---

## 📱 Pages:
- `/register` → Registration page
- `/login`    → Login page
- `/dashboard`→ Login ஆன பிறகு இந்த page வரும்
- `/logout`   → Logout

---

## ⚠️ Common Errors & Fix:

| Error | Fix |
|-------|-----|
| `pip not found` | Python install போது "Add to PATH" tick பண்ணவும் |
| `Access denied for user 'root'` | app.py-ல் password சரியா கொடுக்கவும் |
| `Unknown database 'auth_db'` | database_setup.sql run பண்ணவும் |
| `ModuleNotFoundError: flask` | `pip install flask` run பண்ணவும் |
| Mobile-ல் connect ஆகல | Laptop-ல் Windows Firewall → Port 5000 allow பண்ணவும் |

---

## 🔒 Security Features:
- Password SHA-256 hash-ஆக database-ல் store ஆகும்
- Duplicate userid / email check இருக்கு
- Session-based login management
