#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 MetaGPT Unified Runner
Chạy MetaGPT + track progress + in logs - TẤT CẢ TRONG 1 SCRIPT!

Dùng: python3 unified_runner.py "Create a calculator"
"""

import asyncio
import json
import sys
import threading
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

from metagpt.logs import define_log_level
from metagpt.software_company import generate_repo


def find_latest_team_storage(workspace_path: Path = None) -> Optional[Path]:
    """Tìm thư mục team storage mới nhất"""
    if workspace_path is None:
        workspace_path = Path("./workspace")
    
    storage_base = workspace_path / "storage"
    if not storage_base.exists():
        return None
    
    team_dirs = sorted(
        [d for d in storage_base.iterdir() if d.is_dir()],
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )
    
    return team_dirs[0] if team_dirs else None


def print_status():
    """In trạng thái project hiện tại"""
    team_storage = find_latest_team_storage()
    
    if not team_storage:
        return
    
    team_file = team_storage / "team.json"
    if not team_file.exists():
        return
    
    try:
        with open(team_file) as f:
            team_data = json.load(f)
        
        # In status
        print("\n" + "="*80)
        print("📊 STATUS UPDATE")
        print("="*80)
        
        if "members" in team_data:
            members = team_data["members"]
            print(f"\n👥 Team ({len(members)} members):")
            for member in members:
                role = member.get("role", "?")
                state = member.get("state", "?")
                # Thêm indicator
                if "working" in state.lower():
                    indicator = "🟢"
                elif "completed" in state.lower():
                    indicator = "✅"
                else:
                    indicator = "⭕"
                print(f"   {indicator} {role}: {state}")
        
        if "environment" in team_data and "history" in team_data["environment"]:
            history = team_data["environment"]["history"]
            print(f"\n📝 Actions ({len(history)} total):")
            for action in history[-3:]:
                agent = action.get("agent", "?")
                action_type = action.get("type", "?")
                print(f"   ├─ [{agent}] {action_type}")
        
        print("\n" + "="*80 + "\n")
    except Exception as e:
        pass


def monitor_thread():
    """Thread monitor status mỗi 10 giây"""
    while True:
        time.sleep(10)
        print_status()


def run_metagpt(idea: str, **kwargs):
    """
    Chạy MetaGPT với logging + tracking
    
    Args:
        idea: Project idea
        **kwargs: Additional arguments for generate_repo
    """
    
    # Setup logging - DEBUG level for detailed logs
    define_log_level(print_level="DEBUG", logfile_level="DEBUG", name="metagpt_run")
    
    print("\n" + "="*80)
    print(f"🚀 METAGPT - UNIFIED RUNNER")
    print("="*80)
    print(f"📝 Project: {idea}")
    print(f"🕐 Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"\n🎯 Logs + Status sẽ được in dưới đây...")
    print("="*80 + "\n")
    
    # Start monitoring thread (in status mỗi 10 giây)
    monitor_proc = threading.Thread(target=monitor_thread, daemon=True)
    monitor_proc.start()
    
    try:
        # Chạy MetaGPT (logs tự động in ra console từ define_log_level)
        result = generate_repo(idea, **kwargs)
        
        print("\n" + "="*80)
        print(f"✅ HOÀN THÀNH!")
        print("="*80)
        print(f"📁 Project tại: {result}")
        print(f"🕐 Hoàn thành lúc: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80 + "\n")
        
        return result
        
    except Exception as e:
        print("\n" + "="*80)
        print(f"❌ LỖI: {e}")
        print("="*80 + "\n")
        raise


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['--help', '-h', 'help']:
        print("""
╔════════════════════════════════════════════════════════════════════════════╗
║         MetaGPT Unified Runner - Logs + Tracking in 1 Script               ║
╚════════════════════════════════════════════════════════════════════════════╝

📖 Usage:
   python3 unified_runner.py <idea> [options]

📝 Examples:
   python3 unified_runner.py "Create a calculator"
   python3 unified_runner.py "Build a todo app" --investment 5.0
   python3 unified_runner.py "Create a game" --n-round 10

🎯 Features:
   ✅ Logs console (DEBUG level - tất cả chi tiết)
   ✅ Track team status (update mỗi 10 giây)
   ✅ Real-time progress monitoring
   ✅ Everything in 1 script!

📊 Output:
   - DEBUG logs in real-time
   - Team status update every 10 seconds
   - Final summary khi hoàn thành

╔════════════════════════════════════════════════════════════════════════════╗
        """)
        sys.exit(1)
    
    idea = sys.argv[1]
    
    # Parse additional options
    kwargs = {
        "investment": 3.0,
        "n_round": 5,
        "code_review": True,
        "implement": True,
    }
    
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
    
    # Run MetaGPT with logging + tracking
    run_metagpt(idea, **kwargs)


if __name__ == "__main__":
    main()
