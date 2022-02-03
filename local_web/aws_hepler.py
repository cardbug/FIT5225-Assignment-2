import requests, json

# mZhLWUyMTYtNDc1YS1iYTRjLTJkOGU2YTc1MDNjZSIsImF1ZCI6IjU2M2c3ODcyZzJuZXJ1OG0zZnQ0aXRyaGpvIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjQzODY2NDE5LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV85RTFrcUQzSTciLCJjb2duaXRvOnVzZXJuYW1lIjoiYWEiLCJleHAiOjE2NDM4NzAwMTksImlhdCI6MTY0Mzg2NjQxOSwianRpIjoiZWM1MDVjMGUtMGVjZS00ZDE0LWExY2QtNWYxYzY1MDI5ZjJiIiwiZW1haWwiOiJ3bGl1MDA1NkBzdHVkZW50Lm1vbmFzaC5lZHUifQ.kZNdAAlNRSNgnJNq23kD3Hbcngk3bU66cN_dJyjFqks6P0BuhFOl8SpwOuoDKM_aNqZGsBmlfWuJI7qem209pv3-CTIqGZcJIc0KAX4dK5LbBMp8nZy0-XkXDgiCzJbNhe0i6OeINFKsR0OcXf_36h99aESx3MhU044r7m1l8dzOOa0_ONBATGkhc4jkiXz24Yi3mOn9IXlawByaV7Z5soH4x7VoDhU1g2V9SQBw8uCYSR-Zu4l679zSG1L2rkpF611QEta1DiDAyFDotLu334t4OWBfeSC85vMJNAEXU9WDewCzhb6T3uGYYsIlSxba4Hr-zOmBbX-_0-I5ZYdG2Q&access_token=eyJraWQiOiIyNEVubTZZT2E3enBJRzhpUjE4N2MyTEZzVVpPalFrSXlYUWRuYm56aFVnPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI1ZWYxN2JmYS1lMjE2LTQ3NWEtYmE0Yy0yZDhlNmE3NTAzY2UiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIiwiYXV0aF90aW1lIjoxNjQzODY2NDE5LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV85RTFrcUQzSTciLCJleHAiOjE2NDM4NzAwMTksImlhdCI6MTY0Mzg2NjQxOSwidmVyc2lvbiI6MiwianRpIjoiNjc4NDc0MGQtNzk1OC00NmIzLThiMGMtZmYzNTY0MzBlZjllIiwiY2xpZW50X2lkIjoiNTYzZzc4NzJnMm5lcnU4bTNmdDRpdHJoam8iLCJ1c2VybmFtZSI6ImFhIn0.TIEha1AgWLPnDm21207I6p7s9tckmQ4ezATzULZvc41fDz3oHDcwePRL83QZXgzC5BrKGVU5uFsX68I5i04Pq4-IpMJXFzgdkbJqueNPKc6B-hZJ0x_uCJqfW5Rw7ZW-dgMmNtACqgym6jkjn9pll7AlTaL-UBlOaAdEUZJw6Mu3BZYk2KfCGARuRkDhTOjm8MDOuw5iK6zUmDI-WSGUUJ_UTn9SFYq61wVXV7qX6RURqYzx2FQzcri4Z6apjUXr0a0DgTvICQ4gvjsvS63HFZ4wViC2L-CRNCM7F4gIH80pef5rpF1BEX47vWkpOkApHzDUTIoJ0OJNYyn2JrrEWg'
url = 'https://xubimlo3e2.execute-api.us-east-1.amazonaws.com/test1/search_image'

token = 'eyJraWQiOiJzSnhZVURUUGt6MEhWQm9HOGt5UUFyUW9nU0lmZkZLOWNYR0ROMG5jQ1hrPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoicTVVOUFVRDFfQTkwQkFBRV96TkNaQSIsInN1YiI6IjVlZjE3YmZhLWUyMTYtNDc1YS1iYTRjLTJkOGU2YTc1MDNjZSIsImF1ZCI6IjU2M2c3ODcyZzJuZXJ1OG0zZnQ0aXRyaGpvIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjQzODcxNzEzLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV85RTFrcUQzSTciLCJjb2duaXRvOnVzZXJuYW1lIjoiYWEiLCJleHAiOjE2NDM5NTgxMTMsImlhdCI6MTY0Mzg3MTcxNCwianRpIjoiYjU0NDlmZjQtNzg3OC00NjVlLWI0MjQtYWM1YTdlYTg5ZGZkIiwiZW1haWwiOiJ3bGl1MDA1NkBzdHVkZW50Lm1vbmFzaC5lZHUifQ.A6-VKe01kSXWffuZAjv2UbJeRl04ip8lt62u7DdwKyaUXs3y4DhbeOXKZSeDTom7Bx1yY2ek2OWtQLChbu0LKLjfwtZmnaXnZRqYY59jQutH4Gvjz9qQ0r2C7wXD7OjjPHLm3GS4hfQ52-N2dkOvax4wBL1ebP8gu3UvtElobpKtOXY0bDc7_fyORD08LSfYIylNumyiUwZqwEmzWquTol-BXiQYBNahcRA5pqvivoF_tnk22VoumVv_WUIqgjb54B94qhb2drMPdmOisUM37142NEOwgN_T8SqQ3Au9yIY2LW5H8UvBSbr_zzzmyWFLLnR4nSZpRPIxYnrbs-bIww'
headers = {'Authorization': 'Bearer %s' % (token), 'Content-Type': 'text/plain'}


def upload_aws_image(name, base64file):
    url = 'https://xubimlo3e2.execute-api.us-east-1.amazonaws.com/test1/image_upload'
    playload = {"name": name, "file": base64file}
    response = requests.request("POST", url, headers=headers, data=json.dumps(playload))
    return response


# 根据tag搜索
def search_image_by_tag(tag_list):
    url = 'https://xubimlo3e2.execute-api.us-east-1.amazonaws.com/test1/search_image'
    playload = {"tags": tag_list, "httpMethod": "POST"}
    headers = {'Authorization': 'Bearer %s' % (token), 'Content-Type': 'text/plain'}
    response = requests.request("POST", url, headers=headers, data=json.dumps(playload))
    return response


def search_image_by_image(name, filebase64):
    url = 'https://xubimlo3e2.execute-api.us-east-1.amazonaws.com/test1/search_image_by_image'
    playload = {"httpMethod": "POST", "name": name, "file": filebase64}
    headers = {'Authorization': 'Bearer %s' % (token)}
    response = requests.request("POST", url, headers=headers, data=json.dumps(playload))
    return response.json()


# 删除图片
def delete_img_by_name(imgname):
    url = 'https://xubimlo3e2.execute-api.us-east-1.amazonaws.com/test1/delete_image'
    playload = {"url": 'https://fit5225ass.s3.amazonaws.com/images/%s' % (imgname)}
    headers = {'Authorization': 'Bearer %s' % (token)}
    response = requests.request("POST", url, headers=headers, data=json.dumps(playload))
    return response.json()


def delete_tags_by_tag(name, tag):
    tags=[]
    tags.append(tag)
    url = 'https://xubimlo3e2.execute-api.us-east-1.amazonaws.com/test1/delete_tags'
    playload = {"url": 'https://fit5225ass.s3.amazonaws.com/images/%s' % (name),'tags':tags,"httpMethod":"POST" }
    headers = {'Authorization': 'Bearer %s' % (token)}
    response = requests.request("POST", url, headers=headers, data=json.dumps(playload))
    return response.json()
