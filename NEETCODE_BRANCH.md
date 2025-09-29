# NeetCode Solutions Branch

This branch contains a complete NeetCode problem-solving environment with dual-language support (C++ and Python).

## 🎯 Branch Purpose

**Dedicated branch for systematic LeetCode/NeetCode practice following the NeetCode 150 roadmap.**

## 🏗️ Project Structure

```
neetcode.io/
├── Arrays & Hashing/          # Problem category
│   ├── two_sum.cpp           # C++ solution
│   └── two_sum.py            # Python solution
├── build.sh                  # C++ build system
├── test.sh                   # C++ test runner
├── run.sh                    # C++ program runner
├── test_python.sh            # Python test runner
├── CMakeLists.txt            # C++ build configuration
├── .gitignore               # Excludes build artifacts
└── README*.md               # Documentation
```

## 🚀 Quick Start

```bash
# Switch to this branch
git checkout neetcode

# Work with problems
cd neetcode.io/

# List available problems
./build.sh --list
./test_python.sh --list

# Test solutions
./build.sh 1 && ./run.sh 1     # C++ solution
./test_python.sh 1             # Python solution
```

## 🎯 Workflow

1. **Choose a problem** from NeetCode roadmap
2. **Create solutions** in both languages (C++ and Python)
3. **Test locally** using our build system
4. **Commit progress** to this branch
5. **Track completion** in PROGRESS.md

## 🌿 Branch Management

- **Main branch**: General learning projects and courses
- **NeetCode branch**: Pure competitive programming focus
- **Clean separation**: Each branch serves its purpose

## 📊 Progress Tracking

- ✅ Arrays & Hashing: 1/9 problems completed
- 🎯 Next: Contains Duplicate, Valid Anagram
- 📈 Total: 1/150 NeetCode problems completed

---

**Happy coding! 🚀**
