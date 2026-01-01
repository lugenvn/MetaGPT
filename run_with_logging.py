#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để chạy MetaGPT với verbose logging
Theo dõi từng bước của quá trình tạo project
"""

import asyncio
import sys
from pathlib import Path

# Setup verbose logging trước khi import MetaGPT
from metagpt.logs import define_log_level
from metagpt.software_company import generate_repo

# Cấu hình log level cao nhất - DEBUG
define_log_level(print_level="DEBUG", logfile_level="DEBUG", name="metagpt_run")

def run_project(idea: str, **kwargs):
    """Chạy MetaGPT với logging chi tiết"""
    print(f"\n{'='*80}")
    print(f"🚀 Bắt đầu tạo project: {idea}")
    print(f"{'='*80}\n")
    
    try:
        # Chạy MetaGPT
        result = generate_repo(idea, **kwargs)
        
        print(f"\n{'='*80}")
        print(f"✅ Hoàn thành! Project được lưu tại:")
        print(f"   {result}")
        print(f"{'='*80}\n")
        
        return result
    except Exception as e:
        print(f"\n{'='*80}")
        print(f"❌ Lỗi: {e}")
        print(f"{'='*80}\n")
        raise

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_with_logging.py '<project idea>' [options]")
        print("\nExample:")
        print("  python run_with_logging.py 'Create a todo app'")
        print("  python run_with_logging.py 'Create a calculator' --investment 5.0")
        sys.exit(1)
    
    idea = sys.argv[1]
    
    # Parse additional options
    kwargs = {
        "investment": 3.0,
        "n_round": 5,
        "code_review": True,
        "implement": True,
    }
    
    # Xử lý các argument bổ sung
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--investment":
            kwargs["investment"] = float(sys.argv[i+1])
            i += 2
        elif sys.argv[i] == "--n-round":
            kwargs["n_round"] = int(sys.argv[i+1])
            i += 2
        elif sys.argv[i] == "--no-code-review":
            kwargs["code_review"] = False
            i += 1
        else:
            i += 1
    
    # Chạy
    run_project(idea, **kwargs)
