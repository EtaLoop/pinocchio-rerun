import pinocchio_rerun.pinocchio_rerun_pywrap
import typing

__all__ = [
    "Exception",
    "RerunVisualizer",
    "StdVec_VectorRef",
    "seed",
    "sharedMemory"
]

class Exception():
    pass

class RerunVisualizer():
    pass

class StdVec_VectorRef():
    pass

def seed(seed_value: int) -> None:
    """
    seed( (int)seed_value) -> None :
        Initialize the pseudo-random number generator with the argument seed_value.

        C++ signature :
            void seed(unsigned int)
    """

@typing.overload
def sharedMemory() -> bool:
    """
    sharedMemory( (bool)value) -> None :
        Share the memory when converting from Eigen to Numpy.

        C++ signature :
            void sharedMemory(bool)

        C++ signature :
            bool sharedMemory()
    """
@typing.overload
def sharedMemory(value: bool) -> None:
    pass

__version__ = '0.1.0'

