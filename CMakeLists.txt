cmake_minimum_required(VERSION 3.2)
project(MILD)

set(CMAKE_CXX_STANDARD 11)

if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
   add_compile_options (-fdiagnostics-color=always)
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
   add_compile_options (-fcolor-diagnostics)
endif ()

add_compile_options(
    "-Wall"
    "-Wextra"
    "-pedantic"
    "-Wstrict-aliasing"
    "-pedantic"
    "-fmax-errors=5"
    "-Wunreachable-code"
    "-Wcast-align"
    "-Wcast-qual"
    "-Wctor-dtor-privacy"
    "-Wdisabled-optimization"
    "-Wformat=2"
    "-Winit-self"
    "-Wlogical-op"
    "-Wmissing-include-dirs"
    "-Wold-style-cast"
    "-Woverloaded-virtual"
    "-Wredundant-decls"
    "-Wshadow"
    "-Wsign-promo"
    "-Wstrict-null-sentinel"
    "-Wstrict-overflow=5"
    "-Wswitch-default"
    "-Wundef"
    "$<$<CONFIG:RELEASE>:-O3>")

set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)

file(GLOB helloworld_SRC
"*.cpp"
"*.h"
"MILD/*.cpp"
"MILD/*.h"
"ORBSLAM/*.cpp"
"ORBSLAM/*.h"
)

set(SOURCE_FILES
 ${helloworld_SRC})

set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Wall")

find_package(OpenCV REQUIRED)
set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR})

find_package(Eigen3 REQUIRED)
include_directories( ${EIGEN3_INCLUDE_DIRS} )
set(CMAKE_CXX_FLAGS "-msse4.2") 

add_executable(MILD ${SOURCE_FILES})


include_directories(${OpenCV_INCLUDE_DIRS})

target_link_libraries(MILD ${OpenCV_LIBS} )
