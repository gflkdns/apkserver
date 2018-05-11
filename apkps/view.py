import json
import os

from django.http import HttpResponse

from apkps import cfg


def apk_list(request):
    list = []
    for root, dirs, files in os.walk(cfg.dir):
        for file in files:
            if os.path.splitext(file)[1] == '.apk':
                list.append(file)
    return HttpResponse(json.dumps(list))


def downloadapk(request):
    '''
    根据apk名称下载apk文件
    例如：aaa.apk
    :param request:  apkname
    '''
    apk = request.GET.get("apkname")
    if None == apk:
        apk = 'base.7z'
    dir = cfg.dir
    file = open(dir + apk, 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{filename}"'.format(filename=apk)
    return response


def uploadhole(request):
    """多文件上传"""
    if request.method == 'POST':  # 获取对象
        files = request.FILES.getlist('files')
        packagename = request.POST.get('packagename')
        hashcode = request.POST.get('hashcode')
        # 调用java进行合并的pmap逻辑
        cmd = 'java -jar E:/apps/apkps/apkps/pmap.jar '"{packagename}"' '"{hashcode}"' '"{pmapser}"''.format(
            packagename=packagename,
            hashcode=hashcode,
            pmapser=cfg.pmapdir,
        )
        'java -jar E:/apps/apkps/apkps/pmap.jar com.disney.chukong.WMW 8b2baefaf4af3db001bcd446c5dc0a04 D:/phpStudy/WWW/app_download_fragment/pmap.ser'
        result = os.system(cmd)
        savedir = cfg.dir + '/' + packagename + '/' + hashcode + '/'
        if not os.path.exists(savedir):
            os.makedirs(savedir)
        print(savedir)
        for file in files:
            # 上传文件的文件名
            print(file.name)
            f = open(os.path.join(
                savedir, file.name),
                'wb')
            for chunk in file.chunks():
                f.write(chunk)
            f.close()
        return HttpResponse('OK')
    return HttpResponse(request, 'ERROR')


def hello(request):
    return HttpResponse('hello word!')
    pass
