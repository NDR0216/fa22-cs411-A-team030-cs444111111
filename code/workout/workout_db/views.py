from .serializers import *
from django.db import connection

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def executeSQL(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

def demo(request):
    template = loader.get_template('demo.html')
    return HttpResponse(template.render({}, request))

def user(request):
    queryset = User_Information.objects.all()
    template = loader.get_template('user.html')
    context = {
        'queryset': queryset
    }

    return HttpResponse(template.render(context, request))

def user_add(request):
    template = loader.get_template('user_add.html')
    return HttpResponse(template.render({}, request))

def user_add_post(request):
    user_id = request.POST['user_id']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    password = request.POST['password']

    try:
        user = User_Information.objects.get(user_id=user_id)
    except User_Information.DoesNotExist:
        instance = User_Information(user_id=user_id, email=email, phone_number=phone_number, password=password)
        instance.save()
        return HttpResponseRedirect(reverse('user'))
    else:
        return HttpResponseRedirect(reverse('user'))

def user_delete(request, user_id):
    user = User_Information.objects.get(user_id=user_id)
    user.delete()
    return HttpResponseRedirect(reverse('user'))

def user_update(request, user_id):
    queryset = User_Information.objects.get(user_id=user_id)
    template = loader.get_template('user_update.html')
    context = {
        'queryset': queryset
    }
    return HttpResponse(template.render(context, request))

def user_update_post(request, user_id):
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    password = request.POST['password']

    user = User_Information.objects.get(user_id=user_id)
    user.email = email
    user.phone_number = phone_number
    user.password = password
    user.save()
    return HttpResponseRedirect(reverse('user'))

def video_trainer(request):
    keyword = request.POST.get("keyword", "")
    if keyword != "":
        keyword = '%' + keyword + '%'
        video = Workout_Video_Trainer.objects.raw('SELECT * FROM Workout_Video_Trainer where video_title LIKE %s', [keyword])
    else:
        video = None

    template = loader.get_template('video_trainer.html')
    context = {
        'queryset': video
    }

    return HttpResponse(template.render(context, request))

def adv_query_1(request):
    channel = Channels.objects.raw('SELECT channel_id, channel_title, COUNT(video_id) AS cnt '\
        'FROM workout.Workout_Video_Trainer NATURAL JOIN workout.Channels '\
        'WHERE video_viewCount > 1000000 AND publish_date LIKE "202%%" '\
        'GROUP BY channel_id '\
        'ORDER BY cnt DESC '\
        'LIMIT 15'
    )

    template = loader.get_template('adv_query_1.html')
    context = {
        'queryset': channel
    }
    return HttpResponse(template.render(context, request))

def adv_query_2(request):
    video = Channels.objects.raw('SELECT * '\
        'FROM (SELECT * FROM workout.Recipe_Video WHERE video_viewCount > 100000) AS rv '\
            'NATURAL JOIN (SELECT * FROM workout.Channels WHERE subscriberCount > 1000000) AS ch '\
        'WHERE video_title LIKE "%%vegan%%"')

    template = loader.get_template('adv_query_2.html')
    context = {
        'queryset': video
    }
    return HttpResponse(template.render(context, request))
