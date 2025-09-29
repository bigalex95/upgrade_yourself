# NeetCode C++ Build System

This directory contains a simple CMake-based build system for C++ NeetCode solutions with CTest integration.

## Prerequisites

- CMake 3.16 or higher
- C++17 compatible compiler (g++ or clang++)

### Installing Dependencies

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install cmake g++
```

**macOS (Homebrew):**

```bash
brew install cmake
```

**Arch Linux:**

```bash
sudo pacman -S cmake gcc
```

## Quick Start

1. **Build the project:**

   ```bash
   ./build.sh
   ```

2. **Run all tests:**

   ```bash
   ./test.sh
   ```

3. **Run a specific program:**
   ```bash
   ./run.sh arrays_and_hashing_two_sum
   ```

## Scripts Overview

### `build.sh`

Builds the entire project using CMake.

**Usage:**

```bash
./build.sh [debug|release|clean|help]
```

**Examples:**

```bash
./build.sh              # Release build
./build.sh debug        # Debug build
./build.sh clean        # Clean build files
```

### `test.sh`

Runs all tests using CTest.

**Usage:**

```bash
./test.sh [options]
```

**Options:**

- `-v, --verbose` - Enable verbose output
- `-j, --jobs N` - Run tests with N parallel jobs
- `--build` - Build project before running tests

**Examples:**

```bash
./test.sh               # Run all tests
./test.sh --verbose     # Verbose output
./test.sh --build       # Build then test
./test.sh -j 8          # Use 8 parallel jobs
```

### `run.sh`

Executes individual programs.

**Usage:**

```bash
./run.sh <program_name> [args...]
```

**Examples:**

```bash
./run.sh --list                          # List programs
./run.sh arrays_and_hashing_two_sum      # Run Two Sum
```

## Project Structure

```
neetcode.io/
├── CMakeLists.txt              # Simple CMake configuration
├── build.sh                    # Build script
├── run.sh                      # Execution script
├── test.sh                     # Test script
├── README_BUILD.md             # This file
│
├── Arrays & Hashing/
│   ├── two_sum.cpp            # Problem with assert-based tests
│   └── Makefile               # Simple Makefile (optional)
│
└── build/                     # Build output (generated)
    ├── bin/                   # Executables
    └── ...                    # CMake files
```

## Adding New Problems

1. **Create the C++ file** in the appropriate category folder
2. **Update CMakeLists.txt** by adding a new line:
   ```cmake
   add_neetcode_problem("Category Name" "problem_name")
   ```
3. **Rebuild the project:**
   ```bash
   ./build.sh
   ```

## Problem Template Structure

Each problem should follow this simple structure:

```cpp
#include <vector>
#include <iostream>
#include <cassert>

using namespace std;

class Solution {
public:
    // Your solution here
};

void runTests() {
    Solution solution;

    // Test case 1
    {
        // Test inputs
        vector<int> input = {1, 2, 3};
        vector<int> expected = {1, 2};
        vector<int> result = solution.yourMethod(input);
        assert(result == expected);
        cout << "✅ Test 1 passed" << endl;
    }

    cout << "🎉 All tests passed!" << endl;
}

int main() {
    runTests();
    return 0;
}
```

## Troubleshooting

**Permission denied on scripts:**

```bash
chmod +x build.sh run.sh test.sh
```

**CMake version too old:**

```bash
# Update CMake or modify CMakeLists.txt minimum version
cmake_minimum_required(VERSION 3.10)  # Lower version
```

## Advanced Usage

**Manual CMake build:**

```bash
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j$(nproc)
ctest --verbose
```

**Debug specific test:**

```bash
./build.sh debug
cd build
gdb ./bin/arrays_and_hashing_two_sum
```

**Run only failed tests:**

```bash
cd build
ctest --rerun-failed --verbose
```
