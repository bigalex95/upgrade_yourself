#!/bin/bash

# Build script for NeetCode C++ solutions
# Usage: ./build.sh [debug|release|clean|--list|project_number]

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Default build type
BUILD_TYPE="Release"
BUILD_DIR="build"

# Function to list all available problems with numbers
list_problems() {
    echo -e "${BLUE}Available NeetCode Problems:${NC}"
    echo -e "${CYAN}=============================${NC}"
    
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
                    
                    echo -e "  ${GREEN}$count.${NC} $filename ${CYAN}(target: $target_name)${NC}"
                    ((count++))
                fi
            done
        fi
    done
    
    echo ""
    echo -e "${BLUE}Usage:${NC}"
    echo -e "  ${GREEN}./build.sh${NC}           # Build all problems"
    echo -e "  ${GREEN}./build.sh 1${NC}         # Build specific problem by number"
    echo -e "  ${GREEN}./build.sh debug${NC}     # Debug build"
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
                        target_name=$(echo "$target_name" | tr '[:upper:]' '[:lower:]' | sed 's/ /_/g' | sed 's/&/and/g' | sed 's/\//_/g')
                        echo "$target_name"
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
case "${1:-}" in
    debug)
        BUILD_TYPE="Debug"
        echo -e "${YELLOW}Building in Debug mode...${NC}"
        ;;
    release)
        BUILD_TYPE="Release"
        echo -e "${YELLOW}Building in Release mode...${NC}"
        ;;
    clean)
        echo -e "${YELLOW}Cleaning build directory...${NC}"
        rm -rf "$BUILD_DIR"
        echo -e "${GREEN}Build directory cleaned.${NC}"
        exit 0
        ;;
    --list|-l|list)
        list_problems
        exit 0
        ;;
    help|--help|-h)
        echo "Usage: $0 [debug|release|clean|--list|project_number]"
        echo "  debug      - Build with debug symbols and no optimization"
        echo "  release    - Build with optimization (default)"
        echo "  clean      - Remove build directory"
        echo "  --list     - List all available problems with numbers"
        echo "  NUMBER     - Build specific problem by number (e.g., './build.sh 1')"
        echo "  help       - Show this help message"
        echo ""
        list_problems
        exit 0
        ;;
    [0-9]*)
        # Building specific problem by number
        SPECIFIC_TARGET=$(get_problem_by_number "$1")
        if [[ -z "$SPECIFIC_TARGET" ]]; then
            echo -e "${RED}Error: Problem number $1 not found.${NC}"
            echo ""
            list_problems
            exit 1
        fi
        echo -e "${YELLOW}Building problem #$1: $SPECIFIC_TARGET${NC}"
        ;;
    "")
        echo -e "${YELLOW}Building all problems in Release mode (default)...${NC}"
        ;;
    *)
        echo -e "${RED}Unknown option: $1${NC}"
        echo "Use '$0 help' for usage information."
        exit 1
        ;;
esac

# Check if CMake is installed
if ! command -v cmake &> /dev/null; then
    echo -e "${RED}Error: CMake is not installed or not in PATH${NC}"
    echo "Please install CMake to build this project."
    exit 1
fi

# Check if a C++ compiler is available
if ! command -v g++ &> /dev/null && ! command -v clang++ &> /dev/null; then
    echo -e "${RED}Error: No C++ compiler found${NC}"
    echo "Please install g++ or clang++."
    exit 1
fi

# Create build directory
echo -e "${BLUE}Creating build directory...${NC}"
mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"

# Configure with CMake
echo -e "${BLUE}Configuring with CMake...${NC}"
cmake -DCMAKE_BUILD_TYPE="$BUILD_TYPE" ..

# Build the project
echo -e "${BLUE}Building project...${NC}"
if [[ -n "${SPECIFIC_TARGET:-}" ]]; then
    # Build specific target
    make "$SPECIFIC_TARGET" -j$(nproc 2>/dev/null || echo 4)
else
    # Build all targets
    make -j$(nproc 2>/dev/null || echo 4)
fi

echo -e "${GREEN}Build completed successfully!${NC}"
echo -e "${BLUE}Executables are in: ${BUILD_DIR}/bin${NC}"
echo -e "${BLUE}To run tests: ./test.sh${NC}"
echo -e "${BLUE}To run individual programs: ./run.sh <program_name_or_number>${NC}"