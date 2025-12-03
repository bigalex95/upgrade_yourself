cmake_minimum_required(VERSION 3.10)
project(Cpp_CV)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

file(GLOB SOURCE ${PROJECT_SOURCE_DIR}/src/*.cpp)
add_executable(Cpp_CV src/main.cpp)
target_include_directories(Cpp_CV PUBLIC "${PROJECT_SOURCE_DIR}/include")


