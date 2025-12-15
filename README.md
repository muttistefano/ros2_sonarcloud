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
  
## BUGS #452 
<details><summary><a style='color:blue;font-size:18px;'>ament</a></summary>  

  * file : ament/ament_index/ament_index_python/ament_index_python/search_paths.py:22  
  message : The return value of "str.format" must be used.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi4uWzCYfarq97P2L)  
---
  * file : ament/ament_index/ament_index_python/test/test_ament_index_python.py:81  
  message : Don’t perform an assertion here; An exception is expected to be raised before its execution.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-9x83-gB3mVexO-s)  
---
  * file : ament/ament_index/ament_index_python/test/test_ament_index_python.py:85  
  message : Don’t perform an assertion here; An exception is expected to be raised before its execution.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-9x83-gB3mVexO-t)  
---
  * file : ament/ament_index/ament_index_python/test/test_ament_index_python.py:130  
  message : Don’t perform an assertion here; An exception is expected to be raised before its execution.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-9x83-gB3mVexO-u)  
---
  * file : ament/ament_index/ament_index_python/test/test_ament_index_python.py:142  
  message : Don’t perform an assertion here; An exception is expected to be raised before its execution.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-9x83-gB3mVexO-v)  
---
  * file : ament/ament_lint/ament_cpplint/ament_cpplint/cpplint.py:3621  
  message : Rework this part of the regex to not match the empty string.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi4hnzCYfarq97PyS)  
---
  * file : ament/googletest/docs/_layouts/default.html:3  
  message : Add a title tag to this page.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZz6zeHXxtxeKK1WaA)  
---
</details>  
<details><summary><a style='color:blue;font-size:18px;'>eclipse-iceoryx</a></summary>  

  * file : eclipse-iceoryx/iceoryx/doc/website/overrides/partials/footer.html:62  
  message : Add an "alt" attribute to this image.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi1qYzCYfarq97PE2)  
---
  * file : eclipse-iceoryx/iceoryx/doc/website/overrides/partials/footer.html:64  
  message : Add an "alt" attribute to this image.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi1qYzCYfarq97PE3)  
---
  * file : eclipse-iceoryx/iceoryx/doc/website/overrides/partials/footer.html:66  
  message : Add an "alt" attribute to this image.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi1qYzCYfarq97PE4)  
---
  * file : eclipse-iceoryx/iceoryx/iceoryx_hoofs/include/iceoryx_hoofs/cxx/expected.hpp:65  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPJHepM_KNhuouaqt)  
---
  * file : eclipse-iceoryx/iceoryx/iceoryx_hoofs/include/iceoryx_hoofs/cxx/expected.hpp:108  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPJHepM_KNhuouaqu)  
---
  * file : eclipse-iceoryx/iceoryx/iceoryx_hoofs/include/iceoryx_hoofs/cxx/function_ref.hpp:90  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPJCzpM_KNhuouaqs)  
---
</details>  
<details><summary><a style='color:blue;font-size:18px;'>eProsima</a></summary>  

  * file : eProsima/Fast-CDR/utils/doxygen/pages/customdoxygen.css:176  
  message : Unexpected duplicate "font-size"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZpHgMjlZiJawz635PPk)  
---
  * file : eProsima/Fast-CDR/utils/doxygen/pages/customdoxygen.css:266  
  message : Unexpected nonstandard direction  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0NwzCYfarq97O-_)  
---
  * file : eProsima/Fast-CDR/utils/doxygen/pages/customdoxygen.css:620  
  message : Unexpected duplicate "background-color"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZpHgMjlZiJawz635PPl)  
---
  * file : eProsima/Fast-CDR/utils/doxygen/pages/customdoxygen.css:805  
  message : Unexpected missing generic font family  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0NwzCYfarq97O--)  
---
  * file : eProsima/Fast-CDR/utils/doxygen/pages/customdoxygen.css:1008  
  message : Unexpected duplicate "text-decoration"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0NwzCYfarq97O-9)  
---
  * file : eProsima/Fast-CDR/utils/doxygen/pages/eprosima_header.html:3  
  message : Add "lang" and/or "xml:lang" attributes to this "html" element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0NhzCYfarq97O-z)  
---
  * file : eProsima/Fast-CDR/utils/doxygen/pages/eprosima_header.html:23  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0NhzCYfarq97O-1)  
---
  * file : eProsima/Fast-CDR/utils/doxygen/pages/eprosima_header.html:40  
  message : Duplicate id "projectbrief" found. First occurrence was on line 34.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZpHgMjHZiJawz635PPg)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/log/Log.hpp:292  
  message : Potential leak of memory pointed to by 'p'  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhHYMMoXQXhL-_vi)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "_Bool"). "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALa)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "_Bool"). "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALc)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "_Bool"). "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALd)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "_Bool"). "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALe)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "_Bool"). "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALf)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "_Bool"). "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALg)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Replace "signed char" to "_Bool" type punning with "std::memcpy". "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALj)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Replace "unsigned char" to "_Bool" type punning with "std::memcpy". "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALk)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "unsigned char"). "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALn)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "unsigned char"). "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALp)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "unsigned char"). "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALq)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "unsigned char"). "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALr)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "unsigned char"). "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALs)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "unsigned char"). "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALt)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Replace "_Bool" to "unsigned char" type punning with "std::memcpy". "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALv)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Replace "signed char" to "unsigned char" type punning with "std::memcpy". "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ALx)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Replace "unsigned char" to "signed char" type punning with "std::memcpy". "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AL-)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "signed char"). "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AL0)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "signed char"). "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AL2)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "signed char"). "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AL3)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "signed char"). "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AL4)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "signed char"). "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AL5)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "signed char"). "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AL6)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Replace "_Bool" to "signed char" type punning with "std::memcpy". "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AL8)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "unsigned char"). "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMB)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "unsigned char"). "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMD)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "unsigned char"). "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AME)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "unsigned char"). "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMF)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "unsigned char"). "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMG)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "unsigned char"). "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMH)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Replace "_Bool" to "unsigned char" type punning with "std::memcpy". "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMJ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Replace "signed char" to "unsigned char" type punning with "std::memcpy". "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AML)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMM)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMQ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMS)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMT)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMU)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMV)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMW)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Replace "unsigned short" to "short" type punning with "std::memcpy". "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMY)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMZ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMd)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMf)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMg)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMh)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMi)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMj)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Replace "short" to "unsigned short" type punning with "std::memcpy". "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMl)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMm)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMq)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMr)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMs)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMt)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMu)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMv)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Replace "unsigned int" to "int" type punning with "std::memcpy". "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMx)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Replace "int" to "unsigned int" type punning with "std::memcpy". "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AM-)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AM3)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AM4)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AM5)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AM6)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AM7)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AM8)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AMz)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANA)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AND)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANF)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANG)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANH)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANI)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANJ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Replace "unsigned long" to "long" type punning with "std::memcpy". "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANM)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANN)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANQ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANS)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANT)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANU)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANV)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANW)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Replace "long" to "unsigned long" type punning with "std::memcpy". "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANZ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "float"). "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANa)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "float"). "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANe)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "float"). "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANf)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "float"). "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANg)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "float"). "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANh)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "float"). "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANj)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Replace "int" to "float" type punning with "std::memcpy". "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANk)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Replace "unsigned int" to "float" type punning with "std::memcpy". "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANl)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANn)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANq)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANs)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANt)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANu)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANv)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANw)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Replace "long" to "double" type punning with "std::memcpy". "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_ANy)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AN0)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AN4)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AN5)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AN6)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AN7)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AN8)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AN9)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AN_)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "char"). "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOD)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "char"). "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOF)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "char"). "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOG)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "char"). "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOH)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "char"). "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOJ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Replace "_Bool" to "char" type punning with "std::memcpy". "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOL)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Replace "signed char" to "char" type punning with "std::memcpy". "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOM)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Replace "unsigned char" to "char" type punning with "std::memcpy". "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AON)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "wchar_t"). "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOO)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "wchar_t"). "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOS)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "wchar_t"). "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOT)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "wchar_t"). "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOU)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "wchar_t"). "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOV)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "wchar_t"). "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOX)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Replace "int" to "wchar_t" type punning with "std::memcpy". "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOZ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Replace "unsigned int" to "wchar_t" type punning with "std::memcpy". "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOa)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "int"). "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOb)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "int"). "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOf)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "int"). "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOg)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "int"). "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOh)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "int"). "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOi)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "int"). "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOk)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Replace "unsigned int" to "int" type punning with "std::memcpy". "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOm)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AO0)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOo)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOs)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOu)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOv)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOw)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOx)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AOy)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AO-)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AO2)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AO6)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AO8)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AO9)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_AO_)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_APA)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_APC)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4725  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "class eprosima::fastdds::dds::xtypes::ExtendedAnnotationParameterValue"). "m_extended_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_APG)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4725  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "class eprosima::fastdds::dds::xtypes::ExtendedAnnotationParameterValue"). "m_extended_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_API)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4725  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "class eprosima::fastdds::dds::xtypes::ExtendedAnnotationParameterValue"). "m_extended_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_APJ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4725  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "class eprosima::fastdds::dds::xtypes::ExtendedAnnotationParameterValue"). "m_extended_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_APK)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4725  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "class eprosima::fastdds::dds::xtypes::ExtendedAnnotationParameterValue"). "m_extended_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhOaMMoXQXhL_APM)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Locator.hpp:251  
  message : Use "operator==" to check object equality, "Locator_t" is not a trivially copyable type without padding.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiysezCYfarq97OI_)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/builtin/type_lookup_service/TypeLookupReplyListener.cpp:45  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkgZbMMoXQXhL--7q)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/builtin/type_lookup_service/TypeLookupRequestListener.cpp:98  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkgaCMMoXQXhL--80)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/core/condition/WaitSetImpl.cpp:37  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYW4cZPeJXHd5uT915On)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/core/condition/WaitSetImpl.cpp:42  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYW4cZPeJXHd5uT915Oo)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/log/Log.cpp:57  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pOS0w2X4EK9K44ga)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/subscriber/DataReaderImpl/ReadTakeCommand.hpp:94  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixBhzCYfarq97NHE)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/DataSharing/DataSharingListener.cpp:53  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pNppw2X4EK9K44fO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/participant/PDP.cpp:1363  
  message : Called C++ object pointer is null  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RWB8pZKJaqlJl3_K)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/participant/PDPListener.cpp:245  
  message : Use pointer or reference to avoid slicing from "ParticipantProxyData" to "ParticipantBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH4QeXFK9T8SBv09H)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:210  
  message : Ensure that destructor of "FlowControllerAsyncPublishMode" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MyI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:219  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pNnfw2X4EK9K44fE)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:262  
  message : Give class "FlowControllerSyncPublishMode" a noexcept destructor (for instance, make sure all subclasses have noexcept destructors).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MyP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:276  
  message : Give class "FlowControllerLimitedAsyncPublishMode" a noexcept destructor (for instance, make sure all subclasses have noexcept destructors).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MyR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.cpp:317  
  message : Ensure that destructor of "RTPSMessageGroup" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw0IzCYfarq97M08)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.cpp:331  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw0IzCYfarq97M1H)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.hpp:113  
  message : Ensure that destructor of "RTPSMessageGroup" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkgDlMMoXQXhL--w0)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:784  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwWszCYfarq97LOf)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:2953  
  message : Use pointer or reference to avoid slicing from "WriterProxyData" to "PublicationBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH4ewXFK9T8SBv0-o)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:2970  
  message : Use pointer or reference to avoid slicing from "ReaderProxyData" to "SubscriptionBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH4ewXFK9T8SBv0-p)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3192  
  message : Use pointer or reference to avoid slicing from "ParticipantProxyData" to "ParticipantBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH4ewXFK9T8SBv0-q)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3224  
  message : Use pointer or reference to avoid slicing from "WriterProxyData" to "PublicationBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH4ewXFK9T8SBv0-s)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3255  
  message : Use pointer or reference to avoid slicing from "ReaderProxyData" to "SubscriptionBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH4ewXFK9T8SBv0-u)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:15582  
  message : The result of left shift is undefined because the right operand is negative  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZOFPW4B4Vgb3UCOkJEA)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:54824  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYb886cuwhn1MW9k8YAM)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:60924  
  message : Access of the field 'xBusyHandler' at index 1, while it holds only a single 'void *' element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-05i3-gB3mVexO6D)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:85015  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYb886cuwhn1MW9k8YAO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:89882  
  message : The left operand of '==' is a garbage value  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-05i3-gB3mVexO6E)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:89901  
  message : The left operand of '==' is a garbage value  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-05i3-gB3mVexO6F)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:104629  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZlvXnVqswrv6mz6zQbS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:106483  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYb886cuwhn1MW9k8YAS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:106483  
  message : Null pointer passed to 2nd parameter expecting 'nonnull'  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZOFPW4B4Vgb3UCOkJD9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111516  
  message : Access of the field 'a' containing 1 elements at negative index -1  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZOFPW4B4Vgb3UCOkJD_)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:129897  
  message : The left operand of '' is a garbage value  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuv0X)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:131101  
  message : Remove the useless top-level "volatile" qualifier from this type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvrL)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:150457  
  message : Access to field 'nExpr' results in a dereference of a null pointer (loaded from field 'pList')  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuv0Y)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:150460  
  message : Access to field 'nExpr' results in a dereference of a null pointer (loaded from field 'pList')  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuv0Z)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:161381  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYb886cuwhn1MW9k8YAV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:169766  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYb886cuwhn1MW9k8YAY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:185794  
  message : Returned pointer value points outside the original object (potential buffer overflow)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZLQ_6ad53x7xtMCv3OS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:185887  
  message : Array access (from variable 'zFilename') results in a null pointer dereference  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuv0b)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/resources/ResourceEvent.cpp:51  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pNtIw2X4EK9K44fP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/ChannelResource.cpp:48  
  message : Null pointer passed to 1st parameter expecting 'nonnull'  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwG_zCYfarq97Kys)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/ChannelResource.cpp:54  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pMwJw2X4EK9K44dT)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPAcceptorBasic.h:59  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwH3zCYfarq97Ky8)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPAcceptorBasic.h:60  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwH3zCYfarq97Ky9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPAcceptorSecure.h:65  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwJEzCYfarq97K1o)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPAcceptorSecure.h:66  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwJEzCYfarq97K1p)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPv4Transport.cpp:239  
  message : Use pointer or reference to avoid slicing from "TCPv4TransportDescriptor" to "TCPTransportDescriptor".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwDNzCYfarq97KvP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemLog.hpp:219  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pMq_w2X4EK9K44dJ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemManager.hpp:277  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwAvzCYfarq97Ks8)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/test_UDPv4Transport.cpp:279  
  message : Null pointer passed to 1st parameter expecting 'nonnull'  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeyfMMoXQXhL--qc)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/rtps/messages/RTPSStatisticsMessages.hpp:215  
  message : Use constructors or assignment operators, "Locator_t" is not trivially copyable.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYYAjAHZv_hJbTx3eLSU)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2405  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::BaseStatus_s" to "class std::vectorclass eprosima::fastdds::statistics::Connection"). "m_connection_list" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg0GMMoXQXhL-_qJ)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2405  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::DeadlineMissedStatus_s" to "class std::vectorclass eprosima::fastdds::statistics::Connection"). "m_connection_list" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg0GMMoXQXhL-_qK)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2405  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::IncompatibleQoSStatus_s" to "class std::vectorclass eprosima::fastdds::statistics::Connection"). "m_connection_list" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg0GMMoXQXhL-_qL)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2409  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::BaseStatus_s" to "class std::vectorclass eprosima::fastdds::statistics::Connection"). "m_connection_list" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg0GMMoXQXhL-_qN)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2409  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::DeadlineMissedStatus_s" to "class std::vectorclass eprosima::fastdds::statistics::Connection"). "m_connection_list" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg0GMMoXQXhL-_qO)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2409  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::IncompatibleQoSStatus_s" to "class std::vectorclass eprosima::fastdds::statistics::Connection"). "m_connection_list" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg0GMMoXQXhL-_qP)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2426  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::BaseStatus_s" to "class eprosima::fastdds::statistics::IncompatibleQoSStatus_s"). "m_incompatible_qos_status" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg0GMMoXQXhL-_qR)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2426  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::DeadlineMissedStatus_s" to "class eprosima::fastdds::statistics::IncompatibleQoSStatus_s"). "m_incompatible_qos_status" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg0GMMoXQXhL-_qS)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2426  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class std::vectorclass eprosima::fastdds::statistics::ExtendedIncompatibleQoSStatus_s" to "class eprosima::fastdds::statistics::IncompatibleQoSStatus_s"). "m_incompatible_qos_status" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH6F6XFK9T8SBv1Dn)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2430  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::BaseStatus_s" to "class eprosima::fastdds::statistics::IncompatibleQoSStatus_s"). "m_incompatible_qos_status" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg0GMMoXQXhL-_qV)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2430  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::DeadlineMissedStatus_s" to "class eprosima::fastdds::statistics::IncompatibleQoSStatus_s"). "m_incompatible_qos_status" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg0GMMoXQXhL-_qW)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2430  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class std::vectorclass eprosima::fastdds::statistics::ExtendedIncompatibleQoSStatus_s" to "class eprosima::fastdds::statistics::IncompatibleQoSStatus_s"). "m_incompatible_qos_status" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH6F6XFK9T8SBv1Dp)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:75  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxM)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:88  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxO)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:98  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxQ)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:98  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxR)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_memory/SharedMemWatchdog.hpp:97  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pNx5w2X4EK9K44fk)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:111  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owg)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:152  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owe)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:157  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owf)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:198  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYSYJ7bqjWNzjtTw5p02)  
---
  * file : eProsima/Fast-DDS/test/dds/xtypes/test_build.py:126  
  message : Ensure that the asyncio.CancelledError exception is re-raised after your cleanup code.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZeaxzm8YQO-EckZ69i_)  
---
  * file : eProsima/Fast-DDS/test/dds/xtypes/update_header_and_create_cases.py:24  
  message : Remove or rework this redundant alternative.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkefKMMoXQXhL--qL)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/variadic_templates_tools.hpp:51  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPBZWpM_KNhuouaea)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/segment_manager_helper.hpp:75  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiutdzCYfarq97JkU)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/detail/mem_algo_common.hpp:318  
  message : Remove the unary minus operator or change the expression's underlying type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuxZzCYfarq97Jn-)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/posix/mutex.hpp:132  
  message : This was not the most recently acquired lock. Possible lock order reversal  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISium4zCYfarq97Jex)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/posix/ptime_to_timespec.hpp:34  
  message : Identical sub-expressions on both sides of operator "-".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZV93Ekp7aHhzolCQBTV)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/posix/semaphore_wrapper.hpp:225  
  message : Change this loop body so that it can be executed more than once.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiunGzCYfarq97Je9)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/detail/shared_count.hpp:356  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivXBzCYfarq97KIO)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:256  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivZ1zCYfarq97KJ2)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:471  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivZ1zCYfarq97KKJ)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:484  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivZ1zCYfarq97KKN)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:567  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivZ1zCYfarq97KKS)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:576  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivZ1zCYfarq97KKT)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:578  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivZ1zCYfarq97KKU)  
---
  * file : eProsima/Fast-DDS/thirdparty/filewatch/FileWatch.hpp:124  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pK-Fw2X4EK9K44dG)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:14840  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPB7dpM_KNhuouae0)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:19068  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--oz)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:19083  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--o1)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:20138  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--mo)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:20518  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--pE)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:23519  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--mq)  
---
  * file : eProsima/Fast-DDS/thirdparty/optionparser/optionparser/optionparser.h:2001  
  message : 1 uninitialized field at the end of the constructor call  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv8nzCYfarq97Kft)  
---
  * file : eProsima/Fast-DDS/thirdparty/taocpp-pegtl/pegtl/mmap_input.hpp:38  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPB6DpM_KNhuouaex)  
---
  * file : eProsima/Fast-DDS/thirdparty/taocpp-pegtl/pegtl/mmap_input.hpp:61  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPB6DpM_KNhuouaey)  
---
  * file : eProsima/Fast-DDS/thirdparty/taocpp-pegtl/pegtl/read_input.hpp:27  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPBxrpM_KNhuouaes)  
---
  * file : eProsima/Fast-DDS/thirdparty/taocpp-pegtl/pegtl/read_input.hpp:49  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPBxrpM_KNhuouaet)  
---
  * file : eProsima/Fast-DDS/thirdparty/taocpp-pegtl/pegtl/string_input.hpp:26  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPBzCpM_KNhuouaeu)  
---
  * file : eProsima/Fast-DDS/tools/fastdds/discovery/fastdds_daemon/daemon/__init__.py:154  
  message : Add 1 missing arguments; 'serve' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH6xdXFK9T8SBv1E5)  
---
  * file : eProsima/Fast-DDS/utils/doxygen/pages/customdoxygen.css:176  
  message : Unexpected duplicate "font-size"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZpHgMafZiJawz635PPe)  
---
  * file : eProsima/Fast-DDS/utils/doxygen/pages/customdoxygen.css:266  
  message : Unexpected nonstandard direction  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0IHzCYfarq97O5s)  
---
  * file : eProsima/Fast-DDS/utils/doxygen/pages/customdoxygen.css:620  
  message : Unexpected duplicate "background-color"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZpHgMafZiJawz635PPf)  
---
  * file : eProsima/Fast-DDS/utils/doxygen/pages/customdoxygen.css:805  
  message : Unexpected missing generic font family  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0IHzCYfarq97O5r)  
---
  * file : eProsima/Fast-DDS/utils/doxygen/pages/customdoxygen.css:1008  
  message : Unexpected duplicate "text-decoration"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0IHzCYfarq97O5q)  
---
  * file : eProsima/Fast-DDS/utils/doxygen/pages/eprosima_header.html:3  
  message : Add "lang" and/or "xml:lang" attributes to this "html" element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0H4zCYfarq97O5g)  
---
  * file : eProsima/Fast-DDS/utils/doxygen/pages/eprosima_header.html:23  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0H4zCYfarq97O5i)  
---
  * file : eProsima/Fast-DDS/utils/doxygen/pages/eprosima_header.html:40  
  message : Duplicate id "projectbrief" found. First occurrence was on line 34.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZpHgMaAZiJawz635PPa)  
---
</details>  
<details><summary><a style='color:blue;font-size:18px;'>moveit2</a></summary>  

  * file : moveit2/moveit/scripts/maintainer_table_template.html:27  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYKwcpLzZzpJC77kImkX)  
---
  * file : moveit2/moveit_py/moveit/policies/policy.py:148  
  message : Add a "self" or class parameter  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-5AV3-gB3mVexO6c)  
---
  * file : moveit2/moveit_py/moveit/servo_client/devices/ps4_dualshock.py:143  
  message : Add a "self" or class parameter  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYaQ0q1avTyJunPyDVLW)  
---
</details>  
<details><summary><a style='color:blue;font-size:18px;'>navigation2</a></summary>  

  * file : navigation2/nav2_common/test/test_rewritten_yaml.py:100  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZdSqQ_UXvAjqlUSZWsn)  
---
  * file : navigation2/nav2_common/test/test_rewritten_yaml.py:110  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZdSqQ_UXvAjqlUSZWso)  
---
  * file : navigation2/nav2_common/test/test_rewritten_yaml.py:120  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZdSqQ_UXvAjqlUSZWsp)  
---
  * file : navigation2/nav2_loopback_sim/nav2_loopback_sim/loopback_simulator.py:400  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZcKjD3PNTaJx6YGJ8L8)  
---
  * file : navigation2/nav2_simple_commander/nav2_simple_commander/line_iterator.py:86  
  message : Correct one of the identical sub-expressions on both sides of operator "==".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYR0LI5rHE-0Dh1G_Im6)  
---
</details>  
<details><summary><a style='color:blue;font-size:18px;'>osrf</a></summary>  

  * file : osrf/osrf_testing_tools_cpp/osrf_testing_tools_cpp/src/memory_tools/custom_memory_functions.cpp:147  
  message : Use of memory after it is freed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi48MzCYfarq97P6B)  
---
  * file : osrf/osrf_testing_tools_cpp/osrf_testing_tools_cpp/src/memory_tools/custom_memory_functions.cpp:290  
  message : Use of memory after it is freed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi48MzCYfarq97P6C)  
---
</details>  
<details><summary><a style='color:blue;font-size:18px;'>ros</a></summary>  

  * file : ros/pluginlib/ros2plugin/ros2plugin/verb/list.py:47  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZnbWNjX5WDow3WVC02m)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/gtest-matchers.h:297  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPKkPpM_KNhuouaqv)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/gtest-matchers.h:499  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPKkPpM_KNhuouaqw)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/gtest-matchers.h:520  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPKkPpM_KNhuouaqx)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/gtest-matchers.h:544  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPKkPpM_KNhuouaqy)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/gtest-matchers.h:570  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPKkPpM_KNhuouaqz)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/gtest-matchers.h:598  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPKkPpM_KNhuouaq0)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/internal/gtest-internal.h:325  
  message : Replace "float" to "unsigned int" type punning with "std::memcpy". "bits_" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZz21DHXxtxeKK1WZw)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/internal/gtest-internal.h:328  
  message : Replace "float" to "unsigned int" type punning with "std::memcpy". "bits_" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZz21DHXxtxeKK1WZx)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/internal/gtest-internal.h:351  
  message : Replace "float" to "unsigned int" type punning with "std::memcpy". "bits_" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZz21DHXxtxeKK1WZy)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/internal/gtest-internal.h:351  
  message : Replace "float" to "unsigned int" type punning with "std::memcpy". "bits_" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZz21DHXxtxeKK1WZz)  
---
</details>  
<details><summary><a style='color:blue;font-size:18px;'>ros-perception</a></summary>  

  * file : ros-perception/image_common/camera_info_manager_py/camera_info_manager/camera_info_manager.py:275  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZOFPe0Z4Vgb3UCOkJEf)  
---
  * file : ros-perception/image_common/camera_info_manager_py/camera_info_manager/zoom_camera_info_manager.py:226  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZOFPe0E4Vgb3UCOkJEa)  
---
</details>  
<details><summary><a style='color:blue;font-size:18px;'>ros-visualization</a></summary>  

  * file : ros-visualization/qt_gui_core/qt_gui/src/qt_gui/icon_loader.py:50  
  message : path is used before it is defined. Move the definition before.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi2wxzCYfarq97Pie)  
---
  * file : ros-visualization/qt_gui_core/qt_gui/src/qt_gui/reload_importer.py:77  
  message : Fix this condition that always evaluates to true.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZdSqS-oXvAjqlUSZWsq)  
---
  * file : ros-visualization/qt_gui_core/qt_gui/src/qt_gui/reload_importer.py:77  
  message : Fix this condition that always evaluates to true.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZdSqS-oXvAjqlUSZWsr)  
---
  * file : ros-visualization/rqt/rqt_py_common/src/rqt_py_common/topic_completer.py:102  
  message : Add 1 missing arguments; 'create_node' expects 1 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi2gMzCYfarq97PeC)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_timeline.py:678  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1Ztw_ub2taBKNOi)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_timeline.py:863  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1Ztw_ub2taBKNOj)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_timeline.py:891  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1Ztw_ub2taBKNOk)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_timeline.py:901  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1Ztw_ub2taBKNOl)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_widget.py:415  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1X_w_ub2taBKNOf)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_widget.py:418  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1X_w_ub2taBKNOg)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_widget.py:424  
  message : This branch duplicates the one on line 418.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi24QzCYfarq97PjT)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_widget.py:424  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1X_w_ub2taBKNOh)  
---
  * file : ros-visualization/rqt_graph/src/rqt_graph/dotcode.py:117  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1rWw_ub2taBKNOm)  
---
  * file : ros-visualization/rqt_graph/src/rqt_graph/rosgraph2_impl.py:456  
  message : Introduce a new variable or use its initial value before reassigning 'bad_node'.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi3I9zCYfarq97Plo)  
---
  * file : ros-visualization/rqt_reconfigure/src/rqt_reconfigure/node_selector_widget.py:511  
  message : Fix this attribute access on a value that can be 'None'.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi3A2zCYfarq97Pkt)  
---
  * file : ros-visualization/rqt_reconfigure/src/rqt_reconfigure/node_selector_widget.py:521  
  message : Fix this attribute access on a value that can be 'None'.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi3A2zCYfarq97Pkv)  
---
  * file : ros-visualization/rqt_reconfigure/src/rqt_reconfigure/node_selector_widget.py:522  
  message : Fix this attribute access on a value that can be 'None'.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi3A2zCYfarq97Pks)  
---
  * file : ros-visualization/rqt_topic/rqt_topic/workers/topic.py:186  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLhFmEWS9FtSIxsrC)  
---
  * file : ros-visualization/rqt_topic/test/models/test_topic.py:57  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLhD1EWS9FtSIxsqa)  
---
  * file : ros-visualization/rqt_topic/test/models/test_topic.py:59  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLhD1EWS9FtSIxsqb)  
---
  * file : ros-visualization/rqt_topic/test/models/test_topic.py:60  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLhD1EWS9FtSIxsqc)  
---
  * file : ros-visualization/rqt_topic/test/models/test_topic.py:61  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLhD1EWS9FtSIxsqd)  
---
  * file : ros-visualization/rqt_topic/test/models/test_topic.py:65  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLhD1EWS9FtSIxsqe)  
---
  * file : ros-visualization/rqt_topic/test/models/test_topic.py:78  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLhD1EWS9FtSIxsqf)  
---
  * file : ros-visualization/rqt_topic/test/models/test_topic.py:79  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLhD1EWS9FtSIxsqg)  
---
  * file : ros-visualization/rqt_topic/test/models/test_topic.py:80  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLhD1EWS9FtSIxsqh)  
---
  * file : ros-visualization/rqt_topic/test/models/test_topic.py:81  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLhD1EWS9FtSIxsqi)  
---
</details>  
<details><summary><a style='color:blue;font-size:18px;'>ros2</a></summary>  

  * file : ros2/examples/rclpy/actions/minimal_action_client/examples_rclpy_minimal_action_client/client_asyncio.py:106  
  message : Ensure that the asyncio.CancelledError exception is re-raised after your cleanup code.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLXqXEWS9FtSIxskZ)  
---
  * file : ros2/examples/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server.py:80  
  message : Replace this call to time.sleep() with an asynchronous sleep function.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZeaxtzNYQO-EckZ69ic)  
---
  * file : ros2/examples/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server_defer.py:94  
  message : Replace this call to time.sleep() with an asynchronous sleep function.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZeaxtzEYQO-EckZ69ia)  
---
  * file : ros2/examples/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server_not_composable.py:58  
  message : Replace this call to time.sleep() with an asynchronous sleep function.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZeaxtzbYQO-EckZ69ie)  
---
  * file : ros2/geometry2/test_tf2/test/test_buffer_client.py:83  
  message : Remove this "return" statement from this "finally" block.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISioZUzCYfarq97IVs)  
---
  * file : ros2/geometry2/tf2_tools/tf2_tools/view_frames.py:67  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pENcw2X4EK9K417z)  
---
  * file : ros2/geometry2/tf2_tools/tf2_tools/view_frames.py:116  
  message : Remove this "return" statement from this "finally" block.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISioXazCYfarq97IVX)  
---
  * file : ros2/launch/launch/launch/launch_service.py:358  
  message : Ensure that the asyncio.CancelledError exception is re-raised after your cleanup code.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZeaxvGqYQO-EckZ69iu)  
---
  * file : ros2/launch/launch/test/launch/actions/test_declare_launch_argument.py:81  
  message : Don’t perform an assertion here; An exception is expected to be raised before its execution.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-vLd3-gB3mVexOqc)  
---
  * file : ros2/launch/launch/test/launch/frontend/test_substitutions.py:243  
  message : Refactor this test; if this assertion’s argument raises an exception, the assertion will never get executed.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-vOf3-gB3mVexOqd)  
---
  * file : ros2/launch/launch/test/launch/frontend/test_substitutions.py:253  
  message : Refactor this test; if this assertion’s argument raises an exception, the assertion will never get executed.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-vOf3-gB3mVexOqe)  
---
  * file : ros2/launch/launch/test/launch/test_launch_context.py:82  
  message : Refactor this test; if this assertion’s argument raises an exception, the assertion will never get executed.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-vPF3-gB3mVexOqf)  
---
  * file : ros2/launch/launch/test/launch/test_timer_action.py:153  
  message : Fix this access on a collection that may trigger an 'IndexError'.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZe-o-lRPRvRDl2M6seD)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:187  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN3)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:188  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN4)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:189  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN5)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:190  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN6)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:230  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN7)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:231  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN8)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:232  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN9)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:233  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN-)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:234  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN_)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:235  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZTttbGWvPkZ5NTBu5Fv)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:392  
  message : Add 1 missing arguments; 'get_typed_value' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiniszCYfarq97IJ7)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:396  
  message : Add 1 missing arguments; 'get_typed_value' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiniszCYfarq97IJ8)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:556  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNOA)  
---
  * file : ros2/launch/launch_testing/launch_testing/legacy/__init__.py:265  
  message : Change or remove this string; "actions" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISinshzCYfarq97ILT)  
---
  * file : ros2/launch/launch_testing/test/launch_testing/test_resolve_process.py:191  
  message : Fix this access on a collection that may trigger an 'IndexError'.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZdSqMkgXvAjqlUSZWsl)  
---
  * file : ros2/launch/test_launch_testing/test/dummy_tests/dummy.py:19  
  message : Correct one of the identical sub-expressions on both sides of operator "==".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISin3jzCYfarq97IME)  
---
  * file : ros2/launch/test_launch_testing/test/dummy_tests/locking.cpp:18  
  message : 'return' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISin25zCYfarq97IL_)  
---
  * file : ros2/launch_ros/launch_ros/launch_ros/utilities/__init__.py:37  
  message : Change or remove this string; "evaluate_parameters_dict" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiq9CzCYfarq97Ix3)  
---
  * file : ros2/launch_ros/launch_ros/launch_ros/utilities/__init__.py:44  
  message : Change or remove this string; "normalize_parameters_dict" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiq9CzCYfarq97Ix4)  
---
  * file : ros2/launch_ros/launch_testing_ros/test/examples/check_msgs_launch_test.py:60  
  message : Remove this "return" statement from this "finally" block.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY4rOM_lmANMCkDoQwwB)  
---
  * file : ros2/launch_ros/test_launch_ros/test/test_launch_ros/actions/test_load_composable_nodes.py:247  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYlcmw_ub2taBKNOG)  
---
  * file : ros2/launch_ros/test_launch_ros/test/test_launch_ros/actions/test_ros_timer.py:115  
  message : Fix this access on a collection that may trigger an 'IndexError'.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZe-o-_gPRvRDl2M6seE)  
---
  * file : ros2/launch_ros/test_launch_ros/test/test_launch_ros/descriptions/test_parameter_file.py:127  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiq06zCYfarq97IxA)  
---
  * file : ros2/rclpy/rclpy/rclpy/node.py:1371  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYjQfw_ub2taBKNOF)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:53  
  message : Raise this exception or remove this useless statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZFEP0Hyi5a_X_62zTxy)  
---
  * file : ros2/rclpy/rclpy/test/test_executor.py:481  
  message : Remove this "break" statement from this "finally" block.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiohHzCYfarq97IWQ)  
---
  * file : ros2/rclpy/rclpy/test/test_node.py:1657  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZZWHaPjJaW_00fRkMbT)  
---
  * file : ros2/rclpy/rclpy/test/test_node.py:1658  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZZWHaPjJaW_00fRkMbV)  
---
  * file : ros2/rclpy/rclpy/test/test_parameter_client.py:77  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYi-Ow_ub2taBKNOB)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:82  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZPxVnaCmsyemdV_C1Mn)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:105  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXo)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:108  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXp)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:120  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXq)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:125  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXr)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:127  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXs)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:148  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXt)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:150  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXu)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:152  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXv)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:154  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXw)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:156  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXx)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:158  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXy)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:167  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX2)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:169  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX3)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:171  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX4)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:173  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX5)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:196  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX9)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:198  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX-)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:200  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX_)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:202  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IYA)  
---
  * file : ros2/rcpputils/include/rcpputils/scope_exit.hpp:29  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISir08zCYfarq97JF4)  
---
  * file : ros2/rcutils/src/error_handling_helpers.h:83  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZBIALZkMa3zLak3hqWD)  
---
  * file : ros2/rcutils/src/logging.c:476  
  message : Memory copy function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYqmAQdbWvNZCKI3y18h)  
---
  * file : ros2/rcutils/test/mocking_utils/patch.hpp:160  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirK4zCYfarq97I5p)  
---
  * file : ros2/realtime_support/rttest/src/rttest.cpp:68  
  message : Value assigned to field 'thread_id' in implicit constructor is garbage or undefined  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZHUlC85esNELLGLarFR)  
---
  * file : ros2/realtime_support/rttest/src/rttest.cpp:150  
  message : 7 uninitialized fields at the end of the constructor call  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZHUlC85esNELLGLarFS)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:70  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39k)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:77  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39l)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:84  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39m)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:90  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39n)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:102  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39o)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:108  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39p)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_direct.py:48  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYfNdw_ub2taBKNN2)  
---
  * file : ros2/rosbag2/ros2bag/test/test_recorder_args_parser.py:330  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZkDFBn1j1WFNLSWaJdE)  
---
  * file : ros2/rosbag2/ros2bag/test/test_recorder_args_parser.py:367  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZkDFBn1j1WFNLSWaJdF)  
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
  * file : ros2/rosidl/rosidl_parser/test/test_parser.py:115  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYefSw_ub2taBKNN0)  
---
  * file : ros2/rosidl/rosidl_parser/test/test_parser.py:404  
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
  * file : ros2/rosidl_python/rosidl_generator_py/test/test_interfaces.py:276  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYmnpw_ub2taBKNOL)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/test/test_interfaces.py:277  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYmnpw_ub2taBKNOM)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/test/test_interfaces.py:298  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYmnpw_ub2taBKNON)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/test/test_interfaces.py:299  
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
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:220  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZZWHcoeJaW_00fRkMba)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:223  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZZWHcoeJaW_00fRkMbb)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:228  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZZWHcoeJaW_00fRkMbc)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:231  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZZWHcoeJaW_00fRkMbd)  
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
  * file : ros2/rviz/rviz_common/help/help.html:63  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_s)  
---
  * file : ros2/rviz/rviz_common/help/help.html:76  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_x)  
---
  * file : ros2/rviz/rviz_common/help/help.html:86  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_1)  
---
  * file : ros2/rviz/rviz_common/help/help.html:104  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_5)  
---
  * file : ros2/rviz/rviz_common/help/help.html:129  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97H_9)  
---
  * file : ros2/rviz/rviz_common/help/help.html:159  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97IAB)  
---
  * file : ros2/rviz/rviz_common/help/help.html:184  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97IAF)  
---
  * file : ros2/rviz/rviz_common/help/help.html:209  
  message : Add "th" headers to this "table".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISim9lzCYfarq97IAJ)  
---
</details>  
  
<br />  
  
## VULNERABILITIES #20 
<details><summary><a style='color:blue;font-size:18px;'>eProsima</a></summary>  

  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/os_file_functions.hpp:426  
  message : Remove this TOCTOU race condition window when accessing files  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISius5zCYfarq97JiM)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>moveit2</a></summary>  

  * file : moveit2/moveit_kinematics/ikfast_kinematics_plugin/scripts/create_ikfast_moveit_plugin.py:364  
  message : Disable access to external entities in XML parsing.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYKwcpHFZzpJC77kImjV)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>navigation2</a></summary>  

  * file : navigation2/nav2_bringup/launch/cloned_multi_tb3_simulation_launch.py:201  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY__0Qc5MWueF4yM_B3g)  
---
  * file : navigation2/nav2_bringup/launch/tb3_simulation_launch.py:208  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY__0QdDMWueF4yM_B3h)  
---
  * file : navigation2/nav2_bringup/launch/tb4_simulation_launch.py:250  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY__0QczMWueF4yM_B3f)  
---
  * file : navigation2/nav2_bringup/launch/unique_multi_tb3_simulation_launch.py:150  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZBIAR3SMa3zLak3hqiX)  
---
  * file : navigation2/nav2_simple_commander/launch/assisted_teleop_example_launch.py:54  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj066eBIBOiy31Qq8x)  
---
  * file : navigation2/nav2_simple_commander/launch/follow_path_example_launch.py:53  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj064cBIBOiy31Qq8r)  
---
  * file : navigation2/nav2_simple_commander/launch/inspection_demo_launch.py:53  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj065IBIBOiy31Qq8t)  
---
  * file : navigation2/nav2_simple_commander/launch/nav_through_poses_example_launch.py:53  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj064yBIBOiy31Qq8s)  
---
  * file : navigation2/nav2_simple_commander/launch/nav_to_pose_example_launch.py:53  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj066IBIBOiy31Qq8w)  
---
  * file : navigation2/nav2_simple_commander/launch/picking_demo_launch.py:53  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj065dBIBOiy31Qq8u)  
---
  * file : navigation2/nav2_simple_commander/launch/recoveries_example_launch.py:53  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj065zBIBOiy31Qq8v)  
---
  * file : navigation2/nav2_simple_commander/launch/route_example_launch.py:105  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZaeOZYoH9d-njH5Utd6)  
---
  * file : navigation2/nav2_simple_commander/launch/security_demo_launch.py:53  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj066zBIBOiy31Qq8y)  
---
  * file : navigation2/nav2_simple_commander/launch/waypoint_follower_example_launch.py:53  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj064GBIBOiy31Qq8q)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>ros2</a></summary>  

  * file : ros2/sros2/sros2/sros2/keystore/_permission.py:71  
  message : Disable access to external entities in XML parsing.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimSLzCYfarq97H_a)  
---
  * file : ros2/sros2/sros2/sros2/policy/__init__.py:81  
  message : Disable access to external entities in XML parsing.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimQSzCYfarq97H_J)  
---
  * file : ros2/sros2/sros2/test/policies/policy_to_permissions.py:33  
  message : Disable access to external entities in XML parsing.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimNhzCYfarq97H_F)  
---
  * file : ros2/sros2/sros2/test/test_policy_to_permissions.py:34  
  message : Disable access to external entities in XML parsing.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimOXzCYfarq97H_H)  
---
</details>  
    
<br />  
  
## ISSUES are filtered and only blocking and critical issues are reported due to the high quantity of issues  
The complete list of issues can be found [here](https://sonarcloud.io/summary/overall?id=muttistefano_ros2_sonarcloud) .  
<br />  
  
## ISSUES (level blocker) #598 
<details><summary><a style='color:blue;font-size:18px;'>eclipse-iceoryx</a></summary>  

  * file : eclipse-iceoryx/iceoryx/iceoryx_hoofs/source/log/logger.cpp:141  
  message : Replace this call to the non reentrant function "localtime" by a call to "localtime_r".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi01KzCYfarq97PEZ)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>eProsima</a></summary>  

  * file : eProsima/Fast-CDR/include/fastcdr/FastBuffer.h:268  
  message : Ensure that the move constructor of "FastBuffer" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0NOzCYfarq97O-o)  
---
  * file : eProsima/Fast-CDR/include/fastcdr/FastBuffer.h:280  
  message : Ensure that the move assignment operator of "FastBuffer" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0NOzCYfarq97O-p)  
---
  * file : eProsima/Fast-CDR/include/fastcdr/xcdr/optional.hpp:221  
  message : Ensure that the move assignment operator of "optional" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY6XV5oZLAV-oFEgTkla)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2340  
  message : Ensure that the move constructor of "TypeIdV1" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhEvMMoXQXhL-_vI)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2360  
  message : Ensure that the move assignment operator of "TypeIdV1" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhEvMMoXQXhL-_vJ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2452  
  message : Ensure that the move constructor of "TypeObjectV1" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhEvMMoXQXhL-_vM)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2472  
  message : Ensure that the move assignment operator of "TypeObjectV1" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhEvMMoXQXhL-_vN)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2569  
  message : Ensure that the move constructor of "TypeInformationParameter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhEvMMoXQXhL-_vR)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2591  
  message : Ensure that the move assignment operator of "TypeInformationParameter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhEvMMoXQXhL-_vS)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/domain/qos/DomainParticipantQos.hpp:78  
  message : Remove the "virtual" specifier and refactor the code to not require polymorphism for comparison operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhQnMMoXQXhL_APp)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/log/Log.hpp:292  
  message : Potential leak of memory pointed to by 'p'  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhHYMMoXQXhL-_vi)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/subscriber/qos/DataReaderQos.hpp:43  
  message : Make sure that moving an object of class "DataReaderQos" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY9vnBy5o-3NSYXl8BHO)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/topic/TypeSupport.hpp:225  
  message : Remove the "virtual" specifier and refactor the code to not require polymorphism for comparison operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhPcMMoXQXhL_APb)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/attributes/PropertyPolicy.hpp:44  
  message : Ensure that the move constructor of "PropertyPolicy" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg2xMMoXQXhL-_rB)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/attributes/PropertyPolicy.hpp:59  
  message : Ensure that the move assignment operator of "PropertyPolicy" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg2xMMoXQXhL-_rC)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/attributes/ReaderAttributes.hpp:58  
  message : Make sure that moving an object of class "ReaderAttributes" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg3FMMoXQXhL-_rM)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/BinaryProperty.hpp:48  
  message : Ensure that the move constructor of "BinaryProperty" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg41MMoXQXhL-_rw)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/BinaryProperty.hpp:81  
  message : Ensure that the move assignment operator of "BinaryProperty" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg41MMoXQXhL-_rx)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/CDRMessage_t.hpp:167  
  message : Ensure that the move constructor of "CDRMessage_t" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiystzCYfarq97OJV)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/CDRMessage_t.hpp:186  
  message : Ensure that the move assignment operator of "CDRMessage_t" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiystzCYfarq97OJW)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/EntityId_t.hpp:111  
  message : Ensure that the move constructor of "EntityId_t" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiywOzCYfarq97OLn)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/EntityId_t.hpp:124  
  message : Ensure that the move assignment operator of "EntityId_t" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiywOzCYfarq97OLo)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Guid.hpp:39  
  message : Make sure that moving an object of class "GUID_t" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyxkzCYfarq97OM4)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Locator.hpp:102  
  message : Ensure that the move constructor of "Locator_t" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiysezCYfarq97OIw)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Locator.hpp:251  
  message : Use "operator==" to check object equality, "Locator_t" is not a trivially copyable type without padding.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiysezCYfarq97OI_)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorList.hpp:120  
  message : Ensure that the move constructor of "LocatorList" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg8JMMoXQXhL-_se)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorList.hpp:135  
  message : Ensure that the move assignment operator of "LocatorList" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg8JMMoXQXhL-_sf)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorList.hpp:359  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg8JMMoXQXhL-_sm)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorSelectorEntry.hpp:38  
  message : Make sure that moving an object of class "LocatorSelectorEntry" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY7f680bVxLMsfMbnqZ9)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorSelectorEntry.hpp:43  
  message : Make sure that moving an object of class "EntryState" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY7f680bVxLMsfMbnqZ-)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorWithMask.hpp:34  
  message : Make sure that moving an object of class "LocatorWithMask" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg4rMMoXQXhL-_rv)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorsIterator.hpp:47  
  message : Remove the "virtual" specifier and refactor the code to not require polymorphism for comparison operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyrzzCYfarq97OIO)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorsIterator.hpp:56  
  message : Remove the "virtual" specifier and refactor the code to not require polymorphism for comparison operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyrzzCYfarq97OIP)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Property.hpp:46  
  message : Ensure that the move constructor of "Property" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyuBzCYfarq97OKO)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Property.hpp:83  
  message : Ensure that the move assignment operator of "Property" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyuBzCYfarq97OKP)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/SampleIdentity.hpp:59  
  message : Ensure that the move constructor of "SampleIdentity" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiywqzCYfarq97OLz)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/SampleIdentity.hpp:80  
  message : Ensure that the move assignment operator of "SampleIdentity" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiywqzCYfarq97OL0)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Token.hpp:45  
  message : Ensure that the move constructor of "DataHolder" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg65MMoXQXhL-_sL)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Token.hpp:63  
  message : Ensure that the move assignment operator of "DataHolder" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg65MMoXQXhL-_sM)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/WriteParams.hpp:33  
  message : Make sure that moving an object of class "WriteParams" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYlh3wciG85feRYr0mZ6)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/transport/SenderResource.hpp:79  
  message : Ensure that the move constructor of "SenderResource" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkg-hMMoXQXhL-_tG)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/transport/network/AllowedNetworkInterface.hpp:51  
  message : Ensure that the move constructor of "AllowedNetworkInterface" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY5zXGHQVSszh3Bos0Kr)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/transport/network/BlockedNetworkInterface.hpp:51  
  message : Ensure that the move constructor of "BlockedNetworkInterface" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY5zXGHHVSszh3Bos0Kp)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/transport/network/NetworkInterface.hpp:61  
  message : Ensure that the move constructor of "NetworkInterface" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY5zXGHZVSszh3Bos0Kt)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/transport/network/NetworkInterfaceWithFilter.hpp:74  
  message : Ensure that the move constructor of "NetworkInterfaceWithFilter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY5zXGHhVSszh3Bos0Kw)  
---
  * file : eProsima/Fast-DDS/include/fastdds/utils/IPFinder.hpp:55  
  message : Make sure that moving an object of class "info_IP" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkhT-MMoXQXhL_AP8)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/builtin/type_lookup_service/TypeLookupReplyListener.hpp:51  
  message : Make sure that moving an object of class "ReplyWithServerGUID" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkgW-MMoXQXhL--0G)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/subscriber/DataReaderImpl/SampleLoanManager.hpp:191  
  message : Ensure that the move constructor of "OutstandingLoanItem" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixB-zCYfarq97NHm)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/subscriber/DataReaderImpl/SampleLoanManager.hpp:193  
  message : Ensure that the move assignment operator of "OutstandingLoanItem" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixB-zCYfarq97NHn)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:156  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50_XFK9T8SBv1Bm)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:264  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50_XFK9T8SBv1Bn)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:366  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50_XFK9T8SBv1Bo)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:385  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50_XFK9T8SBv1Bp)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:461  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50_XFK9T8SBv1Bq)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:506  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50_XFK9T8SBv1Bu)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:116  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50vXFK9T8SBv0_x)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:327  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50vXFK9T8SBv0_8)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:1388  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50vXFK9T8SBv1Ah)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:1450  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50vXFK9T8SBv1Am)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:1502  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50vXFK9T8SBv1Ar)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:1546  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50vXFK9T8SBv1Aw)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:1644  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50vXFK9T8SBv1A2)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:1928  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50vXFK9T8SBv1BF)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:2106  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH50vXFK9T8SBv1BL)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/data/ProxyHashTables.hpp:60  
  message : Ensure that the move constructor of "node_segregator" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwUvzCYfarq97LKO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/database/DiscoveryDataBase.hpp:91  
  message : Ensure that the move constructor of "AckedFunctor" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwM8zCYfarq97K66)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/database/DiscoveryParticipantChangeData.hpp:38  
  message : Make sure that moving an object of class "DiscoveryParticipantChangeData" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwNZzCYfarq97K7m)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/participant/PDPListener.cpp:245  
  message : Use pointer or reference to avoid slicing from "ParticipantProxyData" to "ParticipantBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH4QeXFK9T8SBv09H)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/exceptions/Exception.h:85  
  message : Ensure that the move constructor of "Exception" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkfN2MMoXQXhL--vU)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/exceptions/Exception.h:108  
  message : Ensure that the move assignment operator of "Exception" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkfN2MMoXQXhL--vV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:210  
  message : Ensure that destructor of "FlowControllerAsyncPublishMode" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MyI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:262  
  message : Give class "FlowControllerSyncPublishMode" a noexcept destructor (for instance, make sure all subclasses have noexcept destructors).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MyP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:276  
  message : Give class "FlowControllerLimitedAsyncPublishMode" a noexcept destructor (for instance, make sure all subclasses have noexcept destructors).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MyR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:1365  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MzE)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:1366  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MzF)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.cpp:317  
  message : Ensure that destructor of "RTPSMessageGroup" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw0IzCYfarq97M08)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.hpp:113  
  message : Ensure that destructor of "RTPSMessageGroup" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkgDlMMoXQXhL--w0)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/network/ReceiverResource.h:95  
  message : Ensure that the move constructor of "ReceiverResource" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYJ7i3MlILU70yBX0vMT)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:2953  
  message : Use pointer or reference to avoid slicing from "WriterProxyData" to "PublicationBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH4ewXFK9T8SBv0-o)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:2970  
  message : Use pointer or reference to avoid slicing from "ReaderProxyData" to "SubscriptionBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH4ewXFK9T8SBv0-p)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3192  
  message : Use pointer or reference to avoid slicing from "ParticipantProxyData" to "ParticipantBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH4ewXFK9T8SBv0-q)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3224  
  message : Use pointer or reference to avoid slicing from "WriterProxyData" to "PublicationBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH4ewXFK9T8SBv0-s)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3255  
  message : Use pointer or reference to avoid slicing from "ReaderProxyData" to "SubscriptionBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH4ewXFK9T8SBv0-u)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.hpp:170  
  message : Ensure that the move constructor of "ReceiverControlBlock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwWazCYfarq97LNp)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/reader/StatefulReader.cpp:1623  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwY5zCYfarq97LTD)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/reader/StatelessReader.hpp:248  
  message : Make sure that moving an object of class "RemoteWriterInfo_t" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkfJaMMoXQXhL--ur)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/security/common/ParticipantGenericMessage.h:45  
  message : Ensure that the move constructor of "MessageIdentity" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkfMEMMoXQXhL--vC)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/security/common/ParticipantGenericMessage.h:60  
  message : Ensure that the move assignment operator of "MessageIdentity" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkfMEMMoXQXhL--vD)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/security/common/ParticipantGenericMessage.h:159  
  message : Ensure that the move constructor of "ParticipantGenericMessage" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkfMEMMoXQXhL--vH)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/security/common/ParticipantGenericMessage.h:184  
  message : Ensure that the move assignment operator of "ParticipantGenericMessage" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkfMEMMoXQXhL--vI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/ChannelResource.h:34  
  message : Ensure that the move constructor of "ChannelResource" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwFOzCYfarq97KxV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPv4Transport.cpp:239  
  message : Use pointer or reference to avoid slicing from "TCPv4TransportDescriptor" to "TCPTransportDescriptor".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwDNzCYfarq97KvP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/UDPChannelResource.h:36  
  message : Make sure that moving an object of class "eProsimaUDPSocket" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY5zXDtDVSszh3Bos0I6)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/UDPChannelResource.h:159  
  message : Ensure that the move assignment operator of "UDPChannelResource" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwFczCYfarq97Kxh)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemGlobal.hpp:70  
  message : Make sure that moving an object of class "BufferDescriptor" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYlh3tCyG85feRYr0mYd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemLog.hpp:173  
  message : Make sure that moving an object of class "Pkt" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwCGzCYfarq97Kuj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemManager.hpp:685  
  message : Ensure that the move assignment operator of "Listener" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwAvzCYfarq97KtM)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemManager.hpp:720  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwAvzCYfarq97KtR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemManager.hpp:852  
  message : Ensure that the move assignment operator of "Port" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwAvzCYfarq97KtW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/test_UDPv4Transport.cpp:290  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv_UzCYfarq97Kp-)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/test_UDPv4Transport.cpp:291  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv_UzCYfarq97Kp9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/test_UDPv4Transport.cpp:292  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv_UzCYfarq97Kp8)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/LivelinessManager.cpp:126  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw31zCYfarq97M4w)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.cpp:1681  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw4TzCYfarq97M6j)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.cpp:1816  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw4TzCYfarq97M6p)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.hpp:319  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkf8vMMoXQXhL--v_)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.hpp:376  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkf8vMMoXQXhL--wA)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/rtps/messages/RTPSStatisticsMessages.hpp:215  
  message : Use constructors or assignment operators, "Locator_t" is not trivially copyable.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYYAjAHZv_hJbTx3eLSU)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:75  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxM)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:88  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxO)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:98  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxQ)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:98  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxR)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/RefCountedPointer.hpp:127  
  message : Ensure that the move constructor of "Instance" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqjB9YT7Q-GvnLe3)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/RefCountedPointer.hpp:129  
  message : Ensure that the move assignment operator of "Instance" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqjB9YT7Q-GvnLe4)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/SystemInfo.cpp:142  
  message : Replace this call to the non reentrant function "getpwuid" by a call to "getpwuid_r".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixfAzCYfarq97Ndb)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/TimeConversion.hpp:150  
  message : Replace "rand" with the facilities in random.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkgIhMMoXQXhL--xK)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/TimeConversion.hpp:161  
  message : Replace "rand" with the facilities in random.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkgIhMMoXQXhL--xN)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/TimeConversion.hpp:172  
  message : Replace "rand" with the facilities in random.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkgIhMMoXQXhL--xQ)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:111  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owg)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:152  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owe)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:157  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owf)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:198  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYSYJ7bqjWNzjtTw5p02)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:289  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYSYJ7bqjWNzjtTw5p05)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:400  
  message : Ensure that the move constructor of "shared_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owh)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:408  
  message : Ensure that the move assignment operator of "shared_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owi)  
---
  * file : eProsima/Fast-DDS/src/cpp/xmlparser/XMLTree.h:139  
  message : Ensure that the move constructor of "DataNode" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0CvzCYfarq97O4p)  
---
  * file : eProsima/Fast-DDS/src/cpp/xmlparser/XMLTree.h:141  
  message : Ensure that the move assignment operator of "DataNode" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0CvzCYfarq97O4q)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/multiallocation_chain.hpp:90  
  message : Ensure that the move constructor of "basic_multiallocation_chain" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivbKzCYfarq97KK7)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/multiallocation_chain.hpp:94  
  message : Ensure that the move assignment operator of "basic_multiallocation_chain" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivbKzCYfarq97KK8)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/multiallocation_chain.hpp:166  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivbKzCYfarq97KLJ)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/multiallocation_chain.hpp:226  
  message : Ensure that the move constructor of "transform_multiallocation_chain" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivbKzCYfarq97KLM)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/multiallocation_chain.hpp:234  
  message : Ensure that the move assignment operator of "transform_multiallocation_chain" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivbKzCYfarq97KLN)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/multiallocation_chain.hpp:246  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivbKzCYfarq97KLZ)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/date_time/posix_time/posix_time_config.hpp:44  
  message : Make sure that moving an object of class "time_duration" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivG3zCYfarq97J1K)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/allocators/allocator.hpp:168  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuzOzCYfarq97JtD)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/allocators/detail/allocator_common.hpp:299  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuy_zCYfarq97Jr1)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/allocators/detail/allocator_common.hpp:676  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuy_zCYfarq97Jsg)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/atomic.hpp:642  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuvozCYfarq97Jll)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/file_wrapper.hpp:64  
  message : Ensure that the move constructor of "file_wrapper" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuu8zCYfarq97Jk1)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/file_wrapper.hpp:71  
  message : Ensure that the move assignment operator of "file_wrapper" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuu8zCYfarq97Jk2)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/file_wrapper.hpp:80  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuu8zCYfarq97Jk4)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/file_wrapper.hpp:134  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuu8zCYfarq97Jk7)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/managed_memory_impl.hpp:717  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuv3zCYfarq97JmC)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/managed_open_or_create_impl.hpp:230  
  message : Ensure that the move constructor of "managed_open_or_create_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiur1zCYfarq97JhN)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/managed_open_or_create_impl.hpp:233  
  message : Ensure that the move assignment operator of "managed_open_or_create_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiur1zCYfarq97JhO)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/managed_open_or_create_impl.hpp:255  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiur1zCYfarq97JhX)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/managed_open_or_create_impl.hpp:481  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiur1zCYfarq97Jhu)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/exceptions.hpp:82  
  message : Make sure that moving an object of class "lock_exception" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiu0kzCYfarq97JuP)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/exceptions.hpp:96  
  message : Make sure that moving an object of class "bad_alloc" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiu0kzCYfarq97JuR)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/file_mapping.hpp:66  
  message : Ensure that the move constructor of "file_mapping" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuzrzCYfarq97Jtf)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/file_mapping.hpp:74  
  message : Ensure that the move assignment operator of "file_mapping" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuzrzCYfarq97Jtg)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/file_mapping.hpp:83  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuzrzCYfarq97Jti)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/file_mapping.hpp:128  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuzrzCYfarq97Jtj)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/managed_mapped_file.hpp:147  
  message : Ensure that the move constructor of "basic_managed_mapped_file" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiu1vzCYfarq97Jw6)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/managed_mapped_file.hpp:154  
  message : Ensure that the move assignment operator of "basic_managed_mapped_file" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiu1vzCYfarq97Jw7)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/managed_mapped_file.hpp:172  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiu1vzCYfarq97JxF)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/managed_shared_memory.hpp:156  
  message : Ensure that the move constructor of "basic_managed_shared_memory" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuzdzCYfarq97JtN)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/managed_shared_memory.hpp:165  
  message : Ensure that the move assignment operator of "basic_managed_shared_memory" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuzdzCYfarq97JtO)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/managed_shared_memory.hpp:174  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuzdzCYfarq97JtY)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mapped_region.hpp:143  
  message : Ensure that the move constructor of "mapped_region" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuywzCYfarq97Jq3)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mapped_region.hpp:160  
  message : Ensure that the move assignment operator of "mapped_region" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuywzCYfarq97Jq4)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mapped_region.hpp:169  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuywzCYfarq97JrI)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mapped_region.hpp:272  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuywzCYfarq97JrK)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mapped_region.hpp:863  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuywzCYfarq97Jrc)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/detail/mem_algo_common.hpp:63  
  message : Ensure that the move constructor of "basic_multiallocation_chain" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuxZzCYfarq97JnN)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/detail/mem_algo_common.hpp:67  
  message : Ensure that the move assignment operator of "basic_multiallocation_chain" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuxZzCYfarq97JnO)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/rbtree_best_fit.hpp:624  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuxqzCYfarq97Jo7)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/rbtree_best_fit.hpp:872  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuxqzCYfarq97JpV)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/rbtree_best_fit.hpp:980  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuxqzCYfarq97Jpd)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/rbtree_best_fit.hpp:1090  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuxqzCYfarq97Jpo)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/rbtree_best_fit.hpp:1091  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuxqzCYfarq97Jpp)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/rbtree_best_fit.hpp:1270  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuxqzCYfarq97Jp9)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/shared_memory_object.hpp:88  
  message : Ensure that the move constructor of "shared_memory_object" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiu0yzCYfarq97JuU)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/shared_memory_object.hpp:96  
  message : Ensure that the move assignment operator of "shared_memory_object" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiu0yzCYfarq97JuV)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/shared_memory_object.hpp:104  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiu0yzCYfarq97JuX)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/shared_memory_object.hpp:167  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiu0yzCYfarq97JuZ)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/posix/mutex.hpp:132  
  message : This was not the most recently acquired lock. Possible lock order reversal  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISium4zCYfarq97Jex)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/scoped_lock.hpp:131  
  message : Ensure that the move constructor of "scoped_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuptzCYfarq97JgM)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/scoped_lock.hpp:266  
  message : Ensure that the move assignment operator of "scoped_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuptzCYfarq97JgN)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/scoped_lock.hpp:359  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiupuzCYfarq97Jgb)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/sharable_lock.hpp:132  
  message : Ensure that the move constructor of "sharable_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuquzCYfarq97Jgv)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/sharable_lock.hpp:196  
  message : Ensure that the move assignment operator of "sharable_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuquzCYfarq97Jgw)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/sharable_lock.hpp:292  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuquzCYfarq97Jg8)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree.hpp:737  
  message : Ensure that the move constructor of "bstree_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJ0zCYfarq97JUT)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree.hpp:745  
  message : Ensure that the move assignment operator of "bstree_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJ0zCYfarq97JUU)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree.hpp:975  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJ0zCYfarq97JU0)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree.hpp:2102  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJ0zCYfarq97JU6)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree.hpp:2212  
  message : Ensure that the move constructor of "bstree" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJ0zCYfarq97JVC)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree.hpp:2216  
  message : Ensure that the move assignment operator of "bstree" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJ0zCYfarq97JVD)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree_algorithms.hpp:1086  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuKGzCYfarq97JVt)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree_algorithms.hpp:1705  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuKGzCYfarq97JVy)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/ebo_functor_holder.hpp:190  
  message : Ensure that the move constructor of "ebo_functor_holder" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuD-zCYfarq97JN0)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/ebo_functor_holder.hpp:200  
  message : Ensure that the move assignment operator of "ebo_functor_holder" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuD-zCYfarq97JN1)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/ebo_functor_holder.hpp:255  
  message : Ensure that the move constructor of "ebo_functor_holderT, Tag, false" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuD-zCYfarq97JN7)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/ebo_functor_holder.hpp:266  
  message : Ensure that the move assignment operator of "ebo_functor_holderT, Tag, false" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuD-zCYfarq97JN8)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/key_nodeptr_comp.hpp:58  
  message : Make sure that moving an object of class "key_nodeptr_compboost::interprocess::iset_indexboost::interprocess::ipcdetail::index_configchar, boost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::intrusive_key_value_less, boost::intrusive::bhtraitsboost::interprocess::ipcdetail::intrusive_value_type_implboost::intrusive::generic_hookboost::intrusive::RbTreeAlgorithms, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::dft_tag, boost::intrusive::safe_link, boost::intrusive::RbTreeBaseHookId, char, unsigned int, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::safe_link, boost::intrusive::dft_tag, 3, boost::move_detail::identityboost::interprocess::ipcdetail::intrusive_value_type_implboost::intrusive::generic_hookboost::intrusive::RbTreeAlgorithms, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::dft_tag, boost::intrusive::safe_link, boost::intrusive::RbTreeBaseHookId, char, unsigned int" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuCozCYfarq97JNQ)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/key_nodeptr_comp.hpp:58  
  message : Make sure that moving an object of class "key_nodeptr_compboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::size_block_ctrl_compare, boost::intrusive::bhtraitsboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::block_ctrl, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::normal_link, boost::intrusive::dft_tag, 3, boost::move_detail::identityboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::block_ctrl" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuCozCYfarq97JNT)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/key_nodeptr_comp.hpp:58  
  message : Make sure that moving an object of class "key_nodeptr_compstd::lessboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::block_ctrl, boost::intrusive::bhtraitsboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::block_ctrl, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::normal_link, boost::intrusive::dft_tag, 3, boost::move_detail::identityboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::block_ctrl" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuCozCYfarq97JNU)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/key_nodeptr_comp.hpp:58  
  message : Make sure that moving an object of class "key_nodeptr_compstd::lessboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family::block_ctrl, boost::intrusive::bhtraitsboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family::block_ctrl, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, true, boost::intrusive::normal_link, boost::intrusive::dft_tag, 3, boost::move_detail::identityboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family::block_ctrl" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuCozCYfarq97JNV)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/node_cloner_disposer.hpp:75  
  message : Make sure that moving an object of class "node_disposerboost::intrusive::detail::null_disposer, boost::intrusive::bhtraitsboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family::block_ctrl, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, true, boost::intrusive::normal_link, boost::intrusive::dft_tag, 3, boost::intrusive::RbTreeAlgorithms" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuFuzCYfarq97JP0)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/node_cloner_disposer.hpp:75  
  message : Make sure that moving an object of class "node_disposerboost::intrusive::detail::null_disposer, boost::intrusive::bhtraitsboost::interprocess::ipcdetail::intrusive_value_type_implboost::intrusive::generic_hookboost::intrusive::RbTreeAlgorithms, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::dft_tag, boost::intrusive::safe_link, boost::intrusive::RbTreeBaseHookId, char, unsigned int, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::safe_link, boost::intrusive::dft_tag, 3, boost::intrusive::RbTreeAlgorithms" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuFuzCYfarq97JPx)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/node_cloner_disposer.hpp:75  
  message : Make sure that moving an object of class "node_disposerboost::intrusive::detail::null_disposer, boost::intrusive::bhtraitsboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::block_ctrl, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::normal_link, boost::intrusive::dft_tag, 3, boost::intrusive::RbTreeAlgorithms" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuFuzCYfarq97JPy)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/node_cloner_disposer.hpp:75  
  message : Make sure that moving an object of class "node_disposerboost::intrusive::detail::null_disposer, boost::intrusive::bhtraitsboost::interprocess::ipcdetail::intrusive_value_type_implboost::intrusive::generic_hookboost::intrusive::RbTreeAlgorithms, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, true, boost::intrusive::dft_tag, boost::intrusive::safe_link, boost::intrusive::RbTreeBaseHookId, char, unsigned long, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, true, boost::intrusive::safe_link, boost::intrusive::dft_tag, 3, boost::intrusive::RbTreeAlgorithms" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuFuzCYfarq97JPz)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/size_holder.hpp:54  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuAxzCYfarq97JL_)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/rbtree.hpp:143  
  message : Ensure that the move constructor of "rbtree_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuLbzCYfarq97JWg)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/rbtree.hpp:148  
  message : Ensure that the move assignment operator of "rbtree_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuLbzCYfarq97JWh)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/rbtree.hpp:556  
  message : Ensure that the move constructor of "rbtree" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuLbzCYfarq97JXD)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/rbtree.hpp:560  
  message : Ensure that the move assignment operator of "rbtree" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuLbzCYfarq97JXE)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:110  
  message : Ensure that the move constructor of "set_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJFzCYfarq97JRc)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:115  
  message : Ensure that the move assignment operator of "set_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJFzCYfarq97JRd)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:543  
  message : Ensure that the move constructor of "set" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJFzCYfarq97JR_)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:547  
  message : Ensure that the move assignment operator of "set" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJFzCYfarq97JSA)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:647  
  message : Ensure that the move constructor of "multiset_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJFzCYfarq97JSK)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:652  
  message : Ensure that the move assignment operator of "multiset_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJFzCYfarq97JSL)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:1038  
  message : Ensure that the move constructor of "multiset" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJFzCYfarq97JSs)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:1042  
  message : Ensure that the move assignment operator of "multiset" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuJFzCYfarq97JSt)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/slist.hpp:350  
  message : Ensure that the move constructor of "slist_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuMzzCYfarq97JYL)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/slist.hpp:360  
  message : Ensure that the move assignment operator of "slist_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuMzzCYfarq97JYM)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/slist.hpp:718  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuM0zCYfarq97JYn)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/slist.hpp:1995  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuM0zCYfarq97JYy)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/slist.hpp:2226  
  message : Ensure that the move constructor of "slist" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuM0zCYfarq97JY6)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/slist.hpp:2230  
  message : Ensure that the move assignment operator of "slist" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiuM0zCYfarq97JY7)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/detail/shared_count.hpp:356  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivXBzCYfarq97KIO)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:256  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivZ1zCYfarq97KJ2)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:471  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivZ1zCYfarq97KKJ)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:484  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivZ1zCYfarq97KKN)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:567  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivZ1zCYfarq97KKS)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:576  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivZ1zCYfarq97KKT)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:578  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivZ1zCYfarq97KKU)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptboost::bad_weak_ptr" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivn3zCYfarq97KaQ)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptstd::runtime_error" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivn3zCYfarq97KaS)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptboost::gregorian::bad_weekday" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivn3zCYfarq97KaT)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptboost::gregorian::bad_year" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivn3zCYfarq97KaU)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptboost::gregorian::bad_month" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivn3zCYfarq97KaV)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptboost::gregorian::bad_day_of_month" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivn3zCYfarq97KaW)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptboost::gregorian::bad_day_of_year" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivn3zCYfarq97KaX)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:5219  
  message : The move constructor of "iteration_proxy_value" should be unconditionally declared as "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--m2)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:5222  
  message : The move assignment operator of "iteration_proxy_value" should be unconditionally declared as "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--m3)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:6820  
  message : Ensure that the move constructor of "json_sax_dom_parser" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--m5)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:6822  
  message : Ensure that the move assignment operator of "json_sax_dom_parser" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--m6)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7004  
  message : Ensure that the move constructor of "json_sax_dom_callback_parser" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--m7)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7006  
  message : Ensure that the move assignment operator of "json_sax_dom_callback_parser" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--m8)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7504  
  message : Ensure that the move constructor of "lexer" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--m_)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7506  
  message : Ensure that the move assignment operator of "lexer" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--nA)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:8454  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97KiV)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:8517  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97KiW)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:8608  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97KiX)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:9236  
  message : Ensure that the move constructor of "binary_reader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--nC)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:9238  
  message : Ensure that the move assignment operator of "binary_reader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--nD)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:12229  
  message : Make sure that moving an object of class "parsernlohmann::basic_json, nlohmann::detail::iterator_input_adapterconst char *" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9zzCYfarq97KjH)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:12229  
  message : Make sure that moving an object of class "parsernlohmann::basic_json, nlohmann::detail::input_stream_adapter" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9zzCYfarq97KnL)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:19068  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--oz)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:19083  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--o1)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:20518  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkeEwMMoXQXhL--pE)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:22765  
  message : The swap function should be unconditionally declared as "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLaqVEWS9FtSIxskl)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:22782  
  message : The swap function should be unconditionally declared as "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLaqVEWS9FtSIxskm)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:24538  
  message : The swap function should be unconditionally declared as "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZjfLaqVEWS9FtSIxskn)  
---
  * file : eProsima/Fast-DDS/thirdparty/taocpp-pegtl/pegtl/internal/string.hpp:27  
  message : Remove this useless sequence of pointer operators: "&*".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISivwEzCYfarq97Ka5)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:24996  
  message : Replace this call to the non reentrant function "localtime" by a call to "localtime_r".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtAzCYfarq97L3D)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:25287  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvlY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:25309  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvlZ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:30998  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtAzCYfarq97L3n)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:31709  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtAzCYfarq97L4d)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:32136  
  message : Remove this misleading "adjust_width_for_utf8" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtAzCYfarq97L4i)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:32165  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtAzCYfarq97L4v)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:32189  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtAzCYfarq97L4t)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:32373  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtAzCYfarq97L4z)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:35356  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtAzCYfarq97L5O)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:35433  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtAzCYfarq97L5R)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:35983  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtAzCYfarq97L5o)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:36118  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtAzCYfarq97L5t)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:44504  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvmS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:53272  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L7N)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:54824  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYb886cuwhn1MW9k8YAM)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:55881  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L7z)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58526  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L8P)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58530  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L8O)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58531  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L8N)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58533  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L8M)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58838  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L8U)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58839  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L8T)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58850  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L8V)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58957  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L8Z)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58958  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L8Y)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58959  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L8X)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58960  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L8W)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:59562  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L8i)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:60924  
  message : Access of the field 'xBusyHandler' at index 1, while it holds only a single 'void *' element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-05i3-gB3mVexO6D)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:62179  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYo6DGK7sQ9jOKC7SsmJ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:64386  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L9q)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:65821  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L90)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:67267  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L-c)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:67520  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97L-f)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:67705  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvmk)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72200  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvmz)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72201  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvmy)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72202  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvmx)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72203  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvmw)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72204  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvmv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72205  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvmu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72206  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvmt)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:74337  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97MAP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:76258  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97MAu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:76570  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvnQ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:76666  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvnO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:76739  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqRj9YT7Q-GvnLeA)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:77178  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97MBM)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:77453  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97MBS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:77454  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97MBR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:77535  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97MBV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:77605  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97MBY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:78346  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97MBk)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:79725  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97MCL)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:82415  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97MC7)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:82526  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97MDG)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:82695  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97MDK)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:83723  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvnl)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:85015  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYb886cuwhn1MW9k8YAO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:88075  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97MET)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:89810  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97ME1)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:90043  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvny)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:91367  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvn2)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:91443  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtCzCYfarq97MFY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:94446  
  message : Remove this misleading "jump_to_p2_and_check_for_interrupt" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:94459  
  message : Remove this misleading "check_for_interrupt" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZX)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:94495  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvok)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:94495  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvol)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:94554  
  message : Remove this misleading "jump_to_p2" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95272  
  message : Remove this misleading "int_math" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95276  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95277  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95278  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIX)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95281  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95299  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoX)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95299  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95300  
  message : Remove this misleading "fp_math" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95335  
  message : Remove this misleading "arithmetic_result_is_null" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZc)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95478  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIa)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95478  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIb)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95656  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoi)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95656  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95663  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvom)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95663  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvon)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95670  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoo)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95670  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvop)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95702  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvot)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95702  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvou)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95776  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIm)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95776  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIn)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95807  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIo)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95807  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIp)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96069  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIs)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96069  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIt)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96075  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96075  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96093  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIw)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96093  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIx)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96107  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIy)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96107  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIz)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96120  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIe)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96120  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIf)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96213  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96213  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIh)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96245  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MI2)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96245  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MI3)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96266  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIi)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96266  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96352  
  message : Remove this misleading "op_column_restart" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoa)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96383  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvob)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96386  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoc)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96393  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvod)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96448  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MI8)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96453  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoe)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96475  
  message : Remove this misleading "op_column_read_header" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96611  
  message : Remove this misleading "op_column_out" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZe)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96616  
  message : Remove this misleading "op_column_corrupt" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZf)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96722  
  message : Remove this misleading "vdbe_type_error" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvog)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:97147  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJC)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:97147  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJD)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:97720  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoh)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:97795  
  message : Remove this misleading "open_cursor_set_hints" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:97993  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:97993  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJJ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98212  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIk)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98212  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIl)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98344  
  message : Remove this misleading "seek_not_found" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZk)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98348  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98348  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98486  
  message : Remove this misleading "seekscan_search_fail" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZl)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98495  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqRj9YT7Q-GvnLeG)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98495  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqRj9YT7Q-GvnLeH)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98505  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJU)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98505  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98523  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98523  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJX)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98585  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqRj9YT7Q-GvnLeI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98585  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqRj9YT7Q-GvnLeJ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98755  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJb)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98755  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJc)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98759  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqRj9YT7Q-GvnLeK)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98759  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqRj9YT7Q-GvnLeL)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98768  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqRj9YT7Q-GvnLeM)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98768  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqRj9YT7Q-GvnLeN)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98846  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJh)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98846  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJi)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98852  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoq)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98857  
  message : Remove this misleading "notExistsWithKey" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZm)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98881  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98881  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJk)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99028  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJn)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99378  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99378  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJw)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99615  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJ0)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99615  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJ1)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99653  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJ2)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99653  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJ3)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99734  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJ4)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99734  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJ5)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99801  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvor)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99816  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvos)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99831  
  message : Remove this misleading "next_tail" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYkZzxYwHXxtxeKK1WZr)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99840  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJ-)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99840  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJ_)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99845  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJ8)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99845  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJ9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100197  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKC)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100197  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKD)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100598  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKE)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100598  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKF)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100641  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKK)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100641  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKL)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100647  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100647  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKJ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100694  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKN)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100694  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100845  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100845  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKQ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100907  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKU)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100907  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100910  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100910  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKX)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100963  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100963  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKZ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101023  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKa)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101023  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKb)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101039  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101039  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKe)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101431  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKi)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101431  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101771  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKk)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101771  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKl)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101876  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKo)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101876  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKp)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101878  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKm)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101878  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKn)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102248  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqRj9YT7Q-GvnLeO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102248  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZURtqRj9YT7Q-GvnLeP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102305  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKt)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102350  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKr)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102350  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKs)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102582  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MKu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102601  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIC)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102609  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MID)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102617  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIE)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:104629  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZlvXnVqswrv6mz6zQbS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:106483  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYb886cuwhn1MW9k8YAS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:106487  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97ML1)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:106951  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MMN)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:110803  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvpM)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111227  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MOE)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111497  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MOM)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111516  
  message : Access of the field 'a' containing 1 elements at negative index -1  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZOFPW4B4Vgb3UCOkJD_)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111722  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MOR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111798  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvpX)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:112578  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MOf)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:114136  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvps)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:114266  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvpt)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:114619  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvpu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:114685  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvpv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:114691  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MPP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:115115  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MPT)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:115131  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvpz)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:115305  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MPY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:115353  
  message : Remove this misleading "default_expr" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MPZ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:115482  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MPd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:115530  
  message : Remove this misleading "default_expr" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MPe)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:120520  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MRZ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:120539  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MRa)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:122829  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvql)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:123289  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtEzCYfarq97MSe)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:128213  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtFzCYfarq97MUW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:129638  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtFzCYfarq97MUn)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:129655  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtFzCYfarq97MUo)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:138845  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtFzCYfarq97MYC)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:143469  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvsg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:143470  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtGzCYfarq97MZ-)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:143470  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtGzCYfarq97MZ9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:145974  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvsu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:147698  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtGzCYfarq97MbX)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:152982  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtGzCYfarq97Mcu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:155740  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtGzCYfarq97Mdy)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:157366  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtGzCYfarq97MeU)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:161136  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvub)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:161381  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYb886cuwhn1MW9k8YAV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:162730  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtHzCYfarq97MgV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:163570  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtHzCYfarq97Mgu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:163610  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvvI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:164663  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvvb)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:166677  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtHzCYfarq97Mhy)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:167473  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvv7)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:167774  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtHzCYfarq97MiP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:169766  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYb886cuwhn1MW9k8YAY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:170224  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvws)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:170386  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtHzCYfarq97Mjr)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:170387  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtHzCYfarq97Mjq)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:173925  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvw9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:180164  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtIzCYfarq97MnC)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:180338  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtIzCYfarq97MnI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:185266  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtIzCYfarq97MoN)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:185794  
  message : Returned pointer value points outside the original object (potential buffer overflow)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZLQ_6ad53x7xtMCv3OS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:185883  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvxa)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:207767  
  message : Remove this misleading "parse_object_value" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvyX)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:207863  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvya)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:207866  
  message : Remove this misleading "parse_string" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvyb)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:207941  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvyc)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:207950  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvyd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:207963  
  message : Remove this misleading "parse_number" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvye)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208020  
  message : Remove this misleading "parse_number_2" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvyf)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208070  
  message : Remove this misleading "parse_number_finish" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvyg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208102  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvyj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208116  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvyk)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208334  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvyt)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208343  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvyu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208366  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvyv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208512  
  message : Remove this misleading "malformed_jsonb" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvyy)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208786  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvzA)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:209269  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvzT)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:209278  
  message : Remove this misleading "to_double" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvzU)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:209568  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvzc)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:209685  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvzf)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:210569  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvz0)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:210859  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuvz6)  
---
  * file : eProsima/Fast-DDS/tools/fastdds/discovery/fastdds_daemon/daemon/__init__.py:154  
  message : Add 1 missing arguments; 'serve' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH6xdXFK9T8SBv1E5)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>moveit2</a></summary>  

  * file : moveit2/moveit_kinematics/ikfast_kinematics_plugin/scripts/create_ikfast_moveit_plugin.py:364  
  message : Disable access to external entities in XML parsing.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYKwcpHFZzpJC77kImjV)  
---
  * file : moveit2/moveit_py/moveit/policies/policy.py:148  
  message : Add a "self" or class parameter  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY0M-5AV3-gB3mVexO6c)  
---
  * file : moveit2/moveit_py/moveit/servo_client/devices/ps4_dualshock.py:143  
  message : Add a "self" or class parameter  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYaQ0q1avTyJunPyDVLW)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>osrf</a></summary>  

  * file : osrf/osrf_testing_tools_cpp/osrf_testing_tools_cpp/src/memory_tools/custom_memory_functions.cpp:147  
  message : Use of memory after it is freed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi48MzCYfarq97P6B)  
---
  * file : osrf/osrf_testing_tools_cpp/osrf_testing_tools_cpp/src/memory_tools/custom_memory_functions.cpp:290  
  message : Use of memory after it is freed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi48MzCYfarq97P6C)  
---
  * file : osrf/osrf_testing_tools_cpp/osrf_testing_tools_cpp/src/memory_tools/memory_tools_service.cpp:103  
  message : Expression statements should have at most one resource allocation. Consider using factory functions.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi49lzCYfarq97P6b)  
---
  * file : osrf/osrf_testing_tools_cpp/osrf_testing_tools_cpp/src/memory_tools/vendor/bombela/backward-cpp/backward.hpp:545  
  message : Ensure that the move constructor of "handle" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi47yzCYfarq97P32)  
---
  * file : osrf/osrf_testing_tools_cpp/osrf_testing_tools_cpp/src/memory_tools/vendor/bombela/backward-cpp/backward.hpp:546  
  message : Ensure that the move assignment operator of "handle" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi47yzCYfarq97P33)  
---
  * file : osrf/osrf_testing_tools_cpp/osrf_testing_tools_cpp/src/memory_tools/vendor/bombela/backward-cpp/backward.hpp:583  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi47yzCYfarq97P37)  
---
  * file : osrf/osrf_testing_tools_cpp/osrf_testing_tools_cpp/src/memory_tools/vendor/bombela/backward-cpp/backward.hpp:3780  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi47yzCYfarq97P4a)  
---
  * file : osrf/osrf_testing_tools_cpp/osrf_testing_tools_cpp/src/memory_tools/vendor/bombela/backward-cpp/backward.hpp:3783  
  message : Ensure that the move constructor of "SourceFile" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi47yzCYfarq97P4O)  
---
  * file : osrf/osrf_testing_tools_cpp/osrf_testing_tools_cpp/src/memory_tools/vendor/bombela/backward-cpp/backward.hpp:3784  
  message : Ensure that the move assignment operator of "SourceFile" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi47yzCYfarq97P4P)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>ros</a></summary>  

  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/gtest-matchers.h:315  
  message : Ensure that the move constructor of "MatcherBase" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi17XzCYfarq97PKN)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/gtest-matchers.h:320  
  message : Ensure that the move assignment operator of "MatcherBase" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi17XzCYfarq97PKO)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/gtest-matchers.h:510  
  message : Make sure that moving an object of class "Matcherconst std::basic_stringchar &" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi17XzCYfarq97PKd)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/include/gtest/gtest.h:361  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi174zCYfarq97PLv)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/src/gtest-death-test.cc:1386  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi19WzCYfarq97PNy)  
---
  * file : ros/urdfdom/urdf_parser/test/gtest/src/gtest.cc:1195  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi19tzCYfarq97POj)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>ros-visualization</a></summary>  

  * file : ros-visualization/qt_gui_core/qt_gui/src/qt_gui/icon_loader.py:50  
  message : path is used before it is defined. Move the definition before.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi2wxzCYfarq97Pie)  
---
  * file : ros-visualization/rqt/rqt_py_common/src/rqt_py_common/topic_completer.py:102  
  message : Add 1 missing arguments; 'create_node' expects 1 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi2gMzCYfarq97PeC)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>ros2</a></summary>  

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
  * file : ros2/rosidl/rosidl_runtime_cpp/include/rosidl_runtime_cpp/bounded_vector.hpp:229  
  message : Ensure that the move assignment operator of "BoundedVector" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISik0dzCYfarq97Hzd)  
---
  * file : ros2/rosidl_dynamic_typesupport_fastrtps/src/detail/utils.cpp:43  
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
  * file : ros2/rcutils/src/cmdline_parser.c:40  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirRUzCYfarq97I81)  
---
  * file : ros2/rcutils/src/error_handling_helpers.h:83  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZBIALZkMa3zLak3hqWD)  
---
  * file : ros2/rcutils/src/logging.c:476  
  message : Memory copy function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYqmAQdbWvNZCKI3y18h)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:392  
  message : Add 1 missing arguments; 'get_typed_value' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiniszCYfarq97IJ7)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:396  
  message : Add 1 missing arguments; 'get_typed_value' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiniszCYfarq97IJ8)  
---
  * file : ros2/launch/launch_testing/launch_testing/legacy/__init__.py:265  
  message : Change or remove this string; "actions" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISinshzCYfarq97ILT)  
---
  * file : ros2/launch_ros/launch_ros/launch_ros/utilities/__init__.py:37  
  message : Change or remove this string; "evaluate_parameters_dict" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiq9CzCYfarq97Ix3)  
---
  * file : ros2/launch_ros/launch_ros/launch_ros/utilities/__init__.py:44  
  message : Change or remove this string; "normalize_parameters_dict" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiq9CzCYfarq97Ix4)  
---
  * file : ros2/sros2/sros2/sros2/keystore/_permission.py:71  
  message : Disable access to external entities in XML parsing.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimSLzCYfarq97H_a)  
---
  * file : ros2/sros2/sros2/sros2/policy/__init__.py:81  
  message : Disable access to external entities in XML parsing.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimQSzCYfarq97H_J)  
---
  * file : ros2/sros2/sros2/test/policies/policy_to_permissions.py:33  
  message : Disable access to external entities in XML parsing.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimNhzCYfarq97H_F)  
---
  * file : ros2/sros2/sros2/test/test_policy_to_permissions.py:34  
  message : Disable access to external entities in XML parsing.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimOXzCYfarq97H_H)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>ros2_control</a></summary>  

  * file : ros2_control/ros2controlcli/ros2controlcli/verb/list_controllers.py:104  
  message : Refactor this method to not always return the same value.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZGwZD5kFFmecEscKaX_)  
---
</details>  
    
<br />  
  
