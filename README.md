[![stiima](doc/stiima.png)](https://www.stiima.cnr.it/)  
[![serlab](doc/serlab.png)](https://serlab.di.uniba.it/) 
# ROS2_SONARCLOUD  
This repository uses github actions to build ROS2 rolling from source ,plus other relevant packages, and performs static analysis using sonarcloud tools 
.Its aim is to improve stability and code quality of ROS2 packages by mean of static code analysis. 
Extracted bugs, vulnerabilities and code smells are listed below in this document, grouped by package.  
Each entry is formed by a file:line and message, with a link to the specific sonacloud link.  
This page is generated automatically after every static analysys.  
The complete results of the analysis can be found [here](https://sonarcloud.io/summary/overall?id=muttistefano_ros2_sonarcloud) .  
Github truncates this file, i am currently looking for a solution but in the meantime the complete file can be downloaded and rendered locally  
  
<br />  
  
## BUGS #601 
<details><summary><a style='color:blue;font-size:18px;'>ros2</a></summary>  

  * file : ros2/rclpy/rclpy/test/test_node.py:1529  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYi-8w_ub2taBKNOE)  
---
  * file : ros2/rclpy/rclpy/test/test_parameter_client.py:76  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYi-Ow_ub2taBKNOB)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:92  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXo)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:95  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXp)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:107  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXq)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:112  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXr)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:114  
  message : Fix this invalid "-" operation between incompatible types (Duration and Time).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokozCYfarq97IXh)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:114  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXs)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:135  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXt)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:137  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXu)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:139  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXv)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:141  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXw)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:143  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXx)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:145  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXy)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:154  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX2)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:156  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX3)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:158  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX4)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:160  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX5)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:183  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX9)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:185  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX-)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:187  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX_)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:189  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IYA)  
---
  * file : ros2/rcpputils/include/rcpputils/scope_exit.hpp:29  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISir08zCYfarq97JF4)  
---
  * file : ros2/rcutils/src/error_handling_helpers.h:82  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYvGYSeY228C2JcY-al-)  
---
  * file : ros2/rcutils/src/logging.c:436  
  message : Memory copy function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYqmAQdbWvNZCKI3y18h)  
---
  * file : ros2/rcutils/src/strdup.c:53  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirSSzCYfarq97I9X)  
---
  * file : ros2/rcutils/test/mocking_utils/patch.hpp:160  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirK4zCYfarq97I5p)  
---
  * file : ros2/rmw_cyclonedds/rmw_cyclonedds_cpp/src/serdes.hpp:145  
  message : dereference of type 'uint32_t *' (aka 'unsigned int *') that was reinterpret_cast from type 'float *' has undefined behavior  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHenw2X4EK9K44Cn)  
---
  * file : ros2/rmw_cyclonedds/rmw_cyclonedds_cpp/src/serdes.hpp:149  
  message : dereference of type 'uint64_t *' (aka 'unsigned long *') that was reinterpret_cast from type 'double *' has undefined behavior  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHenw2X4EK9K44Co)  
---
  * file : ros2/rmw_cyclonedds/rmw_cyclonedds_cpp/src/serdes.hpp:307  
  message : Replace "unsigned int" to "float" type punning with "std::memcpy". "f" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHenw2X4EK9K44DF)  
---
  * file : ros2/rmw_cyclonedds/rmw_cyclonedds_cpp/src/serdes.hpp:318  
  message : Replace "unsigned long" to "double" type punning with "std::memcpy". "f" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHenw2X4EK9K44DG)  
---
  * file : ros2/rmw_fastrtps/rmw_fastrtps_shared_cpp/include/rmw_fastrtps_shared_cpp/guid_utils.hpp:56  
  message : Use constructors or assignment operators, "EntityId_t" is not trivially copyable.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-wb33-gB3mVexO4O)  
---
  * file : ros2/rmw_fastrtps/rmw_fastrtps_shared_cpp/src/rmw_get_endpoint_network_flow.cpp:192  
  message : Remove this conditional structure or edit its code blocks so that they're not all the same.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-wVy3-gB3mVexO0U)  
---
  * file : ros2/ros2cli/ros2cli/test/test_direct.py:48  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYfNdw_ub2taBKNN2)  
---
  * file : ros2/rosbag2/rosbag2_compression/src/rosbag2_compression/compression_factory_impl.hpp:79  
  message : Remove "e" from this "throw" statement to rethrow the original exception.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBRCw2X4EK9K41ka)  
---
  * file : ros2/rosbag2/rosbag2_compression/src/rosbag2_compression/compression_factory_impl.hpp:86  
  message : Remove "e" from this "throw" statement to rethrow the original exception.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBRCw2X4EK9K41kc)  
---
  * file : ros2/rosbag2/rosbag2_cpp/src/rosbag2_cpp/cache/message_cache.cpp:44  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBqaw2X4EK9K41tI)  
---
  * file : ros2/rosbag2/rosbag2_cpp/src/rosbag2_cpp/serialization_format_converter_factory_impl.hpp:61  
  message : Remove "e" from this "throw" statement to rethrow the original exception.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBoow2X4EK9K41r8)  
---
  * file : ros2/rosbag2/rosbag2_cpp/src/rosbag2_cpp/writers/sequential_writer.cpp:70  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBsBw2X4EK9K41u3)  
---
  * file : ros2/rosbag2/rosbag2_py/src/rosbag2_py/_writer.cpp:42  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pB0Qw2X4EK9K41xj)  
---
  * file : ros2/rosbag2/rosbag2_py/test/common.py:50  
  message : Refactor this loop to do more than one iteration.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimEkzCYfarq97H-9)  
---
  * file : ros2/rosbag2/rosbag2_py/test/test_sequential_reader.py:137  
  message : The return value of "isinstance" must be used.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimEWzCYfarq97H-5)  
---
  * file : ros2/rosbag2/rosbag2_py/test/test_sequential_reader.py:148  
  message : The return value of "isinstance" must be used.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimEWzCYfarq97H-6)  
---
  * file : ros2/rosbag2/rosbag2_py/test/test_sequential_reader.py:159  
  message : The return value of "isinstance" must be used.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimEWzCYfarq97H-8)  
---
  * file : ros2/rosbag2/rosbag2_py/test/test_sequential_reader.py:166  
  message : The return value of "isinstance" must be used.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimEWzCYfarq97H-7)  
---
  * file : ros2/rosbag2/rosbag2_py/test/test_sequential_writer.py:36  
  message : Remove or correct this useless self-assignment.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimDwzCYfarq97H-2)  
---
  * file : ros2/rosbag2/rosbag2_storage/src/rosbag2_storage/impl/storage_factory_impl.hpp:150  
  message : Remove "e" from this "throw" statement to rethrow the original exception.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pB9Gw2X4EK9K41zc)  
---
  * file : ros2/rosbag2/rosbag2_storage/src/rosbag2_storage/impl/storage_factory_impl.hpp:157  
  message : Remove "e" from this "throw" statement to rethrow the original exception.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pB9Gw2X4EK9K41ze)  
---
  * file : ros2/rosidl/rosidl_adapter/test/test_base_type.py:85  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISik3NzCYfarq97H0F)  
---
  * file : ros2/rosidl/rosidl_adapter/test/test_parse_primitive_value_string.py:212  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYeY2w_ub2taBKNNz)  
---
  * file : ros2/rosidl/rosidl_adapter/test/test_type.py:79  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISik3bzCYfarq97H0K)  
---
  * file : ros2/rosidl/rosidl_parser/test/test_parser.py:114  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYefSw_ub2taBKNN0)  
---
  * file : ros2/rosidl/rosidl_parser/test/test_parser.py:393  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYefSw_ub2taBKNN1)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/test/test_interfaces.py:66  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYmnpw_ub2taBKNOH)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/test/test_interfaces.py:67  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYmnpw_ub2taBKNOI)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/test/test_interfaces.py:85  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYmnpw_ub2taBKNOJ)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/test/test_interfaces.py:87  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYmnpw_ub2taBKNOK)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/test/test_interfaces.py:275  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYmnpw_ub2taBKNOL)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/test/test_interfaces.py:276  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYmnpw_ub2taBKNOM)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/test/test_interfaces.py:297  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYmnpw_ub2taBKNON)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/test/test_interfaces.py:298  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYmnpw_ub2taBKNOO)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_convert.py:53  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYm2uw_ub2taBKNOQ)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_convert.py:54  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYm2uw_ub2taBKNOR)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_convert.py:55  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYm2uw_ub2taBKNOS)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_convert.py:56  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYm2uw_ub2taBKNOT)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:184  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYm3kw_ub2taBKNOU)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:187  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYm3kw_ub2taBKNOV)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:200  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYm3kw_ub2taBKNOW)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:203  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYm3kw_ub2taBKNOX)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:206  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYm3kw_ub2taBKNOY)  
---
  * file : ros2/rosidl_typesupport/rosidl_typesupport_c/test/mocking_utils/patch.hpp:343  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirsBzCYfarq97JCI)  
---
  * file : ros2/rviz/rviz_common/help/help.html:8  
  message : Insert a !DOCTYPE declaration to before this html tag.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_e)  
---
  * file : ros2/rviz/rviz_common/help/help.html:8  
  message : Add "lang" and/or "xml:lang" attributes to this "html" element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_f)  
---
  * file : ros2/rviz/rviz_common/help/help.html:9  
  message : Add a title tag to this page.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_g)  
---
  * file : ros2/rviz/rviz_common/help/help.html:24  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_i)  
---
  * file : ros2/rviz/rviz_common/help/help.html:24  
  message : Add a description to this table.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_h)  
---
  * file : ros2/rviz/rviz_common/help/help.html:63  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_s)  
---
  * file : ros2/rviz/rviz_common/help/help.html:63  
  message : Add a description to this table.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_r)  
---
  * file : ros2/rviz/rviz_common/help/help.html:76  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_x)  
---
  * file : ros2/rviz/rviz_common/help/help.html:76  
  message : Add a description to this table.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_w)  
---
  * file : ros2/rviz/rviz_common/help/help.html:86  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_1)  
---
  * file : ros2/rviz/rviz_common/help/help.html:86  
  message : Add a description to this table.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_0)  
---
  * file : ros2/rviz/rviz_common/help/help.html:104  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_5)  
---
  * file : ros2/rviz/rviz_common/help/help.html:104  
  message : Add a description to this table.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_4)  
---
  * file : ros2/rviz/rviz_common/help/help.html:129  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_9)  
---
  * file : ros2/rviz/rviz_common/help/help.html:129  
  message : Add a description to this table.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_8)  
---
  * file : ros2/rviz/rviz_common/help/help.html:159  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97IAB)  
---
  * file : ros2/rviz/rviz_common/help/help.html:159  
  message : Add a description to this table.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97IAA)  
---
  * file : ros2/rviz/rviz_common/help/help.html:184  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97IAF)  
---
  * file : ros2/rviz/rviz_common/help/help.html:184  
  message : Add a description to this table.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97IAE)  
---
  * file : ros2/rviz/rviz_common/help/help.html:209  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97IAJ)  
---
  * file : ros2/rviz/rviz_common/help/help.html:209  
  message : Add a description to this table.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97IAI)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/covariance_visual.cpp:152  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u493-gB3mVexOlm)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:58  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmR)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:60  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmS)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:62  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmT)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:64  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmU)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:66  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmV)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/render_system.cpp:241  
  message : Name this temporary "unique_ptrOgre::RenderSystemCapabilities" object if you want to use it in for RAII.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u8b3-gB3mVexOpI)  
---
  * file : ros2/system_tests/test_communication/test/test_publisher.cpp:58  
  message : Remove "ex" from this "throw" statement to rethrow the original exception.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pIllw2X4EK9K44L7)  
---
  * file : ros2/system_tests/test_communication/test/test_publisher_subscriber.cpp:63  
  message : Remove "ex" from this "throw" statement to rethrow the original exception.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pIiGw2X4EK9K44KC)  
---
</details>  
  
<br />  
  
## VULNERABILITIES #41 
  
<br />  
  
## ISSUES are filtered and only blocking and critical issues are reported due to the high quantity of issues  
The complete list of issues can be found [here](https://sonarcloud.io/summary/overall?id=muttistefano_ros2_sonarcloud) .  
<br />  
  
## ISSUES (level blocker) #1206 
<details><summary><a style='color:blue;font-size:18px;'>eclipse-cyclonedds</a></summary>  

  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:2021  
  message : Replace this call to the non reentrant function "ctime" by a call to "ctime_r".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46dL)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:2609  
  message : Out of bound memory access (index is tainted)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46ex)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:2736  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46ey)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:3250  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46ez)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4267  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46eH)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4271  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46e0)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4394  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46eS)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4721  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46eg)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4723  
  message : Memory comparison function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46e1)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4723  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46ef)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4724  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46ee)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4915  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46ep)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4999  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46es)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:2021  
  message : Replace this call to the non reentrant function "ctime" by a call to "ctime_r".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46dL)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:2609  
  message : Out of bound memory access (index is tainted)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46ex)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:2736  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46ey)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:3250  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46ez)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4267  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46eH)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4271  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46e0)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4394  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46eS)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4721  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46eg)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4723  
  message : Memory comparison function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46e1)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4723  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46ef)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4724  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46ee)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4915  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46ep)  
---
  * file : eclipse-cyclonedds/cyclonedds/src/tools/idlpp/src/system.c:4999  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pYBew2X4EK9K46es)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>ros2</a></summary>  

  * file : ros2/geometry2/tf2_kdl/test/test_tf2_kdl.cpp:86  
  message : Use pointer or reference to avoid slicing from "StampedKDL::Vector" to "Vector".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pETvw2X4EK9K42Dh)  
---
  * file : ros2/geometry2/tf2_kdl/test/test_tf2_kdl.cpp:92  
  message : Use pointer or reference to avoid slicing from "StampedKDL::Vector" to "Vector".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pETvw2X4EK9K42Di)  
---
  * file : ros2/geometry2/tf2_py/src/tf2_py.cpp:51  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pES8w2X4EK9K42Bu)  
---
  * file : ros2/message_filters/include/message_filters/sync_policies/latest_time.h:219  
  message : Make sure that moving an object of class "Rate" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pJDYw2X4EK9K44Rt)  
---
  * file : ros2/message_filters/test/test_approximate_time_policy.cpp:76  
  message : Make sure that moving an object of class "TimeQuad" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pJIzw2X4EK9K44YX)  
---
  * file : ros2/message_filters/test/test_synchronizer.cpp:43  
  message : Make sure that moving an object of class "Header" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pJJww2X4EK9K44bQ)  
---
  * file : ros2/message_filters/test/test_synchronizer.cpp:49  
  message : Make sure that moving an object of class "Msg" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pJJww2X4EK9K44bR)  
---
  * file : ros2/message_filters/test/time_synchronizer_unittest.cpp:44  
  message : Make sure that moving an object of class "Header" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pJJEw2X4EK9K44aT)  
---
  * file : ros2/message_filters/test/time_synchronizer_unittest.cpp:49  
  message : Make sure that moving an object of class "Msg" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pJJEw2X4EK9K44aU)  
---
  * file : ros2/rcl/rcl/test/mocking_utils/patch.hpp:270  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFUPw2X4EK9K42co)  
---
  * file : ros2/rcl/rcl/test/mocking_utils/patch.hpp:339  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFUPw2X4EK9K42ct)  
---
  * file : ros2/rcl/rcl/test/mocking_utils/patch.hpp:345  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFUPw2X4EK9K42cu)  
---
  * file : ros2/rcl/rcl/test/rcl/allocator_testing_utils.h:98  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFNOw2X4EK9K42Sh)  
---
  * file : ros2/rcl/rcl/test/rcl/allocator_testing_utils.h:110  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFNOw2X4EK9K42Sk)  
---
  * file : ros2/rcl/rcl/test/rcl/allocator_testing_utils.h:123  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFNOw2X4EK9K42Sn)  
---
  * file : ros2/rcl/rcl/test/rcl/allocator_testing_utils.h:135  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFNOw2X4EK9K42Sq)  
---
  * file : ros2/rcl/rcl_action/test/rcl_action/test_action_client.cpp:38  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFoHw2X4EK9K42mP)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/mocking_utils/patch.hpp:161  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqR2zCYfarq97Iqz)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/mocking_utils/patch.hpp:230  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqR2zCYfarq97Iq4)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/mocking_utils/patch.hpp:236  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqR2zCYfarq97Iq5)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/time_bomb_allocator_testing_utils.h:39  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqRFzCYfarq97Iqa)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/time_bomb_allocator_testing_utils.h:51  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqRFzCYfarq97Iqb)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/time_bomb_allocator_testing_utils.h:64  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqRFzCYfarq97Iqc)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/time_bomb_allocator_testing_utils.h:76  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqRFzCYfarq97Iqd)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/client.hpp:292  
  message : Potential memory leak  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGEkw2X4EK9K42zv)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/event_handler.hpp:86  
  message : Make sure that moving an object of class "UnsupportedEventTypeException" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGREw2X4EK9K425y)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/exceptions/exceptions.hpp:152  
  message : Make sure that moving an object of class "RCLError" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGD-w2X4EK9K42zQ)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/exceptions/exceptions.hpp:162  
  message : Make sure that moving an object of class "RCLBadAlloc" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGD-w2X4EK9K42zR)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/exceptions/exceptions.hpp:172  
  message : Make sure that moving an object of class "RCLInvalidArgument" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGD-w2X4EK9K42zS)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/exceptions/exceptions.hpp:185  
  message : Make sure that moving an object of class "RCLInvalidROSArgsError" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGD-w2X4EK9K42zT)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/publisher_factory.hpp:50  
  message : Make sure that moving an object of class "PublisherFactory" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGImw2X4EK9K421V)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/serialized_message.hpp:61  
  message : Ensure that the move constructor of "SerializedMessage" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGH-w2X4EK9K421L)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/serialized_message.hpp:73  
  message : Ensure that the move assignment operator of "SerializedMessage" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGH-w2X4EK9K421M)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/service.hpp:201  
  message : Potential memory leak  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGPxw2X4EK9K424h)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/subscription_base.hpp:366  
  message : Potential memory leak  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGNxw2X4EK9K423n)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/subscription_factory.hpp:54  
  message : Make sure that moving an object of class "SubscriptionFactory" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGO2w2X4EK9K423x)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/timer.hpp:230  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGKJw2X4EK9K421i)  
---
  * file : ros2/rclcpp/rclcpp/src/rclcpp/clock.cpp:167  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGnXw2X4EK9K43Kr)  
---
  * file : ros2/rclcpp/rclcpp/src/rclcpp/wait_set_policies/detail/write_preferring_read_write_lock.cpp:54  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGXpw2X4EK9K428Q)  
---
  * file : ros2/rclcpp/rclcpp/src/rclcpp/wait_set_policies/detail/write_preferring_read_write_lock.cpp:82  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGXpw2X4EK9K428T)  
---
  * file : ros2/rclcpp/rclcpp/test/mocking_utils/patch.hpp:343  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHD3w2X4EK9K43sr)  
---
  * file : ros2/rclcpp/rclcpp/test/mocking_utils/patch.hpp:412  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHD3w2X4EK9K43sw)  
---
  * file : ros2/rclcpp/rclcpp/test/mocking_utils/patch.hpp:418  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHD3w2X4EK9K43sx)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, const test_msgs::msg::Empty_std::allocatorvoid &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aF)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, const test_msgs::msg::Empty_std::allocatorvoid &, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aG)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const MyEmpty &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aH)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const MyEmpty &, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aI)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const test_msgs::msg::Empty_std::allocatorvoid &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aJ)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const test_msgs::msg::Empty_std::allocatorvoid &, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aK)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, std::unique_ptrtest_msgs::msg::Empty_std::allocatorvoid" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aL)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, std::unique_ptrtest_msgs::msg::Empty_std::allocatorvoid, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aM)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::unique_ptrtest_msgs::msg::Empty_std::allocatorvoid" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aN)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::unique_ptrtest_msgs::msg::Empty_std::allocatorvoid, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aO)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aP)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aQ)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrconst MyEmpty" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aR)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrconst MyEmpty, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aS)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aT)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aU)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, const std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aV)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, const std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid &, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aW)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const std::shared_ptrconst MyEmpty &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aX)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const std::shared_ptrconst MyEmpty &, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aY)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aZ)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid &, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aa)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, std::shared_ptrtest_msgs::msg::Empty_std::allocatorvoid" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43ab)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, std::shared_ptrtest_msgs::msg::Empty_std::allocatorvoid, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43ac)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrMyEmpty" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43ad)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrMyEmpty, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43ae)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrtest_msgs::msg::Empty_std::allocatorvoid" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43af)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrtest_msgs::msg::Empty_std::allocatorvoid, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43ag)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_copy_all_parameter_values.cpp:52  
  message : Replace "override" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHBow2X4EK9K43rT)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_copy_all_parameter_values.cpp:80  
  message : Replace "override" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHBow2X4EK9K43rV)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_intra_process_manager.cpp:113  
  message : Potential leak of memory pointed to by field '_M_pi'  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG-Xw2X4EK9K43mO)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_intra_process_manager_with_allocators.cpp:207  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHAZw2X4EK9K43pj)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_time_source.cpp:817  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1qw2X4EK9K43bL)  
---
  * file : ros2/rclcpp/rclcpp_action/test/mocking_utils/patch.hpp:178  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHLjw2X4EK9K43zN)  
---
  * file : ros2/rclcpp/rclcpp_action/test/mocking_utils/patch.hpp:247  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHLjw2X4EK9K43zS)  
---
  * file : ros2/rclcpp/rclcpp_action/test/mocking_utils/patch.hpp:253  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHLjw2X4EK9K43zT)  
---
  * file : ros2/rclcpp/rclcpp_lifecycle/test/mocking_utils/patch.hpp:315  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHFRw2X4EK9K43uI)  
---
  * file : ros2/rclcpp/rclcpp_lifecycle/test/mocking_utils/patch.hpp:384  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHFRw2X4EK9K43uN)  
---
  * file : ros2/rclcpp/rclcpp_lifecycle/test/mocking_utils/patch.hpp:390  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHFRw2X4EK9K43uO)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/action_client.cpp:273  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEmJw2X4EK9K42JK)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/action_client.hpp:237  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEgSw2X4EK9K42GT)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/action_goal_handle.cpp:99  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEjaw2X4EK9K42HT)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/action_goal_handle.hpp:85  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pElRw2X4EK9K42Ip)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/action_server.cpp:363  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEkXw2X4EK9K42H6)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/action_server.hpp:263  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEigw2X4EK9K42Gt)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/client.cpp:174  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEfmw2X4EK9K42Fr)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/client.hpp:123  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEhyw2X4EK9K42Gq)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/clock.cpp:175  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEeNw2X4EK9K42EY)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/clock.hpp:120  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEn9w2X4EK9K42KG)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/clock_event.cpp:95  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEqBw2X4EK9K42LX)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/clock_event.hpp:66  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEpDw2X4EK9K42Kn)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/context.cpp:167  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEgDw2X4EK9K42GR)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/context.hpp:62  
  message : Make sure that moving an object of class "Context" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEe3w2X4EK9K42Eo)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/context.hpp:107  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEe3w2X4EK9K42En)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/destroyable.cpp:76  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pElew2X4EK9K42It)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/destroyable.hpp:63  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEnvw2X4EK9K42KF)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/duration.cpp:31  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEl6w2X4EK9K42Iv)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/duration.hpp:28  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEj6w2X4EK9K42HW)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/event_handle.cpp:176  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEmYw2X4EK9K42JT)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/event_handle.hpp:103  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEhXw2X4EK9K42Gn)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/guard_condition.cpp:75  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEebw2X4EK9K42Ee)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/guard_condition.hpp:72  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEoYw2X4EK9K42KL)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/lifecycle.hpp:29  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEhlw2X4EK9K42Go)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/logging_api.hpp:29  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEpRw2X4EK9K42Ko)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/node.cpp:581  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEm4w2X4EK9K42J8)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/node.hpp:31  
  message : Make sure that moving an object of class "Node" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEi-w2X4EK9K42HI)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/node.hpp:221  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEi-w2X4EK9K42HJ)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/publisher.cpp:163  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEk0w2X4EK9K42IQ)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/publisher.hpp:38  
  message : Make sure that moving an object of class "Publisher" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEnUw2X4EK9K42J_)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/publisher.hpp:135  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEnUw2X4EK9K42KA)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/qos.cpp:164  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEklw2X4EK9K42H-)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/qos.hpp:75  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEmlw2X4EK9K42JW)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/service.cpp:177  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEo2w2X4EK9K42Kl)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/service.hpp:125  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEdPw2X4EK9K42Dz)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/service_info.cpp:25  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEiAw2X4EK9K42Gr)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/service_info.hpp:28  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEhJw2X4EK9K42Gl)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/service_introspection.cpp:22  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEnGw2X4EK9K42J-)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/service_introspection.hpp:26  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEjnw2X4EK9K42HV)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/signal_handler.hpp:29  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEgfw2X4EK9K42GU)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/subscription.cpp:185  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEonw2X4EK9K42KY)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/subscription.hpp:38  
  message : Make sure that moving an object of class "Subscription" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEdAw2X4EK9K42Dw)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/subscription.hpp:113  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEdAw2X4EK9K42Dx)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/time_point.cpp:34  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEcyw2X4EK9K42Dv)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/time_point.hpp:28  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEiNw2X4EK9K42Gs)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/timer.cpp:159  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEfFw2X4EK9K42E7)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/timer.hpp:150  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEniw2X4EK9K42KC)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/type_description_service.cpp:61  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEqPw2X4EK9K42Lc)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/type_description_service.hpp:71  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEdsw2X4EK9K42EK)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/wait_set.cpp:255  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEpzw2X4EK9K42LN)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/wait_set.hpp:181  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEkIw2X4EK9K42HX)  
---
  * file : ros2/rcpputils/include/rcpputils/scope_exit.hpp:29  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISir08zCYfarq97JF4)  
---
  * file : ros2/rcpputils/include/rcpputils/scope_exit.hpp:34  
  message : Ensure that the move constructor of "scope_exit" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISir08zCYfarq97JF0)  
---
  * file : ros2/rcpputils/include/rcpputils/scope_exit.hpp:37  
  message : Ensure that the move assignment operator of "scope_exit" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISir08zCYfarq97JF1)  
---
  * file : ros2/rcpputils/test/test_find_library.cpp:63  
  message : Replace "override" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiruozCYfarq97JCx)  
---
  * file : ros2/rcutils/src/error_handling_helpers.h:82  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYvGYSeY228C2JcY-al-)  
---
  * file : ros2/rcutils/test/mocking_utils/patch.hpp:160  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirK4zCYfarq97I5p)  
---
  * file : ros2/rcutils/test/mocking_utils/patch.hpp:234  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirK4zCYfarq97I5q)  
---
  * file : ros2/rcutils/test/mocking_utils/patch.hpp:240  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirK4zCYfarq97I5r)  
---
  * file : ros2/rcutils/test/test_string_map.cpp:1951  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYa0uTVeaL88A9HpsmQA)  
---
  * file : ros2/rcutils/test/time_bomb_allocator_testing_utils.h:39  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirJszCYfarq97I2w)  
---
  * file : ros2/rcutils/test/time_bomb_allocator_testing_utils.h:51  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirJszCYfarq97I2x)  
---
  * file : ros2/rcutils/test/time_bomb_allocator_testing_utils.h:64  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirJszCYfarq97I2y)  
---
  * file : ros2/rcutils/test/time_bomb_allocator_testing_utils.h:76  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirJszCYfarq97I2z)  
---
  * file : ros2/rmw/rmw/test/time_bomb_allocator_testing_utils.h:39  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISioJmzCYfarq97IQh)  
---
  * file : ros2/rmw/rmw/test/time_bomb_allocator_testing_utils.h:51  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISioJmzCYfarq97IQi)  
---
  * file : ros2/rmw/rmw/test/time_bomb_allocator_testing_utils.h:64  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISioJmzCYfarq97IQj)  
---
  * file : ros2/rmw/rmw/test/time_bomb_allocator_testing_utils.h:76  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISioJmzCYfarq97IQk)  
---
  * file : ros2/rmw_fastrtps/rmw_fastrtps_shared_cpp/include/rmw_fastrtps_shared_cpp/guid_utils.hpp:56  
  message : Use constructors or assignment operators, "EntityId_t" is not trivially copyable.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-wb33-gB3mVexO4O)  
---
  * file : ros2/rosbag2/rosbag2_cpp/include/rosbag2_cpp/message_definitions/local_message_definition_source.hpp:86  
  message : Make sure that moving an object of class "MessageSpec" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBmOw2X4EK9K41rg)  
---
  * file : ros2/rosbag2/rosbag2_storage_sqlite3/include/rosbag2_storage_sqlite3/sqlite_statement_wrapper.hpp:81  
  message : Ensure that the move constructor of "Iterator" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pB_Mw2X4EK9K41z9)  
---
  * file : ros2/rosbag2/rosbag2_storage_sqlite3/include/rosbag2_storage_sqlite3/sqlite_statement_wrapper.hpp:82  
  message : Ensure that the move assignment operator of "Iterator" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pB_Mw2X4EK9K41z-)  
---
  * file : ros2/rosbag2/rosbag2_transport/include/rosbag2_transport/play_options.hpp:32  
  message : Make sure that moving an object of class "PlayOptions" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBiPw2X4EK9K41rB)  
---
  * file : ros2/rosbag2/rosbag2_transport/test/rosbag2_transport/test_play_seek.cpp:99  
  message : Field "reader_" shadows a field of the same name in base class "Rosbag2TransportTestFixture".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBe9w2X4EK9K41qY)  
---
  * file : ros2/rosbag2/rosbag2_transport/test/rosbag2_transport/test_play_timing.cpp:38  
  message : Field "storage_options_" shadows a field of the same name in base class "Rosbag2TransportTestFixture".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBd3w2X4EK9K41qK)  
---
  * file : ros2/rosbag2/rosbag2_transport/test/rosbag2_transport/test_play_timing.cpp:39  
  message : Field "play_options_" shadows a field of the same name in base class "Rosbag2TransportTestFixture".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBd3w2X4EK9K41qL)  
---
  * file : ros2/rosidl/rosidl_runtime_cpp/include/rosidl_runtime_cpp/bounded_vector.hpp:219  
  message : Ensure that the move assignment operator of "BoundedVector" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISik0dzCYfarq97Hzd)  
---
  * file : ros2/rosidl/rosidl_runtime_cpp/include/rosidl_runtime_cpp/bounded_vector.hpp:785  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISik0dzCYfarq97Hzq)  
---
  * file : ros2/rosidl_dynamic_typesupport_fastrtps/src/detail/utils.cpp:44  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYdpFSuiMwG3nqqZuH7j)  
---
  * file : ros2/rosidl_typesupport/rosidl_typesupport_c/test/mocking_utils/patch.hpp:343  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirsBzCYfarq97JCI)  
---
  * file : ros2/rosidl_typesupport/rosidl_typesupport_c/test/mocking_utils/patch.hpp:412  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirsBzCYfarq97JCN)  
---
  * file : ros2/rosidl_typesupport/rosidl_typesupport_c/test/mocking_utils/patch.hpp:418  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirsBzCYfarq97JCO)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/covariance_visual.cpp:152  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u493-gB3mVexOlm)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:58  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmR)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:60  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmS)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:62  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmT)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:64  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmU)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:66  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmV)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/render_system.cpp:241  
  message : Name this temporary "unique_ptrOgre::RenderSystemCapabilities" object if you want to use it in for RAII.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u8b3-gB3mVexOpI)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/render_system.cpp:552  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u8b3-gB3mVexOpX)  
---
  * file : ros2/system_tests/test_rclcpp/test/pub_sub_fixtures.hpp:92  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pInOw2X4EK9K44Ml)  
---
  * file : ros2/geometry2/tf2_kdl/test/test_tf2_kdl.cpp:86  
  message : Use pointer or reference to avoid slicing from "StampedKDL::Vector" to "Vector".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pETvw2X4EK9K42Dh)  
---
  * file : ros2/geometry2/tf2_kdl/test/test_tf2_kdl.cpp:92  
  message : Use pointer or reference to avoid slicing from "StampedKDL::Vector" to "Vector".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pETvw2X4EK9K42Di)  
---
  * file : ros2/geometry2/tf2_py/src/tf2_py.cpp:51  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pES8w2X4EK9K42Bu)  
---
  * file : ros2/message_filters/include/message_filters/sync_policies/latest_time.h:219  
  message : Make sure that moving an object of class "Rate" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pJDYw2X4EK9K44Rt)  
---
  * file : ros2/message_filters/test/test_approximate_time_policy.cpp:76  
  message : Make sure that moving an object of class "TimeQuad" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pJIzw2X4EK9K44YX)  
---
  * file : ros2/message_filters/test/test_synchronizer.cpp:43  
  message : Make sure that moving an object of class "Header" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pJJww2X4EK9K44bQ)  
---
  * file : ros2/message_filters/test/test_synchronizer.cpp:49  
  message : Make sure that moving an object of class "Msg" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pJJww2X4EK9K44bR)  
---
  * file : ros2/message_filters/test/time_synchronizer_unittest.cpp:44  
  message : Make sure that moving an object of class "Header" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pJJEw2X4EK9K44aT)  
---
  * file : ros2/message_filters/test/time_synchronizer_unittest.cpp:49  
  message : Make sure that moving an object of class "Msg" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pJJEw2X4EK9K44aU)  
---
  * file : ros2/rcl/rcl/test/mocking_utils/patch.hpp:270  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFUPw2X4EK9K42co)  
---
  * file : ros2/rcl/rcl/test/mocking_utils/patch.hpp:339  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFUPw2X4EK9K42ct)  
---
  * file : ros2/rcl/rcl/test/mocking_utils/patch.hpp:345  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFUPw2X4EK9K42cu)  
---
  * file : ros2/rcl/rcl/test/rcl/allocator_testing_utils.h:98  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFNOw2X4EK9K42Sh)  
---
  * file : ros2/rcl/rcl/test/rcl/allocator_testing_utils.h:110  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFNOw2X4EK9K42Sk)  
---
  * file : ros2/rcl/rcl/test/rcl/allocator_testing_utils.h:123  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFNOw2X4EK9K42Sn)  
---
  * file : ros2/rcl/rcl/test/rcl/allocator_testing_utils.h:135  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFNOw2X4EK9K42Sq)  
---
  * file : ros2/rcl/rcl_action/test/rcl_action/test_action_client.cpp:38  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pFoHw2X4EK9K42mP)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/mocking_utils/patch.hpp:161  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqR2zCYfarq97Iqz)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/mocking_utils/patch.hpp:230  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqR2zCYfarq97Iq4)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/mocking_utils/patch.hpp:236  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqR2zCYfarq97Iq5)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/time_bomb_allocator_testing_utils.h:39  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqRFzCYfarq97Iqa)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/time_bomb_allocator_testing_utils.h:51  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqRFzCYfarq97Iqb)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/time_bomb_allocator_testing_utils.h:64  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqRFzCYfarq97Iqc)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/time_bomb_allocator_testing_utils.h:76  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqRFzCYfarq97Iqd)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/client.hpp:292  
  message : Potential memory leak  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGEkw2X4EK9K42zv)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/event_handler.hpp:86  
  message : Make sure that moving an object of class "UnsupportedEventTypeException" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGREw2X4EK9K425y)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/exceptions/exceptions.hpp:152  
  message : Make sure that moving an object of class "RCLError" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGD-w2X4EK9K42zQ)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/exceptions/exceptions.hpp:162  
  message : Make sure that moving an object of class "RCLBadAlloc" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGD-w2X4EK9K42zR)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/exceptions/exceptions.hpp:172  
  message : Make sure that moving an object of class "RCLInvalidArgument" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGD-w2X4EK9K42zS)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/exceptions/exceptions.hpp:185  
  message : Make sure that moving an object of class "RCLInvalidROSArgsError" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGD-w2X4EK9K42zT)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/publisher_factory.hpp:50  
  message : Make sure that moving an object of class "PublisherFactory" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGImw2X4EK9K421V)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/serialized_message.hpp:61  
  message : Ensure that the move constructor of "SerializedMessage" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGH-w2X4EK9K421L)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/serialized_message.hpp:73  
  message : Ensure that the move assignment operator of "SerializedMessage" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGH-w2X4EK9K421M)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/service.hpp:201  
  message : Potential memory leak  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGPxw2X4EK9K424h)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/subscription_base.hpp:366  
  message : Potential memory leak  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGNxw2X4EK9K423n)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/subscription_factory.hpp:54  
  message : Make sure that moving an object of class "SubscriptionFactory" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGO2w2X4EK9K423x)  
---
  * file : ros2/rclcpp/rclcpp/include/rclcpp/timer.hpp:230  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGKJw2X4EK9K421i)  
---
  * file : ros2/rclcpp/rclcpp/src/rclcpp/clock.cpp:167  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGnXw2X4EK9K43Kr)  
---
  * file : ros2/rclcpp/rclcpp/src/rclcpp/wait_set_policies/detail/write_preferring_read_write_lock.cpp:54  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGXpw2X4EK9K428Q)  
---
  * file : ros2/rclcpp/rclcpp/src/rclcpp/wait_set_policies/detail/write_preferring_read_write_lock.cpp:82  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pGXpw2X4EK9K428T)  
---
  * file : ros2/rclcpp/rclcpp/test/mocking_utils/patch.hpp:343  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHD3w2X4EK9K43sr)  
---
  * file : ros2/rclcpp/rclcpp/test/mocking_utils/patch.hpp:412  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHD3w2X4EK9K43sw)  
---
  * file : ros2/rclcpp/rclcpp/test/mocking_utils/patch.hpp:418  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHD3w2X4EK9K43sx)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, const test_msgs::msg::Empty_std::allocatorvoid &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aF)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, const test_msgs::msg::Empty_std::allocatorvoid &, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aG)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const MyEmpty &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aH)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const MyEmpty &, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aI)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const test_msgs::msg::Empty_std::allocatorvoid &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aJ)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const test_msgs::msg::Empty_std::allocatorvoid &, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aK)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, std::unique_ptrtest_msgs::msg::Empty_std::allocatorvoid" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aL)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, std::unique_ptrtest_msgs::msg::Empty_std::allocatorvoid, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aM)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::unique_ptrtest_msgs::msg::Empty_std::allocatorvoid" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aN)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::unique_ptrtest_msgs::msg::Empty_std::allocatorvoid, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aO)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aP)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aQ)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrconst MyEmpty" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aR)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrconst MyEmpty, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aS)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aT)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aU)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, const std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aV)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, const std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid &, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aW)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const std::shared_ptrconst MyEmpty &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aX)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const std::shared_ptrconst MyEmpty &, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aY)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aZ)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, const std::shared_ptrconst test_msgs::msg::Empty_std::allocatorvoid &, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43aa)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, std::shared_ptrtest_msgs::msg::Empty_std::allocatorvoid" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43ab)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContexttest_msgs::msg::Empty_std::allocatorvoid, std::shared_ptrtest_msgs::msg::Empty_std::allocatorvoid, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43ac)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrMyEmpty" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43ad)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrMyEmpty, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43ae)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrtest_msgs::msg::Empty_std::allocatorvoid" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43af)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_any_subscription_callback.cpp:348  
  message : Make sure that moving an object of class "BindContextrclcpp::TypeAdapterMyEmpty, test_msgs::msg::Empty, std::shared_ptrtest_msgs::msg::Empty_std::allocatorvoid, const rclcpp::MessageInfo &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1Ew2X4EK9K43ag)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_copy_all_parameter_values.cpp:52  
  message : Replace "override" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHBow2X4EK9K43rT)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_copy_all_parameter_values.cpp:80  
  message : Replace "override" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHBow2X4EK9K43rV)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_intra_process_manager.cpp:113  
  message : Potential leak of memory pointed to by field '_M_pi'  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG-Xw2X4EK9K43mO)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_intra_process_manager_with_allocators.cpp:207  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHAZw2X4EK9K43pj)  
---
  * file : ros2/rclcpp/rclcpp/test/rclcpp/test_time_source.cpp:817  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pG1qw2X4EK9K43bL)  
---
  * file : ros2/rclcpp/rclcpp_action/test/mocking_utils/patch.hpp:178  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHLjw2X4EK9K43zN)  
---
  * file : ros2/rclcpp/rclcpp_action/test/mocking_utils/patch.hpp:247  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHLjw2X4EK9K43zS)  
---
  * file : ros2/rclcpp/rclcpp_action/test/mocking_utils/patch.hpp:253  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHLjw2X4EK9K43zT)  
---
  * file : ros2/rclcpp/rclcpp_lifecycle/test/mocking_utils/patch.hpp:315  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHFRw2X4EK9K43uI)  
---
  * file : ros2/rclcpp/rclcpp_lifecycle/test/mocking_utils/patch.hpp:384  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHFRw2X4EK9K43uN)  
---
  * file : ros2/rclcpp/rclcpp_lifecycle/test/mocking_utils/patch.hpp:390  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pHFRw2X4EK9K43uO)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/action_client.cpp:273  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEmJw2X4EK9K42JK)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/action_client.hpp:237  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEgSw2X4EK9K42GT)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/action_goal_handle.cpp:99  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEjaw2X4EK9K42HT)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/action_goal_handle.hpp:85  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pElRw2X4EK9K42Ip)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/action_server.cpp:363  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEkXw2X4EK9K42H6)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/action_server.hpp:263  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEigw2X4EK9K42Gt)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/client.cpp:174  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEfmw2X4EK9K42Fr)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/client.hpp:123  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEhyw2X4EK9K42Gq)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/clock.cpp:175  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEeNw2X4EK9K42EY)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/clock.hpp:120  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEn9w2X4EK9K42KG)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/clock_event.cpp:95  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEqBw2X4EK9K42LX)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/clock_event.hpp:66  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEpDw2X4EK9K42Kn)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/context.cpp:167  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEgDw2X4EK9K42GR)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/context.hpp:62  
  message : Make sure that moving an object of class "Context" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEe3w2X4EK9K42Eo)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/context.hpp:107  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEe3w2X4EK9K42En)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/destroyable.cpp:76  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pElew2X4EK9K42It)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/destroyable.hpp:63  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEnvw2X4EK9K42KF)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/duration.cpp:31  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEl6w2X4EK9K42Iv)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/duration.hpp:28  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEj6w2X4EK9K42HW)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/event_handle.cpp:176  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEmYw2X4EK9K42JT)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/event_handle.hpp:103  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEhXw2X4EK9K42Gn)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/guard_condition.cpp:75  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEebw2X4EK9K42Ee)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/guard_condition.hpp:72  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEoYw2X4EK9K42KL)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/lifecycle.hpp:29  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEhlw2X4EK9K42Go)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/logging_api.hpp:29  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEpRw2X4EK9K42Ko)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/node.cpp:581  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEm4w2X4EK9K42J8)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/node.hpp:31  
  message : Make sure that moving an object of class "Node" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEi-w2X4EK9K42HI)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/node.hpp:221  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEi-w2X4EK9K42HJ)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/publisher.cpp:163  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEk0w2X4EK9K42IQ)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/publisher.hpp:38  
  message : Make sure that moving an object of class "Publisher" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEnUw2X4EK9K42J_)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/publisher.hpp:135  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEnUw2X4EK9K42KA)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/qos.cpp:164  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEklw2X4EK9K42H-)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/qos.hpp:75  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEmlw2X4EK9K42JW)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/service.cpp:177  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEo2w2X4EK9K42Kl)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/service.hpp:125  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEdPw2X4EK9K42Dz)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/service_info.cpp:25  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEiAw2X4EK9K42Gr)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/service_info.hpp:28  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEhJw2X4EK9K42Gl)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/service_introspection.cpp:22  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEnGw2X4EK9K42J-)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/service_introspection.hpp:26  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEjnw2X4EK9K42HV)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/signal_handler.hpp:29  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEgfw2X4EK9K42GU)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/subscription.cpp:185  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEonw2X4EK9K42KY)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/subscription.hpp:38  
  message : Make sure that moving an object of class "Subscription" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEdAw2X4EK9K42Dw)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/subscription.hpp:113  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEdAw2X4EK9K42Dx)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/time_point.cpp:34  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEcyw2X4EK9K42Dv)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/time_point.hpp:28  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEiNw2X4EK9K42Gs)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/timer.cpp:159  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEfFw2X4EK9K42E7)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/timer.hpp:150  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEniw2X4EK9K42KC)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/type_description_service.cpp:61  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEqPw2X4EK9K42Lc)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/type_description_service.hpp:71  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEdsw2X4EK9K42EK)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/wait_set.cpp:255  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEpzw2X4EK9K42LN)  
---
  * file : ros2/rclpy/rclpy/src/rclpy/wait_set.hpp:181  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pEkIw2X4EK9K42HX)  
---
  * file : ros2/rcpputils/include/rcpputils/scope_exit.hpp:29  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISir08zCYfarq97JF4)  
---
  * file : ros2/rcpputils/include/rcpputils/scope_exit.hpp:34  
  message : Ensure that the move constructor of "scope_exit" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISir08zCYfarq97JF0)  
---
  * file : ros2/rcpputils/include/rcpputils/scope_exit.hpp:37  
  message : Ensure that the move assignment operator of "scope_exit" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISir08zCYfarq97JF1)  
---
  * file : ros2/rcpputils/test/test_find_library.cpp:63  
  message : Replace "override" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiruozCYfarq97JCx)  
---
  * file : ros2/rcutils/src/error_handling_helpers.h:82  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYvGYSeY228C2JcY-al-)  
---
  * file : ros2/rcutils/test/mocking_utils/patch.hpp:160  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirK4zCYfarq97I5p)  
---
  * file : ros2/rcutils/test/mocking_utils/patch.hpp:234  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirK4zCYfarq97I5q)  
---
  * file : ros2/rcutils/test/mocking_utils/patch.hpp:240  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirK4zCYfarq97I5r)  
---
  * file : ros2/rcutils/test/test_string_map.cpp:1951  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYa0uTVeaL88A9HpsmQA)  
---
  * file : ros2/rcutils/test/time_bomb_allocator_testing_utils.h:39  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirJszCYfarq97I2w)  
---
  * file : ros2/rcutils/test/time_bomb_allocator_testing_utils.h:51  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirJszCYfarq97I2x)  
---
  * file : ros2/rcutils/test/time_bomb_allocator_testing_utils.h:64  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirJszCYfarq97I2y)  
---
  * file : ros2/rcutils/test/time_bomb_allocator_testing_utils.h:76  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirJszCYfarq97I2z)  
---
  * file : ros2/rmw/rmw/test/time_bomb_allocator_testing_utils.h:39  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISioJmzCYfarq97IQh)  
---
  * file : ros2/rmw/rmw/test/time_bomb_allocator_testing_utils.h:51  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISioJmzCYfarq97IQi)  
---
  * file : ros2/rmw/rmw/test/time_bomb_allocator_testing_utils.h:64  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISioJmzCYfarq97IQj)  
---
  * file : ros2/rmw/rmw/test/time_bomb_allocator_testing_utils.h:76  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISioJmzCYfarq97IQk)  
---
  * file : ros2/rmw_fastrtps/rmw_fastrtps_shared_cpp/include/rmw_fastrtps_shared_cpp/guid_utils.hpp:56  
  message : Use constructors or assignment operators, "EntityId_t" is not trivially copyable.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-wb33-gB3mVexO4O)  
---
  * file : ros2/rosbag2/rosbag2_cpp/include/rosbag2_cpp/message_definitions/local_message_definition_source.hpp:86  
  message : Make sure that moving an object of class "MessageSpec" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBmOw2X4EK9K41rg)  
---
  * file : ros2/rosbag2/rosbag2_storage_sqlite3/include/rosbag2_storage_sqlite3/sqlite_statement_wrapper.hpp:81  
  message : Ensure that the move constructor of "Iterator" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pB_Mw2X4EK9K41z9)  
---
  * file : ros2/rosbag2/rosbag2_storage_sqlite3/include/rosbag2_storage_sqlite3/sqlite_statement_wrapper.hpp:82  
  message : Ensure that the move assignment operator of "Iterator" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pB_Mw2X4EK9K41z-)  
---
  * file : ros2/rosbag2/rosbag2_transport/include/rosbag2_transport/play_options.hpp:32  
  message : Make sure that moving an object of class "PlayOptions" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBiPw2X4EK9K41rB)  
---
  * file : ros2/rosbag2/rosbag2_transport/test/rosbag2_transport/test_play_seek.cpp:99  
  message : Field "reader_" shadows a field of the same name in base class "Rosbag2TransportTestFixture".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBe9w2X4EK9K41qY)  
---
  * file : ros2/rosbag2/rosbag2_transport/test/rosbag2_transport/test_play_timing.cpp:38  
  message : Field "storage_options_" shadows a field of the same name in base class "Rosbag2TransportTestFixture".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBd3w2X4EK9K41qK)  
---
  * file : ros2/rosbag2/rosbag2_transport/test/rosbag2_transport/test_play_timing.cpp:39  
  message : Field "play_options_" shadows a field of the same name in base class "Rosbag2TransportTestFixture".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pBd3w2X4EK9K41qL)  
---
  * file : ros2/rosidl/rosidl_runtime_cpp/include/rosidl_runtime_cpp/bounded_vector.hpp:219  
  message : Ensure that the move assignment operator of "BoundedVector" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISik0dzCYfarq97Hzd)  
---
  * file : ros2/rosidl/rosidl_runtime_cpp/include/rosidl_runtime_cpp/bounded_vector.hpp:785  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISik0dzCYfarq97Hzq)  
---
  * file : ros2/rosidl_dynamic_typesupport_fastrtps/src/detail/utils.cpp:44  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYdpFSuiMwG3nqqZuH7j)  
---
  * file : ros2/rosidl_typesupport/rosidl_typesupport_c/test/mocking_utils/patch.hpp:343  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirsBzCYfarq97JCI)  
---
  * file : ros2/rosidl_typesupport/rosidl_typesupport_c/test/mocking_utils/patch.hpp:412  
  message : Ensure that the move constructor of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirsBzCYfarq97JCN)  
---
  * file : ros2/rosidl_typesupport/rosidl_typesupport_c/test/mocking_utils/patch.hpp:418  
  message : Ensure that the move assignment operator of "PatchID, ReturnT (ArgTs...)" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirsBzCYfarq97JCO)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/covariance_visual.cpp:152  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u493-gB3mVexOlm)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:58  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmR)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:60  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmS)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:62  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmT)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:64  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmU)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/objects/effort_visual.cpp:66  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u5w3-gB3mVexOmV)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/render_system.cpp:241  
  message : Name this temporary "unique_ptrOgre::RenderSystemCapabilities" object if you want to use it in for RAII.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u8b3-gB3mVexOpI)  
---
  * file : ros2/rviz/rviz_rendering/src/rviz_rendering/render_system.cpp:552  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-u8b3-gB3mVexOpX)  
---
  * file : ros2/system_tests/test_rclcpp/test/pub_sub_fixtures.hpp:92  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pInOw2X4EK9K44Ml)  
---
  * file : ros2/rcutils/src/cmdline_parser.c:40  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirRUzCYfarq97I81)  
---
  * file : ros2/rcutils/src/logging.c:436  
  message : Memory copy function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYqmAQdbWvNZCKI3y18h)  
---
  * file : ros2/rcutils/src/strdup.c:53  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirSSzCYfarq97I9X)  
---
  * file : ros2/rcutils/src/cmdline_parser.c:40  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirRUzCYfarq97I81)  
---
  * file : ros2/rcutils/src/logging.c:436  
  message : Memory copy function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYqmAQdbWvNZCKI3y18h)  
---
  * file : ros2/rcutils/src/strdup.c:53  
  message : Out of bound memory access (access exceeds upper limit of memory block)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirSSzCYfarq97I9X)  
---
</details>  
    
<br />  
  
