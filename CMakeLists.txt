cmake_minimum_required(VERSION 3.10)
project(AutoFossDemo C)

set(CMAKE_C_STANDARD 99)
include_directories(${CMAKE_SOURCE_DIR}/third_party/libA)
include_directories(${CMAKE_SOURCE_DIR}/third_party/libB)
include_directories(${CMAKE_SOURCE_DIR}/third_party/libC)
include_directories(${CMAKE_SOURCE_DIR}/third_party/libD)
include_directories(${CMAKE_SOURCE_DIR}/third_party/libE)

# Build static libs for each third_party subdir
add_library(libA_static STATIC
  ${CMAKE_SOURCE_DIR}/third_party/libA/libA_1.c
  ${CMAKE_SOURCE_DIR}/third_party/libA/libA_2.c
)
target_include_directories(libA_static PUBLIC ${CMAKE_SOURCE_DIR}/third_party/libA)

add_library(libB_static STATIC
  ${CMAKE_SOURCE_DIR}/third_party/libB/libB_1.c
  ${CMAKE_SOURCE_DIR}/third_party/libB/libB_2.c
)
target_include_directories(libB_static PUBLIC ${CMAKE_SOURCE_DIR}/third_party/libB)

# Shared lib example (simulate dynamic linkage)
add_library(libC_shared SHARED
  ${CMAKE_SOURCE_DIR}/third_party/libC/libC_1.c
  ${CMAKE_SOURCE_DIR}/third_party/libC/libC_2.c
)
target_include_directories(libC_shared PUBLIC ${CMAKE_SOURCE_DIR}/third_party/libC)

# Main executable that uses some third-party functions
add_executable(app_main src/main.c src/util.c src/feature_a.c src/feature_b.c)
target_link_libraries(app_main PRIVATE libA_static libB_static libC_shared)
