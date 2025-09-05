cmake_minimum_required(VERSION 3.10)
project(libB C)
add_library(libB_static STATIC
  ${CMAKE_SOURCE_DIR}/third_party/libB/libB_1.c
  ${CMAKE_SOURCE_DIR}/third_party/libB/libB_2.c
)

target_include_directories(libB_static PUBLIC ${CMAKE_SOURCE_DIR}/third_party/libB)
