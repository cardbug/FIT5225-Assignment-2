from django.shortcuts import render
from picture.AccountForm import LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.utils import timezone
# Create your views here.
import os, time, hashlib
from django.conf import settings
from picture.models import FileInfo
from aws_hepler import upload_aws_image,search_image_by_tag,delete_img_by_name,search_image_by_image,delete_tags_by_tag
#from pure_pagination import Paginator, PageNotAnInteger
from django.db.models import Q
import base64

def get_md5():
    time_now = timezone.now()
    m = hashlib.md5()
    m.update(str(time_now).encode())
    return m.hexdigest()


# 用户登录
def login(request):
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html', {"login_form": login_form})
    else:
        login_form = LoginForm(request.POST)
        status = False
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                status = True
                auth_login(request, user)
                return JsonResponse({"status": status})
            else:
                login_form.add_error("password", "密码错误")
        return JsonResponse({"res": login_form.errors.as_json(), "status": status})


# 首页
def index(request):
    return render(request, 'index.html')


import base64


def upload_image(request):
    if request.method == "POST":
        image = request.FILES.get('file')
        ext = os.path.splitext(image.name)[1]
        timestrap = time.strftime('%Y%m%d', time.gmtime())
        md5_pwd = get_md5()
        NewFileName = "%s$$%s%s" % (image.name, md5_pwd, ext)
        image_byte = image.read()
        image_base64 = str(base64.b64encode(image_byte))[2:]
        response = upload_aws_image(image.name, image_base64)

        request.session["bs"]=image_base64
        if response.status_code == 200:
            res = {
                "code": 0,
                "msg": 'Uploaded',
                "data": {
                    "src": "/" + os.path.join("static", "uploads", timestrap, NewFileName).replace("\\", "/"),
                    "name": image.name,
                    "base64":image_base64
                }
            }
        else:
            res = {
                "code": 400,
                "msg": 'Failed',
            }

        return JsonResponse(res)

    return render(request, 'upload_image.html')


def edit_tag(request):
    res = {"code": 200, "msg": "sucess"}
    try:
        id = request.POST.get("id")
        fileinfo = FileInfo.objects.get(id=id)
        tags = request.POST.get("tag")
        fileinfo.tags = tags
        fileinfo.save()
    except:
        res["code"] = 500
        res["msg"] = "Failed"
    return JsonResponse(res)
import json

def image_list(request):
    q = request.GET.get("q")
    name=request.GET.get('name')
   
    image_lists = []
    if name is not None  and name !=""  :
        res=search_image_by_image(name, request.session.get("bs"))

        body = json.loads(res["body"])
        if len(body):
            for item in body:
                if item['tags']:
                    tags = item["tags"]
                else:
                    tags = []
                image_lists.append({
                    "name":os.path.basename(item["id"]),
                    "tags":tags
                })
    else:
        tag_list=[]
        if q !="" and q is not None:
            tag_list.append(q)
        res=search_image_by_tag(tag_list)
        if res.status_code==200:

            links=json.loads(res.json()["body"])["links"]
            if len(links):
                for item in links:
                    if item['tags']:
                        tags=item["tags"]
                    else:
                        tags=[]
                    image_lists.append({
                        "name": os.path.basename(item["id"]),
                        "tags": tags
                    })

        else:
            pass

    if q is None:
        q=""


    return render(request, 'img_list.html', {"img_list": image_lists, "q": q})

#删除图像
def delete_img(request):
    res = {"code": 200, "msg": "sucess"}
    if request.method == "POST":
        try:
            imagename = request.POST.get("imagename")
            result=delete_img_by_name(imagename)
            if "errorMessage" in result:
                res["msg"] = "Delete failed"
                res["code"] = 500
                return JsonResponse(res)
            return JsonResponse(res)
        except:
            res["msg"] = "Delete failed"
            res["code"] = 500
            return JsonResponse(res)


def delete_tag(request):
    res={"code":200,"msg":"sucess"}
    name=request.POST.get("name")
    tag=request.POST.get("tag")
    result=delete_tags_by_tag(name,tag)

    return JsonResponse(res)










