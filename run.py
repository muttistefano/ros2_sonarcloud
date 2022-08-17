import json
import requests
import os
import sys
import math
from dataclasses import dataclass

@dataclass
class BUG_entry:
    key:  str
    pkg:  str
    msg:  str
    line: str
    path: str

def check_tag(str_in):
    str_out = str_in.replace("<","")
    str_out = str_out.replace(">","")
    return str_out

# def entry_to_str(el_in):
#     return "<h4>file : " + el_in.path + ":" + el_in.line + "</h4>\n<br />" \
#             + "<h4>message : " + check_tag(el_in.msg) + "</h4>\n<br />" \
#             + "<h4>[LINK](" + base_bug_link + el_in.key + ")" + "</h4>\n<br />"

def entry_to_str(el_in):
    return "  * file : " + el_in.path + ":" + el_in.line + "  \n  " \
            + "message : " + check_tag(el_in.msg) + "  \n  " \
            + "[LINK](" + base_bug_link + el_in.key + ")" + "  \n  \n---\n  \n"

base_bug_link = "https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open="

BUGS_list       = []
VULN_list       = []
ISSUES_BLOCKER_list      = []
ISSUES_CRITICAL_list     = []
PKGS_set_bugs   = set({})
PKGS_set_vuln   = set({})
PKGS_set_issue_blocker   = set({})
PKGS_set_issue_critical  = set({})

token = "301e66ef00d908ca799a1c9352411a2c7a4bd6be"
headers = {'Authorization': f'Token {token}'}


issue_url  = 'https://sonarcloud.io/api/issues/search?s=FILE_LINE&resolved=false&types=CODE_SMELL&ps=100&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&p=1&additionalFields=_all'
response = requests.get(issue_url, headers=headers)
issues_len = response.json()['total']
print("issues len: ",issues_len)

bugs_url  = 'https://sonarcloud.io/api/issues/search?s=FILE_LINE&resolved=false&types=BUG&ps=100&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&p=1&additionalFields=_all'
response = requests.get(bugs_url, headers=headers)
bugs_len = response.json()['total']
print("bugs len: ",bugs_len)

vuln_url  = 'https://sonarcloud.io/api/issues/search?s=FILE_LINE&resolved=false&types=VULNERABILITY&ps=100&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&p=1&additionalFields=_all'
response = requests.get(vuln_url, headers=headers)
vuln_len = response.json()['total']
print("vuln len: ",vuln_len)


path_iss = "https://sonarcloud.io/api/issues/search?s=FILE_LINE&languages=cpp&resolved=false&severities=BLOCKER&ps=100&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all"
response = requests.get(path_iss, headers=headers)
iss_cpp_blocker_len = response.json()['total']
print("iss_cpp_crit_len len: ",iss_cpp_blocker_len)

path_iss = "https://sonarcloud.io/api/issues/search?s=FILE_LINE&languages=cpp&resolved=false&severities=CRITICAL&ps=100&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all"
response = requests.get(path_iss, headers=headers)
iss_cpp_crit_len = response.json()['total']
print("iss_cpp_crit_len len: ",iss_cpp_crit_len)

path_iss = "https://sonarcloud.io/api/issues/search?s=FILE_LINE&languages=c&resolved=false&severities=BLOCKER&ps=100&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all"
response = requests.get(path_iss, headers=headers)
iss_c_blocker_len = response.json()['total']
print("iss_c_crit_len len: ",iss_c_blocker_len)

path_iss = "https://sonarcloud.io/api/issues/search?s=FILE_LINE&languages=c&resolved=false&severities=CRITICAL&ps=100&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all"
response = requests.get(path_iss, headers=headers)
iss_c_crit_len = response.json()['total']
print("iss_c_crit_len len: ",iss_c_crit_len)

path_iss = "https://sonarcloud.io/api/issues/search?s=FILE_LINE&languages=py&resolved=false&severities=BLOCKER&ps=100&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all"
response = requests.get(path_iss, headers=headers)
iss_py_blocker_len = response.json()['total']
print("iss_py_crit_len len: ",iss_py_blocker_len)

path_iss = "https://sonarcloud.io/api/issues/search?s=FILE_LINE&languages=py&resolved=false&severities=CRITICAL&ps=100&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all"
response = requests.get(path_iss, headers=headers)
iss_py_crit_len = response.json()['total']
print("iss_py_crit_len len: ",iss_py_crit_len)





#region BUGS RETRIEVAL

#TODO take care of the case in which BUGS>500 -> merge dicts
bugs_dict = {}

bugs_cnt_tot = math.ceil(bugs_len/500) + 1

for bugs_cnt in range(1,bugs_cnt_tot):

    bugs_url  = 'https://sonarcloud.io/api/issues/search?s=FILE_LINE&resolved=false&types=BUG&ps=500&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&p='+str(bugs_cnt)+'&additionalFields=_all'
    response = requests.get(bugs_url, headers=headers)
    ret_json_bugs = response.json()


for elem in ret_json_bugs['issues']:
    pkg = elem['component'].split("/")[1]
    if pkg=="ros2_sonarcloud":
        pkg = elem['component'].split("/")[2]
    
    BUGS_list.append(BUG_entry(elem['key'],pkg,elem['message'],str(elem['line']),elem['component'][33:]))
    PKGS_set_bugs.add(pkg)

PKGS_set_bugs = sorted(PKGS_set_bugs, key=str.lower)


#endregion


#region vuln RETRIEVAL

vuln_dict = {}

vuln_cnt_tot = math.ceil(vuln_len/500) + 1

for vuln_cnt in range(1,vuln_cnt_tot):

    vuln_url  = 'https://sonarcloud.io/api/issues/search?s=FILE_LINE&resolved=false&types=VULNERABILITY&ps=500&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&p='+str(bugs_cnt)+'&additionalFields=_all'
    response = requests.get(vuln_url, headers=headers)
    ret_json_vuln = response.json()


for elem in ret_json_vuln['issues']:
    pkg = elem['component'].split("/")[1]
    if pkg=="ros2_sonarcloud":
        pkg = elem['component'].split("/")[2]
    
    VULN_list.append(BUG_entry(elem['key'],pkg,elem['message'],str(elem['line']),elem['component'][33:]))
    PKGS_set_vuln.add(pkg)

PKGS_set_vuln = sorted(PKGS_set_vuln, key=str.lower)


#endregion


#region blocker issues RETRIEVAL

blocker_issues_dict_list = []

idx = math.ceil(iss_cpp_blocker_len/500) + 1

for counter in range(1,idx):
    iss_url   = "https://sonarcloud.io/api/issues/search?s=FILE_LINE&languages=cpp&resolved=false&severities=BLOCKER&ps=500&p="+str(bugs_cnt)+"&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all"
    response = requests.get(iss_url, headers=headers)
    blocker_issues_dict_list.append(response.json())

idx = math.ceil(iss_c_blocker_len/500) + 1

for counter in range(1,idx):
    iss_url   = "https://sonarcloud.io/api/issues/search?s=FILE_LINE&languages=c&resolved=false&severities=BLOCKER&ps=500&p="+str(bugs_cnt)+"&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all"
    response = requests.get(iss_url, headers=headers)
    blocker_issues_dict_list.append(response.json())
    
idx = math.ceil(iss_py_blocker_len/500) + 1

for counter in range(1,idx):
    iss_url   = "https://sonarcloud.io/api/issues/search?s=FILE_LINE&languages=py&resolved=false&severities=BLOCKER&ps=500&p="+str(bugs_cnt)+"&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all"
    response = requests.get(iss_url, headers=headers)
    blocker_issues_dict_list.append(response.json())
    

for ret in blocker_issues_dict_list:
    for elem in ret['issues']:
        pkg = elem['component'].split("/")[1]
        if pkg=="ros2_sonarcloud":
            pkg = elem['component'].split("/")[2]
        
        ISSUES_BLOCKER_list.append(BUG_entry(elem['key'],pkg,elem['message'],str(elem['line']),elem['component'][33:]))
        PKGS_set_issue_blocker.add(pkg)

PKGS_set_issue_blocker = sorted(PKGS_set_issue_blocker, key=str.lower)

#endregion


#region critical issues RETRIEVAL

critical_issues_dict_list = []

idx = math.ceil(iss_cpp_crit_len/500) + 1

for counter in range(1,idx):
    iss_url   = "https://sonarcloud.io/api/issues/search?s=FILE_LINE&languages=cpp&resolved=false&severities=CRITICAL&ps=500&p="+str(bugs_cnt)+"&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all"
    response = requests.get(iss_url, headers=headers)
    critical_issues_dict_list.append(response.json())

idx = math.ceil(iss_c_crit_len/500) + 1

for counter in range(1,idx):
    iss_url   = "https://sonarcloud.io/api/issues/search?s=FILE_LINE&languages=c&resolved=false&severities=CRITICAL&ps=500&p="+str(bugs_cnt)+"&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all"
    response = requests.get(iss_url, headers=headers)
    critical_issues_dict_list.append(response.json())
    
idx = math.ceil(iss_py_crit_len/500) + 1

for counter in range(1,idx):
    iss_url   = "https://sonarcloud.io/api/issues/search?s=FILE_LINE&languages=py&resolved=false&severities=CRITICAL&ps=500&p="+str(bugs_cnt)+"&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all"
    response = requests.get(iss_url, headers=headers)
    critical_issues_dict_list.append(response.json())
    

for ret in critical_issues_dict_list:
    for elem in ret['issues']:
        pkg = elem['component'].split("/")[1]
        if pkg=="ros2_sonarcloud":
            pkg = elem['component'].split("/")[2]
        
        ISSUES_CRITICAL_list.append(BUG_entry(elem['key'],pkg,elem['message'],str(elem['line']),elem['component'][33:]))
        PKGS_set_issue_critical.add(pkg)

PKGS_set_issue_critical = sorted(PKGS_set_issue_critical, key=str.lower)

#endregion





###README WRITING

f = open("README.md", "w")
f.write("# ROS2_SONARCLOUD  \n")
f.write("This repository uses github actions to build ROS2 rolling from source ,plus other relevant packages, and performs static analysis using sonarcloud tools.")
f.write("  \n")
f.write("Extracted bugs, vulnerabilities and code smells are listed below in this document, grouped by package.  \n")
f.write("Each entry is formed by a file:line and message, with a link to the specific sonacloud link.  \n")
f.write("This page is generated automatically after every static analysys.  \n")
f.write("The complete results of the analysis can be found [here](https://sonarcloud.io/summary/overall?id=muttistefano_ros2_sonarcloud) .")
f.write("  \n")

    
f.write("  \n")
f.write("<br />  \n")    
f.write("  \n")
f.write("## BUGS #" + str(bugs_len) + " \n")

for PK in PKGS_set_bugs:
    f.write("<details><summary><a style='color:blue;font-size:18px;'>" + str(PK) + "</a></summary>  \n\n")
      
    for BG in BUGS_list:
        # f.write("asd\n")
        if BG.pkg == PK:
            ret_str=entry_to_str(BG)
            f.write(ret_str)
    f.write("</details>  \n")


f.write("  \n")
f.write("<br />  \n")
f.write("  \n")
f.write("## VULNERABILITIES #" + str(vuln_len) + " \n")

for PK in PKGS_set_vuln:
    f.write("<details><summary><a style='color:blue;font-size:18px;'>" + str(PK) + "</a></summary>  \n\n")
      
    for BG in VULN_list:
        # f.write("asd\n")
        if BG.pkg == PK:
            ret_str=entry_to_str(BG)
            f.write(ret_str)
    f.write("</details>  \n  ")


f.write("  \n")
f.write("<br />  \n")
f.write("  \n")
f.write("## ISSUES are filtered and only blocking and critical issues are reported due to the high quantity of issues  \n")
f.write("The complete list of issues can be found [here](https://sonarcloud.io/summary/overall?id=muttistefano_ros2_sonarcloud) .")



f.write("  \n")
f.write("<br />  \n")
f.write("  \n")
f.write("## ISSUES (level blocker) #" + str(iss_c_blocker_len+iss_cpp_blocker_len+iss_py_blocker_len) + " \n")

for PK in PKGS_set_issue_blocker:
    f.write("<details><summary><a style='color:blue;font-size:18px;'>" + str(PK) + "</a></summary>  \n\n")
      
    for BG in ISSUES_BLOCKER_list:
        # f.write("asd\n")
        if BG.pkg == PK:
            ret_str=entry_to_str(BG)
            f.write(ret_str)
    f.write("</details>  \n  ")


f.write("  \n")
f.write("<br />  \n")
f.write("  \n")
f.write("## ISSUES (level critical) #" + str(iss_c_crit_len+iss_cpp_crit_len+iss_py_crit_len) + " \n")

for PK in PKGS_set_issue_critical:
    f.write("<details><summary><a style='color:blue;font-size:18px;'>" + str(PK) + "</a></summary>  \n\n")
      
    for BG in ISSUES_CRITICAL_list:
        # f.write("asd\n")
        if BG.pkg == PK:
            ret_str=entry_to_str(BG)
            f.write(ret_str)
    f.write("</details>  \n  ")



f.close()


