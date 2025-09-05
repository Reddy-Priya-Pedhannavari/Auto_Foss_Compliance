cmake_minimum_required(VERSION 3.10)
project(libC C)
add_library(libC_static STATIC
  ${CMAKE_SOURCE_DIR}/third_party/libC/libC_1.c
  ${CMAKE_SOURCE_DIR}/third_party/libC/libC_2.c
)

target_include_directories(libC_static PUBLIC ${CMAKE_SOURCE_DIR}/third_party/libC)
