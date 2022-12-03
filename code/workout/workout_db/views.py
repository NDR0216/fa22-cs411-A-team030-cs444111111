from .models import *
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

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def keywordsearch(request):
    keyword = request.POST.get("keyword", "")
    if keyword != "":
        keyword = '%' + keyword + '%'
        video = Workout_Video_Trainer.objects.raw('SELECT video_id, video_title, video_viewCount FROM Workout_Video_Trainer where video_title LIKE %s'\
                                                    'UNION SELECT video_id, video_title, video_viewCount FROM Workout_Video_Type where video_title LIKE %s'\
                                                    'UNION SELECT video_id, video_title, video_viewCount FROM Recipe_Video where video_title LIKE %s ORDER BY video_viewCount DESC LIMIT 50', [keyword, keyword, keyword])
    else:
        video = None

    template = loader.get_template('keywordsearch.html')
    context = {
        'queryset': video
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))

def workout_type(request):
    template = loader.get_template('workout_type.html')
    return HttpResponse(template.render({}, request))

def workout_type_grid(request):
    type = request.GET.get("type", "")

    if type == "0":
        text = "HIIT&crossfit"
    elif type == "1":
        text = "aerobic&cardio"
    elif type == "2":
        text = "yoga&pilates"
    elif type == "3":
        text = "stretching&balance"
        
    video = Workout_Video_Type.objects.raw('SELECT * FROM Workout_Video_Type WHERE workout_type ="'+text+'"LIMIT 4')

    template = loader.get_template('workout_type_grid.html')
    context = {
        'type': type,
        'text': text,
        'queryset': video
    }
    return HttpResponse(template.render(context, request))

def workout_type_table(request):
    type = request.GET.get("type", "")
    condition = request.GET.get("condition", "")

    if type == "0":
        text = "HIIT&crossfit"
    elif type == "1":
        text = "aerobic&cardio"
    elif type == "2":
        text = "yoga&pilates"
    elif type == "3":
        text = "stretching&balance"

    if condition == "Popularity":
        video = Workout_Video_Type.objects.raw('SELECT * FROM Workout_Video_Type WHERE workout_type ="'+text+'"ORDER BY video_viewCount DESC LIMIT 15')
    elif condition == "Newest":
        video = Workout_Video_Type.objects.raw('SELECT * FROM Workout_Video_Type WHERE workout_type ="'+text+'"ORDER BY publish_date DESC LIMIT 15')
    elif condition == "After":
        condition = "After 2020"
        video = Workout_Video_Type.objects.raw('SELECT * FROM Workout_Video_Type WHERE workout_type ="'+text+'"AND publish_date > "2020" LIMIT 15')
    elif condition == "Before":
        condition = "Before 2020"
        video = Workout_Video_Type.objects.raw('SELECT * FROM Workout_Video_Type WHERE workout_type ="'+text+'"AND publish_date < "2020" LIMIT 15')

    template = loader.get_template('workout_type_table.html')
    context = {
        'type': type,
        'text': text,
        'condition': condition,
        'queryset': video
    }
    return HttpResponse(template.render(context, request))

def workout_trainer(request):
    template = loader.get_template('workout_trainer.html')
    return HttpResponse(template.render({}, request))

def workout_trainer_grid(request):
    type = request.GET.get("type", "")

    if type == "0":
        text = "Caroline Girvan"
    elif type == "1":
        text = "Chloe Ting"
    elif type == "2":
        text = "Daniela Suarez"
    elif type == "3":
        text = "Deepti"
    elif type == "4":
        text = "Jorge Tabet"
    elif type == "5":
        text = "Kit Rich"
    elif type == "6":
        text = "Lucy Wyndham-Read"
    elif type == "7":
        text = "Mady Morrison"
    elif type == "8":
        text = "Nicole"
    elif type == "9":
        text = "Pamela Reif"
    elif type == "10":
        text = "Heather Robertson"
    elif type == "11":
        text = "Simeon Panda"
    
    video = Workout_Video_Trainer.objects.raw('SELECT * FROM Workout_Video_Trainer WHERE trainer = "'+text+'" LIMIT 4')


    template = loader.get_template('workout_trainer_grid.html')
    context = {
        'type': type,
        'text': text,
        'queryset': video
    }
    return HttpResponse(template.render(context, request))

def workout_trainer_table(request):
    type = request.GET.get("type", "")
    condition = request.GET.get("condition", "")

    if type == "0":
        text = "Caroline Girvan"
    elif type == "1":
        text = "Chloe Ting"
    elif type == "2":
        text = "Daniela Suarez"
    elif type == "3":
        text = "Deepti"
    elif type == "4":
        text = "Jorge Tabet"
    elif type == "5":
        text = "Kit Rich"
    elif type == "6":
        text = "Lucy Wyndham-Read"
    elif type == "7":
        text = "Mady Morrison"
    elif type == "8":
        text = "Nicole"
    elif type == "9":
        text = "Pamela Reif"
    elif type == "10":
        text = "Heather Robertson"
    elif type == "11":
        text = "Simeon Panda"

    if condition == "Popularity":
        video = Workout_Video_Trainer.objects.raw('SELECT * FROM Workout_Video_Trainer WHERE trainer = "'+text+'"ORDER BY video_viewCount DESC LIMIT 15')
    elif condition == "Newest":
        video = Workout_Video_Trainer.objects.raw('SELECT * FROM Workout_Video_Trainer WHERE trainer = "'+text+'"ORDER BY publish_date DESC LIMIT 15')
    elif condition == "After":
        condition = "After 2020"
        video = Workout_Video_Trainer.objects.raw('SELECT * FROM Workout_Video_Trainer WHERE trainer = "'+text+'"AND publish_date > "2020" LIMIT 15')
    elif condition == "Before":
        condition = "Before 2020"
        video = Workout_Video_Trainer.objects.raw('SELECT * FROM Workout_Video_Trainer WHERE trainer = "'+text+'"AND publish_date < "2020" LIMIT 15')

    template = loader.get_template('workout_trainer_table.html')
    context = {
        'type': type,
        'text': text,
        'condition': condition,
        'queryset': video
    }
    return HttpResponse(template.render(context, request))

def recipe(request):
    video = Recipe_Video.objects.raw('SELECT * FROM Recipe_Video LIMIT 4')

    template = loader.get_template('recipe.html')
    context = {
        'queryset': video
    }
    return HttpResponse(template.render(context, request))

def recipe_table(request):
    condition = request.GET.get("condition", "")

    if condition == "Popularity":
        video = Workout_Video_Trainer.objects.raw('SELECT * FROM Recipe_Video ORDER BY video_viewCount DESC LIMIT 15')
    elif condition == "Newest":
        video = Workout_Video_Trainer.objects.raw('SELECT * FROM Recipe_Video ORDER BY publish_date DESC LIMIT 15')
    elif condition == "After":
        condition = "After 2020"
        video = Workout_Video_Trainer.objects.raw('SELECT * FROM Recipe_Video WHERE publish_date > "2020" LIMIT 15')
    elif condition == "Before":
        condition = "Before 2020"
        video = Workout_Video_Trainer.objects.raw('SELECT * FROM Recipe_Video WHERE publish_date < "2020" LIMIT 15')

    template = loader.get_template('recipe_table.html')
    context = {
        'condition': condition,
        'queryset': video
    }
    return HttpResponse(template.render(context, request))

def forum(request):
    Username = request.session.get("Username", "")

    post = Forum.objects.raw('SELECT * FROM workout.Forum ORDER BY post_id DESC')
    
    template = loader.get_template('forum.html')
    context = {
        'Username': Username,
        'queryset': post
    }
    return HttpResponse(template.render(context, request))

def forum_post(request):
    Username = request.session.get("Username", "")
    
    template = loader.get_template('forum_post.html')
    context = {}
    if Username == "" or Username == None:
        context = {
            'error': "Please sign in"
        }
    
    return HttpResponse(template.render(context, request))

def forum_edit(request):
    post_id = request.GET['post_id']

    post = Forum.objects.raw('SELECT * FROM workout.Forum WHERE post_id = ' + str(post_id))

    template = loader.get_template('forum_edit.html')
    context = {
        'post_id': post_id,
        'title': post[0].post_title,
        'content': post[0].post_content
    }
    
    return HttpResponse(template.render(context, request))

def forum_add(request):
    title = request.POST['title']
    content = request.POST['content']
    
    Username = request.session['Username']

    instance = Forum(user_id=Username, post_title=title, post_content=content)
    instance.save()

    return HttpResponseRedirect(reverse('forum'))

def forum_update(request):
    post_id = request.POST['post_id']
    title = request.POST['title']
    content = request.POST['content']

    post = Forum.objects.get(post_id=post_id)
    post.post_title = title
    post.post_content = content
    post.save()

    return HttpResponseRedirect(reverse('forum'))

def forum_delete(request):
    post_id = request.GET['post_id']

    post = Forum.objects.get(post_id=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('forum'))

def recommendation(request):
    type = request.POST.get("type", "")
    keyword = request.POST.get("keyword", "")
    minViewCnt = request.POST.get("minViewCnt", "")
    MinSubscriberCnt = request.POST.get("MinSubscriberCnt", "")

    if keyword != "":
        res = executeSQL('CALL new_procedure ('+type+', "'+keyword+'", '+minViewCnt+', '+MinSubscriberCnt+')')
    else:
        res = None
    
    template = loader.get_template('recommendation.html')
    context = {
        'type': type == 'true',
        'queryset': res
    }
    return HttpResponse(template.render(context, request))

def visual(request):
    workout_type = request.POST.get("workout_type", "")
    start_yr = request.POST.get("start_yr", "")
    start_month = request.POST.get("start_month", "")
    end_yr = request.POST.get("end_yr", "")
    end_month = request.POST.get("end_month", "")

    video = Workout_Video_Type.objects.raw('SELECT * FROM workout.Workout_Video_Type WHERE workout_type = "'+workout_type+'" AND publish_date > "'+start_yr+'-'+start_month+'" AND publish_date < "'+end_yr+'-'+end_month+'-99"')

    dict = {}

    for i in video:
        print(i)
        key = int(i.publish_date[0:4]+i.publish_date[5:7])

        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1

    labels = "["
    data = "["
    for i in sorted(dict.items()):
        labels += str(i[0])+','
        data += str(i[1])+','
    labels += ']'
    data += ']'

    template = loader.get_template('visual.html')
    context = {
        'labels': labels,
        'data': data
    }
    return HttpResponse(template.render(context, request))

def signin(request):
    Username = request.POST.get("Username", "")
    inputPassword = request.POST.get("inputPassword", "")

    user = User_Information.objects.raw('SELECT * FROM workout.User_Information WHERE user_id = %s AND password = %s', [Username, inputPassword])

    error = ""
    if Username != "" and len(list(user)) == 0:
        error = "Please sign up"
    elif len(list(user)) == 1:
        request.session['Username'] = Username
        request.session['password'] = inputPassword
        return HttpResponseRedirect(reverse('index'))

    template = loader.get_template('signin.html')
    context = {
        'error': error
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    Username = request.POST.get("Username", "")
    email = request.POST.get("email", "")
    phone_number = request.POST.get("phone_number", "")
    inputPassword = request.POST.get("inputPassword", "")

    user = User_Information.objects.raw('SELECT * FROM workout.User_Information WHERE user_id = %s', [Username])

    error = ""
    if len(list(user)) == 1:
        error = "User name exists"
    elif Username != "":
        instance = User_Information(user_id=Username, email=email, phone_number=phone_number, password=inputPassword)
        instance.save()
        error = "successfully register"

    template = loader.get_template('signup.html')
    context = {
        'error': error
    }
    return HttpResponse(template.render(context, request))

def user_info(request):
    email = request.POST.get("email", "")
    phone_number = request.POST.get("phone_number", "")
    inputPassword = request.POST.get("inputPassword", "")

    Username = request.session.get("Username", "")

    user = User_Information.objects.raw('SELECT * FROM workout.User_Information WHERE user_id = %s', [Username])

    error = ""
    if email != "":
        user = User_Information.objects.get(user_id=Username)
        user.email = email
        user.phone_number = phone_number
        user.password = inputPassword
        user.save()

        error = "successfully update"

    user = User_Information.objects.raw('SELECT * FROM workout.User_Information WHERE user_id = %s', [Username])

    if len(list(user)) == 0:
        error = "Please sign in"
    else:
        email = user[0].email
        phone_number = user[0].phone_number
        inputPassword = user[0].password

    template = loader.get_template('user_info.html')
    context = {
        'email': email,
        'phone_number': phone_number,
        'inputPassword': inputPassword,
        'error': error
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    request.session['Username'] = ""
    request.session['password'] = ""
    
    return HttpResponseRedirect(reverse('index'))