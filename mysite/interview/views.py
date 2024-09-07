from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import OuterRef, Subquery
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout

from jobs.models import Job, candidate
from user.models import Interviewer
from .models import resumeSubmitRecord, qqGroup, InterviewResult

import random


# Create your views here.

def interviewHome(request):
    if request.user.is_authenticated:
        interviewer = Interviewer.objects.filter(user=request.user).first()
    else:
        return redirect('/admin/login/')

    if interviewer.type == 0:
        resumeRecord = resumeSubmitRecord.objects.filter(interviewer1=interviewer,
                                                         interviewResult1__isnull=True)  # 当前一面面试官被分配的工单
    elif interviewer.type == 1:
        resumeRecord = resumeSubmitRecord.objects.filter(interviewer2=interviewer, interviewResult1__isnull=False,
                                                         interviewResult2__isnull=True)  # 当前二面面试官，一面面试已经结束，需进行二面面试的工单

    candidate_name = candidate.objects.filter(user=OuterRef('user')).values('name')
    candidate_jobname = candidate.objects.filter(user=OuterRef('user')).values('job_wanted')

    Record = resumeRecord.annotate(
        name=Subquery(candidate_name),
        job_wanted=Subquery(candidate_jobname)
    )

    return render(request, './InterviewHome.html', {'record': Record})


def startInterview(request, username):
    if (request.method == "POST"):

        # print(request.POST)
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken', None)  # 删除 CSRF token
        interviewer = Interviewer.objects.filter(user=request.user).first()
        user = User.objects.filter(username=username).first()
        data['interview_name'] = interviewer.name

        print(user,interviewer.type)
        interviewResult,created = InterviewResult.objects.update_or_create(**{'user':user,'type': interviewer.type},defaults= data)

        if not created:
            interviewResult.save()

        record = resumeSubmitRecord.objects.filter(user = user,department=interviewer.department).first()

        if interviewer.type==0:
             record.interviewResult1 = interviewResult
        else:
             record.interviewResult2= interviewResult

        record.save()

        return redirect('/interview/')





    user_candidate = candidate.objects.filter(user__username=username).first()

    return render(request, './InterviewPane.html', {'user_candidate': user_candidate})


def sendResume(request):
    if request.user.is_anonymous:
        return JsonResponse({'msg': '你还未登入！请登入在投递简历！', 'status': False})

    JobId = request.POST.get('JobId')

    job = Job.objects.filter(JobID=JobId).first()

    department = request.POST.get('department').split('-')[0].strip()

    qqgroup = qqGroup.objects.filter(department=department).first().qqGroupNum

    interviewer1 = Interviewer.objects.filter(department=department, type=0)

    interviewer1 = random.choice(interviewer1)

    interviewer2 = Interviewer.objects.filter(department=department, type=1)

    interviewer2 = random.choice(interviewer2)
    try:
        resumeSubmitRecord.objects.create(job=job, user=request.user, department=department, interviewer1=interviewer1,
                                          interviewer2=interviewer2, qqgroup_id=qqgroup)
        return JsonResponse({'msg': '投递成功！请耐心等待通知哦！', 'qqgroup_id': qqgroup, 'status': True})
    except:

        return JsonResponse({'msg': '你已经在这个部门投递过，请勿重复投递!', 'status': False, 'qqgroup_id': qqgroup})


def interviewerLogout(request):
    logout(request)
    return redirect('/admin/login/')