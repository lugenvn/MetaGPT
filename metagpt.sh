#!/bin/bash
# Quick launcher for MetaGPT with tracking options

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

show_help() {
    echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}           MetaGPT Project Generator - Quick Start${NC}"
    echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}\n"
    
    echo "📖 Usage:"
    echo "   $0 <command> [options]\n"
    
    echo "🎯 Commands:"
    echo "   create <idea>       - Tạo project (VD: create 'Create a calculator')"
    echo "   create-verbose      - Tạo project với verbose logging"
    echo "   status              - Xem trạng thái project hiện tại"
    echo "   monitor             - Monitor real-time progress (cần chạy trong terminal khác)"
    echo "   help                - Hiển thị help này\n"
    
    echo "📝 Examples:"
    echo "   $0 create 'Create a calculator'"
    echo "   $0 create-verbose 'Build a todo app'"
    echo "   $0 status"
    echo "   $0 monitor\n"
    
    echo "📚 Full guide:"
    echo "   cat TRACKING_GUIDE.md\n"
}

case "${1:-help}" in
    create)
        if [ -z "$2" ]; then
            echo "❌ Error: Idea required"
            echo "Usage: $0 create '<project idea>'"
            exit 1
        fi
        echo -e "${BLUE}🚀 Creating project: $2${NC}\n"
        metagpt "$2"
        echo -e "\n${GREEN}✅ Project created!${NC}"
        ;;
    
    create-verbose)
        if [ -z "$2" ]; then
            echo "❌ Error: Idea required"
            echo "Usage: $0 create-verbose '<project idea>'"
            exit 1
        fi
        echo -e "${BLUE}🚀 Creating project with verbose logging: $2${NC}\n"
        python3 run_with_logging.py "$2"
        ;;
    
    status)
        echo -e "${BLUE}📊 Checking project status...${NC}\n"
        python3 track_progress.py
        ;;
    
    monitor)
        echo -e "${YELLOW}👀 Starting real-time monitor (refresh every 2 seconds)${NC}"
        echo -e "${YELLOW}Press Ctrl+C to stop${NC}\n"
        watch -n 2 'python3 track_progress.py'
        ;;
    
    help|--help|-h)
        show_help
        ;;
    
    *)
        echo -e "${YELLOW}Unknown command: $1${NC}\n"
        show_help
        exit 1
        ;;
esac
