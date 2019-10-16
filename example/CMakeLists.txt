add_executable(test main.cpp)
target_link_libraries(test
    PUBLIC
    mild
    opencv_core
    opencv_imgproc
    opencv_imgcodecs
)

target_include_directories(test
    PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}
)
