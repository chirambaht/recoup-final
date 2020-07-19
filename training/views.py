from django.shortcuts import render, redirect
from dashboard.models import Athelete, Practice, plan, KB
from django.utils import timezone as datetime
from django.contrib.auth.decorators import login_required
from dashboard.forms import AtheleteRegisterForm, PracticeRegisterForm, UserUpdateForm, AtheleteUpdateForm, PlanUpdateMonday, PlanUpdateSaturday, PlanUpdateFriday, PlanUpdateSunday, PlanUpdateTuesday, PlanUpdateWednesday, PlanUpdateThursday
from django.contrib import messages
from django.db.models import Q



# Create your views here.
@login_required
def training(request):
    
    user_plan = request.user.athelete.training_plan
    context = {
        'title':'Training',
        'day': datetime.localtime().date,
        'weekday': datetime.localtime().weekday,
        'mode': user_plan.type,
        'mon' : user_plan.Monday_Title,
        'mon_d' : user_plan.Monday_Description,
        'tue' : user_plan.Tuesday_Title,
        'tue_d' : user_plan.Tuesday_Description,
        'wed' : user_plan.Wednesday_Title,
        'wed_d' : user_plan.Wednesday_Description,
        'thu' : user_plan.Thursday_Title,
        'thu_d' : user_plan.Thursday_Description,
        'fri' : user_plan.Friday_Title,
        'fri_d' : user_plan.Friday_Description,
        'sat' : user_plan.Saturday_Title,
        'sat_d' : user_plan.Saturday_Description,
        'sun' : user_plan.Sunday_Title,
        'sun_d' : user_plan.Sunday_Description,
        'sun_v' : user_plan.Sunday_Video_url,
        'mon_v' : user_plan.Monday_Video_url,
        'tue_v' : user_plan.Tuesday_Video_url,
        'wed_v' : user_plan.Wednesday_Video_url,
        'thu_v' : user_plan.Thursday_Video_url,
        'fri_v' : user_plan.Friday_Video_url,
        'sat_v' : user_plan.Saturday_Video_url,
    }

    if request.method == 'POST':
        

        forms = [
            PlanUpdateMonday(request.POST, instance=user_plan),
            PlanUpdateTuesday(request.POST, instance=user_plan),
            PlanUpdateWednesday(request.POST, instance=user_plan),
            PlanUpdateThursday(request.POST, instance=user_plan),
            PlanUpdateFriday(request.POST, instance=user_plan),
            PlanUpdateSaturday(request.POST, instance=user_plan),
            PlanUpdateSunday(request.POST, instance=user_plan),
        ]
        c = 0
        for form in forms:
            if form.is_valid():
                form.save()
        messages.success(request, f'Updated!')
        return redirect('training_home')
    else:
        forms = {
            'mon' : PlanUpdateMonday(instance=user_plan),
            'tue' : PlanUpdateTuesday(instance=user_plan),
            'wed' : PlanUpdateWednesday(instance=user_plan),
            'thu' : PlanUpdateThursday(instance=user_plan),
            'fri' : PlanUpdateFriday(instance=user_plan),
            'sat' : PlanUpdateSaturday(instance=user_plan),
            'sun' : PlanUpdateSunday(instance=user_plan),
        }
        context['form'] = forms
        
    return render(request, 'training/training.html', context)

@login_required
def play(request):
    user_plan = request.user.athelete.training_plan
    context = {
        'title':'Video',
        'day': datetime.localtime().date,
        'weekday': datetime.localtime().weekday,
        'mode': user_plan.type,
        'mon' : user_plan.Monday_Title,
        'mon_d' : user_plan.Monday_Description,
        'tue' : user_plan.Tuesday_Title,
        'tue_d' : user_plan.Tuesday_Description,
        'wed' : user_plan.Wednesday_Title,
        'wed_d' : user_plan.Wednesday_Description,
        'thu' : user_plan.Thursday_Title,
        'thu_d' : user_plan.Thursday_Description,
        'fri' : user_plan.Friday_Title,
        'fri_d' : user_plan.Friday_Description,
        'sat' : user_plan.Saturday_Title,
        'sat_d' : user_plan.Saturday_Description,
        'sun' : user_plan.Sunday_Title,
        'sun_d' : user_plan.Sunday_Description,
        'sun_v' : user_plan.Sunday_Video_url,
        'mon_v' : user_plan.Monday_Video_url,
        'tue_v' : user_plan.Tuesday_Video_url,
        'wed_v' : user_plan.Wednesday_Video_url,
        'thu_v' : user_plan.Thursday_Video_url,
        'fri_v' : user_plan.Friday_Video_url,
        'sat_v' : user_plan.Saturday_Video_url,
    }
    return render(request, 'training/video.html', context)

@login_required
def clip(request, video_id='ScMzIvxBSi4'):
    item = KB.objects.filter(url=video_id).first()
    user_plan = request.user.athelete.training_plan
    context = {
        'day': datetime.localtime().date,
        'weekday': datetime.localtime().weekday,
        'mode': user_plan.type,
        'mon' : user_plan.Monday_Title,
        'mon_d' : user_plan.Monday_Description,
        'tue' : user_plan.Tuesday_Title,
        'tue_d' : user_plan.Tuesday_Description,
        'wed' : user_plan.Wednesday_Title,
        'wed_d' : user_plan.Wednesday_Description,
        'thu' : user_plan.Thursday_Title,
        'thu_d' : user_plan.Thursday_Description,
        'fri' : user_plan.Friday_Title,
        'fri_d' : user_plan.Friday_Description,
        'sat' : user_plan.Saturday_Title,
        'sat_d' : user_plan.Saturday_Description,
        'sun' : user_plan.Sunday_Title,
        'sun_d' : user_plan.Sunday_Description,
        'sun_v' : user_plan.Sunday_Video_url,
        'mon_v' : user_plan.Monday_Video_url,
        'tue_v' : user_plan.Tuesday_Video_url,
        'wed_v' : user_plan.Wednesday_Video_url,
        'thu_v' : user_plan.Thursday_Video_url,
        'fri_v' : user_plan.Friday_Video_url,
        'sat_v' : user_plan.Saturday_Video_url,
    }
    if item != None:
        context['title'] = item.title
        context['kb'] = True
        context['link'] = video_id
        context['video_title'] = item.title
        context['practice_name'] = item.practice
        context['presenter_name'] = item.presenter
        context['description'] = item.description
        context['personal'] = False
    else:
        context['title'] = 'Video'
        context['kb'] = True
        context['link'] = video_id
        context['personal'] = True
    return render(request, 'training/video.html', context)

@login_required
def overview(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = AtheleteUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.athelete)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('overview')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = AtheleteUpdateForm(instance=request.user.athelete)
        user_plan = request.user.athelete.training_plan
        context = {
        'u_form': u_form,
        'p_form': p_form,
        'title' : 'Overview',
        'day': datetime.localtime().date,
        'weekday': datetime.localtime().weekday,
        'mode': user_plan.type,
        'mon' : user_plan.Monday_Title,
        'mon_d' : user_plan.Monday_Description,
        'tue' : user_plan.Tuesday_Title,
        'tue_d' : user_plan.Tuesday_Description,
        'wed' : user_plan.Wednesday_Title,
        'wed_d' : user_plan.Wednesday_Description,
        'thu' : user_plan.Thursday_Title,
        'thu_d' : user_plan.Thursday_Description,
        'fri' : user_plan.Friday_Title,
        'fri_d' : user_plan.Friday_Description,
        'sat' : user_plan.Saturday_Title,
        'sat_d' : user_plan.Saturday_Description,
        'sun' : user_plan.Sunday_Title,
        'sun_d' : user_plan.Sunday_Description,
        'sun_v' : user_plan.Sunday_Video_url,
        'mon_v' : user_plan.Monday_Video_url,
        'tue_v' : user_plan.Tuesday_Video_url,
        'wed_v' : user_plan.Wednesday_Video_url,
        'thu_v' : user_plan.Thursday_Video_url,
        'fri_v' : user_plan.Friday_Video_url,
        'sat_v' : user_plan.Saturday_Video_url,
    }    
    return render(request, 'training/overview.html', context)

@login_required
def query(request):
    context = {'title':'Knowledge Base'}
    if request.method == 'GET':
        req = request.GET.get('query')
        if req != None:
            context['items'] = KB.objects.all().filter(Q(title__contains = req) | Q(practice__contains=req) | Q(Focus_Area__contains=req))
        else:
            context['items'] = KB.objects.all()
            
    else:
        context['items'] = KB.objects.all()
    
    return render(request, 'training/knowledge.html', context)

@login_required
def doctor(request):
    user_plan = request.user.athelete.training_plan
    context = {
        'day': datetime.localtime().date,
        'weekday': datetime.localtime().weekday,
        'mode': user_plan.type,
        'mon' : user_plan.Monday_Title,
        'mon_d' : user_plan.Monday_Description,
        'tue' : user_plan.Tuesday_Title,
        'tue_d' : user_plan.Tuesday_Description,
        'wed' : user_plan.Wednesday_Title,
        'wed_d' : user_plan.Wednesday_Description,
        'thu' : user_plan.Thursday_Title,
        'thu_d' : user_plan.Thursday_Description,
        'fri' : user_plan.Friday_Title,
        'fri_d' : user_plan.Friday_Description,
        'sat' : user_plan.Saturday_Title,
        'sat_d' : user_plan.Saturday_Description,
        'sun' : user_plan.Sunday_Title,
        'sun_d' : user_plan.Sunday_Description,
        'sun_v' : user_plan.Sunday_Video_url,
        'mon_v' : user_plan.Monday_Video_url,
        'tue_v' : user_plan.Tuesday_Video_url,
        'wed_v' : user_plan.Wednesday_Video_url,
        'thu_v' : user_plan.Thursday_Video_url,
        'fri_v' : user_plan.Friday_Video_url,
        'sat_v' : user_plan.Saturday_Video_url,
    }

    context['title'] = 'Contact a doctor'
    context['practices'] = Practice.objects.all()
    
    return render(request, 'training/doctor.html', context)

# Video pages to come down here