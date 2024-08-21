# Install script for directory: /local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ldematteis/mambaforge/envs/Release")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set path to fallback-tool for dependency-resolution.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/home/ldematteis/mambaforge/envs/Release/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/python3.12/site-packages/pinocchio_rerun/pinocchio_rerun_pywrap.cpython-312-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/python3.12/site-packages/pinocchio_rerun/pinocchio_rerun_pywrap.cpython-312-x86_64-linux-gnu.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/python3.12/site-packages/pinocchio_rerun/pinocchio_rerun_pywrap.cpython-312-x86_64-linux-gnu.so"
         RPATH "\$ORIGIN/../../../../lib")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/ldematteis/mambaforge/envs/Release/lib/python3.12/site-packages/pinocchio_rerun/pinocchio_rerun_pywrap.cpython-312-x86_64-linux-gnu.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/ldematteis/mambaforge/envs/Release/lib/python3.12/site-packages/pinocchio_rerun" TYPE SHARED_LIBRARY FILES "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/python/pinocchio_rerun/pinocchio_rerun_pywrap.cpython-312-x86_64-linux-gnu.so")
  if(EXISTS "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/python3.12/site-packages/pinocchio_rerun/pinocchio_rerun_pywrap.cpython-312-x86_64-linux-gnu.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/python3.12/site-packages/pinocchio_rerun/pinocchio_rerun_pywrap.cpython-312-x86_64-linux-gnu.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/python3.12/site-packages/pinocchio_rerun/pinocchio_rerun_pywrap.cpython-312-x86_64-linux-gnu.so"
         OLD_RPATH "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/lib:"
         NEW_RPATH "\$ORIGIN/../../../../lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/home/ldematteis/mambaforge/envs/Release/bin/strip" "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/python3.12/site-packages/pinocchio_rerun/pinocchio_rerun_pywrap.cpython-312-x86_64-linux-gnu.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/python/CMakeFiles/pinocchio_rerun_pywrap.dir/install-cxx-module-bmi-Release.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.12/site-packages/pinocchio_rerun" TYPE FILE FILES "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/python/pinocchio_rerun/__init__.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/ldematteis/mambaforge/envs/Release/lib/python3.12/site-packages/pinocchio_rerun")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/ldematteis/mambaforge/envs/Release/lib/python3.12/site-packages" TYPE DIRECTORY FILES "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/python/pinocchio_rerun" FILES_MATCHING REGEX "/[^/]*\\.pyi$")
endif()

