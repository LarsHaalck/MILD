project(mild)
cmake_minimum_required(VERSION 3.8)
set(VERSION 1.0)

set(CMAKE_CXX_STANDARD 17)

option(BUILD_EXAMPLE "Build small toy example" TRUE)

# only for debug builds
# medium.com/@alasher/colored-c-compiler-output-with-ninja-clang-gcc-10bfe7f2b949
option(FORCE_COLORED_OUTPUT "Always produce ANSI-colored output (GNU/Clang only)." TRUE)
if (${FORCE_COLORED_OUTPUT})
    if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
       add_compile_options (-fdiagnostics-color=always)
    elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
       add_compile_options (-fcolor-diagnostics)
    endif ()
endif ()

# enable highest error level and optimizations
if(MSVC)
    add_compile_options("/W4" "$<$<CONFIG:RELEASE>:/O2>")
else()
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

    # handle clang specifics
    if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
        add_compile_options("-stdlib=libc++")
    endif()
endif()


find_package(OpenCV REQUIRED)
find_package(Eigen3 REQUIRED)


add_subdirectory(lib)
if (BUILD_EXAMPLE)
    add_subdirectory(example)
endif ()

# install all exported targets
include(CMakePackageConfigHelpers)
set(versionConfig "${PROJECT_BINARY_DIR}/mild-config-version.cmake")
set(packageConfig "${PROJECT_BINARY_DIR}/mild-config.cmake")

write_basic_package_version_file(
    ${versionConfig}
    VERSION ${VERSION}
    COMPATIBILITY AnyNewerVersion
)

configure_package_config_file(
    ${PROJECT_SOURCE_DIR}/mild-config.cmake.in
    ${packageConfig}
    INSTALL_DESTINATION cmake
)

install(FILES ${versionConfig} ${packageConfig}
    DESTINATION
    cmake
)

install(EXPORT mild-export
  FILE
    mildTargets.cmake
  NAMESPACE
    mild::
  DESTINATION
    cmake
)


