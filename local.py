# import requests
# res = requests.get("http://127.0.0.1:3000/api/courses")
# print(res.json())

# import requests
# res = requests.post("http://127.0.0.1:3000/api/courses/1")
# print(res.json())

# import requests
# res = requests.delete("http://127.0.0.1:3000/api/courses/1")
# print(res.json())

# import requests
# res = requests.post("http://127.0.0.1:3000/api/courses/3", json={"name": "Golang", "videos": 5})
# res = requests.post("http://127.0.0.1:3000/api/courses/4", json={"name": "PHP", "videos": 15})
# print(res.json())

import requests
res = requests.put("http://127.0.0.1:3000/api/courses/2", json={"name": "Golang", "videos": 5})
print(res.json())