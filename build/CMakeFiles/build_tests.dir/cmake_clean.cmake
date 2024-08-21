file(REMOVE_RECURSE
  "doc/doxygen-html"
  "doc/doxygen.log"
  "doc/pinocchio_rerun.doxytag"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/build_tests.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
