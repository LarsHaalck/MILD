add_executable(sample_test main.cpp)
target_link_libraries(sample_test
    PUBLIC
    mild
    opencv_core
    opencv_imgproc
    opencv_imgcodecs
)

target_include_directories(sample_test
    PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}
)
