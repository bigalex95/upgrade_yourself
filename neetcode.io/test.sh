#!/bin/bash

# Test script for NeetCode C++ solutions
# Usage: ./test.sh [options|project_number]

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

BUILD_DIR="build"
VERBOSE=false
PARALLEL_JOBS=$(nproc 2>/dev/null || echo 4)
SPECIFIC_TEST=""

# Function to list all available problems with numbers
list_problems() {
    echo -e "${BLUE}Available NeetCode Problems for Testing:${NC}"
    echo -e "${CYAN}=========================================${NC}"
    
    local count=1
    for category in */; do
        if [[ -d "$category" && "$category" != "build/" ]]; then
            category_name=$(basename "$category")
            echo -e "\n${YELLOW}📁 $category_name${NC}"
            
            for file in "$category"*.cpp; do
                if [[ -f "$file" ]]; then
                    filename=$(basename "$file" .cpp)
                    target_name="${category_name}_${filename}"
                    target_name=$(echo "$target_name" | tr '[:upper:]' '[:lower:]' | sed 's/ /_/g' | sed 's/&/and/g' | sed 's/\//_/g')
                    
                    echo -e "  ${GREEN}$count.${NC} $filename ${CYAN}(test: $target_name)${NC}"
                    ((count++))
                fi
            done
        fi
    done
    
    echo ""
    echo -e "${BLUE}Usage:${NC}"
    echo -e "  ${GREEN}./test.sh${NC}           # Run all tests"
    echo -e "  ${GREEN}./test.sh 1${NC}         # Run specific test by number"
    echo -e "  ${GREEN}./test.sh --verbose${NC} # Run with verbose output"
}

# Function to get problem by number
get_problem_by_number() {
    local target_num=$1
    local current_num=1
    
    for category in */; do
        if [[ -d "$category" && "$category" != "build/" ]]; then
            for file in "$category"*.cpp; do
                if [[ -f "$file" ]]; then
                    if [[ $current_num -eq $target_num ]]; then
                        filename=$(basename "$file" .cpp)
                        category_name=$(basename "$category")
                        target_name="${category_name}_${filename}"
                        echo "$(echo "$target_name" | tr '[:upper:]' '[:lower:]' | sed 's/ /_/g' | sed 's/&/and/g' | sed 's/\//_/g')"
                        return 0
                    fi
                    ((current_num++))
                fi
            done
        fi
    done
    return 1
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -j|--jobs)
            PARALLEL_JOBS="$2"
            shift 2
            ;;
        --build)
            echo -e "${BLUE}Building project before running tests...${NC}"
            ./build.sh
            shift
            ;;
        --list|-l|list)
            list_problems
            exit 0
            ;;
        -h|--help|help)
            echo "Usage: $0 [options|project_number]"
            echo ""
            echo "Options:"
            echo "  -v, --verbose     Enable verbose output"
            echo "  -j, --jobs N      Run tests with N parallel jobs"
            echo "  --build          Build project before running tests"
            echo "  --list           List all available problems with numbers"
            echo "  NUMBER           Run specific test by number (e.g., './test.sh 1')"
            echo "  -h, --help       Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0                # Run all tests"
            echo "  $0 1              # Run test #1"
            echo "  $0 --verbose      # Run tests with verbose output"
            echo "  $0 --build        # Build and then run tests"
            echo "  $0 -j 8           # Run tests with 8 parallel jobs"
            echo ""
            list_problems
            exit 0
            ;;
        [0-9]*)
            # Running specific test by number
            SPECIFIC_TEST=$(get_problem_by_number "$1")
            if [[ -z "$SPECIFIC_TEST" ]]; then
                echo -e "${RED}Error: Test number $1 not found.${NC}"
                echo ""
                list_problems
                exit 1
            fi
            echo -e "${YELLOW}Running test #$1: $SPECIFIC_TEST${NC}"
            shift
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            echo "Use '$0 --help' for usage information."
            exit 1
            ;;
    esac
done

# Check if build directory exists
if [ ! -d "$BUILD_DIR" ]; then
    echo -e "${RED}Error: Build directory not found.${NC}"
    echo -e "${YELLOW}Please run './build.sh' first to build the project.${NC}"
    echo -e "${BLUE}Or use './test.sh --build' to build and test.${NC}"
    exit 1
fi

# Check if CTest is available
if ! command -v ctest &> /dev/null; then
    echo -e "${RED}Error: CTest is not available.${NC}"
    echo "Please make sure CMake is properly installed."
    exit 1
fi

# Change to build directory
cd "$BUILD_DIR"

# Prepare CTest arguments
CTEST_ARGS=()
if [ "$VERBOSE" = true ]; then
    CTEST_ARGS+=("--verbose")
fi
CTEST_ARGS+=("--parallel" "$PARALLEL_JOBS")
CTEST_ARGS+=("--output-on-failure")

# Add specific test filter if specified
if [[ -n "$SPECIFIC_TEST" ]]; then
    CTEST_ARGS+=("-R" "$SPECIFIC_TEST")
fi

# Run tests
if [[ -n "$SPECIFIC_TEST" ]]; then
    echo -e "${BLUE}Running specific test: $SPECIFIC_TEST${NC}"
else
    echo -e "${BLUE}Running all tests...${NC}"
fi

if ctest "${CTEST_ARGS[@]}"; then
    
    if [[ -n "$SPECIFIC_TEST" ]]; then
        echo -e "${GREEN}Test $SPECIFIC_TEST passed! 🎉${NC}"
    else
        echo -e "${GREEN}All tests passed! 🎉${NC}"
    fi
    
    # Show test summary
    echo ""
    echo -e "${BLUE}Test Summary:${NC}"
    ctest --print-labels 2>/dev/null || echo "No test labels found"
else
    EXIT_CODE=$?
    
    echo -e "${RED}Some tests failed! ❌${NC}"
    echo ""
    echo -e "${BLUE}To debug failed tests:${NC}"
    echo -e "  ${YELLOW}./test.sh --verbose${NC}  # Run with verbose output"
    echo -e "  ${YELLOW}cd build && ctest --rerun-failed --verbose${NC}  # Rerun only failed tests"
    exit $EXIT_CODE
fi

# Show available executables
echo ""
echo -e "${BLUE}Available executables:${NC}"
if [ -d "bin" ] && [ "$(ls -A bin 2>/dev/null)" ]; then
    count=1
    for program in bin/*; do
        if [ -x "$program" ]; then
            basename="$(basename "$program")"
            echo -e "  ${GREEN}$count. ./run.sh $basename${NC}"
            ((count++))
        fi
    done
else
    echo -e "  ${YELLOW}No executables found.${NC}"
fi

# Check if build directory exists
if [ ! -d "$BUILD_DIR" ]; then
    echo -e "${RED}Error: Build directory not found.${NC}"
    echo -e "${YELLOW}Please run './build.sh' first to build the project.${NC}"
    echo -e "${BLUE}Or use './test.sh --build' to build and test.${NC}"
    exit 1
fi

# Check if CTest is available
if ! command -v ctest &> /dev/null; then
    echo -e "${RED}Error: CTest is not available.${NC}"
    echo "Please make sure CMake is properly installed."
    exit 1
fi

# Change to build directory
cd "$BUILD_DIR"

# Prepare CTest arguments
CTEST_ARGS=()
if [ "$VERBOSE" = true ]; then
    CTEST_ARGS+=("--verbose")
fi
CTEST_ARGS+=("--parallel" "$PARALLEL_JOBS")
CTEST_ARGS+=("--output-on-failure")

# Run tests
echo -e "${BLUE}Running all tests...${NC}"


if ctest "${CTEST_ARGS[@]}"; then
    
    echo -e "${GREEN}All tests passed! 🎉${NC}"
    
    # Show test summary
    echo ""
    echo -e "${BLUE}Test Summary:${NC}"
    ctest --print-labels 2>/dev/null || echo "No test labels found"
else
    EXIT_CODE=$?
    
    echo -e "${RED}Some tests failed! ❌${NC}"
    echo ""
    echo -e "${BLUE}To debug failed tests:${NC}"
    echo -e "  ${YELLOW}./test.sh --verbose${NC}  # Run with verbose output"
    echo -e "  ${YELLOW}cd build && ctest --rerun-failed --verbose${NC}  # Rerun only failed tests"
    exit $EXIT_CODE
fi

# Show available executables
echo ""
echo -e "${BLUE}Available executables:${NC}"
if [ -d "bin" ] && [ "$(ls -A bin 2>/dev/null)" ]; then
    for program in bin/*; do
        if [ -x "$program" ]; then
            basename="$(basename "$program")"
            echo -e "  ${GREEN}./run.sh $basename${NC}"
        fi
    done
else
    echo -e "  ${YELLOW}No executables found.${NC}"
fi