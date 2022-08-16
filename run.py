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
    return "  * file : " + el_in.path + ":" + el_in.line + "\n<br />" \
            + "message : " + check_tag(el_in.msg) + "\n<br />" \
            + "[LINK](" + base_bug_link + el_in.key + ")" + "\n<br />\n---\n<br />\n"

base_bug_link = "https://sonarcloud.io/project/issues?resolved=false&types=BUG&id=muttistefano_ros2_sonarcloud&open="

BUGS_list   = []
VULN_list   = []
ISSUES_list = []
PKGS_set    = set({})

token = "301e66ef00d908ca799a1c9352411a2c7a4bd6be"
headers = {'Authorization': f'Token {token}'}


issue_url  = 'https://sonarcloud.io/api/issues/search?s=FILE_LINE&resolved=false&types=CODE_SMELL&ps=100&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&p=10&additionalFields=_all'
response = requests.get(issue_url, headers=headers)
issues_len = response.json()['total']
print("issues len: ",issues_len)

bugs_url  = 'https://sonarcloud.io/api/issues/search?s=FILE_LINE&resolved=false&types=BUG&ps=100&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&p=1&additionalFields=_all'
response = requests.get(bugs_url, headers=headers)
bugs_len = response.json()['total']
print("bugs len: ",bugs_len)

vuln_url  = 'https://sonarcloud.io/api/issues/search?s=FILE_LINE&resolved=false&types=VULNERABILITY&ps=100&facets=severities%2CsonarsourceSecurity%2Ctypes&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all'
response = requests.get(vuln_url, headers=headers)
vuln_len = response.json()['total']
print("vuln len: ",vuln_len)


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
    PKGS_set.add(pkg)



PKGS_set = sorted(PKGS_set, key=str.lower)
print(PKGS_set)

f = open("test_readme.md", "w")
f.write("This repository uses github actions to build ROS2 rolling from source , plus other relevant packages, and performs static analysis using sonarcloud.")
f.write("<br />")
f.write("The results of the analysis can be found [here](https://sonarcloud.io/summary/overall?id=muttistefano_ros2_sonarcloud) .")
f.write("<br />")

    
    
    

for PK in PKGS_set:
    # f.write("<details><summary>" + str(PK) + "</summary>\n")
    f.write("<details><summary><a style='color:blue;font-size:18px;'>" + str(PK) + "</a></summary>\n")
      
    for BG in BUGS_list:
        # f.write("asd\n")
        if BG.pkg == PK:
            ret_str=entry_to_str(BG)
            f.write(ret_str)
    f.write("</details>")




f.close()


# print(len(ret_json_bugs.keys()))
# print(len(ret_json_bugs['issues']))
# print(len(ret_json_bugs['issues']))
# print("\n\n\n")
# print(ret_json_bugs['issues'][1])
# print(json.dumps(ret_json_bugs['issues'][0],sort_keys=True, indent=4))
# print("\n\n\n")
# print(json.dumps(ret_json_bugs['issues'][1],sort_keys=True, indent=4))
# print("\n\n\n")
# print(json.dumps(ret_json_bugs['issues'][2],sort_keys=True, indent=4))
# print("\n\n\n")
# print(json.dumps(ret_json_bugs['issues'][3],sort_keys=True, indent=4))
# print("\n\n\n")
# print(json.dumps(ret_json_bugs['issues'][4],sort_keys=True, indent=4))
# print("\n\n\n")
# print(json.dumps(ret_json_bugs['issues'][5],sort_keys=True, indent=4))
# print("\n\n\n")




