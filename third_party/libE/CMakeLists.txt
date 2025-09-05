cmake_minimum_required(VERSION 3.10)
project(libE C)
add_library(libE_static STATIC
  ${CMAKE_SOURCE_DIR}/third_party/libE/libE_1.c
  ${CMAKE_SOURCE_DIR}/third_party/libE/libE_2.c
)

target_include_directories(libE_static PUBLIC ${CMAKE_SOURCE_DIR}/third_party/libE)
