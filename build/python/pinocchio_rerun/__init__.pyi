import pinocchio_rerun
import typing

__all__ = [
    "Exception",
    "RerunVisualizer",
    "StdVec_VectorRef",
    "pinocchio_rerun_pywrap",
    "seed",
    "sharedMemory"
]

class Exception(Boost.Python.instance):
    @staticmethod
    def __init__(arg1: object, arg2: str) -> None: 
        """
        __init__( (object)arg1, (str)arg2) -> None :

            C++ signature :
                void __init__(_object*,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
    @property
    def message(self) -> None:
        """
        :type: None
        """
    __instance_size__ = 72
    pass

class RerunVisualizer(Boost.Python.instance):
    def __init__(self, model: Model, geomModel: GeometryModel) -> None: 
        """
        __init__( (object)self, (Model)model, (GeometryModel)geomModel) -> None :

            C++ signature :
                void __init__(_object*,pinocchio::ModelTpl<double, 0, pinocchio::JointCollectionDefaultTpl>,pinocchio::GeometryModel)
        """
    def clean(self) -> None: 
        """
        clean( (RerunVisualizer)self) -> None :

            C++ signature :
                void clean(pinrerun::RerunVisualizer {lvalue})
        """
    def disableTimeline(self, name: str) -> None: 
        """
        disableTimeline( (RerunVisualizer)self, (str)name) -> None :
            Disable a Rerun timeline.

            C++ signature :
                void disableTimeline(pinrerun::RerunVisualizer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
    def display(self, q: numpy.ndarray = None) -> None: 
        """
        display( (RerunVisualizer)self [, (numpy.ndarray)q=None]) -> None :

            C++ signature :
                void display(pinrerun::RerunVisualizer {lvalue} [,std::optional<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1> const, 0, Eigen::InnerStride<1> > >=None])
        """
    def drawFrameVelocities(self, frame_ids: StdVec_Index) -> None: 
        """
        drawFrameVelocities( (RerunVisualizer)self, (StdVec_Index)frame_ids) -> None :

            C++ signature :
                void drawFrameVelocities(pinrerun::RerunVisualizer {lvalue},std::vector<unsigned long, std::allocator<unsigned long> >)
        """
    @staticmethod
    def initViewer(arg1: RerunVisualizer) -> None: 
        """
        initViewer( (RerunVisualizer)arg1) -> None :

            C++ signature :
                void initViewer(pinrerun::RerunVisualizer {lvalue})
        """
    @staticmethod
    def loadViewerModel(arg1: RerunVisualizer) -> None: 
        """
        loadViewerModel( (RerunVisualizer)arg1) -> None :

            C++ signature :
                void loadViewerModel(pinrerun::RerunVisualizer {lvalue})
        """
    def play(self, qs: StdVec_VectorRef, dt_: float, timeline: str = 'trajectory') -> None: 
        """
        play( (RerunVisualizer)self, (StdVec_VectorRef)qs, (float)dt [, (str)timeline='trajectory']) -> None :

            C++ signature :
                void play(pinrerun::RerunVisualizer {lvalue},std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > >,double [,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >='trajectory'])
        """
    @staticmethod
    def rebuildData(arg1: RerunVisualizer) -> None: 
        """
        rebuildData( (RerunVisualizer)arg1) -> None :

            C++ signature :
                void rebuildData(pinrerun::RerunVisualizer {lvalue})
        """
    def setCameraPose(self, pose: numpy.ndarray) -> None: 
        """
        setCameraPose( (RerunVisualizer)self, (numpy.ndarray)pose) -> None :

            C++ signature :
                void setCameraPose(pinrerun::RerunVisualizer {lvalue},Eigen::Matrix<double, 4, 4, 0, 4, 4>)
        """
    def setCameraPosition(self, position: numpy.ndarray) -> None: 
        """
        setCameraPosition( (RerunVisualizer)self, (numpy.ndarray)position) -> None :

            C++ signature :
                void setCameraPosition(pinrerun::RerunVisualizer {lvalue},Eigen::Ref<Eigen::Matrix<double, 3, 1, 0, 3, 1> const, 0, Eigen::InnerStride<1> >)
        """
    def setCameraTarget(self, target: numpy.ndarray) -> None: 
        """
        setCameraTarget( (RerunVisualizer)self, (numpy.ndarray)target) -> None :

            C++ signature :
                void setCameraTarget(pinrerun::RerunVisualizer {lvalue},Eigen::Ref<Eigen::Matrix<double, 3, 1, 0, 3, 1> const, 0, Eigen::InnerStride<1> >)
        """
    def setCameraZoom(self, value: SE3) -> None: 
        """
        setCameraZoom( (RerunVisualizer)self, (SE3)value) -> None :

            C++ signature :
                void setCameraZoom(pinrerun::RerunVisualizer {lvalue},pinocchio::SE3Tpl<double, 0>)
        """
    def switchTimeline(self, name: str) -> None: 
        """
        switchTimeline( (RerunVisualizer)self, (str)name) -> None :
            Switch Rerun timelines.

            C++ signature :
                void switchTimeline(pinrerun::RerunVisualizer {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
    @property
    def collisionData(self) -> None:
        """
        :type: None
        """
    @property
    def collisionModel(self) -> None:
        """
        :type: None
        """
    @property
    def data(self) -> None:
        """
        :type: None
        """
    @property
    def initialized(self) -> None:
        """
        :type: None
        """
    @property
    def model(self) -> None:
        """
        :type: None
        """
    @property
    def visualData(self) -> None:
        """
        :type: None
        """
    @property
    def visualModel(self) -> None:
        """
        :type: None
        """
    pass

class StdVec_VectorRef(Boost.Python.instance):
    @staticmethod
    def __contains__(arg1: StdVec_VectorRef, arg2: object) -> bool: 
        """
        __contains__( (StdVec_VectorRef)arg1, (object)arg2) -> bool :

            C++ signature :
                bool __contains__(std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > > {lvalue},_object*)
        """
    def __copy__(self) -> StdVec_VectorRef: 
        """
        __copy__( (StdVec_VectorRef)self) -> StdVec_VectorRef :
            Returns a copy of *this.

            C++ signature :
                std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > > __copy__(std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > >)
        """
    def __deepcopy__(self, memo: dict) -> StdVec_VectorRef: 
        """
        __deepcopy__( (StdVec_VectorRef)self, (dict)memo) -> StdVec_VectorRef :
            Returns a deep copy of *this.

            C++ signature :
                std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > > __deepcopy__(std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > >,boost::python::dict)
        """
    @staticmethod
    def __delitem__(arg1: StdVec_VectorRef, arg2: object) -> None: 
        """
        __delitem__( (StdVec_VectorRef)arg1, (object)arg2) -> None :

            C++ signature :
                void __delitem__(std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > > {lvalue},_object*)
        """
    @staticmethod
    def __getinitargs__(arg1: StdVec_VectorRef) -> tuple: 
        """
        __getinitargs__( (StdVec_VectorRef)arg1) -> tuple :

            C++ signature :
                boost::python::tuple __getinitargs__(std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > >)
        """
    @staticmethod
    def __getitem__(arg1: object, arg2: object) -> object: 
        """
        __getitem__( (object)arg1, (object)arg2) -> object :

            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > >&>,_object*)
        """
    @staticmethod
    def __getstate__(arg1: object) -> tuple: 
        """
        __getstate__( (object)arg1) -> tuple :

            C++ signature :
                boost::python::tuple __getstate__(boost::python::api::object)
        """
    @staticmethod
    @typing.overload
    def __init__(arg1: object) -> None: 
        """
        __init__( (object)arg1) -> None :

            C++ signature :
                void __init__(_object*)

            C++ signature :
                void __init__(_object*,unsigned long,Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >)

            C++ signature :
                void __init__(_object*,std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > >)
        """
    @typing.overload
    def __init__(self, other: StdVec_VectorRef) -> None: ...
    @typing.overload
    def __init__(self, size: int, value: numpy.ndarray) -> None: ...
    @staticmethod
    def __iter__(arg1: object) -> object: 
        """
        __iter__( (object)arg1) -> object :

            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_internal_reference<1ul, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >*, std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > > > > __iter__(boost::python::back_reference<std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > >&>)
        """
    @staticmethod
    def __len__(arg1: StdVec_VectorRef) -> int: 
        """
        __len__( (StdVec_VectorRef)arg1) -> int :

            C++ signature :
                unsigned long __len__(std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > > {lvalue})
        """
    @staticmethod
    def __setitem__(arg1: StdVec_VectorRef, arg2: object, arg3: object) -> None: 
        """
        __setitem__( (StdVec_VectorRef)arg1, (object)arg2, (object)arg3) -> None :

            C++ signature :
                void __setitem__(std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > > {lvalue},_object*,_object*)
        """
    @staticmethod
    def __setstate__(arg1: object, arg2: tuple) -> None: 
        """
        __setstate__( (object)arg1, (tuple)arg2) -> None :

            C++ signature :
                void __setstate__(boost::python::api::object,boost::python::tuple)
        """
    @staticmethod
    def append(arg1: StdVec_VectorRef, arg2: object) -> None: 
        """
        append( (StdVec_VectorRef)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > > {lvalue},boost::python::api::object)
        """
    def copy(self) -> StdVec_VectorRef: 
        """
        copy( (StdVec_VectorRef)self) -> StdVec_VectorRef :
            Returns a copy of *this.

            C++ signature :
                std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > > copy(std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > >)
        """
    @staticmethod
    def extend(arg1: StdVec_VectorRef, arg2: object) -> None: 
        """
        extend( (StdVec_VectorRef)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > > {lvalue},boost::python::api::object)
        """
    def reserve(self, new_cap: int) -> None: 
        """
        reserve( (StdVec_VectorRef)self, (int)new_cap) -> None :
            Increase the capacity of the vector to a value that's greater or equal to new_cap.

            C++ signature :
                void reserve(std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > > {lvalue},unsigned long)
        """
    def tolist(self, deep_copy: bool = False) -> list: 
        """
        tolist( (StdVec_VectorRef)self [, (bool)deep_copy=False]) -> list :
            Returns the std::vector as a Python list.

            C++ signature :
                boost::python::list tolist(std::vector<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> >, std::allocator<Eigen::Ref<Eigen::Matrix<double, -1, 1, 0, -1, 1>, 0, Eigen::InnerStride<1> > > > {lvalue} [,bool=False])
        """
    __getstate_manages_dict__ = True
    __instance_size__ = 56
    __safe_for_unpickling__ = True
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
import Boost.Python
import numpy
_Shape = typing.Tuple[int, ...]

