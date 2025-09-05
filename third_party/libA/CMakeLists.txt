cmake_minimum_required(VERSION 3.10)
project(libA C)
add_library(libA_static STATIC
  ${CMAKE_SOURCE_DIR}/third_party/libA/libA_1.c
  ${CMAKE_SOURCE_DIR}/third_party/libA/libA_2.c
)

target_include_directories(libA_static PUBLIC ${CMAKE_SOURCE_DIR}/third_party/libA)
