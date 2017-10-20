from django.shortcuts import render,HttpResponse
from app01 import models
from PIL import Image
from PIL.ExifTags import TAGS
from app01.form import Photo
import datetime
import os
import re

# Create your views here.
def index(request):
    return render(request,'index.html')
def index1(request):
    return render(request,'index1.html')
def index2(request):
    return render(request,'index2.html')
def photo(request):
    if request.method == 'POST':
        form = Photo(request.POST,request.FILES)
        print(request.FILES['photo'])
        if form.is_valid():
            # 获取时间
            photo = form.cleaned_data['photo']
            address = form.cleaned_data['address']
            type = form.cleaned_data['type']
            f = Image.open(photo)
            try:
                xf = f._getexif()
                ret={}
                for tag ,value  in xf.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
                date = ret['DateTime']
            except:
                time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                date = str(time+'(上传时间)')
            #保存
            f.save('app01/static/images/upload_photo/%s'%photo,'png')
            models.Photo.objects.create(photo='images/upload_photo/%s'%photo,dianzan=0,time=date,type=type,address=address)
            photo_obj = models.Photo.objects.all()
            photo_form = Photo()
            return render(request,'photo.html',{'photo':photo_form,'photo_obj':photo_obj,'massage':'success'})
        photo_obj = models.Photo.objects.all()
        photo_form = Photo()
        return render(request,'photo.html',{'photo':photo_form,'photo_obj':photo_obj,'error':'上传失败'})
    else:
        photo_form = Photo()
        photo_obj = models.Photo.objects.all()
        return render(request,'photo.html',{'photo':photo_form,'photo_obj':photo_obj})

def video(request):
    ret = models.Video.objects.all()
    return render(request,'video.html',{'video':ret})

def getvideo(request):
    if request.method == 'POST':
        src = request.POST.get('src',None)
        return render(request,'getvideo.html',{'src':src})
    # ret = os.walk('F:/python/python_test/django_chuchu/app01/static/images/video')
    # for root,dirs,files in ret:
    #     for file in files:
    #         if re.search(r'jpg',file):
    #             photo = file
    #             video = str(file[:-4]+'.mp4')
    #             models.Video.objects.create(video=str('images/video/'+video),photo=str('images/video/'+photo),time='2017-4-13 10:47:32',content='小视频')
    # return HttpResponse('chenggong')
    # ret = models.Video.objects.all()
    # for i in ret:
    #     i.delete()
    # return HttpResponse('true')
def content(request):
    return render(request,'content.html')

def top_fixed(request):
    return render(request,'top_fixed.html')



def ceshi_photo(request):
    # f = Image.open('app01/static/images/2016-10-03 153827.jpg')
    # xf = f._getexif()
    # ret={}
    # for tag ,value  in xf.items():
    #     decoded = TAGS.get(tag, tag)
    #     ret[decoded] = value
    # date = ret['DateTime']
    # print(date)
    return  render(request,'top_fixed.html')

def delete_photo_model(request):
    ret = models.Photo.objects.all()
    for i in ret:
        i.delete()
