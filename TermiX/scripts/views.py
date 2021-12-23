from django.shortcuts import render,redirect
from .python_scripts.dir.organize_dir import organize
from .python_scripts.dir.rename import rename_files_main
from django.http import HttpResponse
import json
# /home/richeshgupta/pro/TermiX/TermiX/scripts/python-scripts/dir/organize_dir.py
def organize_files(request):
    return render(request,"main/organize-files.html",{})

def ErrorPage(request,msg):
    return render(request,"main/error.html",{'error':msg})

def organize_api(request):
    if request.method=="POST":
        path = request.POST.getlist("path")
        print("Path : ",path)
        try:
            zz = organize(path[0])
            
        except FileNotFoundError:
            return ErrorPage(request,"Directory doesn't exist")

        return render(request,"main/organize-files.html",{})
    else:
        return render(request,"main/organize-files.html",{})

def renaming_api(request):
    if request.method =="POST":
        folder_path = request.POST.getlist('folder_path')[0]
        new_name = request.POST.getlist('new_name')[0]
        ext = request.POST.getlist('ext')[0]
        rename_files_main(folder_path,new_name,ext)
        return render(request,"main/rename.html",{})
    else:
        return render(request,"main/rename.html",{})

from .python_scripts.util.diff import similarity_per

def diff_api(request):
    if request.method=="POST":
        f1_path = request.POST.getlist("f1")[0]
        f2_path = request.POST.getlist("f2")[0]
        percentage = similarity_per(f1_path,f2_path)
        resp = str(percentage)
        # return render(request,"main/diff-result.html",{percentage:'percentage'})
        return HttpResponse(resp)
    elif request.method=="GET":
        return render(request,"main/diff.html",{})


def show_diff_result(request,percentage):
    return render(request,"main/diff-result.html",{percentage:'percentage'})

def image_resize_api(request):
    return render(request,"main/image-resize-api.html",{})


def crawler_all_links(request):
    return render(request,"main/find_all_links.html",{})

from .python_scripts.crawler.all_links import get_all_links

def crawler_all_links_api(request):
    if request.method=="POST":
        url = request.POST.getlist('path')[0]
        resp = get_all_links(url)
        resp = json.dumps(resp)
        return HttpResponse(resp,content_type="application/json")
    else:
        return render(request,"main/find_all_links.html",{})