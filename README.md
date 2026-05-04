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
  
## BUGS #489 
<details><summary><a style='color:blue;font-size:18px;'>ament</a></summary>  

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
  * file : eclipse-iceoryx/iceoryx/iceoryx_hoofs/source/error_handling/error_handling.cpp:68  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ0Yka8wRvqNgnlDYVwx)  
---
  * file : eclipse-iceoryx/iceoryx/iceoryx_hoofs/source/file_reader/file_reader.cpp:57  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ0Yka_rRvqNgnlDYVxO)  
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
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9B_-MbZ4NfMLP0zl)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "_Bool"). "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Ll)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "_Bool"). "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Lm)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "_Bool"). "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Ln)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "_Bool"). "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Lo)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "_Bool"). "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Lp)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "_Bool"). "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Lq)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Replace "signed char" to "_Bool" type punning with "std::memcpy". "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Lr)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4653  
  message : Replace "unsigned char" to "_Bool" type punning with "std::memcpy". "m_boolean_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Ls)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Replace "signed char" to "unsigned char" type punning with "std::memcpy". "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1L0)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "unsigned char"). "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Lt)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "unsigned char"). "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Lu)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "unsigned char"). "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Lv)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "unsigned char"). "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Lw)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "unsigned char"). "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Lx)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "unsigned char"). "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Ly)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4657  
  message : Replace "_Bool" to "unsigned char" type punning with "std::memcpy". "m_byte_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Lz)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "signed char"). "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1L1)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "signed char"). "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1L2)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "signed char"). "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1L3)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "signed char"). "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1L4)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "signed char"). "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1L5)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "signed char"). "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1L6)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Replace "_Bool" to "signed char" type punning with "std::memcpy". "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1L7)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4661  
  message : Replace "unsigned char" to "signed char" type punning with "std::memcpy". "m_int8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1L8)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "unsigned char"). "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1L-)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "unsigned char"). "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1L9)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "unsigned char"). "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1L_)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "unsigned char"). "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MA)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "unsigned char"). "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MB)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "unsigned char"). "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MC)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Replace "_Bool" to "unsigned char" type punning with "std::memcpy". "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MD)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4665  
  message : Replace "signed char" to "unsigned char" type punning with "std::memcpy". "m_uint8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1ME)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MF)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MG)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MH)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MI)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MJ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MK)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "short"). "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1ML)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4669  
  message : Replace "unsigned short" to "short" type punning with "std::memcpy". "m_int16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MM)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MN)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MO)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MP)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MQ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MR)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MS)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "unsigned short"). "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MT)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4673  
  message : Replace "short" to "unsigned short" type punning with "std::memcpy". "m_uint_16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MU)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MV)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MW)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MX)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MY)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1MZ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Ma)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "int"). "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mb)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4677  
  message : Replace "unsigned int" to "int" type punning with "std::memcpy". "m_int32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mc)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Md)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Me)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mf)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mg)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mh)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned long" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mi)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "unsigned int"). "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mj)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4681  
  message : Replace "int" to "unsigned int" type punning with "std::memcpy". "m_uint32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mk)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Ml)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mm)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mn)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mo)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mp)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mq)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "long"). "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mr)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4685  
  message : Replace "unsigned long" to "long" type punning with "std::memcpy". "m_int64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Ms)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Replace "long" to "unsigned long" type punning with "std::memcpy". "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1M0)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mt)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mu)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mv)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mw)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mx)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1My)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4689  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "unsigned long"). "m_uint64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Mz)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "float"). "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1M1)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "float"). "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1M2)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "float"). "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1M3)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "float"). "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1M4)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "float"). "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1M5)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "float"). "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1M6)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Replace "int" to "float" type punning with "std::memcpy". "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1M7)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4693  
  message : Replace "unsigned int" to "float" type punning with "std::memcpy". "m_float32_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1M8)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1M-)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1M9)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1M_)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NA)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NB)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NC)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "double"). "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1ND)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4697  
  message : Replace "long" to "double" type punning with "std::memcpy". "m_float64_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NE)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NF)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NG)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NH)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NI)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NJ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NK)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NL)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4701  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "long double"). "m_float128_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NM)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "char"). "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NN)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "char"). "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NO)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "char"). "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NP)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "char"). "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NQ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "char"). "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NR)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Replace "_Bool" to "char" type punning with "std::memcpy". "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NS)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Replace "signed char" to "char" type punning with "std::memcpy". "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NT)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4705  
  message : Replace "unsigned char" to "char" type punning with "std::memcpy". "m_char_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NU)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "wchar_t"). "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NV)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "wchar_t"). "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NW)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "wchar_t"). "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NX)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "wchar_t"). "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NY)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "wchar_t"). "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1NZ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "wchar_t"). "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Na)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Replace "int" to "wchar_t" type punning with "std::memcpy". "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nb)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4709  
  message : Replace "unsigned int" to "wchar_t" type punning with "std::memcpy". "m_wchar_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nc)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "int"). "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nd)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "int"). "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Ne)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "int"). "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nf)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "int"). "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Ng)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "int"). "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nh)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "int"). "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Ni)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4713  
  message : Replace "unsigned int" to "int" type punning with "std::memcpy". "m_enumerated_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nj)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nk)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nl)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nm)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nn)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1No)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Np)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nq)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4717  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "struct eprosima::fastcdr::fixed_string128"). "m_string8_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nr)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("_Bool" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Ns)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nt)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nu)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nv)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("signed char" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nw)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned char" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nx)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Ny)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4721  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "class std::basic_stringwchar_t"). "m_string16_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1Nz)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4725  
  message : Remove the undefined behavior caused by type punning types of different sizes ("int" to "class eprosima::fastdds::dds::xtypes::ExtendedAnnotationParameterValue"). "m_extended_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1N0)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4725  
  message : Remove the undefined behavior caused by type punning types of different sizes ("long" to "class eprosima::fastdds::dds::xtypes::ExtendedAnnotationParameterValue"). "m_extended_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1N1)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4725  
  message : Remove the undefined behavior caused by type punning types of different sizes ("short" to "class eprosima::fastdds::dds::xtypes::ExtendedAnnotationParameterValue"). "m_extended_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1N2)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4725  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned int" to "class eprosima::fastdds::dds::xtypes::ExtendedAnnotationParameterValue"). "m_extended_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1N3)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/xtypes/type_representation/detail/dds_xtypes_typeobject.hpp:4725  
  message : Remove the undefined behavior caused by type punning types of different sizes ("unsigned short" to "class eprosima::fastdds::dds::xtypes::ExtendedAnnotationParameterValue"). "m_extended_value" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CEkMbZ4NfMLP1N4)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Locator.hpp:270  
  message : Use "operator==" to check object equality, "Locator_t" is not a trivially copyable type without padding.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BvbMbZ4NfMLP0o_)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/builtin/type_lookup_service/TypeLookupReplyListener.cpp:45  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A5SMbZ4NfMLPz4f)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/builtin/type_lookup_service/TypeLookupRequestListener.cpp:98  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A6AMbZ4NfMLPz5k)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/core/condition/WaitSetImpl.cpp:37  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BPrMbZ4NfMLP0MP)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/core/condition/WaitSetImpl.cpp:42  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BPrMbZ4NfMLP0MQ)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/log/Log.cpp:57  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Ba9MbZ4NfMLP0Wo)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/publisher/DataWriterImpl.cpp:2372  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BUKMbZ4NfMLP0PX)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/publisher/DataWriterImpl.cpp:2403  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BUKMbZ4NfMLP0PW)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/publisher/DataWriterImpl.cpp:2434  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BUKMbZ4NfMLP0PV)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/subscriber/DataReaderImpl.cpp:1939  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BZNMbZ4NfMLP0Ty)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/subscriber/DataReaderImpl.cpp:1962  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BZNMbZ4NfMLP0Tx)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/subscriber/DataReaderImpl.cpp:1986  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BZNMbZ4NfMLP0Tw)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/subscriber/DataReaderImpl/ReadTakeCommand.hpp:94  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BXtMbZ4NfMLP0Sg)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/DynamicDataImpl.cpp:2859  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BEyMbZ4NfMLPz_Z)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/DynamicDataImpl.cpp:2950  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BEyMbZ4NfMLPz_a)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/MemberDescriptorImpl.cpp:280  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BBPMbZ4NfMLPz9-)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/TypeDescriptorImpl.cpp:320  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BEEMbZ4NfMLPz_R)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/type_representation/TypeObjectRegistry.cpp:1447  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BGuMbZ4NfMLP0Dg)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/type_representation/TypeObjectUtils.cpp:2409  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BIvMbZ4NfMLP0I1)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/type_representation/TypeObjectUtils.cpp:3029  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BIvMbZ4NfMLP0I2)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/DataSharing/DataSharingListener.cpp:53  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AmTMbZ4NfMLPzUg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/participant/PDP.cpp:1331  
  message : Called C++ object pointer is null  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_0IMbZ4NfMLPxzg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/participant/PDPListener.cpp:245  
  message : Use pointer or reference to avoid slicing from "ParticipantProxyData" to "ParticipantBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_zWMbZ4NfMLPxxm)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:215  
  message : Ensure that destructor of "FlowControllerAsyncPublishMode" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Aj7MbZ4NfMLPzSn)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:224  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Aj7MbZ4NfMLPzSo)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:267  
  message : Give class "FlowControllerSyncPublishMode" a noexcept destructor (for instance, make sure all subclasses have noexcept destructors).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Aj7MbZ4NfMLPzSr)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:281  
  message : Give class "FlowControllerLimitedAsyncPublishMode" a noexcept destructor (for instance, make sure all subclasses have noexcept destructors).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Aj7MbZ4NfMLPzSv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.cpp:303  
  message : Ensure that destructor of "RTPSMessageGroup" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_9OMbZ4NfMLPx9t)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.cpp:317  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_9OMbZ4NfMLPx91)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.hpp:114  
  message : Ensure that destructor of "RTPSMessageGroup" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_8OMbZ4NfMLPx8U)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:822  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzVz)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:1727  
  message : 'return' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzVQ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:2984  
  message : Use pointer or reference to avoid slicing from "WriterProxyData" to "PublicationBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzXF)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3001  
  message : Use pointer or reference to avoid slicing from "ReaderProxyData" to "SubscriptionBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzXG)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3223  
  message : Use pointer or reference to avoid slicing from "ParticipantProxyData" to "ParticipantBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzXO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3255  
  message : Use pointer or reference to avoid slicing from "WriterProxyData" to "PublicationBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzXR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3286  
  message : Use pointer or reference to avoid slicing from "ReaderProxyData" to "SubscriptionBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzXU)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:15582  
  message : The result of left shift is undefined because the right operand is negative  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzB0)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:54823  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBr)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:60923  
  message : Access of the field 'xBusyHandler' at index 1, while it holds only a single 'void *' element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBs)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:85014  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBt)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:89881  
  message : The left operand of '==' is a garbage value  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:89900  
  message : The left operand of '==' is a garbage value  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:104628  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBw)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:106482  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBy)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:106482  
  message : Null pointer passed to 2nd parameter expecting 'nonnull'  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBx)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111515  
  message : Access of the field 'a' containing 1 elements at negative index -1  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBz)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:129898  
  message : The left operand of '' is a garbage value  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzB1)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:131102  
  message : Remove the useless top-level "volatile" qualifier from this type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPypn)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:150458  
  message : Access to field 'nExpr' results in a dereference of a null pointer (loaded from field 'pList')  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzB2)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:150461  
  message : Access to field 'nExpr' results in a dereference of a null pointer (loaded from field 'pList')  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzB3)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:161382  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzB4)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:169767  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzB5)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:185795  
  message : Returned pointer value points outside the original object (potential buffer overflow)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzB6)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:185888  
  message : Array access (from variable 'zFilename') results in a null pointer dereference  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzB7)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/resources/ResourceEvent.cpp:51  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Am6MbZ4NfMLPzU6)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/ChannelResource.cpp:48  
  message : Null pointer passed to 1st parameter expecting 'nonnull'  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_k8MbZ4NfMLPxhR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/ChannelResource.cpp:54  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_k8MbZ4NfMLPxhP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPAcceptorBasic.h:59  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_hmMbZ4NfMLPxeb)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPAcceptorBasic.h:60  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_hmMbZ4NfMLPxec)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPAcceptorSecure.h:65  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_iXMbZ4NfMLPxen)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPAcceptorSecure.h:66  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_iXMbZ4NfMLPxeo)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPv4Transport.cpp:240  
  message : Use pointer or reference to avoid slicing from "TCPv4TransportDescriptor" to "TCPTransportDescriptor".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_jFMbZ4NfMLPxf5)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemLog.hpp:219  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_gLMbZ4NfMLPxdu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemManager.hpp:277  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_fgMbZ4NfMLPxca)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/test_UDPv4Transport.cpp:284  
  message : Null pointer passed to 1st parameter expecting 'nonnull'  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_clMbZ4NfMLPxYZ)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/rtps/messages/RTPSStatisticsMessages.hpp:215  
  message : Use constructors or assignment operators, "Locator_t" is not trivially copyable.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bd9MbZ4NfMLP0Xf)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2405  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::BaseStatus_s" to "class std::vectorclass eprosima::fastdds::statistics::Connection"). "m_connection_list" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bj3MbZ4NfMLP0kx)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2405  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::DeadlineMissedStatus_s" to "class std::vectorclass eprosima::fastdds::statistics::Connection"). "m_connection_list" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bj3MbZ4NfMLP0ky)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2405  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::IncompatibleQoSStatus_s" to "class std::vectorclass eprosima::fastdds::statistics::Connection"). "m_connection_list" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bj3MbZ4NfMLP0kz)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2409  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::BaseStatus_s" to "class std::vectorclass eprosima::fastdds::statistics::Connection"). "m_connection_list" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bj3MbZ4NfMLP0k0)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2409  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::DeadlineMissedStatus_s" to "class std::vectorclass eprosima::fastdds::statistics::Connection"). "m_connection_list" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bj3MbZ4NfMLP0k1)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2409  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::IncompatibleQoSStatus_s" to "class std::vectorclass eprosima::fastdds::statistics::Connection"). "m_connection_list" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bj3MbZ4NfMLP0k2)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2426  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::BaseStatus_s" to "class eprosima::fastdds::statistics::IncompatibleQoSStatus_s"). "m_incompatible_qos_status" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bj3MbZ4NfMLP0k3)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2426  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::DeadlineMissedStatus_s" to "class eprosima::fastdds::statistics::IncompatibleQoSStatus_s"). "m_incompatible_qos_status" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bj3MbZ4NfMLP0k4)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2426  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class std::vectorclass eprosima::fastdds::statistics::ExtendedIncompatibleQoSStatus_s" to "class eprosima::fastdds::statistics::IncompatibleQoSStatus_s"). "m_incompatible_qos_status" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bj3MbZ4NfMLP0k5)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2430  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::BaseStatus_s" to "class eprosima::fastdds::statistics::IncompatibleQoSStatus_s"). "m_incompatible_qos_status" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bj3MbZ4NfMLP0k6)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2430  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class eprosima::fastdds::statistics::DeadlineMissedStatus_s" to "class eprosima::fastdds::statistics::IncompatibleQoSStatus_s"). "m_incompatible_qos_status" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bj3MbZ4NfMLP0k7)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/types/monitorservice_types.hpp:2430  
  message : Remove the undefined behavior caused by type punning types of different sizes ("class std::vectorclass eprosima::fastdds::statistics::ExtendedIncompatibleQoSStatus_s" to "class eprosima::fastdds::statistics::IncompatibleQoSStatus_s"). "m_incompatible_qos_status" is not an active member of the union  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bj3MbZ4NfMLP0k8)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:75  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AuJMbZ4NfMLPzaB)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:88  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AuJMbZ4NfMLPzaD)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:98  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AuJMbZ4NfMLPzaF)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:98  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AuJMbZ4NfMLPzaG)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_memory/SharedMemWatchdog.hpp:97  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AsQMbZ4NfMLPzZa)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:111  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AwLMbZ4NfMLPzbe)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:152  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AwLMbZ4NfMLPzbf)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:157  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AwLMbZ4NfMLPzbg)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:198  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AwLMbZ4NfMLPzbh)  
---
  * file : eProsima/Fast-DDS/test/dds/xtypes/test_build.py:126  
  message : Ensure that the asyncio.CancelledError exception is re-raised after your cleanup code.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZeaxzm8YQO-EckZ69i_)  
---
  * file : eProsima/Fast-DDS/test/dds/xtypes/update_header_and_create_cases.py:25  
  message : Remove or rework this redundant alternative.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZSlkefKMMoXQXhL--qL)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/variadic_templates_tools.hpp:51  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_FuMbZ4NfMLPw61)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/segment_manager_helper.hpp:75  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-gIMbZ4NfMLPwO6)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/detail/mem_algo_common.hpp:318  
  message : Remove the unary minus operator or change the expression's underlying type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-l6MbZ4NfMLPwWq)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/posix/mutex.hpp:132  
  message : This was not the most recently acquired lock. Possible lock order reversal  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-dMMbZ4NfMLPwL0)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/posix/ptime_to_timespec.hpp:34  
  message : Identical sub-expressions on both sides of operator "-".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-cmMbZ4NfMLPwLj)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/posix/semaphore_wrapper.hpp:225  
  message : Change this loop body so that it can be executed more than once.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-b0MbZ4NfMLPwLJ)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/detail/shared_count.hpp:356  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_AuMbZ4NfMLPw2g)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:256  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_DgMbZ4NfMLPw4o)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:471  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_DgMbZ4NfMLPw49)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:484  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_DgMbZ4NfMLPw4_)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:567  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_DgMbZ4NfMLPw5C)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:576  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_DgMbZ4NfMLPw5D)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:578  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_DgMbZ4NfMLPw5E)  
---
  * file : eProsima/Fast-DDS/thirdparty/filewatch/FileWatch.hpp:124  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_bMMbZ4NfMLPxVw)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:14840  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxOZ)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:19068  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxR-)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:19083  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxSA)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:20138  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxOV)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:20518  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_ayMbZ4NfMLPxSb)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:23519  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxOX)  
---
  * file : eProsima/Fast-DDS/thirdparty/optionparser/optionparser/optionparser.h:2001  
  message : 1 uninitialized field at the end of the constructor call  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_YnMbZ4NfMLPxNf)  
---
  * file : eProsima/Fast-DDS/thirdparty/taocpp-pegtl/pegtl/mmap_input.hpp:38  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_YIMbZ4NfMLPxLI)  
---
  * file : eProsima/Fast-DDS/thirdparty/taocpp-pegtl/pegtl/mmap_input.hpp:61  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_YIMbZ4NfMLPxLJ)  
---
  * file : eProsima/Fast-DDS/thirdparty/taocpp-pegtl/pegtl/read_input.hpp:27  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_WlMbZ4NfMLPxK9)  
---
  * file : eProsima/Fast-DDS/thirdparty/taocpp-pegtl/pegtl/read_input.hpp:49  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_WlMbZ4NfMLPxK-)  
---
  * file : eProsima/Fast-DDS/thirdparty/taocpp-pegtl/pegtl/string_input.hpp:26  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_WyMbZ4NfMLPxK_)  
---
  * file : eProsima/Fast-DDS/tools/fastdds/discovery/fastdds_daemon/daemon/__init__.py:154  
  message : Add 1 missing arguments; 'serve' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZYOH6xdXFK9T8SBv1E5)  
---
  * file : eProsima/Fast-DDS/tools/fds/CliDiscoveryEntrypoint.cpp:66  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Cx0MbZ4NfMLP1Qy)  
---
  * file : eProsima/Fast-DDS/tools/fds/CliDiscoveryEntrypoint.cpp:69  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Cx0MbZ4NfMLP1Qx)  
---
  * file : eProsima/Fast-DDS/tools/fds/CliDiscoveryEntrypoint.cpp:72  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Cx0MbZ4NfMLP1Qw)  
---
  * file : eProsima/Fast-DDS/tools/fds/CliDiscoveryEntrypoint.cpp:75  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Cx0MbZ4NfMLP1Qv)  
---
  * file : eProsima/Fast-DDS/tools/fds/CliDiscoveryEntrypoint.cpp:78  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Cx0MbZ4NfMLP1Qu)  
---
  * file : eProsima/Fast-DDS/tools/fds/CliDiscoveryEntrypoint.cpp:81  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Cx0MbZ4NfMLP1Qt)  
---
  * file : eProsima/Fast-DDS/tools/fds/CliDiscoveryEntrypoint.cpp:84  
  message : 'break' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Cx0MbZ4NfMLP1Qs)  
---
  * file : eProsima/Fast-DDS/tools/fds/CliDiscoveryManager.cpp:412  
  message : 'return' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CyFMbZ4NfMLP1Q5)  
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
  * file : navigation2/nav2_simple_commander/test/test_occupancy_grid.py:41  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNQgMZONY8qvbqfsa)  
---
  * file : navigation2/nav2_simple_commander/test/test_occupancy_grid.py:42  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNQgMZONY8qvbqfsb)  
---
  * file : navigation2/nav2_simple_commander/test/test_occupancy_grid.py:43  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNQgMZONY8qvbqfsc)  
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
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_timeline.py:679  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1Ztw_ub2taBKNOi)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_timeline.py:864  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1Ztw_ub2taBKNOj)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_timeline.py:892  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1Ztw_ub2taBKNOk)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_timeline.py:902  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1Ztw_ub2taBKNOl)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_widget.py:416  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1X_w_ub2taBKNOf)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_widget.py:419  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1X_w_ub2taBKNOg)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_widget.py:425  
  message : This branch duplicates the one on line 419.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi24QzCYfarq97PjT)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_widget.py:425  
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
  * file : ros-visualization/rqt_reconfigure/src/rqt_reconfigure/node_selector_widget.py:513  
  message : Fix this attribute access on a value that can be 'None'.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9FfQMbZ4NfMLP1Xp)  
---
  * file : ros-visualization/rqt_reconfigure/src/rqt_reconfigure/node_selector_widget.py:523  
  message : Fix this attribute access on a value that can be 'None'.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9FfQMbZ4NfMLP1Xq)  
---
  * file : ros-visualization/rqt_reconfigure/src/rqt_reconfigure/node_selector_widget.py:524  
  message : Fix this attribute access on a value that can be 'None'.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9FfQMbZ4NfMLP1Xo)  
---
  * file : ros-visualization/rqt_topic/rqt_topic/models/message.py:42  
  message : Move this time-dependent expression out of the class body and into a method.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZz0i1lknvODKcpvIRSV)  
---
  * file : ros-visualization/rqt_topic/rqt_topic/models/topic.py:108  
  message : Move this time-dependent expression out of the class body and into a method.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZz0i1lznvODKcpvIRSW)  
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
  * file : ros2/launch/launch_testing/launch_testing/legacy/__init__.py:263  
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
  * file : ros2/launch_ros/launch_ros/launch_ros/utilities/__init__.py:37  
  message : Change or remove this string; "evaluate_parameters_dict" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiq9CzCYfarq97Ix3)  
---
  * file : ros2/launch_ros/launch_ros/launch_ros/utilities/__init__.py:44  
  message : Change or remove this string; "normalize_parameters_dict" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiq9CzCYfarq97Ix4)  
---
  * file : ros2/launch_ros/launch_testing_ros/test/examples/check_msgs_launch_test.py:62  
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
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:65  
  message : Add "node_name" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Izv)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:66  
  message : Add "node_namespace" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Izw)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:67  
  message : Add "topic_type" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Izx)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:68  
  message : Add "topic_type_hash" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Izy)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:69  
  message : Add "endpoint_type" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Izz)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:70  
  message : Add "endpoint_gid" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz0)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:71  
  message : Add "qos_profile" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz1)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:242  
  message : Add "node_name" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz2)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:243  
  message : Add "node_namespace" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz3)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:244  
  message : Add "service_type" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz4)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:245  
  message : Add "service_type_hash" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz5)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:246  
  message : Add "endpoint_type" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz6)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:247  
  message : Add "endpoint_gids" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz7)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:248  
  message : Add "qos_profiles" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz8)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:249  
  message : Add "endpoint_count" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz9)  
---
  * file : ros2/rclpy/rclpy/rclpy/node.py:1304  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYjQfw_ub2taBKNOF)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:60  
  message : Raise this exception or remove this useless statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZFEP0Hyi5a_X_62zTxy)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:98  
  message : Add "history" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_Iz-)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:105  
  message : Add "depth" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_Iz_)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:107  
  message : Add "reliability" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0A)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:110  
  message : Add "durability" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0B)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:113  
  message : Add "lifespan" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0C)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:116  
  message : Add "deadline" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0D)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:119  
  message : Add "liveliness" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0E)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:122  
  message : Add "liveliness_lease_duration" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0F)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:126  
  message : Add "avoid_ros_namespace_conventions" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0G)  
---
  * file : ros2/rclpy/rclpy/rclpy/type_hash.py:36  
  message : Add "version" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O7Ts0Fbzs2j_Izt)  
---
  * file : ros2/rclpy/rclpy/rclpy/type_hash.py:37  
  message : Add "value" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O7Ts0Fbzs2j_Izu)  
---
  * file : ros2/rclpy/rclpy/test/test_async_clock.py:124  
  message : Add a checkpoint inside this cancellation scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ3M_Ecn4igBKyOZM2_X)  
---
  * file : ros2/rclpy/rclpy/test/test_async_timer.py:170  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ3M_Edo4igBKyOZM2_d)  
---
  * file : ros2/rclpy/rclpy/test/test_node.py:1672  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZZWHaPjJaW_00fRkMbT)  
---
  * file : ros2/rclpy/rclpy/test/test_node.py:1673  
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
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:87  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39k)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:94  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39l)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:101  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39m)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:107  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39n)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:119  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39o)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:125  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39p)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_direct.py:48  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYfNdw_ub2taBKNN2)  
---
  * file : ros2/rosbag2/ros2bag/test/test_recorder_args_parser.py:405  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZkDFBn1j1WFNLSWaJdE)  
---
  * file : ros2/rosbag2/ros2bag/test/test_recorder_args_parser.py:442  
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
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:41  
  message : Add "header" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5QWTs0Fbzs2j_I0i)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:75  
  message : Add "timestamp1" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5QWTs0Fbzs2j_I0j)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:76  
  message : Add "timestamp2" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5QWTs0Fbzs2j_I0k)  
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
  
## VULNERABILITIES #37 
<details><summary><a style='color:blue;font-size:18px;'>eProsima</a></summary>  

  * file : eProsima/Fast-DDS/src/cpp/utils/md5.cpp:310  
  message : This "memset" is likely to be optimized away by the compiler; either remove it or replace it with "memset_s".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AvbMbZ4NfMLPza-)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_memory/RobustExclusiveLock.hpp:227  
  message : Granting permissions to "others" can lead to unauthorized access to files.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AsrMbZ4NfMLPzZl)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_memory/RobustSharedLock.hpp:366  
  message : Granting permissions to "others" can lead to unauthorized access to files.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AsDMbZ4NfMLPzZS)  
---
  * file : eProsima/Fast-DDS/test/dds/communication/test_build.py:280  
  message : Change this code to not log user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNTM8ZONY8qvbqfsd)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/os_file_functions.hpp:426  
  message : Remove this TOCTOU race condition window when accessing files  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-hbMbZ4NfMLPwPd)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/os_file_functions.hpp:426  
  message : Granting permissions to "others" can lead to unauthorized access to files.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-hbMbZ4NfMLPwPc)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/os_file_functions.hpp:426  
  message : Granting permissions to "others" can lead to unauthorized access to files.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-hbMbZ4NfMLPwPe)  
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
  * file : navigation2/nav2_bringup/launch/tb3_simulation_launch.py:217  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY__0QdDMWueF4yM_B3h)  
---
  * file : navigation2/nav2_bringup/launch/tb4_simulation_launch.py:259  
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
  <details><summary><a style='color:blue;font-size:18px;'>ros-tooling</a></summary>  

  * file : ros-tooling/libstatistics_collector/.github/workflows/autoapprove.yml:13  
  message : Workflows should not rely on forgeable GitHub context values to trust events  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZtn-43b0uebLXI9fXvl)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>ros2</a></summary>  

  * file : ros2/rosidl/rosidl_generator_type_description/rosidl_generator_type_description/__init__.py:205  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZyIXMQp0TDJ4yT6vtRY)  
---
  * file : ros2/rosidl/rosidl_pycommon/rosidl_pycommon/__init__.py:55  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZxAQ2i94cQIsYvStOBd)  
---
  * file : ros2/rosidl/rosidl_pycommon/rosidl_pycommon/__init__.py:200  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZxAQ2i94cQIsYvStOBe)  
---
  * file : ros2/rosidl/rosidl_pycommon/rosidl_pycommon/__init__.py:201  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNLz-ZONY8qvbqfsH)  
---
  * file : ros2/rosidl/rosidl_pycommon/rosidl_pycommon/__init__.py:216  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZxAQ2i94cQIsYvStOBf)  
---
  * file : ros2/rosidl/rosidl_pycommon/rosidl_pycommon/__init__.py:217  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZxAQ2i94cQIsYvStOBg)  
---
  * file : ros2/rosidl/rosidl_pycommon/rosidl_pycommon/__init__.py:219  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNLz-ZONY8qvbqfsG)  
---
  * file : ros2/rosidl/rosidl_pycommon/rosidl_pycommon/__init__.py:229  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNLz-ZONY8qvbqfsI)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/rosidl_generator_py/generate_py_impl.py:130  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNPeeZONY8qvbqfsK)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/rosidl_generator_py/generate_py_impl.py:209  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNPeeZONY8qvbqfsJ)  
---
  * file : ros2/sros2/sros2/sros2/keystore/_permission.py:71  
  message : Disable access to external entities in XML parsing.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimSLzCYfarq97H_a)  
---
  * file : ros2/sros2/sros2/sros2/policy/__init__.py:70  
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
  
## ISSUES (level blocker) #607 
<details><summary><a style='color:blue;font-size:18px;'>eclipse-iceoryx</a></summary>  

  * file : eclipse-iceoryx/iceoryx/iceoryx_hoofs/source/log/logger.cpp:141  
  message : Replace this call to the non reentrant function "localtime" by a call to "localtime_r".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi01KzCYfarq97PEZ)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>eProsima</a></summary>  

  * file : eProsima/Fast-CDR/include/fastcdr/FastBuffer.h:268  
  message : Ensure that the move constructor of "FastBuffer" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9C3kMbZ4NfMLP1Sm)  
---
  * file : eProsima/Fast-CDR/include/fastcdr/FastBuffer.h:280  
  message : Ensure that the move assignment operator of "FastBuffer" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9C3kMbZ4NfMLP1Sn)  
---
  * file : eProsima/Fast-CDR/include/fastcdr/xcdr/optional.hpp:221  
  message : Ensure that the move assignment operator of "optional" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9C2hMbZ4NfMLP1Rk)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2338  
  message : Ensure that the move constructor of "TypeIdV1" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9B8YMbZ4NfMLP0yF)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2358  
  message : Ensure that the move assignment operator of "TypeIdV1" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9B8YMbZ4NfMLP0yG)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2450  
  message : Ensure that the move constructor of "TypeObjectV1" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9B8YMbZ4NfMLP0yL)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2470  
  message : Ensure that the move assignment operator of "TypeObjectV1" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9B8YMbZ4NfMLP0yM)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2567  
  message : Ensure that the move constructor of "TypeInformationParameter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9B8YMbZ4NfMLP0yS)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2589  
  message : Ensure that the move assignment operator of "TypeInformationParameter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9B8YMbZ4NfMLP0yT)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/domain/qos/DomainParticipantQos.hpp:78  
  message : Remove the "virtual" specifier and refactor the code to not require polymorphism for comparison operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CH4MbZ4NfMLP1Oh)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/log/Log.hpp:292  
  message : Potential leak of memory pointed to by 'p'  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9B_-MbZ4NfMLP0zl)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/subscriber/qos/DataReaderQos.hpp:43  
  message : Make sure that moving an object of class "DataReaderQos" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CLaMbZ4NfMLP1PJ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/topic/TypeSupport.hpp:225  
  message : Remove the "virtual" specifier and refactor the code to not require polymorphism for comparison operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CF-MbZ4NfMLP1OB)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/attributes/PropertyPolicy.hpp:44  
  message : Ensure that the move constructor of "PropertyPolicy" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BqZMbZ4NfMLP0l0)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/attributes/PropertyPolicy.hpp:59  
  message : Ensure that the move assignment operator of "PropertyPolicy" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BqZMbZ4NfMLP0l1)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/attributes/ReaderAttributes.hpp:58  
  message : Make sure that moving an object of class "ReaderAttributes" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BqmMbZ4NfMLP0l9)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/BinaryProperty.hpp:48  
  message : Ensure that the move constructor of "BinaryProperty" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BwbMbZ4NfMLP0pa)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/BinaryProperty.hpp:81  
  message : Ensure that the move assignment operator of "BinaryProperty" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BwbMbZ4NfMLP0pb)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/CDRMessage_t.hpp:168  
  message : Ensure that the move constructor of "CDRMessage_t" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BtlMbZ4NfMLP0nu)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/CDRMessage_t.hpp:187  
  message : Ensure that the move assignment operator of "CDRMessage_t" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BtlMbZ4NfMLP0nv)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/EntityId_t.hpp:111  
  message : Ensure that the move constructor of "EntityId_t" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bx0MbZ4NfMLP0qi)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/EntityId_t.hpp:124  
  message : Ensure that the move assignment operator of "EntityId_t" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bx0MbZ4NfMLP0qj)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Guid.hpp:39  
  message : Make sure that moving an object of class "GUID_t" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BuaMbZ4NfMLP0oM)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Locator.hpp:107  
  message : Ensure that the move constructor of "Locator_t" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BvbMbZ4NfMLP0o5)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Locator.hpp:270  
  message : Use "operator==" to check object equality, "Locator_t" is not a trivially copyable type without padding.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BvbMbZ4NfMLP0o_)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorList.hpp:120  
  message : Ensure that the move constructor of "LocatorList" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9ByhMbZ4NfMLP0rW)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorList.hpp:135  
  message : Ensure that the move assignment operator of "LocatorList" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9ByhMbZ4NfMLP0rX)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorList.hpp:359  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9ByhMbZ4NfMLP0ri)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorSelectorEntry.hpp:38  
  message : Make sure that moving an object of class "LocatorSelectorEntry" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bt_MbZ4NfMLP0n7)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorSelectorEntry.hpp:43  
  message : Make sure that moving an object of class "EntryState" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bt_MbZ4NfMLP0n8)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorWithMask.hpp:34  
  message : Make sure that moving an object of class "LocatorWithMask" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BwPMbZ4NfMLP0pZ)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorsIterator.hpp:47  
  message : Remove the "virtual" specifier and refactor the code to not require polymorphism for comparison operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bv3MbZ4NfMLP0pU)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorsIterator.hpp:56  
  message : Remove the "virtual" specifier and refactor the code to not require polymorphism for comparison operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bv3MbZ4NfMLP0pW)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/OriginalWriterInfo.hpp:55  
  message : Ensure that the move constructor of "OriginalWriterInfo" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bs8MbZ4NfMLP0ms)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/OriginalWriterInfo.hpp:61  
  message : Ensure that the move assignment operator of "OriginalWriterInfo" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bs8MbZ4NfMLP0mv)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Property.hpp:46  
  message : Ensure that the move constructor of "Property" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9ByEMbZ4NfMLP0qx)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Property.hpp:83  
  message : Ensure that the move assignment operator of "Property" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9ByEMbZ4NfMLP0qy)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/SampleIdentity.hpp:33  
  message : Make sure that moving an object of class "SampleIdentity" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BwyMbZ4NfMLP0pk)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Token.hpp:45  
  message : Ensure that the move constructor of "DataHolder" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bu0MbZ4NfMLP0oa)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Token.hpp:63  
  message : Ensure that the move assignment operator of "DataHolder" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bu0MbZ4NfMLP0ob)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/WriteParams.hpp:36  
  message : Make sure that moving an object of class "WriteParams" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BwDMbZ4NfMLP0pX)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/transport/network/AllowedNetworkInterface.hpp:51  
  message : Ensure that the move constructor of "AllowedNetworkInterface" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9B0TMbZ4NfMLP0r9)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/transport/network/BlockedNetworkInterface.hpp:51  
  message : Ensure that the move constructor of "BlockedNetworkInterface" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9B0IMbZ4NfMLP0r7)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/transport/network/NetworkInterface.hpp:61  
  message : Ensure that the move constructor of "NetworkInterface" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9B0fMbZ4NfMLP0sA)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/transport/network/NetworkInterfaceWithFilter.hpp:74  
  message : Ensure that the move constructor of "NetworkInterfaceWithFilter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9B0qMbZ4NfMLP0sE)  
---
  * file : eProsima/Fast-DDS/include/fastdds/utils/IPFinder.hpp:55  
  message : Make sure that moving an object of class "info_IP" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9CQTMbZ4NfMLP1QK)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/builtin/type_lookup_service/TypeLookupReplyListener.hpp:51  
  message : Make sure that moving an object of class "ReplyWithServerGUID" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A28MbZ4NfMLPzy0)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/subscriber/DataReaderImpl/SampleLoanManager.hpp:193  
  message : Ensure that the move constructor of "OutstandingLoanItem" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BX6MbZ4NfMLP0Sv)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/subscriber/DataReaderImpl/SampleLoanManager.hpp:195  
  message : Ensure that the move assignment operator of "OutstandingLoanItem" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9BX6MbZ4NfMLP0Sw)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:75  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A_OMbZ4NfMLPz82)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:161  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A_OMbZ4NfMLPz85)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:260  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A_OMbZ4NfMLPz86)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:353  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A_OMbZ4NfMLPz87)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:372  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A_OMbZ4NfMLPz88)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:434  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A_OMbZ4NfMLPz89)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlModule.hpp:474  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A_OMbZ4NfMLPz9B)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:87  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A-iMbZ4NfMLPz7M)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:303  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A-iMbZ4NfMLPz7O)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:1407  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A-iMbZ4NfMLPz7h)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:1465  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A-iMbZ4NfMLPz7l)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:1513  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A-iMbZ4NfMLPz7o)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:1590  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A-iMbZ4NfMLPz7t)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:1739  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A-iMbZ4NfMLPz70)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:2108  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A-iMbZ4NfMLPz7_)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/xtypes/dynamic_types/idl_parser/IdlParser.hpp:2328  
  message : Replace "module" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A-iMbZ4NfMLPz8C)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/data/ProxyHashTables.hpp:60  
  message : Ensure that the move constructor of "node_segregator" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_3oMbZ4NfMLPx3s)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/database/DiscoveryDataBase.hpp:91  
  message : Ensure that the move constructor of "AckedFunctor" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_w8MbZ4NfMLPxwH)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/database/DiscoveryParticipantChangeData.hpp:38  
  message : Make sure that moving an object of class "DiscoveryParticipantChangeData" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_xVMbZ4NfMLPxwd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/participant/PDPListener.cpp:245  
  message : Use pointer or reference to avoid slicing from "ParticipantProxyData" to "ParticipantBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_zWMbZ4NfMLPxxm)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/exceptions/Exception.h:85  
  message : Ensure that the move constructor of "Exception" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AB1MbZ4NfMLPyAO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/exceptions/Exception.h:108  
  message : Ensure that the move assignment operator of "Exception" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AB1MbZ4NfMLPyAP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:215  
  message : Ensure that destructor of "FlowControllerAsyncPublishMode" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Aj7MbZ4NfMLPzSn)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:267  
  message : Give class "FlowControllerSyncPublishMode" a noexcept destructor (for instance, make sure all subclasses have noexcept destructors).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Aj7MbZ4NfMLPzSr)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:281  
  message : Give class "FlowControllerLimitedAsyncPublishMode" a noexcept destructor (for instance, make sure all subclasses have noexcept destructors).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Aj7MbZ4NfMLPzSv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:1414  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Aj7MbZ4NfMLPzTS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:1415  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Aj7MbZ4NfMLPzTT)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.cpp:303  
  message : Ensure that destructor of "RTPSMessageGroup" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_9OMbZ4NfMLPx9t)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.hpp:114  
  message : Ensure that destructor of "RTPSMessageGroup" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_8OMbZ4NfMLPx8U)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/network/ReceiverResource.h:95  
  message : Ensure that the move constructor of "ReceiverResource" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_rjMbZ4NfMLPxom)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:486  
  message : unannotated fall-through between switch labels  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzVO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:2984  
  message : Use pointer or reference to avoid slicing from "WriterProxyData" to "PublicationBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzXF)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3001  
  message : Use pointer or reference to avoid slicing from "ReaderProxyData" to "SubscriptionBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzXG)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3223  
  message : Use pointer or reference to avoid slicing from "ParticipantProxyData" to "ParticipantBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzXO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3255  
  message : Use pointer or reference to avoid slicing from "WriterProxyData" to "PublicationBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzXR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:3286  
  message : Use pointer or reference to avoid slicing from "ReaderProxyData" to "SubscriptionBuiltinTopicData".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AoQMbZ4NfMLPzXU)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.hpp:173  
  message : Ensure that the move constructor of "ReceiverControlBlock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AomMbZ4NfMLPzXa)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/reader/StatefulReader.cpp:1672  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_pLMbZ4NfMLPxnW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/reader/StatelessReader.hpp:248  
  message : Make sure that moving an object of class "RemoteWriterInfo_t" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_oVMbZ4NfMLPxk9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/security/common/ParticipantGenericMessage.h:45  
  message : Ensure that the move constructor of "MessageIdentity" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_-ZMbZ4NfMLPx-p)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/security/common/ParticipantGenericMessage.h:60  
  message : Ensure that the move assignment operator of "MessageIdentity" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_-ZMbZ4NfMLPx-q)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/security/common/ParticipantGenericMessage.h:159  
  message : Ensure that the move constructor of "ParticipantGenericMessage" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_-ZMbZ4NfMLPx-u)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/security/common/ParticipantGenericMessage.h:184  
  message : Ensure that the move assignment operator of "ParticipantGenericMessage" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_-ZMbZ4NfMLPx-v)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/ChannelResource.h:34  
  message : Ensure that the move constructor of "ChannelResource" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_dkMbZ4NfMLPxZK)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPv4Transport.cpp:240  
  message : Use pointer or reference to avoid slicing from "TCPv4TransportDescriptor" to "TCPTransportDescriptor".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_jFMbZ4NfMLPxf5)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/UDPChannelResource.h:36  
  message : Make sure that moving an object of class "eProsimaUDPSocket" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_kkMbZ4NfMLPxhC)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/UDPChannelResource.h:159  
  message : Ensure that the move assignment operator of "UDPChannelResource" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_kkMbZ4NfMLPxhF)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemGlobal.hpp:70  
  message : Make sure that moving an object of class "BufferDescriptor" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_d2MbZ4NfMLPxZQ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemLog.hpp:173  
  message : Make sure that moving an object of class "Pkt" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_gLMbZ4NfMLPxdl)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemManager.hpp:685  
  message : Ensure that the move assignment operator of "Listener" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_fgMbZ4NfMLPxct)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemManager.hpp:720  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_fgMbZ4NfMLPxcx)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemManager.hpp:852  
  message : Ensure that the move assignment operator of "Port" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_fgMbZ4NfMLPxc1)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/test_UDPv4Transport.cpp:295  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_clMbZ4NfMLPxYV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/test_UDPv4Transport.cpp:296  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_clMbZ4NfMLPxYU)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/test_UDPv4Transport.cpp:297  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_clMbZ4NfMLPxYT)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/LivelinessManager.cpp:126  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AhwMbZ4NfMLPzRI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.cpp:1702  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AfVMbZ4NfMLPzPY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.cpp:1849  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AfVMbZ4NfMLPzPd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.hpp:322  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AehMbZ4NfMLPzNm)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.hpp:378  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AehMbZ4NfMLPzNn)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/rtps/messages/RTPSStatisticsMessages.hpp:215  
  message : Use constructors or assignment operators, "Locator_t" is not trivially copyable.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9Bd9MbZ4NfMLP0Xf)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:75  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AuJMbZ4NfMLPzaB)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:88  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AuJMbZ4NfMLPzaD)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:98  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AuJMbZ4NfMLPzaF)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/ProxyPool.hpp:98  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AuJMbZ4NfMLPzaG)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/RefCountedPointer.hpp:127  
  message : Ensure that the move constructor of "Instance" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AtwMbZ4NfMLPzZ5)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/RefCountedPointer.hpp:129  
  message : Ensure that the move assignment operator of "Instance" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AtwMbZ4NfMLPzZ6)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/SystemInfo.cpp:142  
  message : Replace this call to the non reentrant function "getpwuid" by a call to "getpwuid_r".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AvAMbZ4NfMLPzam)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/TimeConversion.hpp:150  
  message : Replace "rand" with the facilities in random.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AvoMbZ4NfMLPzbL)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/TimeConversion.hpp:161  
  message : Replace "rand" with the facilities in random.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AvoMbZ4NfMLPzbO)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/TimeConversion.hpp:172  
  message : Replace "rand" with the facilities in random.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AvoMbZ4NfMLPzbR)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/md5.cpp:310  
  message : This "memset" is likely to be optimized away by the compiler; either remove it or replace it with "memset_s".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AvbMbZ4NfMLPza-)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:111  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AwLMbZ4NfMLPzbe)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:152  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AwLMbZ4NfMLPzbf)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:157  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AwLMbZ4NfMLPzbg)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:198  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AwLMbZ4NfMLPzbh)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:289  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AwLMbZ4NfMLPzbi)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:400  
  message : Ensure that the move constructor of "shared_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AwLMbZ4NfMLPzbj)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_mutex.hpp:408  
  message : Ensure that the move assignment operator of "shared_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AwLMbZ4NfMLPzbk)  
---
  * file : eProsima/Fast-DDS/src/cpp/xmlparser/XMLTree.h:139  
  message : Ensure that the move constructor of "DataNode" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A07MbZ4NfMLPzuN)  
---
  * file : eProsima/Fast-DDS/src/cpp/xmlparser/XMLTree.h:141  
  message : Ensure that the move assignment operator of "DataNode" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9A07MbZ4NfMLPzuO)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/multiallocation_chain.hpp:90  
  message : Ensure that the move constructor of "basic_multiallocation_chain" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_FQMbZ4NfMLPw6O)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/multiallocation_chain.hpp:94  
  message : Ensure that the move assignment operator of "basic_multiallocation_chain" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_FQMbZ4NfMLPw6P)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/multiallocation_chain.hpp:166  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_FQMbZ4NfMLPw6a)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/multiallocation_chain.hpp:226  
  message : Ensure that the move constructor of "transform_multiallocation_chain" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_FQMbZ4NfMLPw6d)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/multiallocation_chain.hpp:234  
  message : Ensure that the move assignment operator of "transform_multiallocation_chain" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_FQMbZ4NfMLPw6e)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/container/detail/multiallocation_chain.hpp:246  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_FQMbZ4NfMLPw6n)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/date_time/posix_time/posix_time_config.hpp:44  
  message : Make sure that moving an object of class "time_duration" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-xiMbZ4NfMLPwt0)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/allocators/allocator.hpp:168  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-mhMbZ4NfMLPwXJ)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/allocators/detail/allocator_common.hpp:299  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-m1MbZ4NfMLPwXZ)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/allocators/detail/allocator_common.hpp:676  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-m1MbZ4NfMLPwX_)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/atomic.hpp:642  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-jMMbZ4NfMLPwRb)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/file_wrapper.hpp:64  
  message : Ensure that the move constructor of "file_wrapper" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-iuMbZ4NfMLPwQ6)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/file_wrapper.hpp:71  
  message : Ensure that the move assignment operator of "file_wrapper" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-iuMbZ4NfMLPwQ7)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/file_wrapper.hpp:80  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-iuMbZ4NfMLPwQ8)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/file_wrapper.hpp:134  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-iuMbZ4NfMLPwQ-)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/managed_memory_impl.hpp:717  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-jcMbZ4NfMLPwR6)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/managed_open_or_create_impl.hpp:230  
  message : Ensure that the move constructor of "managed_open_or_create_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-ffMbZ4NfMLPwNB)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/managed_open_or_create_impl.hpp:233  
  message : Ensure that the move assignment operator of "managed_open_or_create_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-ffMbZ4NfMLPwNC)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/managed_open_or_create_impl.hpp:255  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-ffMbZ4NfMLPwNK)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/detail/managed_open_or_create_impl.hpp:481  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-ffMbZ4NfMLPwNY)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/exceptions.hpp:82  
  message : Make sure that moving an object of class "lock_exception" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-nTMbZ4NfMLPwYw)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/exceptions.hpp:96  
  message : Make sure that moving an object of class "bad_alloc" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-nTMbZ4NfMLPwYy)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/file_mapping.hpp:66  
  message : Ensure that the move constructor of "file_mapping" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-o6MbZ4NfMLPwc0)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/file_mapping.hpp:74  
  message : Ensure that the move assignment operator of "file_mapping" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-o6MbZ4NfMLPwc1)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/file_mapping.hpp:83  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-o6MbZ4NfMLPwc2)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/file_mapping.hpp:128  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-o6MbZ4NfMLPwc3)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/managed_mapped_file.hpp:147  
  message : Ensure that the move constructor of "basic_managed_mapped_file" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-oCMbZ4NfMLPwa1)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/managed_mapped_file.hpp:154  
  message : Ensure that the move assignment operator of "basic_managed_mapped_file" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-oCMbZ4NfMLPwa2)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/managed_mapped_file.hpp:172  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-oCMbZ4NfMLPwbD)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/managed_shared_memory.hpp:156  
  message : Ensure that the move constructor of "basic_managed_shared_memory" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-otMbZ4NfMLPwca)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/managed_shared_memory.hpp:165  
  message : Ensure that the move assignment operator of "basic_managed_shared_memory" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-otMbZ4NfMLPwcb)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/managed_shared_memory.hpp:174  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-otMbZ4NfMLPwcp)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mapped_region.hpp:143  
  message : Ensure that the move constructor of "mapped_region" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-lWMbZ4NfMLPwTe)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mapped_region.hpp:160  
  message : Ensure that the move assignment operator of "mapped_region" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-lWMbZ4NfMLPwTf)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mapped_region.hpp:169  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-lWMbZ4NfMLPwTi)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mapped_region.hpp:272  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-lWMbZ4NfMLPwTk)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mapped_region.hpp:863  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-lWMbZ4NfMLPwT5)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/detail/mem_algo_common.hpp:63  
  message : Ensure that the move constructor of "basic_multiallocation_chain" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-l6MbZ4NfMLPwV8)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/detail/mem_algo_common.hpp:67  
  message : Ensure that the move assignment operator of "basic_multiallocation_chain" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-l6MbZ4NfMLPwV9)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/rbtree_best_fit.hpp:624  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-lqMbZ4NfMLPwUk)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/rbtree_best_fit.hpp:872  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-lqMbZ4NfMLPwU5)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/rbtree_best_fit.hpp:980  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-lqMbZ4NfMLPwVA)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/rbtree_best_fit.hpp:1090  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-lqMbZ4NfMLPwVJ)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/rbtree_best_fit.hpp:1091  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-lqMbZ4NfMLPwVK)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/mem_algo/rbtree_best_fit.hpp:1270  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-lqMbZ4NfMLPwVa)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/shared_memory_object.hpp:88  
  message : Ensure that the move constructor of "shared_memory_object" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-pJMbZ4NfMLPwc9)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/shared_memory_object.hpp:96  
  message : Ensure that the move assignment operator of "shared_memory_object" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-pJMbZ4NfMLPwc-)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/shared_memory_object.hpp:104  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-pJMbZ4NfMLPwc_)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/shared_memory_object.hpp:167  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-pJMbZ4NfMLPwdB)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/posix/mutex.hpp:132  
  message : This was not the most recently acquired lock. Possible lock order reversal  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-dMMbZ4NfMLPwL0)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/scoped_lock.hpp:131  
  message : Ensure that the move constructor of "scoped_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-esMbZ4NfMLPwMh)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/scoped_lock.hpp:266  
  message : Ensure that the move assignment operator of "scoped_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-esMbZ4NfMLPwMi)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/scoped_lock.hpp:359  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-esMbZ4NfMLPwMs)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/sharable_lock.hpp:132  
  message : Ensure that the move constructor of "sharable_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-eEMbZ4NfMLPwMF)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/sharable_lock.hpp:196  
  message : Ensure that the move assignment operator of "sharable_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-eEMbZ4NfMLPwMG)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/interprocess/sync/sharable_lock.hpp:292  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-eEMbZ4NfMLPwMR)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree.hpp:737  
  message : Ensure that the move constructor of "bstree_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-MyMbZ4NfMLPwBN)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree.hpp:745  
  message : Ensure that the move assignment operator of "bstree_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-MyMbZ4NfMLPwBO)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree.hpp:975  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-MyMbZ4NfMLPwBs)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree.hpp:2102  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-MyMbZ4NfMLPwBy)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree.hpp:2212  
  message : Ensure that the move constructor of "bstree" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-MyMbZ4NfMLPwB6)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree.hpp:2216  
  message : Ensure that the move assignment operator of "bstree" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-MyMbZ4NfMLPwB7)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree_algorithms.hpp:1086  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-PAMbZ4NfMLPwFC)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/bstree_algorithms.hpp:1705  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-PAMbZ4NfMLPwFR)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/ebo_functor_holder.hpp:190  
  message : Ensure that the move constructor of "ebo_functor_holder" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-GdMbZ4NfMLPv63)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/ebo_functor_holder.hpp:200  
  message : Ensure that the move assignment operator of "ebo_functor_holder" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-GdMbZ4NfMLPv64)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/ebo_functor_holder.hpp:255  
  message : Ensure that the move constructor of "ebo_functor_holderT, Tag, false" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-GdMbZ4NfMLPv66)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/ebo_functor_holder.hpp:266  
  message : Ensure that the move assignment operator of "ebo_functor_holderT, Tag, false" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-GdMbZ4NfMLPv67)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/key_nodeptr_comp.hpp:58  
  message : Make sure that moving an object of class "key_nodeptr_compstd::lessboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::block_ctrl, boost::intrusive::bhtraitsboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::block_ctrl, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::normal_link, boost::intrusive::dft_tag, 3, boost::move_detail::identityboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::block_ctrl" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-JSMbZ4NfMLPv9o)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/key_nodeptr_comp.hpp:58  
  message : Make sure that moving an object of class "key_nodeptr_compboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::size_block_ctrl_compare, boost::intrusive::bhtraitsboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::block_ctrl, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::normal_link, boost::intrusive::dft_tag, 3, boost::move_detail::identityboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::block_ctrl" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-JSMbZ4NfMLPv9p)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/key_nodeptr_comp.hpp:58  
  message : Make sure that moving an object of class "key_nodeptr_compboost::interprocess::iset_indexboost::interprocess::ipcdetail::index_configchar, boost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::intrusive_key_value_less, boost::intrusive::bhtraitsboost::interprocess::ipcdetail::intrusive_value_type_implboost::intrusive::generic_hookboost::intrusive::RbTreeAlgorithms, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::dft_tag, boost::intrusive::safe_link, boost::intrusive::RbTreeBaseHookId, char, unsigned int, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::safe_link, boost::intrusive::dft_tag, 3, boost::move_detail::identityboost::interprocess::ipcdetail::intrusive_value_type_implboost::intrusive::generic_hookboost::intrusive::RbTreeAlgorithms, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::dft_tag, boost::intrusive::safe_link, boost::intrusive::RbTreeBaseHookId, char, unsigned int" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-JSMbZ4NfMLPv9q)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/key_nodeptr_comp.hpp:58  
  message : Make sure that moving an object of class "key_nodeptr_compstd::lessboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family::block_ctrl, boost::intrusive::bhtraitsboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family::block_ctrl, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, true, boost::intrusive::normal_link, boost::intrusive::dft_tag, 3, boost::move_detail::identityboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family::block_ctrl" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-JSMbZ4NfMLPv9r)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/node_cloner_disposer.hpp:75  
  message : Make sure that moving an object of class "node_disposerboost::intrusive::detail::null_disposer, boost::intrusive::bhtraitsboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family, boost::interprocess::offset_ptrvoid, unsigned int::block_ctrl, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::normal_link, boost::intrusive::dft_tag, 3, boost::intrusive::RbTreeAlgorithms" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-HQMbZ4NfMLPv8J)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/node_cloner_disposer.hpp:75  
  message : Make sure that moving an object of class "node_disposerboost::intrusive::detail::null_disposer, boost::intrusive::bhtraitsboost::interprocess::ipcdetail::intrusive_value_type_implboost::intrusive::generic_hookboost::intrusive::RbTreeAlgorithms, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::dft_tag, boost::intrusive::safe_link, boost::intrusive::RbTreeBaseHookId, char, unsigned int, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, unsigned int, true, boost::intrusive::safe_link, boost::intrusive::dft_tag, 3, boost::intrusive::RbTreeAlgorithms" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-HQMbZ4NfMLPv8K)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/node_cloner_disposer.hpp:75  
  message : Make sure that moving an object of class "node_disposerboost::intrusive::detail::null_disposer, boost::intrusive::bhtraitsboost::interprocess::rbtree_best_fitboost::interprocess::mutex_family::block_ctrl, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, true, boost::intrusive::normal_link, boost::intrusive::dft_tag, 3, boost::intrusive::RbTreeAlgorithms" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-HQMbZ4NfMLPv8L)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/node_cloner_disposer.hpp:75  
  message : Make sure that moving an object of class "node_disposerboost::intrusive::detail::null_disposer, boost::intrusive::bhtraitsboost::interprocess::ipcdetail::intrusive_value_type_implboost::intrusive::generic_hookboost::intrusive::RbTreeAlgorithms, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, true, boost::intrusive::dft_tag, boost::intrusive::safe_link, boost::intrusive::RbTreeBaseHookId, char, unsigned long, boost::intrusive::rbtree_node_traitsboost::interprocess::offset_ptrvoid, true, boost::intrusive::safe_link, boost::intrusive::dft_tag, 3, boost::intrusive::RbTreeAlgorithms" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-HQMbZ4NfMLPv8M)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/detail/size_holder.hpp:54  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-FRMbZ4NfMLPv6B)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/rbtree.hpp:143  
  message : Ensure that the move constructor of "rbtree_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-QBMbZ4NfMLPwFw)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/rbtree.hpp:148  
  message : Ensure that the move assignment operator of "rbtree_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-QBMbZ4NfMLPwFx)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/rbtree.hpp:556  
  message : Ensure that the move constructor of "rbtree" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-QBMbZ4NfMLPwGQ)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/rbtree.hpp:560  
  message : Ensure that the move assignment operator of "rbtree" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-QBMbZ4NfMLPwGR)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:110  
  message : Ensure that the move constructor of "set_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-OaMbZ4NfMLPwDR)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:115  
  message : Ensure that the move assignment operator of "set_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-OaMbZ4NfMLPwDS)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:543  
  message : Ensure that the move constructor of "set" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-OaMbZ4NfMLPwDw)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:547  
  message : Ensure that the move assignment operator of "set" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-OaMbZ4NfMLPwDx)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:647  
  message : Ensure that the move constructor of "multiset_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-OaMbZ4NfMLPwD4)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:652  
  message : Ensure that the move assignment operator of "multiset_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-OaMbZ4NfMLPwD5)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:1038  
  message : Ensure that the move constructor of "multiset" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-OaMbZ4NfMLPwEX)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/set.hpp:1042  
  message : Ensure that the move assignment operator of "multiset" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-OaMbZ4NfMLPwEY)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/slist.hpp:350  
  message : Ensure that the move constructor of "slist_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-QsMbZ4NfMLPwGw)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/slist.hpp:360  
  message : Ensure that the move assignment operator of "slist_impl" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-QsMbZ4NfMLPwGx)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/slist.hpp:718  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-QsMbZ4NfMLPwHL)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/slist.hpp:1995  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-QsMbZ4NfMLPwHW)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/slist.hpp:2226  
  message : Ensure that the move constructor of "slist" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-QsMbZ4NfMLPwHe)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/intrusive/slist.hpp:2230  
  message : Ensure that the move assignment operator of "slist" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8-QsMbZ4NfMLPwHf)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/detail/shared_count.hpp:356  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_AuMbZ4NfMLPw2g)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:256  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_DgMbZ4NfMLPw4o)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:471  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_DgMbZ4NfMLPw49)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:484  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_DgMbZ4NfMLPw4_)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:567  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_DgMbZ4NfMLPw5C)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:576  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_DgMbZ4NfMLPw5D)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/smart_ptr/shared_ptr.hpp:578  
  message : Replace this use of "std::auto_ptr" with "std::unique_ptr"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_DgMbZ4NfMLPw5E)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptboost::bad_weak_ptr" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_M5MbZ4NfMLPxJP)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptstd::runtime_error" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_M5MbZ4NfMLPxJS)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptboost::gregorian::bad_weekday" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_M5MbZ4NfMLPxJT)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptboost::gregorian::bad_year" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_M5MbZ4NfMLPxJU)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptboost::gregorian::bad_month" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_M5MbZ4NfMLPxJV)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptboost::gregorian::bad_day_of_month" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_M5MbZ4NfMLPxJW)  
---
  * file : eProsima/Fast-DDS/thirdparty/boost/include/boost/throw_exception.hpp:103  
  message : Make sure that moving an object of class "wrapexceptboost::gregorian::bad_day_of_year" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_M5MbZ4NfMLPxJX)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:5219  
  message : The move constructor of "iteration_proxy_value" should be unconditionally declared as "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxOj)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:5222  
  message : The move assignment operator of "iteration_proxy_value" should be unconditionally declared as "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxOk)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:6820  
  message : Ensure that the move constructor of "json_sax_dom_parser" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxO4)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:6822  
  message : Ensure that the move assignment operator of "json_sax_dom_parser" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxO5)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7004  
  message : Ensure that the move constructor of "json_sax_dom_callback_parser" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxO6)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7006  
  message : Ensure that the move assignment operator of "json_sax_dom_callback_parser" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxO7)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7504  
  message : Ensure that the move constructor of "lexer" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxPJ)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7506  
  message : Ensure that the move assignment operator of "lexer" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxPK)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:8454  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxPU)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:8517  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxPV)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:8608  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxPW)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:9236  
  message : Ensure that the move constructor of "binary_reader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxPY)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:9238  
  message : Ensure that the move assignment operator of "binary_reader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxPZ)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:12229  
  message : Make sure that moving an object of class "parsernlohmann::basic_json, nlohmann::detail::iterator_input_adapterconst char *" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxQG)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:12229  
  message : Make sure that moving an object of class "parsernlohmann::basic_json, nlohmann::detail::iterator_input_adapter__gnu_cxx::__normal_iteratorconst char *, std::basic_stringchar" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_ayMbZ4NfMLPxVr)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:12229  
  message : Make sure that moving an object of class "parsernlohmann::basic_json, nlohmann::detail::input_stream_adapter" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_ayMbZ4NfMLPxVs)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:19068  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxR-)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:19083  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_axMbZ4NfMLPxSA)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:20518  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_ayMbZ4NfMLPxSb)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:22765  
  message : The swap function should be unconditionally declared as "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_ayMbZ4NfMLPxSk)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:22782  
  message : The swap function should be unconditionally declared as "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_ayMbZ4NfMLPxSl)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:24538  
  message : The swap function should be unconditionally declared as "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_ayMbZ4NfMLPxTF)  
---
  * file : eProsima/Fast-DDS/thirdparty/taocpp-pegtl/pegtl/internal/string.hpp:27  
  message : Remove this useless sequence of pointer operators: "&*".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g8_SjMbZ4NfMLPxKE)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:24996  
  message : Replace this call to the non reentrant function "localtime" by a call to "localtime_r".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyKM)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:25287  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyKV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:25309  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyKW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:30998  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyK7)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:31709  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyLu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:32136  
  message : Remove this misleading "adjust_width_for_utf8" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyLw)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:32165  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyL9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:32189  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyL8)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:32373  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyME)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:35355  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyMW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:35432  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyMZ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:35982  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyM2)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:36117  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyM7)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:44503  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZUMbZ4NfMLPyN_)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:53271  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyOW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:54823  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBr)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:55880  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPB)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58525  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPb)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58529  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPa)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58530  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPZ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58532  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58837  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58838  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPf)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58849  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPh)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58956  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPl)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58957  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPk)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58958  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:58959  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPi)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:59561  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyPu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:60923  
  message : Access of the field 'xBusyHandler' at index 1, while it holds only a single 'void *' element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBs)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:62178  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyQa)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:64385  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyQ6)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:65820  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyRD)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:67266  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyRl)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:67519  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyRo)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:67704  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyRt)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72199  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPySh)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72200  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPySg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72201  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPySf)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72202  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPySe)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72203  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPySd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72204  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPySc)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:72205  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPySb)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:74336  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyTU)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:76257  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyT3)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:76569  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyUD)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:76665  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyUN)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:76738  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyUQ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:77177  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyUg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:77452  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyUm)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:77453  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyUl)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:77534  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyUp)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:77604  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyUs)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:78345  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyU4)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:79724  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyVi)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:82414  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyWN)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:82525  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyWV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:82694  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyWY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:83722  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyWf)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:85014  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBt)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:88074  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyXj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:89809  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyYF)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:90042  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyYK)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:91366  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyYn)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:91442  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZVMbZ4NfMLPyYo)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:94445  
  message : Remove this misleading "jump_to_p2_and_check_for_interrupt" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybf)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:94458  
  message : Remove this misleading "check_for_interrupt" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:94494  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybh)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:94494  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybi)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:94553  
  message : Remove this misleading "jump_to_p2" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95271  
  message : Remove this misleading "int_math" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybm)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95275  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybn)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95276  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybo)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95277  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybp)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95280  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybq)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95298  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybs)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95298  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybt)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95299  
  message : Remove this misleading "fp_math" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybr)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95334  
  message : Remove this misleading "arithmetic_result_is_null" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybl)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95477  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95477  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95655  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyby)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95655  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybz)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95662  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyb0)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95662  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyb1)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95669  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyb2)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95669  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyb3)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95701  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyb4)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95701  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyb5)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95775  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyb6)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95775  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyb7)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95806  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyb8)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95806  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyb9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96068  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyb-)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96068  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyb_)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96074  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycA)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96074  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycB)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96092  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycC)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96092  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycD)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96106  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycE)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96106  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycF)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96119  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycG)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96119  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycH)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96212  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycJ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96212  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycK)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96244  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycL)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96244  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycM)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96265  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycN)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96265  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96351  
  message : Remove this misleading "op_column_restart" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96382  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96385  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycT)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96392  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycU)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96447  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96452  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96474  
  message : Remove this misleading "op_column_read_header" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycX)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96610  
  message : Remove this misleading "op_column_out" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycQ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96615  
  message : Remove this misleading "op_column_corrupt" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96721  
  message : Remove this misleading "vdbe_type_error" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycZ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:97146  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycc)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:97146  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:97719  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:97794  
  message : Remove this misleading "open_cursor_set_hints" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPych)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:97992  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyci)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:97992  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98211  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycm)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98211  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycn)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98343  
  message : Remove this misleading "seek_not_found" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyck)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98347  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyco)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98347  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycp)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98485  
  message : Remove this misleading "seekscan_search_fail" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycr)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98494  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycs)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98494  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyct)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98504  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98504  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98522  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycw)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98522  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycx)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98584  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycy)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98584  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPycz)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98754  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyc0)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98754  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyc1)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98758  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyc2)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98758  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyc3)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98767  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyc4)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98767  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyc5)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98845  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyc8)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98845  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyc9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98851  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyc6)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98856  
  message : Remove this misleading "notExistsWithKey" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyc7)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98880  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyc-)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98880  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyc_)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99027  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydB)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99377  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydC)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99377  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydD)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99614  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydF)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99614  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydG)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99652  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydH)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99652  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99733  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydJ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99733  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydK)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99800  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydL)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99815  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydM)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99830  
  message : Remove this misleading "next_tail" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydN)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99839  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydQ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99839  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99844  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:99844  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100196  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100196  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydT)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100597  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydU)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100597  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100640  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydZ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100640  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyda)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100646  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydX)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100646  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100693  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydc)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100693  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100844  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyde)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100844  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydf)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100906  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100906  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydh)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100909  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydi)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100909  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100962  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydk)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:100962  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydl)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101022  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydm)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101022  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydn)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101038  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydp)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101038  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydq)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101430  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyds)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101430  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydt)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101770  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydu)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101770  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101875  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydy)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101875  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydz)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101877  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydw)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:101877  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPydx)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102247  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyd1)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102247  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyd2)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102304  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyd5)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102349  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyd3)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102349  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyd4)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102581  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyd6)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102600  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybb)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102608  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybc)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102616  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPybd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:104628  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBw)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:106482  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBy)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:106486  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyfC)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:106950  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyfZ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:110802  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyhJ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111226  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyhV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111496  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyhd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111515  
  message : Access of the field 'a' containing 1 elements at negative index -1  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBz)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111721  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyhi)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111797  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyhk)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:112577  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyh6)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:114135  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyit)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:114265  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyiw)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:114618  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyiz)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:114684  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyi0)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:114690  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyi1)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:115114  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyi9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:115130  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyi-)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:115304  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyjC)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:115352  
  message : Remove this misleading "default_expr" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyjD)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:115481  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyjH)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:115529  
  message : Remove this misleading "default_expr" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZWMbZ4NfMLPyjI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:120519  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPylX)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:120538  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPylY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:122828  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPymD)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:123288  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPymU)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:128214  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPyoc)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:129639  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPyov)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:129656  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPyow)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:138846  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPysp)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:143470  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPyu9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:143471  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPyu-)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:143471  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPyu8)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:145975  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPyv9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:147699  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZXMbZ4NfMLPywi)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:152983  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZYMbZ4NfMLPyye)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:155741  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZYMbZ4NfMLPyzt)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:157367  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZYMbZ4NfMLPy0N)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:161137  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZYMbZ4NfMLPy1u)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:161382  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzB4)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:162731  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZYMbZ4NfMLPy23)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:163571  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZYMbZ4NfMLPy3b)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:163611  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZYMbZ4NfMLPy3e)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:164664  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZYMbZ4NfMLPy4G)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:166678  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZYMbZ4NfMLPy4u)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:167474  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZYMbZ4NfMLPy5Y)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:167775  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZYMbZ4NfMLPy5h)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:169767  
  message : Memory set function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzB5)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:170225  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZYMbZ4NfMLPy7V)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:170387  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy7h)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:170388  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy7g)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:173926  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy8t)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:180165  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy9T)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:180339  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy9X)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:185267  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy-h)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:185795  
  message : Returned pointer value points outside the original object (potential buffer overflow)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzB6)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:185884  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy-t)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:207768  
  message : Remove this misleading "parse_object_value" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy_s)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:207864  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy_v)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:207867  
  message : Remove this misleading "parse_string" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy_w)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:207942  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy_x)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:207951  
  message : The direct parent of this switch-label is not the body of a switch statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy_y)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:207964  
  message : Remove this misleading "parse_number" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy_z)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208021  
  message : Remove this misleading "parse_number_2" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy_0)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208071  
  message : Remove this misleading "parse_number_finish" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy_1)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208103  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy_4)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208117  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPy_5)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208335  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzAC)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208344  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzAD)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208367  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzAE)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208513  
  message : Remove this misleading "malformed_jsonb" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzAH)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:208787  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzAV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:209270  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzAo)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:209279  
  message : Remove this misleading "to_double" label.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzAp)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:209569  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzAx)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:209686  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzA0)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:210570  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBJ)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:210860  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ1g9AZZMbZ4NfMLPzBP)  
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

  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:392  
  message : Add 1 missing arguments; 'get_typed_value' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiniszCYfarq97IJ7)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:396  
  message : Add 1 missing arguments; 'get_typed_value' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiniszCYfarq97IJ8)  
---
  * file : ros2/launch/launch_testing/launch_testing/legacy/__init__.py:263  
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
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:65  
  message : Add "node_name" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Izv)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:66  
  message : Add "node_namespace" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Izw)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:67  
  message : Add "topic_type" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Izx)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:68  
  message : Add "topic_type_hash" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Izy)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:69  
  message : Add "endpoint_type" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Izz)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:70  
  message : Add "endpoint_gid" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz0)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:71  
  message : Add "qos_profile" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz1)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:242  
  message : Add "node_name" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz2)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:243  
  message : Add "node_namespace" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz3)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:244  
  message : Add "service_type" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz4)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:245  
  message : Add "service_type_hash" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz5)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:246  
  message : Add "endpoint_type" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz6)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:247  
  message : Add "endpoint_gids" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz7)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:248  
  message : Add "qos_profiles" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz8)  
---
  * file : ros2/rclpy/rclpy/rclpy/endpoint_info.py:249  
  message : Add "endpoint_count" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O77s0Fbzs2j_Iz9)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:98  
  message : Add "history" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_Iz-)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:105  
  message : Add "depth" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_Iz_)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:107  
  message : Add "reliability" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0A)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:110  
  message : Add "durability" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0B)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:113  
  message : Add "lifespan" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0C)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:116  
  message : Add "deadline" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0D)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:119  
  message : Add "liveliness" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0E)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:122  
  message : Add "liveliness_lease_duration" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0F)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:126  
  message : Add "avoid_ros_namespace_conventions" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O8Ls0Fbzs2j_I0G)  
---
  * file : ros2/rclpy/rclpy/rclpy/type_hash.py:36  
  message : Add "version" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O7Ts0Fbzs2j_Izt)  
---
  * file : ros2/rclpy/rclpy/rclpy/type_hash.py:37  
  message : Add "value" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5O7Ts0Fbzs2j_Izu)  
---
  * file : ros2/rosidl/rosidl_generator_type_description/rosidl_generator_type_description/__init__.py:205  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZyIXMQp0TDJ4yT6vtRY)  
---
  * file : ros2/rosidl/rosidl_pycommon/rosidl_pycommon/__init__.py:201  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNLz-ZONY8qvbqfsH)  
---
  * file : ros2/rosidl/rosidl_pycommon/rosidl_pycommon/__init__.py:219  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNLz-ZONY8qvbqfsG)  
---
  * file : ros2/rosidl/rosidl_pycommon/rosidl_pycommon/__init__.py:229  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNLz-ZONY8qvbqfsI)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/rosidl_generator_py/generate_py_impl.py:130  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNPeeZONY8qvbqfsK)  
---
  * file : ros2/rosidl_python/rosidl_generator_py/rosidl_generator_py/generate_py_impl.py:209  
  message : Change this code to not construct the path from user-controlled data.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZwcNPeeZONY8qvbqfsJ)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:41  
  message : Add "header" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5QWTs0Fbzs2j_I0i)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:75  
  message : Add "timestamp1" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5QWTs0Fbzs2j_I0j)  
---
  * file : ros2/rosidl_runtime_py/test/rosidl_runtime_py/test_set_message.py:76  
  message : Add "timestamp2" to the class's "__slots__".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZ2E5QWTs0Fbzs2j_I0k)  
---
  * file : ros2/sros2/sros2/sros2/keystore/_permission.py:71  
  message : Disable access to external entities in XML parsing.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISimSLzCYfarq97H_a)  
---
  * file : ros2/sros2/sros2/sros2/policy/__init__.py:70  
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
  
