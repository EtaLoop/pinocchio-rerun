# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.30

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/ldematteis/mambaforge/envs/Release/bin/cmake

# The command to remove a file.
RM = /home/ldematteis/mambaforge/envs/Release/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build

# Utility rule file for release_changelog.

# Include any custom commands dependencies for this target.
include CMakeFiles/release_changelog.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/release_changelog.dir/progress.make

CMakeFiles/release_changelog:
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Update CHANGELOG.md"
	cd /local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun && sed -i.back "s|##\ \[Unreleased\]|##\ [Unreleased]\n\n##\ [$$VERSION]\ -\ 2024-08-09|" CHANGELOG.md && sed -i.back "s|^\[Unreleased]:\ \(https://.*compare/\)\(v.*\)...HEAD|[Unreleased]:\ \1v$$VERSION...HEAD\n[$$VERSION]:\ \1\2...v$$VERSION|" CHANGELOG.md && if ! ( git diff --quiet CHANGELOG.md ) then ( /usr/bin/git add CHANGELOG.md && /usr/bin/git commit -m release:\ Update\ CHANGELOG.md\ for\ $$VERSION && echo Updated\ CHANGELOG.md\ and\ committed ) fi

release_changelog: CMakeFiles/release_changelog
release_changelog: CMakeFiles/release_changelog.dir/build.make
.PHONY : release_changelog

# Rule to build all files generated by this target.
CMakeFiles/release_changelog.dir/build: release_changelog
.PHONY : CMakeFiles/release_changelog.dir/build

CMakeFiles/release_changelog.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/release_changelog.dir/cmake_clean.cmake
.PHONY : CMakeFiles/release_changelog.dir/clean

CMakeFiles/release_changelog.dir/depend:
	cd /local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun /local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun /local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build /local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build /local/usr/ldematteis/Repositories/Software_Perso/pinocchio-rerun/build/CMakeFiles/release_changelog.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/release_changelog.dir/depend
