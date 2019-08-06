from .models import Student,Faculty
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from collections import defaultdict
@api_view(['GET'])  #5
def api_best_student_maths(request):
    all=Student.objects.all()
    if all:
        bsm=[]
        for i in all:
            if i.subject=='Mathematics':
                d={}
                d["name"]=i.name
                d["subject"]=i.subject
                d["marks"]=i.marks
                bsm.append(d)
                bsm.sort(key=lambda x:x['marks'],reverse=True)
    return JsonResponse(bsm[0],safe=False)

@api_view(['GET']) #4
def api_hrc(request):
    obj=Student.objects.all()
    hsc=defaultdict(int)
    for i in obj:
        hsc[i.name] += int(i.marks)
    s=sorted(hsc.items(),key=lambda x:x[1],reverse=True)
    return Response(s[0])


@api_view(['GET']) #7
def api_lrc(request):
    obj=Student.objects.all()
    lrc=defaultdict(int)
    for i in obj:
        lrc[i.name] += int(i.marks)
    s=sorted(lrc.items(),key=lambda x:x[1])
    return Response(s[0])

@api_view(['GET'])  #6
def api_avg(request):
    obj=Student.objects.all()
    am=defaultdict(list)
    for i in obj:
        am[i.subject].append(int(i.marks))
    av=defaultdict(int)
    for k,v in am.items():
        av[k]=sum(v)/len(v)
    return Response(av)
            

@api_view(['GET'])
def api_more90(request):
    obj=Student.objects.all()
    obj1=Faculty.objects.all()
    mor=defaultdict(list)
    for i in obj:
        if i.marks>90:
            mor[i.subject].append(int(i.marks))
    s,m=max(mor.items(),key=lambda x:len(x[1]))        
    for j in obj1:
        if j.subject==s:
            result=j.fname
        
    return Response([s,m,len(m),result])



@api_view(['GET'])
def api_less40(request):
    obj=Student.objects.all()
    obj1=Faculty.objects.all()
    van=defaultdict(list)
    for i in obj:
        if i.marks<40:
            van[i.subject].append(int(i.marks))
    su,ma=max(van.items(),key=lambda x:len(x[1]))
    for j in obj1:
        if j.subject==su:
            result=j.fname
    return Response([su,ma,len(ma),result])


@api_view(['GET'])
def api_above40(request):
    obj=Student.objects.all()
    obj1=Faculty.objects.all()
    nav=defaultdict(list)
    for i in obj:
        if i.marks>40:
            nav[i.subject].append(int(i.marks))
    sub,mar=max(nav.items(),key=lambda x: len(x[1]))
    for j in obj1:
        if j.subject==sub:
            result=j.fname
    return Response([sub,mar,len(mar),result])