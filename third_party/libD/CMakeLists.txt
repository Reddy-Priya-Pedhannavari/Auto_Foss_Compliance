cmake_minimum_required(VERSION 3.10)
project(libD C)
add_library(libD_static STATIC
  ${CMAKE_SOURCE_DIR}/third_party/libD/libD_1.c
  ${CMAKE_SOURCE_DIR}/third_party/libD/libD_2.c
)

target_include_directories(libD_static PUBLIC ${CMAKE_SOURCE_DIR}/third_party/libD)
