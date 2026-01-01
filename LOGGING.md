# 📊 MetaGPT Logging & Tracking Guide

## ✅ Câu Hỏi: "Có in logs ra console không? Làm thế nào để tracking?"

**Trả lời: CÓ! MetaGPT tự động in logs ra console. Có 3 cách để tracking chi tiết hơn:**

---

## 🎯 3 Cách Tracking MetaGPT

### **0️⃣ RECOMMENDED - Unified Runner (Logs + Tracking in 1)**

```bash
python3 unified_runner.py "Create a calculator"
```

⭐⭐⭐⭐⭐ **KHUYÊN DÙNG NHẤT**  
✅ **Logs console (DEBUG level chi tiết)**  
✅ **Monitor team status mỗi 10 giây**  
✅ **Tất cả trong 1 script, không cần terminal khác!**

---

### **1️⃣ Chạy Đơn Giản - Logs Tự Động In Ra Console**

```bash
metagpt "Create a calculator"
```

**Console output sẽ hiển thị:**
```
2026-01-01 10:00:00.123 | INFO | metagpt.team - Team hired 5 agents
2026-01-01 10:00:01.456 | INFO | metagpt.roles.product_manager - Writing PRD
2026-01-01 10:00:05.012 | INFO | metagpt.provider.openai_api - API called
2026-01-01 10:00:10.345 | INFO | metagpt.roles.architect - Design completed
...
```

✅ **Có log console luôn**  
⭐⭐ **Chi tiết cơ bản** (INFO level)  
✅ **Real-time**

---

### **2️⃣ Xem Chi Tiết DEBUG Logs - Dùng Script**

```bash
# Cách 1: Dùng script Python
python3 run_with_logging.py "Create a calculator"

# Cách 2: Set environment variable
export METAGPT_LOG_LEVEL=DEBUG
metagpt "Create a calculator"
```

**Output sẽ rất chi tiết:**
```
2026-01-01 10:00:00 | INFO | metagpt.team - Team hired 5 agents
2026-01-01 10:00:01 | DEBUG | metagpt.roles.product_manager - Starting action: write_prd
2026-01-01 10:00:02 | DEBUG | metagpt.provider.openai_api - POST /chat/completions with model=gpt-4-turbo
2026-01-01 10:00:03 | DEBUG | metagpt.utils.token_counter - Input: 256 tokens, Output: 512 tokens
2026-01-01 10:00:05 | INFO | metagpt.actions.write_prd - PRD document completed
2026-01-01 10:00:10 | DEBUG | metagpt.roles.architect - Starting action: write_design
...
```

✅ **Logs rất chi tiết**  
⭐⭐⭐⭐⭐ **Chi tiết tối đa** (DEBUG level)  
✅ **Real-time**

---

### **3️⃣ Monitor Real-Time Status - Xem Team State**

Chạy trong terminal khác:
```bash
python3 track_progress.py
```

**Output sẽ hiển thị:**
```
================================================================================
📊 TRẠNG THÁI PROJECT
================================================================================
Storage: workspace/storage/team

👥 Team Members (5):
   ├─ TeamLeader: working
   ├─ ProductManager: working (100% PRD done)
   ├─ Architect: working (50% Design in progress)
   ├─ Engineer2: idle
   └─ DataAnalyst: idle

📝 Actions History (8 total):
   ├─ [ProductManager] write_prd
   ├─ [Architect] write_design
   └─ [Engineer2] write_code
================================================================================
```

✅ **Xem trạng thái agents**  
⭐⭐⭐ **Chi tiết vừa đủ**  
⚠️ **Cần refresh bằng tay (hoặc dùng watch)**

---

## 🛠️ Công Cụ Sẵn Có

| File | Mục đích | Cách dùng |
|------|---------|----------|
| `unified_runner.py` | ⭐ **Logs + Tracking** (KHUYÊN DÙNG) | `python3 unified_runner.py "idea"` |
| `run_with_logging.py` | Chạy với DEBUG logs | `python3 run_with_logging.py "idea"` |
| `track_progress.py` | Monitor team state | `python3 track_progress.py` |
| `metagpt.sh` | Wrapper script dễ dùng | `./metagpt.sh create "idea"` |

---

## 📋 So Sánh 3 Cách

| Yếu tố | Cách 0 (Unified) | Cách 1 | Cách 2 | Cách 3 |
|--------|---------|--------|--------|--------|
| **Console Log** | ✅ DEBUG | ✅ INFO | ✅ DEBUG | ⚠️ No |
| **Team Status** | ✅ Auto | ❌ | ✅ Manual | ⚠️ Manual |
| **Chi tiết** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Real-time** | ✅ | ✅ | ✅ | ⚠️ Manual |
| **Terminal cần** | 1️⃣ | 1️⃣ | 2️⃣ | 1-3 |
| **Khó độ** | ⭐ | ⭐ | ⭐ | ⭐ |
| **Best for** | **KHUYÊN DÙNG** | Quick | Dev | Monitor |

---

## 💡 Lựa Chọn Nên Dùng

### **⭐ Muốn dùng tốt nhất? Dùng Unified Runner!**
```bash
python3 unified_runner.py "Create a calculator"
```
→ Vừa in DEBUG logs, vừa monitor team status - Tất cả trong 1!

### **Muốn chạy nhanh?**
```bash
metagpt "Create a calculator"
```
→ Logs hiển thị console, xong!

### **Muốn xem từng bước chi tiết?**
```bash
python3 run_with_logging.py "Create a calculator"
```
→ Tất cả DEBUG logs hiển thị, biết chính xác code chạy ở đâu

### **Muốn monitor long-running task?**
```bash
python3 unified_runner.py "Create complex app"
```
→ Vừa xem logs, vừa monitor status (mỗi 10 giây)

---

## 🔧 Log Levels Explained

| Level | Hiển thị | Khi nào thấy | Dùng khi |
|-------|----------|-------------|---------|
| **ERROR** | Chỉ lỗi | Khi xảy ra lỗi | Debugging failures |
| **WARNING** | Lỗi + cảnh báo | Khi có vấn đề nhỏ | Production mode |
| **INFO** | Key events (mặc định) | `metagpt "idea"` | Normal operation |
| **DEBUG** | Tất cả chi tiết | `python3 run_with_logging.py` | Development |

---

## 📝 Ví Dụ Logs Bạn Sẽ Thấy

```
[TIMESTAMP] | LEVEL | MODULE:LINE - MESSAGE

2026-01-01 10:00:00.123 | INFO | metagpt.const:15 - Package root set to /path/to/MetaGPT
2026-01-01 10:00:01.456 | INFO | metagpt.team:50 - Team hired [ProductManager, Architect, Engineer]
2026-01-01 10:00:02.789 | DEBUG | metagpt.roles.product_manager:100 - Starting action: write_prd
2026-01-01 10:00:03.012 | DEBUG | metagpt.provider.openai_api:175 - POST /chat/completions
2026-01-01 10:00:03.245 | DEBUG | metagpt.utils.token_counter:50 - Input: 256 tokens
2026-01-01 10:00:05.678 | DEBUG | metagpt.provider.openai_api:180 - Response received: 512 tokens
2026-01-01 10:00:06.901 | INFO | metagpt.actions.write_prd:200 - PRD document completed
2026-01-01 10:00:07.134 | INFO | metagpt.roles.architect:100 - Starting architecture design
2026-01-01 10:00:12.567 | INFO | metagpt.roles.architect:105 - Architecture completed
2026-01-01 10:00:13.890 | INFO | metagpt.roles.engineer:200 - Starting code implementation
```

---

## 🚀 Quick Start Examples

### **Ví dụ 1: Tạo project với console logs**
```bash
$ metagpt "Create a calculator"

2026-01-01 10:00:00.123 | INFO | metagpt.team - Team hired 5 agents
2026-01-01 10:00:01.456 | INFO | metagpt.roles.product_manager - Writing PRD
...
✅ Project created in workspace/
```

### **Ví dụ 2: Tạo project với DEBUG logs chi tiết**
```bash
$ python3 run_with_logging.py "Create a calculator"

================================================================================
🚀 Bắt đầu tạo project: Create a calculator
================================================================================

2026-01-01 10:00:00 | INFO | metagpt.team - Team started
2026-01-01 10:00:01 | DEBUG | metagpt.roles.product_manager - action=write_prd
2026-01-01 10:00:02 | DEBUG | metagpt.provider.openai_api - tokens=256
...
================================================================================
✅ Hoàn thành! Project: workspace/calculator_xxx
================================================================================
```

### **Ví dụ 3: Monitor real-time + logs**
```bash
# Terminal 1
$ python3 run_with_logging.py "Create a complex app"

2026-01-01 10:00:00 | INFO | metagpt.team - Starting
2026-01-01 10:00:01 | INFO | ProductManager - Starting
...

# Terminal 2 (in parallel)
$ watch -n 2 'python3 track_progress.py'

📊 TRẠNG THÁI PROJECT
👥 Team Members (5):
   ├─ ProductManager: working
   ├─ Architect: working
   └─ Engineer2: waiting
```

---

## ⚡ Advanced Usage

### **Capture & Save Logs**
```bash
# Save to file
metagpt "Create app" > my_project.log 2>&1

# Monitor file changes
tail -f my_project.log

# Search logs
grep "ERROR" my_project.log
grep "write_prd" my_project.log
```

### **Set Custom Log Level**
```bash
# DEBUG level (maximum verbosity)
METAGPT_LOG_LEVEL=DEBUG metagpt "Create app"

# INFO level (default)
METAGPT_LOG_LEVEL=INFO metagpt "Create app"

# WARNING only
METAGPT_LOG_LEVEL=WARNING metagpt "Create app"
```

### **Parse Logs Programmatically**
```python
import json
import subprocess

# Run and capture output
result = subprocess.run(
    ['metagpt', 'Create calculator'],
    capture_output=True,
    text=True
)

# Print logs line by line
for line in result.stderr.split('\n'):
    if 'ERROR' in line or 'WARNING' in line:
        print(f"Alert: {line}")
```

---

## 🎯 Workflow Recommendations

### **For Development**
```bash
# Terminal 1: Run with debug logs
python3 run_with_logging.py "Create app"

# Terminal 2: Monitor status
watch -n 2 'python3 track_progress.py'

# Terminal 3: Check workspace
ls -la workspace/
```

### **For Production**
```bash
# Run normally with console logs
metagpt "Create app" > project.log 2>&1

# Keep logs for reference
cat project.log  # Review later
```

### **For Long Tasks**
```bash
# Run in background
nohup python3 run_with_logging.py "Create complex app" > project.log 2>&1 &

# Monitor from another terminal
tail -f project.log
```

---

## ❓ FAQ

**Q: MetaGPT có in logs ra console không?**  
A: ✅ CÓ! Mặc định in INFO level logs. Chạy `metagpt "idea"` là có logs luôn.

**Q: Muốn xem DEBUG logs thì sao?**  
A: Chạy `python3 run_with_logging.py "idea"` hoặc `export METAGPT_LOG_LEVEL=DEBUG && metagpt "idea"`

**Q: Logs được lưu ở đâu?**  
A: Console (STDOUT), có thể export bằng `> file.log 2>&1`

**Q: Sao không thấy logs?**  
A: Dùng `metagpt "idea" 2>&1 | head -30` để xem (stderr có logs)

**Q: Muốn xem tất cả thông tin chi tiết không?**  
A: Dùng `python3 run_with_logging.py "idea"` - sẽ thấy DEBUG logs rất chi tiết

---

## 📚 File Structure

```
MetaGPT/
├── run_with_logging.py       # Script chạy với DEBUG logs
├── track_progress.py         # Script monitor team state
├── metagpt.sh               # Wrapper script dễ dùng
├── LOGGING.md               # This file - hướng dẫn đầy đủ
│
├── workspace/
│   ├── calculator_1767235826/  # Generated code
│   └── storage/
│       └── team/
│           ├── team.json
│           └── agents/
```

---

## ✨ Tóm Tắt

| Cần | Làm gì |
|-----|--------|
| **⭐ Tốt nhất** | `python3 unified_runner.py "idea"` ← Logs + Tracking |
| Chạy nhanh | `metagpt "idea"` → Logs console |
| Xem chi tiết | `python3 run_with_logging.py "idea"` → DEBUG logs |
| Monitor status | `python3 track_progress.py` → Team state |

---

**Bây giờ bạn biết cách tracking MetaGPT đầy đủ! 🎉**

```bash
# Quick test
metagpt "Create a calculator"  # Thấy logs ngay!
```
