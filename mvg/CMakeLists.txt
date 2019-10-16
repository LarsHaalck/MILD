project(compare)
cmake_minimum_required(VERSION 3.8)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -Wall -pedantic -Wextra")

find_package(OpenMVG REQUIRED)
find_package(Eigen3 REQUIRED)

add_executable(main main.cpp)
target_link_libraries(main
  PRIVATE
    OpenMVG::openMVG_matching
    Eigen3::Eigen
)

