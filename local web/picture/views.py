from django.shortcuts import render
from picture.AccountForm import LoginForm
from django.contrib.auth import  authenticate, login as auth_login
from django.http import JsonResponse
from django.utils import timezone
# Create your views here.
import os,time,hashlib
from django.conf import settings
from picture.models import FileInfo
from object_detection import get_tags
from pure_pagination import Paginator, PageNotAnInteger
from django.db.models import Q
def get_md5():
    time_now=timezone.now()
    m=hashlib.md5()
    m.update(str(time_now).encode())
    return  m.hexdigest()
#用户登录
def login(request):
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html',{"login_form":login_form})
    else:
        login_form = LoginForm(request.POST)
        status = False
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                status=True
                auth_login(request, user)
                return JsonResponse({"status": status})
            else:
                login_form.add_error("password", "密码错误")
        return JsonResponse({"res": login_form.errors.as_json(), "status": status})

#首页
def index(request):
    return render(request,'index.html')

def upload_image(request):
    if request.method=="POST":
        try:
            s = request.FILES.get('file')
            ext = os.path.splitext(s.name)[1]
            timestrap = time.strftime('%Y%m%d', time.gmtime())
            md5_pwd = get_md5()
            NewFileName = "%s$$%s%s" % (s.name, md5_pwd, ext)
            file_save_path = os.path.join(settings.BASE_DIR, "static", "uploads", timestrap)
            if not os.path.exists(file_save_path):
                os.mkdir(file_save_path)
            with open(os.path.join(file_save_path, NewFileName), 'wb') as f:
                for i in s.chunks():
                    f.write(i)
            tags=get_tags(os.path.join(file_save_path, NewFileName))
            FileInfo.objects.create(
                filename=s.name,
                md5_name=os.path.join(file_save_path,NewFileName),
                user=request.user,
                tags=tags
            )
            res = {
                "code": 0,
                "msg": '上传成功',
                "data": {
                    "src": "/" + os.path.join("static", "uploads", timestrap, NewFileName).replace("\\", "/"),
                    "title": s.name,
                    "tags":tags
                }
            }
        except:
            res = {
                "code": 1,
                "msg": '上传失败',
            }
        return JsonResponse(res)


    return render(request,'upload_image.html')

def edit_tag(request):
    res={"code":200,"msg":"sucess"}
    try:
        id=request.POST.get("id")
        fileinfo=FileInfo.objects.get(id=id)
        tags=request.POST.get("tag")
        fileinfo.tags=tags
        fileinfo.save()
    except:
        res["code"]=500
        res["msg"]="操作失败"
    return JsonResponse(res)




def image_list(request):
    q=request.GET.get("q")
    query_parm = Q()
    query_parm.connector = 'or'
    if q!=None:
        query_parm.children.append(("filename__contains",q))
        query_parm.children.append(("tags__contains", q))
    else:
        q = ''

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    img_list = FileInfo.objects.filter(query_parm).order_by('-upload_date')
    p = Paginator(img_list, 8, request=request)
    img_list = p.page(page)
    

    return render(request,'img_list.html',{"img_list":img_list,"q":q})

def delete_img(request):
    res={"code":200,"msg":"sucess"}
    if request.method=="POST":
      try:
          id=request.POST.get("id")
          fileinfo=FileInfo.objects.get(id=id)
          os.remove(os.path.join(settings.BASE_DIR,'static',fileinfo.md5_name))
          fileinfo.delete()
          return JsonResponse(res)
      except:
          res["msg"]="删除失败"
          res["code"]=500
          return JsonResponse(res)

