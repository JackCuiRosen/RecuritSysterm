import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse, QueryDict
from django.db.models import OuterRef, Subquery
from django.shortcuts import render, redirect
from django.template import loader
from interview.models import resumeSubmitRecord

from .models import Job, candidate

from user.models import userProfile


# Create your views here.
def jobs(request, page_num):
    page_num = int(page_num)

    job_list = Job.objects.order_by('JobID')[(page_num - 1) * 7:page_num * 7]

    template = loader.get_template('jobs.html')

    job_cnt = len(Job.objects.all())

    page_cnt = int((job_cnt + 6) / 7)

    context = {'job_list': job_list, 'job_cnt': job_cnt, 'page_cnt': page_cnt}
    return HttpResponse(template.render(context))


def jobdetatils(request, job_place):
    # job_place = int(job_place)

    # job = Job.objects.order_by("JobID")[job_place]

    job = Job.objects.filter(JobID__exact=job_place)[0]

    template = loader.get_template('Jobdetails.html')

    if request.user.id is not None:
        is_login = True

        user = userProfile.objects.filter(user__username=request.user.username).first()

        print(user)

    else:
        is_login = False
        user = None

    context = {'job': job, 'user': user, 'is_login': is_login}

    return HttpResponse(template.render(context))


def jobshow(request):
    page = request.GET.get('page')

    if page == '':
        page = 1

    keyword = request.GET.get('keyword')

    category = request.GET.get('category')
    # category.splite
    if (category != None):
        category = category.split(",")
    city = request.GET.get('city')
    if (city != None):
        city = city.split(',')

    page = int(page)

    job_list = Job.objects.filter(JobName=-1)

    if (category):
        for i in category:
            if (i != None):
                job_list = job_list | Job.objects.filter(WorkKind=i)

    if (city):
        for i in city:
            if (i != None):
                job_list = job_list | Job.objects.filter(WorkPlace=i)
                # print(len(job_list))
    if (keyword):
        job_list = job_list | Job.objects.findAll(keyword)
    elif (len(job_list) == 0):
        job_list = job_list | Job.objects.all()

    num_of_items = 7
    job_cnt = len(job_list)

    # print(job_cnt)
    if (page * num_of_items > job_cnt or job_list == None):
        return render(request, './JobNotfound.html')
    paginator = Paginator(job_list, num_of_items)

    btn_limit = 5

    try:
        job_list = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        job_list = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages

    if paginator.num_pages <= btn_limit:
        page_range = range(1, paginator.num_pages + 1)
    else:
        left_num = max(page - int(btn_limit / 2), 1)
        right_num = min(left_num + btn_limit - 1, paginator.num_pages)

        if right_num - left_num < btn_limit - 1:
            left_num = right_num - btn_limit + 1
        page_range = range(left_num, right_num + 1)

    page_cnt = paginator.num_pages

    if request.user.id != None:
        is_login = True
        user = userProfile.objects.filter(user__username=request.user.username).first()

    else:
        is_login = False
        user = None


    context = {'job_list': job_list, 'job_cnt': job_cnt, 'page_cnt': page_cnt, 'paginator': paginator,
               'page_range': page_range, 'page_now': page, 'user': user, 'is_login': is_login}
    return render(request, './jobs.html', context)


def get_jobdata(request):
    data = {'message': 'Hello, World!'}

    return JsonResponse(data)


@login_required(login_url='/login/')
def edit_candidate(request):
    if request.user.id is not None:
        is_login = True

        user = userProfile.objects.filter(user__username=request.user.username).first()

    else:
        is_login = False
        user = None

    if request.method == "GET":


        user_candidate = candidate.objects.filter(user=request.user).first()

        if user_candidate is None:
            return render(request, './candidateForm.html', {'user':user,'is_login':is_login})


        user_candidate = model_to_dict(user_candidate)


        context = {'user_candidate': user_candidate, 'user': user, 'is_login': is_login}

        return render(request, './candidateForm.html', context)

    if request.method == "POST":
        data = request.POST

        query_dict = QueryDict('', mutable=True)
        query_dict.update(data)


        education_list = query_dict.get("education")
        project_list = query_dict.get("project")
        social_list = query_dict.get("social")
        baseinfo = query_dict.get('baseinfo')

        self = query_dict.get('self')
        award_list = query_dict.get('award')
        advantage = query_dict.get('advantage')
        baseinfo = json.loads(baseinfo)

        candidate.objects.update_or_create(user=request.user,
                                           defaults={"name": baseinfo["name"], "phone": baseinfo["phone"],
                                                     "email": baseinfo["email"], "job_wanted": baseinfo["intention"],
                                                     "education": education_list, "project": project_list,
                                                     "award": award_list, "social": social_list,
                                                     "evaluation": self, "advantage": advantage})
        userProfile.objects.filter(user=request.user).update(nickname = baseinfo["name"]);



    return render(request, './candidateForm.html', {'user': user, 'is_login': is_login})


@login_required(login_url='/login/')
def mycandidate(request):
    if request.user.id is not None:
        is_login = True
        user = userProfile.objects.filter(user__username=request.user.username).first()

    else:
        is_login = False
        user = None

    user_candidate = candidate.objects.filter(user=request.user).first()
    if user_candidate is None:
        return redirect('/editcandidate/')
    last_editTime = user_candidate.last_editTime

    # print(User_candidate.last_editTime)
    return render(request, './resume1.html', {'user': user, 'is_login': is_login, 'last_editTime': last_editTime,'user_candidate':user_candidate})


@login_required(login_url='/login/')
def acceptRecord(request):
    if request.user.id is not None:
        is_login = True
        user = userProfile.objects.filter(user__username=request.user.username).first()

    else:
        is_login = False
        user = None


    record = resumeSubmitRecord.objects.filter(user=request.user).first()

    # job_city = Job.objects.filter(Job = OuterRef('Job'))

    # print(record)


    return render(request,'./acceptRecord.html',{'user':user,'is_login':is_login,'record':record})