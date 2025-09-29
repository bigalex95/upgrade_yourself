#!/bin/bash

# Run script for NeetCode C++ solutions
# Usage: ./run.sh [program_name|project_number] [args...]

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

BUILD_DIR="build"
BIN_DIR="$BUILD_DIR/bin"

# Function to list available programs with numbers
list_programs() {
    echo -e "${BLUE}Available NeetCode Programs:${NC}"
    echo -e "${CYAN}=============================${NC}"
    
    if [ -d "$BIN_DIR" ] && [ "$(ls -A $BIN_DIR 2>/dev/null)" ]; then
        local count=1
        for program in "$BIN_DIR"/*; do
            if [ -x "$program" ]; then
                basename="$(basename "$program")"
                # Try to extract problem info
                category="$(echo "$basename" | cut -d'_' -f1-3 | sed 's/_/ /g' | sed 's/and/\&/g')"
                problem="$(echo "$basename" | cut -d'_' -f4- | sed 's/_/ /g')"
                
                echo -e "  ${GREEN}$count.${NC} $problem ${CYAN}($category)${NC}"
                echo -e "      ${YELLOW}Command: ./run.sh $count${NC} or ${YELLOW}./run.sh $basename${NC}"
                ((count++))
            fi
        done
    else
        echo -e "  ${YELLOW}No programs found. Build the project first with './build.sh'${NC}"
    fi
    
    echo ""
    echo -e "${BLUE}Usage Examples:${NC}"
    echo -e "  ${GREEN}./run.sh --list${NC}     # Show this list"
    echo -e "  ${GREEN}./run.sh 1${NC}          # Run program #1"
    echo -e "  ${GREEN}./run.sh arrays_and_hashing_two_sum${NC}  # Run by name"
}

# Function to get program by number
get_program_by_number() {
    local target_num=$1
    local current_num=1
    
    if [ -d "$BIN_DIR" ]; then
        for program in "$BIN_DIR"/*; do
            if [ -x "$program" ]; then
                if [[ $current_num -eq $target_num ]]; then
                    basename "$program"
                    return 0
                fi
                ((current_num++))
            fi
        done
    fi
    return 1
}

# Check if build directory exists
if [ ! -d "$BUILD_DIR" ]; then
    echo -e "${RED}Error: Build directory not found.${NC}"
    echo -e "${YELLOW}Please run './build.sh' first to build the project.${NC}"
    exit 1
fi

# Check if bin directory exists
if [ ! -d "$BIN_DIR" ]; then
    echo -e "${RED}Error: Binary directory not found.${NC}"
    echo -e "${YELLOW}Please run './build.sh' first to build the project.${NC}"
    exit 1
fi

# Handle arguments
if [ $# -eq 0 ]; then
    echo -e "${YELLOW}Usage: $0 <program_name|project_number> [args...]${NC}"
    echo ""
    list_programs
    exit 1
fi

# Handle special arguments
case "$1" in
    --list|-l|list)
        list_programs
        exit 0
        ;;
    --help|-h|help)
        echo "Usage: $0 <program_name|project_number> [args...]"
        echo ""
        echo "Options:"
        echo "  --list, -l    List all available programs with numbers"
        echo "  --help, -h    Show this help message"
        echo "  NUMBER        Run program by number (e.g., './run.sh 1')"
        echo "  NAME          Run program by exact name"
        echo ""
        list_programs
        exit 0
        ;;
    [0-9]*)
        # Running by number
        PROGRAM_NAME=$(get_program_by_number "$1")
        if [[ -z "$PROGRAM_NAME" ]]; then
            echo -e "${RED}Error: Program number $1 not found.${NC}"
            echo ""
            list_programs
            exit 1
        fi
        echo -e "${BLUE}Running program #$1: $PROGRAM_NAME${NC}"
        shift  # Remove program number from arguments
        ;;
    *)
        # Running by name
        PROGRAM_NAME="$1"
        shift  # Remove program name from arguments
        ;;
esac

# Check if program exists
PROGRAM_PATH="$BIN_DIR/$PROGRAM_NAME"
if [ ! -f "$PROGRAM_PATH" ]; then
    echo -e "${RED}Error: Program '$PROGRAM_NAME' not found.${NC}"
    echo ""
    list_programs
    exit 1
fi

# Check if program is executable
if [ ! -x "$PROGRAM_PATH" ]; then
    echo -e "${RED}Error: Program '$PROGRAM_NAME' is not executable.${NC}"
    exit 1
fi

# Run the program
echo -e "${YELLOW}$(printf '=%.0s' {1..50})${NC}"
"$PROGRAM_PATH" "$@"
EXIT_CODE=$?
echo -e "${YELLOW}$(printf '=%.0s' {1..50})${NC}"

if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}Program completed successfully.${NC}"
else
    echo -e "${RED}Program exited with code: $EXIT_CODE${NC}"
fi

exit $EXIT_CODE

# Check if program exists
PROGRAM_PATH="$BIN_DIR/$PROGRAM_NAME"
if [ ! -f "$PROGRAM_PATH" ]; then
    echo -e "${RED}Error: Program '$PROGRAM_NAME' not found.${NC}"
    echo ""
    list_programs
    exit 1
fi

# Check if program is executable
if [ ! -x "$PROGRAM_PATH" ]; then
    echo -e "${RED}Error: Program '$PROGRAM_NAME' is not executable.${NC}"
    exit 1
fi

# Run the program
echo -e "${BLUE}Running: $PROGRAM_NAME${NC}"
echo -e "${YELLOW}" + "=" * 50 + "${NC}"
"$PROGRAM_PATH" "$@"
EXIT_CODE=$?
echo -e "${YELLOW}" + "=" * 50 + "${NC}"

if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}Program completed successfully.${NC}"
else
    echo -e "${RED}Program exited with code: $EXIT_CODE${NC}"
fi

exit $EXIT_CODE