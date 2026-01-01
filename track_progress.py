#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script theo dõi tiến độ của MetaGPT
Hiển thị thông tin chi tiết từ workspace storage
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


def find_latest_team_storage(workspace_path: Path = None) -> Optional[Path]:
    """Tìm thư mục team storage mới nhất"""
    if workspace_path is None:
        workspace_path = Path("./workspace")
    
    storage_base = workspace_path / "storage"
    if not storage_base.exists():
        return None
    
    # Tìm thư mục mới nhất
    team_dirs = sorted(
        [d for d in storage_base.iterdir() if d.is_dir()],
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )
    
    return team_dirs[0] if team_dirs else None


def print_project_status(team_storage: Path = None):
    """Hiển thị trạng thái project"""
    if team_storage is None:
        team_storage = find_latest_team_storage()
    
    if not team_storage:
        print("❌ Không tìm thấy storage folder. Chạy MetaGPT trước đã!")
        return
    
    print(f"\n{'='*80}")
    print(f"📊 TRẠNG THÁI PROJECT")
    print(f"{'='*80}")
    print(f"Storage: {team_storage}\n")
    
    # Xem team.json
    team_file = team_storage / "team.json"
    if team_file.exists():
        try:
            with open(team_file) as f:
                team_data = json.load(f)
            
            # Hiển thị members
            if "members" in team_data:
                members = team_data["members"]
                print(f"👥 Team Members ({len(members)}):")
                for member in members:
                    role = member.get("role", "?")
                    state = member.get("state", "?")
                    print(f"   ├─ {role}: {state}")
            
            # Hiển thị environment info
            if "environment" in team_data and "history" in team_data["environment"]:
                history = team_data["environment"]["history"]
                print(f"\n📝 Actions History ({len(history)} total):")
                # Hiển thị vài action gần đây
                for action in history[-5:]:
                    action_type = action.get("type", "?")
                    agent = action.get("agent", "?")
                    print(f"   ├─ [{agent}] {action_type}")
        except Exception as e:
            print(f"   ⚠️  Không thể đọc team.json: {e}")
    
    print(f"\n{'='*80}\n")


def show_help():
    """Hiển thị hướng dẫn"""
    print("""
📍 CÁCH TRACKING METAGPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ CHẠY VỚI LOGGING VERBOSE:
   
   python3 run_with_logging.py "Create a calculator"
   
   Sẽ hiển thị tất cả DEBUG logs trong quá trình chạy

2️⃣ XEM STORAGE STRUCTURE:
   
   python3 track_progress.py
   
   Hiển thị thông tin chi tiết về project: agents, actions, messages

3️⃣ XEM LOG FILES:
   
   # Log file default của MetaGPT
   cat logs/metagpt_*.log
   
   # Hoặc theo dõi real-time
   tail -f logs/metagpt_*.log

4️⃣ CÁCH HIỂU LOGS:
   
   [2025-01-01 09:45:00] | INFO | metagpt.team - Team hired agents
   [2025-01-01 09:45:01] | INFO | metagpt.roles.product_manager - ProductManager is working
   [2025-01-01 09:45:02] | DEBUG | metagpt.provider.openai_api - Calling OpenAI API
   [2025-01-01 09:45:03] | INFO | metagpt.actions.write_prd - Completed PRD document

5️⃣ WORKSPACE STRUCTURE:
   
   workspace/
   ├── <project_name>/           # Code được sinh ra
   │   ├── src/
   │   ├── package.json
   │   └── README.md
   └── storage/                   # Internal state của team
       └── <team_id>/
           ├── agents/            # Lưu state của từng agent
           ├── messages.jsonl     # Tất cả messages giữa agents
           └── ...

6️⃣ ENVIRONMENT VARIABLES:
   
   # Tăng log level
   export METAGPT_LOG_LEVEL=DEBUG
   
   # Tắt logging to file
   export METAGPT_LOG_FILE=
   
   metagpt "Create a calculator"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        show_help()
    else:
        print_project_status()
        show_help()
