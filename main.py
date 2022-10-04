import requests

website_2 = "https://jsonplaceholder.typicode.com/comments/108"
print(requests.get(website_2).json())
response_2 = requests.put(website_2,
                        data={
                            "id":108,
                            'postId':2,
                            "name":'malets',
                            "email":"mail@mail.by",
                            "body":"my body",
                        }
                        )
print(response_2.json())

# headers = {
#     "User-Agent": "malets"
# }
# # response = requests.get("https://httpbin.org/get", headers=headers, params={'a':'b'})
#
# response = requests.post("https://httpbin.org/post",
#                          headers=headers,
#                          params={'a':'b'},
#                          json={'username': 'supersecret'}
#                          )
#
#
#
#
# # if response.status_code == 200:
# #     print ('OK')
# print(response.text)
# print (response.json())

website = "https://jsonplaceholder.typicode.com/posts/99"
print(requests.get(website).json())

response = requests.put(website,
                        data={
                            "id":99,
                            'userId':108,
                            "title":'malets',
                            "body":"body for my post",
                        }
                        )
# print(response.status_code)
print(response.json())