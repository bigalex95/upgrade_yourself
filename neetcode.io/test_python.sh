#!/bin/bash

# Python-specific test runner
# Usage: ./test_python.sh [problem_number]

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Function to list Python problems
list_python_problems() {
    echo -e "${BLUE}Available Python Problems:${NC}"
    echo -e "${YELLOW}=========================${NC}"
    
    local count=1
    for category in */; do
        if [[ -d "$category" && "$category" != "build/" ]]; then
            category_name=$(basename "$category")
            
            for file in "$category"*.py; do
                if [[ -f "$file" ]]; then
                    filename=$(basename "$file" .py)
                    echo -e "  ${GREEN}$count.${NC} $filename ${YELLOW}($category_name)${NC}"
                    ((count++))
                fi
            done
        fi
    done
}

# Function to get Python problem by number
get_python_problem_by_number() {
    local target_num=$1
    local current_num=1
    
    for category in */; do
        if [[ -d "$category" && "$category" != "build/" ]]; then
            for file in "$category"*.py; do
                if [[ -f "$file" ]]; then
                    if [[ $current_num -eq $target_num ]]; then
                        echo "$file"
                        return 0
                    fi
                    ((current_num++))
                fi
            done
        fi
    done
    return 1
}

# Handle arguments
case "${1:-}" in
    --list|-l|list)
        list_python_problems
        exit 0
        ;;
    --help|-h|help)
        echo "Usage: $0 [problem_number|--list]"
        echo ""
        list_python_problems
        exit 0
        ;;
    [0-9]*)
        PYTHON_FILE=$(get_python_problem_by_number "$1")
        if [[ -z "$PYTHON_FILE" ]]; then
            echo -e "${RED}Error: Python problem number $1 not found.${NC}"
            list_python_problems
            exit 1
        fi
        echo -e "${BLUE}Running Python problem #$1: $(basename "$PYTHON_FILE")${NC}"
        echo "=================================================="
        uv run python "$PYTHON_FILE"
        echo "=================================================="
        echo -e "${GREEN}Python test completed.${NC}"
        ;;
    "")
        echo "Usage: $0 [problem_number|--list]"
        echo ""
        list_python_problems
        ;;
    *)
        echo "Unknown option: $1"
        exit 1
        ;;
esac