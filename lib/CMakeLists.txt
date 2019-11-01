set(sources
    src/loop_closure_detector.cpp
)


add_library(mild STATIC ${sources})
target_include_directories(mild
    PUBLIC
    $<INSTALL_INTERFACE:include>
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/src
)
target_link_libraries(mild
    PRIVATE
    opencv_core
    opencv_features2d
)

if(MSVC)
    target_compile_options(mild PRIVATE /arch:SSE4.2)
else()
    target_compile_options(mild PRIVATE -msse4.2)
endif()

install(TARGETS mild
    EXPORT mild-export
    DESTINATION mild
)

install(DIRECTORY include/MILD DESTINATION include)
