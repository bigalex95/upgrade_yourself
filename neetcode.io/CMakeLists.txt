cmake_minimum_required(VERSION 3.16)
project(NeetCode LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Compiler flags
set(CMAKE_CXX_FLAGS "-Wall -Wextra -Wpedantic")
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0 -DDEBUG")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")

# Output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Enable testing
enable_testing()

# Function to add a problem with tests
function(add_neetcode_problem category problem_name)
    set(SOURCE_FILE "${category}/${problem_name}.cpp")
    set(TARGET_NAME "${category}_${problem_name}")

    # Replace spaces and special characters in target name
    string(REPLACE " " "_" TARGET_NAME ${TARGET_NAME})
    string(REPLACE "&" "and" TARGET_NAME ${TARGET_NAME})
    string(REPLACE "/" "_" TARGET_NAME ${TARGET_NAME})
    string(TOLOWER ${TARGET_NAME} TARGET_NAME)

    if(EXISTS "${CMAKE_SOURCE_DIR}/${SOURCE_FILE}")
        # Create executable
        add_executable(${TARGET_NAME} ${SOURCE_FILE})

        # Add test that runs the executable
        add_test(NAME ${TARGET_NAME} COMMAND ${TARGET_NAME})

        message(STATUS "Added problem: ${TARGET_NAME}")
    endif()
endfunction()

# Add all problems by category
add_neetcode_problem("Arrays & Hashing" "two_sum")
# Add more problems as you create them:
# add_neetcode_problem("Arrays & Hashing" "contains_duplicate")
# add_neetcode_problem("Arrays & Hashing" "valid_anagram")
# add_neetcode_problem("Two Pointers" "valid_palindrome")
# add_neetcode_problem("Stack" "valid_parentheses")

# Print build information
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "C++ compiler: ${CMAKE_CXX_COMPILER}")
