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
  
## BUGS #267 
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

  * file : eProsima/Fast-CDR/utils/doxygen/pages/customdoxygen.css:179  
  message : Unexpected duplicate "font-size"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0NwzCYfarq97O-7)  
---
  * file : eProsima/Fast-CDR/utils/doxygen/pages/customdoxygen.css:266  
  message : Unexpected nonstandard direction  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0NwzCYfarq97O-_)  
---
  * file : eProsima/Fast-CDR/utils/doxygen/pages/customdoxygen.css:624  
  message : Unexpected duplicate "background-color"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0NwzCYfarq97O-8)  
---
  * file : eProsima/Fast-CDR/utils/doxygen/pages/customdoxygen.css:805  
  message : Unexpected missing generic font family  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0NwzCYfarq97O--)  
---
  * file : eProsima/Fast-CDR/utils/doxygen/pages/customdoxygen.css:1013  
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
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Locator.h:252  
  message : Use "operator==" to check object equality, "Locator_t" is not a trivially copyable type without padding.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiysezCYfarq97OI_)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/messages/RTPSMessageGroup.h:110  
  message : Ensure that destructor of "RTPSMessageGroup" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiy1zzCYfarq97OPc)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/ProxyPool.hpp:75  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxM)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/ProxyPool.hpp:88  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxO)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/ProxyPool.hpp:98  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxQ)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/ProxyPool.hpp:98  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxR)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/shared_mutex.hpp:111  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owg)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/shared_mutex.hpp:152  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owe)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/shared_mutex.hpp:157  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owf)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/shared_mutex.hpp:198  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYSYJ7bqjWNzjtTw5p02)  
---
  * file : eProsima/Fast-DDS/src/cpp/dynamic-types/DynamicData.cpp:1229  
  message : 1st function call argument is an uninitialized value  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixjWzCYfarq97N7i)  
---
  * file : eProsima/Fast-DDS/src/cpp/dynamic-types/DynamicTypeBuilderFactory.cpp:1108  
  message : Forming reference to null pointer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixkXzCYfarq97N_c)  
---
  * file : eProsima/Fast-DDS/src/cpp/dynamic-types/DynamicTypeBuilderFactory.cpp:1113  
  message : Forming reference to null pointer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixkXzCYfarq97N_d)  
---
  * file : eProsima/Fast-DDS/src/cpp/dynamic-types/DynamicTypeBuilderFactory.cpp:1119  
  message : Forming reference to null pointer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixkXzCYfarq97N_e)  
---
  * file : eProsima/Fast-DDS/src/cpp/dynamic-types/DynamicTypeBuilderFactory.cpp:1124  
  message : Forming reference to null pointer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixkXzCYfarq97N_f)  
---
  * file : eProsima/Fast-DDS/src/cpp/dynamic-types/DynamicTypeBuilderFactory.cpp:1129  
  message : Forming reference to null pointer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixkXzCYfarq97N_g)  
---
  * file : eProsima/Fast-DDS/src/cpp/dynamic-types/DynamicTypeBuilderFactory.cpp:1134  
  message : Forming reference to null pointer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixkXzCYfarq97N_h)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/builtin/typelookup/common/TypeLookupTypes.cpp:1056  
  message : This conditional operation returns the same value whether the condition is "true" or "false".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pOQRw2X4EK9K44gQ)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/builtin/typelookup/common/TypeLookupTypes.cpp:1160  
  message : This conditional operation returns the same value whether the condition is "true" or "false".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pOQRw2X4EK9K44gR)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/core/condition/WaitSetImpl.cpp:39  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYW4cZPeJXHd5uT915On)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/core/condition/WaitSetImpl.cpp:44  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYW4cZPeJXHd5uT915Oo)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/core/policy/ParameterList.cpp:210  
  message : The left operand of '==' is a garbage value  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixU7zCYfarq97NV0)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/log/Log.cpp:57  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pOS0w2X4EK9K44ga)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/subscriber/DataReaderImpl/ReadTakeCommand.hpp:95  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixBhzCYfarq97NHE)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/DataSharing/DataSharingListener.cpp:50  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pNppw2X4EK9K44fO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/participant/PDP.cpp:1257  
  message : Called C++ object pointer is null  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RWB8pZKJaqlJl3_K)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:209  
  message : Ensure that destructor of "FlowControllerAsyncPublishMode" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MyI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:218  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pNnfw2X4EK9K44fE)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:261  
  message : Give class "FlowControllerSyncPublishMode" a noexcept destructor (for instance, make sure all subclasses have noexcept destructors).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MyP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:275  
  message : Give class "FlowControllerLimitedAsyncPublishMode" a noexcept destructor (for instance, make sure all subclasses have noexcept destructors).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MyR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/history/TopicPayloadPool.hpp:270  
  message : Access of the field 'data' at negative byte offset -12  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RWTQpZKJaqlJl3_S)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/history/WriterHistory.cpp:24  
  message : Remove non-standard characters from this #include.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RWRupZKJaqlJl3_R)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.cpp:244  
  message : Ensure that destructor of "RTPSMessageGroup" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw0IzCYfarq97M08)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.cpp:256  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw0IzCYfarq97M1H)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.cpp:897  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwWszCYfarq97LOf)  
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
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:106483  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYb886cuwhn1MW9k8YAS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:106483  
  message : Null pointer passed to 2nd parameter expecting 'nonnull'  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZOFPW4B4Vgb3UCOkJD9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:111516  
  message : Access of the field 'a' at negative byte offset -24  
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
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:163409  
  message : Access of the field 'a' at index 3, while it holds only 3 'struct WhereOrCost' elements  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RW2dpZKJaqlJl3_3)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:167529  
  message : Dereference of null pointer (loaded from variable 'pbRetryLimit')  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuv0a)  
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
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:206640  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuv0c)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/resources/ResourceEvent.cpp:50  
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
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPAcceptorSecure.h:62  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwJEzCYfarq97K1o)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPAcceptorSecure.h:63  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwJEzCYfarq97K1p)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPv4Transport.cpp:241  
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
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/tcp/RTCPMessageManager.cpp:78  
  message : Memory copy function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv_EzCYfarq97Kpv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.cpp:341  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw4TzCYfarq97M5g)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.cpp:348  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw4TzCYfarq97M5h)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.cpp:355  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw4TzCYfarq97M5i)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/xmlparser/XMLDynamicParser.cpp:196  
  message : Called C++ object pointer is null  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwhUzCYfarq97Lna)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/rtps/messages/RTPSStatisticsMessages.hpp:207  
  message : Use constructors or assignment operators, "Locator_t" is not trivially copyable.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYYAjAHZv_hJbTx3eLSU)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/shared_memory/SharedMemWatchdog.hpp:97  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pNx5w2X4EK9K44fk)  
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
  * file : eProsima/Fast-DDS/thirdparty/filewatch/FileWatch.hpp:122  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pK-Fw2X4EK9K44dG)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:9920  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97Kiu)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:12626  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPB7dpM_KNhuouae0)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:18010  
  message : Ensure this forwarding constructor has constraints that prevent copying / moving objects of the same type.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYUEPB7dpM_KNhuouaez)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:25311  
  message : Identical sub-expressions on both sides of operator "&&".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9zzCYfarq97KnK)  
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
  * file : eProsima/Fast-DDS/utils/doxygen/pages/customdoxygen.css:179  
  message : Unexpected duplicate "font-size"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0IHzCYfarq97O5o)  
---
  * file : eProsima/Fast-DDS/utils/doxygen/pages/customdoxygen.css:266  
  message : Unexpected nonstandard direction  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0IHzCYfarq97O5s)  
---
  * file : eProsima/Fast-DDS/utils/doxygen/pages/customdoxygen.css:624  
  message : Unexpected duplicate "background-color"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0IHzCYfarq97O5p)  
---
  * file : eProsima/Fast-DDS/utils/doxygen/pages/customdoxygen.css:805  
  message : Unexpected missing generic font family  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0IHzCYfarq97O5r)  
---
  * file : eProsima/Fast-DDS/utils/doxygen/pages/customdoxygen.css:1013  
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

  * file : navigation2/nav2_simple_commander/nav2_simple_commander/line_iterator.py:84  
  message : Correct one of the identical sub-expressions on both sides of operator "==".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYR0LI5rHE-0Dh1G_Im6)  
---
</details>  
<details><summary><a style='color:blue;font-size:18px;'>osrf</a></summary>  

  * file : osrf/osrf_pycommon/tests/unit/test_cli_utils/test_common.py:32  
  message : Provide a value for field(s) with index 1.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi40lzCYfarq97P2b)  
---
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

  * file : ros/class_loader/src/class_loader.cpp:75  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYKfo4YVEkPBL9VHvoyl)  
---
  * file : ros/class_loader/src/multi_library_class_loader.cpp:89  
  message : Do not throw uncaught exceptions in a destructor.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYKfo4YIEkPBL9VHvoyk)  
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
  * file : ros-perception/image_common/camera_info_manager_py/camera_info_manager/zoom_camera_info_manager.py:229  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZOFPe0E4Vgb3UCOkJEa)  
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
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_timeline.py:635  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1Ztw_ub2taBKNOi)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_timeline.py:820  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1Ztw_ub2taBKNOj)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_timeline.py:848  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruY1Ztw_ub2taBKNOk)  
---
  * file : ros-visualization/rqt_bag/rqt_bag/src/rqt_bag/bag_timeline.py:858  
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
  * file : ros-visualization/rqt_graph/src/rqt_graph/rosgraph2_impl.py:436  
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
</details>  
<details><summary><a style='color:blue;font-size:18px;'>ros2</a></summary>  

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
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:228  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN7)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:229  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN8)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:230  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN9)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:231  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN-)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:232  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNN_)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:389  
  message : Add 1 missing arguments; 'get_typed_value' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiniszCYfarq97IJ7)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:393  
  message : Add 1 missing arguments; 'get_typed_value' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiniszCYfarq97IJ8)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:551  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYh66w_ub2taBKNOA)  
---
  * file : ros2/launch/launch_testing/launch_testing/legacy/__init__.py:265  
  message : Change or remove this string; "actions" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISinshzCYfarq97ILT)  
---
  * file : ros2/launch/test_launch_testing/test/dummy_tests/dummy.py:19  
  message : Correct one of the identical sub-expressions on both sides of operator "==".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISin3jzCYfarq97IME)  
---
  * file : ros2/launch/test_launch_testing/test/dummy_tests/locking.cpp:18  
  message : 'return' will never be executed  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISin25zCYfarq97IL_)  
---
  * file : ros2/launch_ros/launch_ros/launch_ros/utilities/__init__.py:36  
  message : Change or remove this string; "evaluate_parameters_dict" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiq9CzCYfarq97Ix3)  
---
  * file : ros2/launch_ros/launch_ros/launch_ros/utilities/__init__.py:42  
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
  * file : ros2/launch_ros/test_launch_ros/test/test_launch_ros/descriptions/test_parameter_file.py:127  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiq06zCYfarq97IxA)  
---
  * file : ros2/rcl/rcl_yaml_param_parser/test/mocking_utils/patch.hpp:161  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiqR2zCYfarq97Iqz)  
---
  * file : ros2/rclpy/rclpy/rclpy/node.py:1397  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYjQfw_ub2taBKNOF)  
---
  * file : ros2/rclpy/rclpy/rclpy/qos.py:54  
  message : Raise this exception or remove this useless statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZFEP0Hyi5a_X_62zTxy)  
---
  * file : ros2/rclpy/rclpy/test/test_action_server.py:405  
  message : Fix this attribute access on a value that can be 'None'.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiolQzCYfarq97IYE)  
---
  * file : ros2/rclpy/rclpy/test/test_executor.py:381  
  message : Remove this "break" statement from this "finally" block.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiohHzCYfarq97IWQ)  
---
  * file : ros2/rclpy/rclpy/test/test_node.py:1538  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYi-8w_ub2taBKNOD)  
---
  * file : ros2/rclpy/rclpy/test/test_node.py:1539  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYi-8w_ub2taBKNOE)  
---
  * file : ros2/rclpy/rclpy/test/test_parameter_client.py:77  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYi-Ow_ub2taBKNOB)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:81  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZPxVnaCmsyemdV_C1Mn)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:104  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXo)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:107  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXp)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:119  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXq)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:124  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXr)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:126  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXs)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:147  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXt)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:149  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXu)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:151  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXv)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:153  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXw)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:155  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXx)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:157  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IXy)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:166  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX2)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:168  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX3)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:170  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX4)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:172  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX5)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:195  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX9)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:197  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX-)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:199  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IX_)  
---
  * file : ros2/rclpy/rclpy/test/test_time.py:201  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiokpzCYfarq97IYA)  
---
  * file : ros2/rcpputils/include/rcpputils/scope_exit.hpp:29  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISir08zCYfarq97JF4)  
---
  * file : ros2/rcutils/src/error_handling_helpers.h:82  
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
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:64  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39k)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:71  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39l)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:77  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39m)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:82  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39n)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:94  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39o)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_daemon.py:100  
  message : Remove or refactor this statement; it has no side effects.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RM_kpZKJaqlJl39p)  
---
  * file : ros2/ros2cli/ros2cli/test/test_ros2cli_direct.py:48  
  message : Do not perform equality checks with floating point values.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYruYfNdw_ub2taBKNN2)  
---
  * file : ros2/ros2cli/ros2doctor/ros2doctor/api/network.py:54  
  message : Return a value of type `str` in this method.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj0mexBIBOiy31Qq8o)  
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
  * file : ros2/rosidl/rosidl_parser/test/test_parser.py:398  
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
  
## VULNERABILITIES #21 
<details><summary><a style='color:blue;font-size:18px;'>eProsima</a></summary>  

  * file : eProsima/Fast-DDS/include/fastrtps/utils/fixed_size_string.hpp:241  
  message : "memccpy" overflows read buffer "c_string"; passed size "MAX_CHARS" (255) exceeds buffer size (1)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-rzCYfarq97Ow0)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/fixed_size_string.hpp:241  
  message : "memccpy" overflows read buffer "c_string"; passed size "MAX_CHARS" (255) exceeds buffer size (6)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-rzCYfarq97Owz)  
---
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

  * file : navigation2/nav2_bringup/launch/cloned_multi_tb3_simulation_launch.py:180  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY__0Qc5MWueF4yM_B3g)  
---
  * file : navigation2/nav2_bringup/launch/tb3_simulation_launch.py:205  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY__0QdDMWueF4yM_B3h)  
---
  * file : navigation2/nav2_bringup/launch/tb4_simulation_launch.py:207  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY__0QczMWueF4yM_B3f)  
---
  * file : navigation2/nav2_bringup/launch/unique_multi_tb3_simulation_launch.py:138  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZBIAR3SMa3zLak3hqiX)  
---
  * file : navigation2/nav2_simple_commander/launch/assisted_teleop_example_launch.py:61  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj066eBIBOiy31Qq8x)  
---
  * file : navigation2/nav2_simple_commander/launch/follow_path_example_launch.py:60  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj064cBIBOiy31Qq8r)  
---
  * file : navigation2/nav2_simple_commander/launch/inspection_demo_launch.py:60  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj065IBIBOiy31Qq8t)  
---
  * file : navigation2/nav2_simple_commander/launch/nav_through_poses_example_launch.py:60  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj064yBIBOiy31Qq8s)  
---
  * file : navigation2/nav2_simple_commander/launch/nav_to_pose_example_launch.py:60  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj066IBIBOiy31Qq8w)  
---
  * file : navigation2/nav2_simple_commander/launch/picking_demo_launch.py:60  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj065dBIBOiy31Qq8u)  
---
  * file : navigation2/nav2_simple_commander/launch/recoveries_example_launch.py:60  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj065zBIBOiy31Qq8v)  
---
  * file : navigation2/nav2_simple_commander/launch/security_demo_launch.py:60  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj066zBIBOiy31Qq8y)  
---
  * file : navigation2/nav2_simple_commander/launch/waypoint_follower_example_launch.py:60  
  message : 'tempfile.mktemp' is insecure. Use 'tempfile.TemporaryFile' instead  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj064GBIBOiy31Qq8q)  
---
</details>  
  <details><summary><a style='color:blue;font-size:18px;'>ros2</a></summary>  

  * file : ros2/sros2/sros2/sros2/keystore/_permission.py:70  
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
  
## ISSUES (level blocker) #802 
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
  * file : eProsima/Fast-CDR/include/fastcdr/xcdr/optional.hpp:215  
  message : Ensure that the move assignment operator of "optional" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY6XV5oZLAV-oFEgTkla)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/builtin/typelookup/common/TypeLookupTypes.hpp:114  
  message : Ensure that the move constructor of "TypeLookup_getTypes_Result" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pP4Ew2X4EK9K44te)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/builtin/typelookup/common/TypeLookupTypes.hpp:120  
  message : Ensure that the move assignment operator of "TypeLookup_getTypes_Result" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pP4Ew2X4EK9K44tf)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/builtin/typelookup/common/TypeLookupTypes.hpp:248  
  message : Ensure that the move constructor of "TypeLookup_getTypeDependencies_Result" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pP4Ew2X4EK9K44tg)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/builtin/typelookup/common/TypeLookupTypes.hpp:254  
  message : Ensure that the move assignment operator of "TypeLookup_getTypeDependencies_Result" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pP4Ew2X4EK9K44th)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/builtin/typelookup/common/TypeLookupTypes.hpp:315  
  message : Ensure that the move constructor of "TypeLookup_Call" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pP4Ew2X4EK9K44ti)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/builtin/typelookup/common/TypeLookupTypes.hpp:321  
  message : Ensure that the move assignment operator of "TypeLookup_Call" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pP4Ew2X4EK9K44tj)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/builtin/typelookup/common/TypeLookupTypes.hpp:426  
  message : Ensure that the move constructor of "TypeLookup_Return" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pP4Ew2X4EK9K44tk)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/builtin/typelookup/common/TypeLookupTypes.hpp:432  
  message : Ensure that the move assignment operator of "TypeLookup_Return" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pP4Ew2X4EK9K44tl)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2339  
  message : Ensure that the move constructor of "TypeIdV1" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizIrzCYfarq97OYX)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2359  
  message : Ensure that the move assignment operator of "TypeIdV1" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizIrzCYfarq97OYY)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2451  
  message : Ensure that the move constructor of "TypeObjectV1" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizIrzCYfarq97OYd)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2471  
  message : Ensure that the move assignment operator of "TypeObjectV1" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizIrzCYfarq97OYe)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2568  
  message : Ensure that the move constructor of "TypeInformation" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizIrzCYfarq97OYk)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/core/policy/QosPolicies.hpp:2590  
  message : Ensure that the move assignment operator of "TypeInformation" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizIrzCYfarq97OYl)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/subscriber/qos/DataReaderQos.hpp:175  
  message : Make sure that moving an object of class "DataReaderQos" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY9vnBy5o-3NSYXl8BHO)  
---
  * file : eProsima/Fast-DDS/include/fastdds/dds/topic/TypeSupport.hpp:250  
  message : Remove the "virtual" specifier and refactor the code to not require polymorphism for comparison operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizOgzCYfarq97Obs)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/attributes/PropertyPolicy.h:44  
  message : Ensure that the move constructor of "PropertyPolicy" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY5zXGFAVSszh3Bos0Kh)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/attributes/PropertyPolicy.h:59  
  message : Ensure that the move assignment operator of "PropertyPolicy" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY5zXGFAVSszh3Bos0Ki)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/attributes/ServerAttributes.h:47  
  message : Make sure that moving an object of class "RemoteServerAttributes" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyydzCYfarq97ONW)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/BinaryProperty.h:42  
  message : Ensure that the move constructor of "BinaryProperty" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiysQzCYfarq97OId)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/BinaryProperty.h:63  
  message : Ensure that the move assignment operator of "BinaryProperty" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiysQzCYfarq97OIe)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/CDRMessage_t.h:132  
  message : Ensure that the move constructor of "CDRMessage_t" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiystzCYfarq97OJV)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/CDRMessage_t.h:151  
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
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Guid.h:39  
  message : Make sure that moving an object of class "GUID_t" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyxkzCYfarq97OM4)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Locator.h:103  
  message : Ensure that the move constructor of "Locator_t" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiysezCYfarq97OIw)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Locator.h:252  
  message : Use "operator==" to check object equality, "Locator_t" is not a trivially copyable type without padding.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiysezCYfarq97OI_)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorList.hpp:119  
  message : Ensure that the move constructor of "LocatorList" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyxVzCYfarq97OMj)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorList.hpp:134  
  message : Ensure that the move assignment operator of "LocatorList" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyxVzCYfarq97OMk)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorList.hpp:377  
  message : Ensure that the swap function is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyxVzCYfarq97OMz)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorSelectorEntry.hpp:38  
  message : Make sure that moving an object of class "LocatorSelectorEntry" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY7f680bVxLMsfMbnqZ9)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorSelectorEntry.hpp:43  
  message : Make sure that moving an object of class "EntryState" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY7f680bVxLMsfMbnqZ-)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorWithMask.hpp:35  
  message : Make sure that moving an object of class "LocatorWithMask" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYOb722oECTpe_WiKJPC)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorsIterator.hpp:47  
  message : Remove the "virtual" specifier and refactor the code to not require polymorphism for comparison operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyrzzCYfarq97OIO)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/LocatorsIterator.hpp:56  
  message : Remove the "virtual" specifier and refactor the code to not require polymorphism for comparison operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyrzzCYfarq97OIP)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Property.h:48  
  message : Ensure that the move constructor of "Property" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyuBzCYfarq97OKO)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Property.h:85  
  message : Ensure that the move assignment operator of "Property" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyuBzCYfarq97OKP)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/SampleIdentity.h:59  
  message : Ensure that the move constructor of "SampleIdentity" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiywqzCYfarq97OLz)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/SampleIdentity.h:80  
  message : Ensure that the move assignment operator of "SampleIdentity" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiywqzCYfarq97OL0)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Token.h:40  
  message : Ensure that the move constructor of "DataHolder" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyxyzCYfarq97OM9)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/Token.h:54  
  message : Ensure that the move assignment operator of "DataHolder" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyxyzCYfarq97OM-)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/common/WriteParams.h:33  
  message : Make sure that moving an object of class "WriteParams" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYlh3wciG85feRYr0mZ6)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/exceptions/Exception.h:80  
  message : Ensure that the move constructor of "Exception" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiy5JzCYfarq97OQg)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/exceptions/Exception.h:99  
  message : Ensure that the move assignment operator of "Exception" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiy5JzCYfarq97OQh)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/messages/RTPSMessageGroup.h:110  
  message : Ensure that destructor of "RTPSMessageGroup" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiy1zzCYfarq97OPc)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/reader/StatelessReader.h:263  
  message : Make sure that moving an object of class "RemoteWriterInfo_t" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiyrlzCYfarq97OIL)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/security/common/ParticipantGenericMessage.h:41  
  message : Ensure that the move constructor of "MessageIdentity" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiy_PzCYfarq97OSV)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/security/common/ParticipantGenericMessage.h:54  
  message : Ensure that the move assignment operator of "MessageIdentity" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiy_PzCYfarq97OSW)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/security/common/ParticipantGenericMessage.h:137  
  message : Ensure that the move constructor of "ParticipantGenericMessage" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiy_PzCYfarq97OSb)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/security/common/ParticipantGenericMessage.h:159  
  message : Ensure that the move assignment operator of "ParticipantGenericMessage" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiy_PzCYfarq97OSc)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/transport/SenderResource.h:76  
  message : Ensure that the move constructor of "SenderResource" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYb889hywhn1MW9k8YAd)  
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
  * file : eProsima/Fast-DDS/include/fastdds/rtps/writer/StatefulWriter.h:344  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiy7hzCYfarq97ORq)  
---
  * file : eProsima/Fast-DDS/include/fastdds/rtps/writer/StatefulWriter.h:477  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiy7hzCYfarq97ORs)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/AnnotationParameterValue.h:89  
  message : Ensure that the move constructor of "ExtendedAnnotationParameterValue" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrszCYfarq97Om5)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/AnnotationParameterValue.h:103  
  message : Ensure that the move assignment operator of "ExtendedAnnotationParameterValue" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrszCYfarq97Om6)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/AnnotationParameterValue.h:197  
  message : Ensure that the move constructor of "AnnotationParameterValue" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrszCYfarq97Om9)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/AnnotationParameterValue.h:211  
  message : Ensure that the move assignment operator of "AnnotationParameterValue" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrszCYfarq97Om-)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/AnnotationParameterValue.h:855  
  message : Ensure that the move constructor of "AppliedAnnotationParameter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrszCYfarq97OnL)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/AnnotationParameterValue.h:869  
  message : Ensure that the move assignment operator of "AppliedAnnotationParameter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrszCYfarq97OnM)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/AnnotationParameterValue.h:1067  
  message : Ensure that the move constructor of "AppliedAnnotation" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrszCYfarq97OnP)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/AnnotationParameterValue.h:1071  
  message : Ensure that the move assignment operator of "AppliedAnnotation" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrszCYfarq97OnQ)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/AnnotationParameterValue.h:1169  
  message : Ensure that the move constructor of "AppliedVerbatimAnnotation" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrszCYfarq97OnT)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/AnnotationParameterValue.h:1175  
  message : Ensure that the move assignment operator of "AppliedVerbatimAnnotation" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrszCYfarq97OnU)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/AnnotationParameterValue.h:1299  
  message : Ensure that the move constructor of "AppliedBuiltinMemberAnnotations" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrszCYfarq97OnW)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/AnnotationParameterValue.h:1305  
  message : Ensure that the move assignment operator of "AppliedBuiltinMemberAnnotations" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrszCYfarq97OnX)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifier.h:105  
  message : Ensure that the move constructor of "TypeIdentifier" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizsPzCYfarq97Ont)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifier.h:119  
  message : Ensure that the move assignment operator of "TypeIdentifier" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizsPzCYfarq97Onu)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:84  
  message : Ensure that the move constructor of "StringSTypeDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97OkV)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:98  
  message : Ensure that the move assignment operator of "StringSTypeDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97OkW)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:203  
  message : Ensure that the move constructor of "StringLTypeDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97OkY)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:217  
  message : Ensure that the move assignment operator of "StringLTypeDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97OkZ)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:322  
  message : Ensure that the move constructor of "PlainCollectionHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okb)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:336  
  message : Ensure that the move assignment operator of "PlainCollectionHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okc)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:466  
  message : Ensure that the move constructor of "PlainSequenceSElemDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Oke)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:480  
  message : Ensure that the move assignment operator of "PlainSequenceSElemDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okf)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:646  
  message : Ensure that the move constructor of "PlainSequenceLElemDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okh)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:660  
  message : Ensure that the move assignment operator of "PlainSequenceLElemDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Oki)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:826  
  message : Ensure that the move constructor of "PlainArraySElemDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okk)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:840  
  message : Ensure that the move assignment operator of "PlainArraySElemDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okl)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:1016  
  message : Ensure that the move constructor of "PlainArrayLElemDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okn)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:1030  
  message : Ensure that the move assignment operator of "PlainArrayLElemDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Oko)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:1206  
  message : Ensure that the move constructor of "PlainMapSTypeDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okq)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:1220  
  message : Ensure that the move assignment operator of "PlainMapSTypeDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okr)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:1441  
  message : Ensure that the move constructor of "PlainMapLTypeDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okt)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:1455  
  message : Ensure that the move assignment operator of "PlainMapLTypeDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Oku)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:1676  
  message : Ensure that the move constructor of "StronglyConnectedComponentId" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okw)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:1690  
  message : Ensure that the move assignment operator of "StronglyConnectedComponentId" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okx)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:1859  
  message : Ensure that the move constructor of "ExtendedTypeDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Okz)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:1866  
  message : Remove the "virtual" specifier; polymorphism should not be used with assignment operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Ok7)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:1873  
  message : Ensure that the move assignment operator of "ExtendedTypeDefn" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Ok0)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeIdentifierTypes.h:1873  
  message : Remove the "virtual" specifier; polymorphism should not be used with assignment operators.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizp1zCYfarq97Ok8)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:51  
  message : Ensure that the move constructor of "CommonStructMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OqZ)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:55  
  message : Ensure that the move assignment operator of "CommonStructMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqa)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:168  
  message : Ensure that the move constructor of "CompleteMemberDetail" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqd)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:172  
  message : Ensure that the move assignment operator of "CompleteMemberDetail" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqe)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:284  
  message : Ensure that the move constructor of "MinimalMemberDetail" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqg)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:288  
  message : Ensure that the move assignment operator of "MinimalMemberDetail" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqh)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:354  
  message : Ensure that the move constructor of "CompleteStructMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqj)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:358  
  message : Ensure that the move assignment operator of "CompleteStructMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqk)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:450  
  message : Ensure that the move constructor of "MinimalStructMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqn)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:454  
  message : Ensure that the move assignment operator of "MinimalStructMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqo)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:544  
  message : Ensure that the move constructor of "AppliedBuiltinTypeAnnotations" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqr)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:548  
  message : Ensure that the move assignment operator of "AppliedBuiltinTypeAnnotations" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqs)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:612  
  message : Ensure that the move constructor of "MinimalTypeDetail" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqu)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:616  
  message : Ensure that the move assignment operator of "MinimalTypeDetail" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqv)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:662  
  message : Ensure that the move constructor of "CompleteTypeDetail" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqy)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:666  
  message : Ensure that the move assignment operator of "CompleteTypeDetail" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oqz)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:776  
  message : Ensure that the move constructor of "CompleteStructHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oq1)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:780  
  message : Ensure that the move assignment operator of "CompleteStructHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oq2)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:867  
  message : Ensure that the move constructor of "MinimalStructHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oq4)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:871  
  message : Ensure that the move assignment operator of "MinimalStructHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oq5)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:960  
  message : Ensure that the move constructor of "CompleteStructType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oq7)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:964  
  message : Ensure that the move assignment operator of "CompleteStructType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oq8)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1076  
  message : Ensure that the move constructor of "MinimalStructType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oq-)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1080  
  message : Ensure that the move assignment operator of "MinimalStructType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oq_)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1199  
  message : Ensure that the move constructor of "CommonUnionMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrC)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1203  
  message : Ensure that the move assignment operator of "CommonUnionMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrD)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1338  
  message : Ensure that the move constructor of "CompleteUnionMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrG)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1342  
  message : Ensure that the move assignment operator of "CompleteUnionMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrH)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1434  
  message : Ensure that the move constructor of "MinimalUnionMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrK)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1438  
  message : Ensure that the move assignment operator of "MinimalUnionMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrL)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1529  
  message : Ensure that the move constructor of "CommonDiscriminatorMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrO)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1533  
  message : Ensure that the move assignment operator of "CommonDiscriminatorMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrP)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1623  
  message : Ensure that the move constructor of "CompleteDiscriminatorMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrR)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1627  
  message : Ensure that the move assignment operator of "CompleteDiscriminatorMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrS)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1738  
  message : Ensure that the move constructor of "MinimalDiscriminatorMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrU)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1742  
  message : Ensure that the move assignment operator of "MinimalDiscriminatorMember" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrV)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1806  
  message : Ensure that the move constructor of "CompleteUnionHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrX)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1810  
  message : Ensure that the move assignment operator of "CompleteUnionHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OrY)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1874  
  message : Ensure that the move constructor of "MinimalUnionHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ora)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1878  
  message : Ensure that the move assignment operator of "MinimalUnionHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Orb)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1945  
  message : Ensure that the move constructor of "CompleteUnionType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ord)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:1949  
  message : Ensure that the move assignment operator of "CompleteUnionType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ore)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2085  
  message : Ensure that the move constructor of "MinimalUnionType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Org)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2089  
  message : Ensure that the move assignment operator of "MinimalUnionType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Orh)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2224  
  message : Ensure that the move constructor of "CommonAnnotationParameter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Orj)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2228  
  message : Ensure that the move assignment operator of "CommonAnnotationParameter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ork)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2319  
  message : Ensure that the move constructor of "CompleteAnnotationParameter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Orm)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2323  
  message : Ensure that the move assignment operator of "CompleteAnnotationParameter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Orn)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2436  
  message : Ensure that the move constructor of "MinimalAnnotationParameter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Orq)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2440  
  message : Ensure that the move assignment operator of "MinimalAnnotationParameter" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Orr)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2552  
  message : Ensure that the move constructor of "CompleteAnnotationHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oru)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2556  
  message : Ensure that the move assignment operator of "CompleteAnnotationHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Orv)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2620  
  message : Ensure that the move constructor of "MinimalAnnotationHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Orx)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2624  
  message : Ensure that the move assignment operator of "MinimalAnnotationHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ory)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2670  
  message : Ensure that the move constructor of "CompleteAnnotationType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Or1)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2674  
  message : Ensure that the move assignment operator of "CompleteAnnotationType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Or2)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2785  
  message : Ensure that the move constructor of "MinimalAnnotationType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Or4)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2789  
  message : Ensure that the move assignment operator of "MinimalAnnotationType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Or5)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2901  
  message : Ensure that the move constructor of "CommonAliasBody" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Or7)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2905  
  message : Ensure that the move assignment operator of "CommonAliasBody" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Or8)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2993  
  message : Ensure that the move constructor of "CompleteAliasBody" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Or-)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:2997  
  message : Ensure that the move assignment operator of "CompleteAliasBody" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Or_)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3106  
  message : Ensure that the move constructor of "MinimalAliasBody" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsB)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3110  
  message : Ensure that the move assignment operator of "MinimalAliasBody" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsC)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3173  
  message : Ensure that the move constructor of "CompleteAliasHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsE)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3177  
  message : Ensure that the move assignment operator of "CompleteAliasHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsF)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3240  
  message : Ensure that the move constructor of "MinimalAliasHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsH)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3244  
  message : Ensure that the move assignment operator of "MinimalAliasHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsI)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3289  
  message : Ensure that the move constructor of "CompleteAliasType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsL)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3293  
  message : Ensure that the move assignment operator of "CompleteAliasType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsM)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3403  
  message : Ensure that the move constructor of "MinimalAliasType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsO)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3407  
  message : Ensure that the move assignment operator of "MinimalAliasType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsP)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3518  
  message : Ensure that the move constructor of "CompleteElementDetail" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsR)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3522  
  message : Ensure that the move assignment operator of "CompleteElementDetail" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsS)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3609  
  message : Ensure that the move constructor of "CommonCollectionElement" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsU)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3613  
  message : Ensure that the move assignment operator of "CommonCollectionElement" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsV)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3701  
  message : Ensure that the move constructor of "CompleteCollectionElement" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsX)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3705  
  message : Ensure that the move assignment operator of "CompleteCollectionElement" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OsY)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3792  
  message : Ensure that the move constructor of "MinimalCollectionElement" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osa)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3796  
  message : Ensure that the move assignment operator of "MinimalCollectionElement" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osb)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3860  
  message : Ensure that the move constructor of "CommonCollectionHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osd)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3864  
  message : Ensure that the move assignment operator of "CommonCollectionHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ose)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3929  
  message : Ensure that the move constructor of "CompleteCollectionHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osh)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:3933  
  message : Ensure that the move assignment operator of "CompleteCollectionHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osi)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4020  
  message : Ensure that the move constructor of "MinimalCollectionHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osk)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4024  
  message : Ensure that the move assignment operator of "MinimalCollectionHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osl)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4091  
  message : Ensure that the move constructor of "CompleteSequenceType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osn)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4095  
  message : Ensure that the move assignment operator of "CompleteSequenceType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oso)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4207  
  message : Ensure that the move constructor of "MinimalSequenceType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osq)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4211  
  message : Ensure that the move assignment operator of "MinimalSequenceType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osr)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4322  
  message : Ensure that the move constructor of "CommonArrayHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ost)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4326  
  message : Ensure that the move assignment operator of "CommonArrayHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osu)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4391  
  message : Ensure that the move constructor of "CompleteArrayHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osw)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4395  
  message : Ensure that the move assignment operator of "CompleteArrayHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osx)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4482  
  message : Ensure that the move constructor of "MinimalArrayHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Osz)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4486  
  message : Ensure that the move assignment operator of "MinimalArrayHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Os0)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4552  
  message : Ensure that the move constructor of "CompleteArrayType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Os2)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4556  
  message : Ensure that the move assignment operator of "CompleteArrayType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Os3)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4668  
  message : Ensure that the move constructor of "MinimalArrayType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Os5)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4672  
  message : Ensure that the move assignment operator of "MinimalArrayType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Os6)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4786  
  message : Ensure that the move constructor of "CompleteMapType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Os8)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4790  
  message : Ensure that the move assignment operator of "CompleteMapType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Os9)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4925  
  message : Ensure that the move constructor of "MinimalMapType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Os_)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:4929  
  message : Ensure that the move assignment operator of "MinimalMapType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtA)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5068  
  message : Ensure that the move constructor of "CommonEnumeratedLiteral" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtD)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5072  
  message : Ensure that the move assignment operator of "CommonEnumeratedLiteral" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtE)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5162  
  message : Ensure that the move constructor of "CompleteEnumeratedLiteral" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtH)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5166  
  message : Ensure that the move assignment operator of "CompleteEnumeratedLiteral" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtI)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5258  
  message : Ensure that the move constructor of "MinimalEnumeratedLiteral" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtL)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5262  
  message : Ensure that the move assignment operator of "MinimalEnumeratedLiteral" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtM)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5352  
  message : Ensure that the move constructor of "CommonEnumeratedHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtP)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5356  
  message : Ensure that the move assignment operator of "CommonEnumeratedHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtQ)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5421  
  message : Ensure that the move constructor of "CompleteEnumeratedHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtT)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5425  
  message : Ensure that the move assignment operator of "CompleteEnumeratedHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtU)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5512  
  message : Ensure that the move constructor of "MinimalEnumeratedHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtW)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5516  
  message : Ensure that the move assignment operator of "MinimalEnumeratedHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtX)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5583  
  message : Ensure that the move constructor of "CompleteEnumeratedType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OtZ)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5587  
  message : Ensure that the move assignment operator of "CompleteEnumeratedType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ota)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5699  
  message : Ensure that the move constructor of "MinimalEnumeratedType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Otc)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5703  
  message : Ensure that the move assignment operator of "MinimalEnumeratedType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Otd)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5816  
  message : Ensure that the move constructor of "CommonBitflag" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Otf)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5820  
  message : Ensure that the move assignment operator of "CommonBitflag" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Otg)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5908  
  message : Ensure that the move constructor of "CompleteBitflag" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Otj)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:5912  
  message : Ensure that the move assignment operator of "CompleteBitflag" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Otk)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6001  
  message : Ensure that the move constructor of "MinimalBitflag" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Otn)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6005  
  message : Ensure that the move assignment operator of "MinimalBitflag" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oto)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6095  
  message : Ensure that the move constructor of "CommonBitmaskHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Otr)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6099  
  message : Ensure that the move assignment operator of "CommonBitmaskHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ots)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6167  
  message : Ensure that the move constructor of "CompleteBitmaskType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Otx)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6171  
  message : Ensure that the move assignment operator of "CompleteBitmaskType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oty)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6283  
  message : Ensure that the move constructor of "MinimalBitmaskType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ot0)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6287  
  message : Ensure that the move assignment operator of "MinimalBitmaskType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ot1)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6401  
  message : Ensure that the move constructor of "CommonBitfield" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ot3)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6405  
  message : Ensure that the move assignment operator of "CommonBitfield" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ot4)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6539  
  message : Ensure that the move constructor of "CompleteBitfield" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ot9)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6543  
  message : Ensure that the move assignment operator of "CompleteBitfield" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ot-)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6632  
  message : Ensure that the move constructor of "MinimalBitfield" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuB)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6636  
  message : Ensure that the move assignment operator of "MinimalBitfield" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuC)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6724  
  message : Ensure that the move constructor of "CompleteBitsetHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuF)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6728  
  message : Ensure that the move assignment operator of "CompleteBitsetHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuG)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6815  
  message : Ensure that the move constructor of "MinimalBitsetHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuI)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6819  
  message : Ensure that the move assignment operator of "MinimalBitsetHeader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuJ)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6884  
  message : Ensure that the move constructor of "CompleteBitsetType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuL)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:6888  
  message : Ensure that the move assignment operator of "CompleteBitsetType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuM)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7000  
  message : Ensure that the move constructor of "MinimalBitsetType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuO)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7004  
  message : Ensure that the move assignment operator of "MinimalBitsetType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuP)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7118  
  message : Ensure that the move constructor of "CompleteExtendedType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuR)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7122  
  message : Ensure that the move assignment operator of "CompleteExtendedType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuS)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7166  
  message : Ensure that the move constructor of "MinimalExtendedType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuV)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7170  
  message : Ensure that the move assignment operator of "MinimalExtendedType" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuW)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7211  
  message : Ensure that the move constructor of "CompleteTypeObject" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97OuZ)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7215  
  message : Ensure that the move assignment operator of "CompleteTypeObject" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oua)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7325  
  message : Ensure that the move constructor of "MinimalTypeObject" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oud)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7329  
  message : Ensure that the move assignment operator of "MinimalTypeObject" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oue)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7455  
  message : Ensure that the move constructor of "TypeObject" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ouh)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7469  
  message : Ensure that the move assignment operator of "TypeObject" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oui)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7618  
  message : Ensure that the move constructor of "TypeIdentifierTypeObjectPair" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oum)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7622  
  message : Ensure that the move assignment operator of "TypeIdentifierTypeObjectPair" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Oun)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7704  
  message : Ensure that the move constructor of "TypeIdentifierPair" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ouq)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7708  
  message : Ensure that the move assignment operator of "TypeIdentifierPair" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Our)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7790  
  message : Ensure that the move constructor of "TypeIdentifierWithSize" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ouu)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7794  
  message : Ensure that the move assignment operator of "TypeIdentifierWithSize" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ouv)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7879  
  message : Ensure that the move constructor of "TypeIdentifierWithDependencies" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ouz)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7883  
  message : Ensure that the move assignment operator of "TypeIdentifierWithDependencies" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ou0)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7993  
  message : Ensure that the move constructor of "TypeInformation" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ou4)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObject.h:7997  
  message : Ensure that the move assignment operator of "TypeInformation" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizuIzCYfarq97Ou5)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObjectHashId.h:76  
  message : Ensure that the move constructor of "TypeObjectHashId" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pQT3w2X4EK9K44uC)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypeObjectHashId.h:90  
  message : Ensure that the move assignment operator of "TypeObjectHashId" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AY13pQT3w2X4EK9K44uD)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypesBase.h:353  
  message : Ensure that the move constructor of "MemberFlag" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrNzCYfarq97Ol9)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypesBase.h:366  
  message : Ensure that the move assignment operator of "MemberFlag" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrNzCYfarq97Ol-)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypesBase.h:517  
  message : Ensure that the move constructor of "TypeFlag" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrNzCYfarq97OmN)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/types/TypesBase.h:530  
  message : Ensure that the move assignment operator of "TypeFlag" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISizrNzCYfarq97OmO)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/IPFinder.h:56  
  message : Make sure that moving an object of class "info_IP" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0AczCYfarq97Ox7)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/ProxyPool.hpp:75  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxM)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/ProxyPool.hpp:88  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxO)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/ProxyPool.hpp:98  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxQ)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/ProxyPool.hpp:98  
  message : "std::move" shouldn't be called on a forwarding reference. Replace it with "std::forward".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz_kzCYfarq97OxR)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/RefCountedPointer.hpp:129  
  message : Ensure that the move constructor of "Instance" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZNhDBAKKI8rTADJ3tkM)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/RefCountedPointer.hpp:131  
  message : Ensure that the move assignment operator of "Instance" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZNhDBAKKI8rTADJ3tkN)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/TimeConversion.h:137  
  message : Replace "rand" with the facilities in random.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0AAzCYfarq97Oxg)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/TimeConversion.h:144  
  message : Replace "rand" with the facilities in random.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0AAzCYfarq97Oxj)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/TimeConversion.h:151  
  message : Replace "rand" with the facilities in random.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0AAzCYfarq97Oxm)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/fixed_size_string.hpp:241  
  message : "memccpy" overflows read buffer "c_string"; passed size "MAX_CHARS" (255) exceeds buffer size (1)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-rzCYfarq97Ow0)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/fixed_size_string.hpp:241  
  message : "memccpy" overflows read buffer "c_string"; passed size "MAX_CHARS" (255) exceeds buffer size (6)  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-rzCYfarq97Owz)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/shared_mutex.hpp:111  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owg)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/shared_mutex.hpp:152  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owe)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/shared_mutex.hpp:157  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owf)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/shared_mutex.hpp:198  
  message : Add a condition argument to this call to "wait".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYSYJ7bqjWNzjtTw5p02)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/shared_mutex.hpp:289  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYSYJ7bqjWNzjtTw5p05)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/shared_mutex.hpp:400  
  message : Ensure that the move constructor of "shared_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owh)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/utils/shared_mutex.hpp:408  
  message : Ensure that the move assignment operator of "shared_lock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiz-czCYfarq97Owi)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/xmlparser/XMLTree.h:139  
  message : Ensure that the move constructor of "DataNode" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0CvzCYfarq97O4p)  
---
  * file : eProsima/Fast-DDS/include/fastrtps/xmlparser/XMLTree.h:141  
  message : Ensure that the move assignment operator of "DataNode" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi0CvzCYfarq97O4q)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/subscriber/DataReaderImpl/SampleLoanManager.hpp:202  
  message : Ensure that the move constructor of "OutstandingLoanItem" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixB-zCYfarq97NHm)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastdds/subscriber/DataReaderImpl/SampleLoanManager.hpp:204  
  message : Ensure that the move assignment operator of "OutstandingLoanItem" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixB-zCYfarq97NHn)  
---
  * file : eProsima/Fast-DDS/src/cpp/fastrtps_deprecated/subscriber/SubscriberHistory.cpp:707  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw-PzCYfarq97M_P)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/data/ProxyHashTables.hpp:60  
  message : Ensure that the move constructor of "node_segregator" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwUvzCYfarq97LKO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/database/DiscoveryDataBase.hpp:92  
  message : Ensure that the move constructor of "AckedFunctor" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwM8zCYfarq97K66)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/builtin/discovery/database/DiscoveryParticipantChangeData.hpp:38  
  message : Make sure that moving an object of class "DiscoveryParticipantChangeData" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwNZzCYfarq97K7m)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:209  
  message : Ensure that destructor of "FlowControllerAsyncPublishMode" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MyI)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:261  
  message : Give class "FlowControllerSyncPublishMode" a noexcept destructor (for instance, make sure all subclasses have noexcept destructors).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MyP)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:275  
  message : Give class "FlowControllerLimitedAsyncPublishMode" a noexcept destructor (for instance, make sure all subclasses have noexcept destructors).  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MyR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:1364  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MzE)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/flowcontrol/FlowControllerImpl.hpp:1365  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwwkzCYfarq97MzF)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/history/TopicPayloadPool.hpp:270  
  message : Access of the field 'data' at negative byte offset -12  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RWTQpZKJaqlJl3_S)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/messages/RTPSMessageGroup.cpp:244  
  message : Ensure that destructor of "RTPSMessageGroup" is exception-free and declare it "noexcept"  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw0IzCYfarq97M08)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/network/ReceiverResource.h:94  
  message : Ensure that the move constructor of "ReceiverResource" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYJ7i3MlILU70yBX0vMT)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/participant/RTPSParticipantImpl.h:156  
  message : Ensure that the move constructor of "ReceiverControlBlock" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwWazCYfarq97LNp)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/reader/StatefulReader.cpp:1645  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwY5zCYfarq97LTD)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/ChannelResource.h:34  
  message : Ensure that the move constructor of "ChannelResource" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwFOzCYfarq97KxV)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/TCPv4Transport.cpp:241  
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
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemGlobal.hpp:68  
  message : Make sure that moving an object of class "BufferDescriptor" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYlh3tCyG85feRYr0mYd)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemLog.hpp:173  
  message : Make sure that moving an object of class "Pkt" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwCGzCYfarq97Kuj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemManager.hpp:684  
  message : Ensure that the move assignment operator of "Listener" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwAvzCYfarq97KtM)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemManager.hpp:719  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwAvzCYfarq97KtR)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/shared_mem/SharedMemManager.hpp:851  
  message : Ensure that the move assignment operator of "Port" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwAvzCYfarq97KtW)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/tcp/RTCPMessageManager.cpp:78  
  message : Memory copy function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv_EzCYfarq97Kpv)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/test_UDPv4Transport.cpp:332  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv_UzCYfarq97Kp-)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/test_UDPv4Transport.cpp:333  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv_UzCYfarq97Kp9)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/transport/test_UDPv4Transport.cpp:334  
  message : Remove any side effects from right hand operands of logical || operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv_UzCYfarq97Kp8)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/LivelinessManager.cpp:111  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw31zCYfarq97M4w)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.cpp:1722  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw4TzCYfarq97M6j)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/writer/StatefulWriter.cpp:1857  
  message : Replace "final" with another name.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiw4TzCYfarq97M6p)  
---
  * file : eProsima/Fast-DDS/src/cpp/statistics/rtps/messages/RTPSStatisticsMessages.hpp:207  
  message : Use constructors or assignment operators, "Locator_t" is not trivially copyable.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYYAjAHZv_hJbTx3eLSU)  
---
  * file : eProsima/Fast-DDS/src/cpp/utils/SystemInfo.cpp:143  
  message : Replace this call to the non reentrant function "getpwuid" by a call to "getpwuid_r".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISixfAzCYfarq97Ndb)  
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
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:3908  
  message : Make sure that moving an object of class "iteration_proxy_valuenlohmann::detail::iter_implconst nlohmann::basic_json" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97Khm)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:5416  
  message : Ensure that the move constructor of "json_sax_dom_parser" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97Kh5)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:5418  
  message : Ensure that the move assignment operator of "json_sax_dom_parser" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97Kh6)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:5591  
  message : Ensure that the move constructor of "json_sax_dom_callback_parser" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97Kh7)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:5593  
  message : Ensure that the move assignment operator of "json_sax_dom_callback_parser" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97Kh8)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:6070  
  message : Ensure that the move constructor of "lexer" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97KiK)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:6072  
  message : Ensure that the move assignment operator of "lexer" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97KiL)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7020  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97KiV)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7083  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97KiW)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7174  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97KiX)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7787  
  message : Ensure that the move constructor of "binary_reader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97Kib)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:7789  
  message : Ensure that the move assignment operator of "binary_reader" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97Kic)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:9920  
  message : "std::forward" should only be called on a forwarding reference.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9yzCYfarq97Kiu)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:10232  
  message : Make sure that moving an object of class "parsernlohmann::basic_json, nlohmann::detail::iterator_input_adapterconst char *" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9zzCYfarq97KjH)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:10232  
  message : Make sure that moving an object of class "parsernlohmann::basic_json, nlohmann::detail::input_stream_adapter" is "noexcept" (for instance, by ensuring that moving base classes and member data is "noexcept").  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9zzCYfarq97KnL)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:12633  
  message : Ensure that the move constructor of "json_ref" is exception-free and declare it "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9zzCYfarq97Kjb)  
---
  * file : eProsima/Fast-DDS/thirdparty/nlohmann-json/nlohmann/json.hpp:25310  
  message : The swap function should be unconditionally declared as "noexcept".  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiv9zzCYfarq97KnJ)  
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
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtBzCYfarq97MA7)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:76666  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvnO)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:76739  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvnQ)  
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
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJY)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:94495  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJZ)  
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
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIe)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95656  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIf)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95663  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIg)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95663  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIh)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95670  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIi)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95670  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIj)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95702  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIk)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:95702  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MIl)  
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
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MI0)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96120  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MI1)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96213  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MI4)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96213  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MI5)  
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
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJM)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:96266  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJN)  
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
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJS)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98212  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiwtDzCYfarq97MJT)  
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
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoi)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98495  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoj)  
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
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvok)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98585  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvol)  
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
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvom)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98759  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvon)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98768  
  message : This goto statement must be replaced by a standard iteration statement.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvoo)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:98768  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvop)  
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
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvot)  
---
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:102248  
  message : Remove this "goto" statement or rewrite it so that it jumps to a label that is located in the same scope or in an enclosing scope.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNaEA-kGpjXuvou)  
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
  message : Access of the field 'a' at negative byte offset -24  
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
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:163409  
  message : Access of the field 'a' at index 3, while it holds only 3 'struct WhereOrCost' elements  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZD8RW2dpZKJaqlJl3_3)  
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
  * file : eProsima/Fast-DDS/src/cpp/rtps/persistence/sqlite3.c:206640  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZRdaPNbEA-kGpjXuv0c)  
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
  * file : osrf/osrf_pycommon/tests/unit/test_cli_utils/test_common.py:32  
  message : Provide a value for field(s) with index 1.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISi40lzCYfarq97P2b)  
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
  * file : ros2/rcutils/src/cmdline_parser.c:40  
  message : Remove any side effects from right hand operands of logical && operator.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISirRUzCYfarq97I81)  
---
  * file : ros2/rcutils/src/error_handling_helpers.h:82  
  message : Memory copy function accesses out-of-bound array element  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZBIALZkMa3zLak3hqWD)  
---
  * file : ros2/rcutils/src/logging.c:476  
  message : Memory copy function overflows the destination buffer  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYqmAQdbWvNZCKI3y18h)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:389  
  message : Add 1 missing arguments; 'get_typed_value' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiniszCYfarq97IJ7)  
---
  * file : ros2/launch/launch/test/launch/utilities/test_type_utils.py:393  
  message : Add 1 missing arguments; 'get_typed_value' expects 2 positional arguments.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiniszCYfarq97IJ8)  
---
  * file : ros2/launch/launch_testing/launch_testing/legacy/__init__.py:265  
  message : Change or remove this string; "actions" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISinshzCYfarq97ILT)  
---
  * file : ros2/launch_ros/launch_ros/launch_ros/utilities/__init__.py:36  
  message : Change or remove this string; "evaluate_parameters_dict" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiq9CzCYfarq97Ix3)  
---
  * file : ros2/launch_ros/launch_ros/launch_ros/utilities/__init__.py:42  
  message : Change or remove this string; "normalize_parameters_dict" is not defined.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AYISiq9CzCYfarq97Ix4)  
---
  * file : ros2/ros2cli/ros2doctor/ros2doctor/api/network.py:54  
  message : Return a value of type `str` in this method.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZAj0mexBIBOiy31Qq8o)  
---
  * file : ros2/sros2/sros2/sros2/keystore/_permission.py:70  
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

  * file : ros2_control/ros2controlcli/ros2controlcli/verb/list_controllers.py:107  
  message : Refactor this method to not always return the same value.  
  [LINK](https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open=AZGwZD5kFFmecEscKaX_)  
---
</details>  
    
<br />  
  
