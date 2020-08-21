import requests
import json
import users_list

jiraSession = requests.Session()

login = 'admin'
password = 'admin'
baseURL = 'http://192.168.56.101:8080'

project = 'KEK'
role = '10100' #  10001 - Developers; 10000 - Users
users = users_list.users


def ft_create():
    for i in users:
        body = json.dumps({
            "user": [i]
        })
        response = jiraSession.request(
            "POST",
            baseURL + '/rest/api/2/project/' + project + '/role/' + role,
            data=body,
            headers={'content-type': 'application/json; charset=UTF-8'}
        )
        if response.status_code != 200:
            print(i, response.status_code, sep=" -> ")


try:
    jiraSession.post(baseURL + '/rest/auth/1/session', auth=(login, password))
    ft_create()
except:
    print("Please check connection / Login Details")


#   curl -D- -u admin:admin -H "Content-Type:application/json" -X POST -d '{"user":["admin"]}' -k http://192.168.56.101:8080/rest/api/2/project/KEK/role/10100
