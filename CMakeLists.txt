cmake_minimum_required(VERSION 3.10)

set(CXX_DISABLE_WERROR TRUE)
set(DOXYGEN_USE_MATHJAX YES)
set(DOXYGEN_USE_TEMPLATE_CSS TRUE)
set(PROJECT_USE_CMAKE_EXPORT FALSE)

set(PROJECT_NAME pinocchio-rerun)
set(PROJECT_URL "")
set(PROJECT_DESCRIPTION
    "Display of pinocchio kinematic chains in rerun visualizer")

include(cmake/base.cmake)
include(cmake/python.cmake)

project(${PROJECT_NAME})

if(NOT FINDPYTHON_ALREADY_CALLED)
  findpython()
endif()

add_library(${PROJECT_NAME} INTERFACE)
add_subdirectory(src)
