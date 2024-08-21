cmake_minimum_required(VERSION 3.10)

project(stubgen NONE)

include(ExternalProject)
ExternalProject_Add(stubgen
  GIT_REPOSITORY    https://github.com/jcarpent/pybind11-stubgen.git
  GIT_TAG           "master"
  SOURCE_DIR        "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/python/stubgen/src"
  BINARY_DIR        ""
  CONFIGURE_COMMAND ""
  BUILD_COMMAND     ""
  INSTALL_COMMAND   ""
  TEST_COMMAND      ""
)
