# Install script for directory: /local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun

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
  execute_process(COMMAND "/home/ldematteis/mambaforge/envs/Release/bin/cmake" --build ""  --target uninstall)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/pinocchio_rerun" TYPE FILE PERMISSIONS OWNER_READ GROUP_READ WORLD_READ OWNER_WRITE FILES "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/include/pinocchio_rerun/config.hpp")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/pinocchio_rerun" TYPE FILE PERMISSIONS OWNER_READ GROUP_READ WORLD_READ OWNER_WRITE FILES "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/include/pinocchio_rerun/deprecated.hpp")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/pinocchio_rerun" TYPE FILE PERMISSIONS OWNER_READ GROUP_READ WORLD_READ OWNER_WRITE FILES "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/include/pinocchio_rerun/warning.hpp")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  EXECUTE_PROCESS(COMMAND /usr/bin/gmake doc)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/doc/pinocchio_rerun" TYPE DIRECTORY FILES "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/doc/doxygen-html")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/libpinocchio_rerun.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/libpinocchio_rerun.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/libpinocchio_rerun.so"
         RPATH "\$ORIGIN")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/ldematteis/mambaforge/envs/Release/lib/libpinocchio_rerun.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/ldematteis/mambaforge/envs/Release/lib" TYPE SHARED_LIBRARY FILES "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/lib/libpinocchio_rerun.so")
  if(EXISTS "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/libpinocchio_rerun.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/libpinocchio_rerun.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/libpinocchio_rerun.so"
         OLD_RPATH ":::::::"
         NEW_RPATH "\$ORIGIN")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/home/ldematteis/mambaforge/envs/Release/bin/strip" "$ENV{DESTDIR}/home/ldematteis/mambaforge/envs/Release/lib/libpinocchio_rerun.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/pinocchio_rerun" TYPE FILE FILES
    "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/src/data_types.hpp"
    "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/src/eigen_adapters.hpp"
    "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/src/load_mesh.hpp"
    "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/src/pinocchio.hpp"
    "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/src/pinocchio_rerun.hpp"
    "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/src/rerun_visualizer.hpp"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/python/cmake_install.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE PERMISSIONS OWNER_READ GROUP_READ WORLD_READ OWNER_WRITE FILES "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/pinocchio_rerun.pc")
endif()

if(CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_COMPONENT MATCHES "^[a-zA-Z0-9_.+-]+$")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
  else()
    string(MD5 CMAKE_INST_COMP_HASH "${CMAKE_INSTALL_COMPONENT}")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INST_COMP_HASH}.txt")
    unset(CMAKE_INST_COMP_HASH)
  endif()
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
  file(WRITE "/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
