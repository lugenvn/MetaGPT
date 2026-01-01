# 📊 MetaGPT Logging & Tracking - Quick Reference

## ✅ **MetaGPT CÓ IN LOGS RA CONSOLE LUÔN!**

Khi chạy → **Logs tự động hiển thị trong console**

---

## 🎯 **4 Cách Tracking**

### **⭐ 0️⃣ KHUYÊN DÙNG - Unified Runner** (Logs + Tracking in 1)
```bash
python3 unified_runner.py "Create a calculator"
```
Vừa in DEBUG logs, vừa monitor team status - **TẬT CẢ TRONG 1!**

### **1️⃣ Chạy Đơn Giản** (Logs INFO level)
```bash
metagpt "Create a calculator"
```

### **2️⃣ DEBUG Logs Chi Tiết** (Xem tất cả thông tin)
```bash
python3 run_with_logging.py "Create a calculator"
```

### **3️⃣ Monitor Real-Time** (Xem team state)
```bash
python3 track_progress.py
```

---

## 📚 **File Hướng Dẫn**

- **LOGGING.md** ← **ĐỌC CÁI NÀY** (hướng dẫn đầy đủ, tất cả trong 1 file)
- **run_with_logging.py** - Script chạy với DEBUG logs
- **track_progress.py** - Script monitor status
- **unified_runner.py** - ⭐ Script gộp logs + tracking (KHUYÊN DÙNG)
- **metagpt.sh** - Wrapper script easy-to-use

---

## 💡 **Tóm Tắt**

```bash
# ⭐ Tốt nhất - Logs + Tracking in 1
python3 unified_runner.py "Create app"

# Chạy nhanh - có log console
metagpt "Create app"

# Xem DEBUG chi tiết
python3 run_with_logging.py "Create app"

# Monitor status
python3 track_progress.py

# Xem hướng dẫn đầy đủ
cat LOGGING.md
```

---

**Tất cả trong LOGGING.md, không cần doc khác! 📖**
**unified_runner.py là giải pháp tốt nhất! ⭐**
