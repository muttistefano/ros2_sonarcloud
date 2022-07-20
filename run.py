# import requests
import json

# issue_url = 'https://sonarcloud.io/api/issues/search?s=FILE_LINE&resolved=false&types=CODE_SMELL&ps=100&facets=severities%2CsonarsourceSecurity%2Ctypes&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all'
# bugs_url  = 'https://sonarcloud.io/api/issues/search?s=FILE_LINE&resolved=false&types=BUG&ps=100&facets=severities%2CsonarsourceSecurity%2Ctypes&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all'
# vuln_url  = 'https://sonarcloud.io/api/issues/search?s=FILE_LINE&resolved=false&types=VULNERABILITY&ps=100&facets=severities%2CsonarsourceSecurity%2Ctypes&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all'
# token = '301e66ef00d908ca799a1c9352411a2c7a4bd6be'

# session = requests.Session()
# session.auth = token, ''
# call = getattr(session, 'get')
# res = call(issue_url)

# # print(res.json())
# print(json.dumps(res.json(), indent=4, sort_keys=True))

import requests
import os

# token = os.environ.get('NAUTOBOT_TOKEN')
token = "301e66ef00d908ca799a1c9352411a2c7a4bd6be"

headers = {'Authorization': f'Token {token}'}

issue_url = 'https://sonarcloud.io/api/issues/search?s=FILE_LINE&resolved=false&types=CODE_SMELL&ps=5&facets=severities%2CsonarsourceSecurity%2Ctypes&componentKeys=muttistefano_ros2_sonarcloud&organization=muttistefano&additionalFields=_all'

# Get the list of devices from Nautobot using the requests module and passing in the authorization header defined above
response = requests.get(issue_url, headers=headers)
print(json.dumps(response.json(), indent=4, sort_keys=True))

