from django.db import models

class Channels(models.Model):
    channel_id = models.CharField(max_length=24, primary_key=True)
    channel_title = models.CharField(max_length=255)
    subscriberCount = models.IntegerField()
    channel_viewCount  = models.BigIntegerField()
    videoCount = models.IntegerField()

    class Meta:
        db_table = "Channels"

class Workout_Video_Trainer(models.Model):
    video_id = models.CharField(max_length=11, primary_key=True)
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE)
    publish_date = models.CharField(max_length=20)
    video_title = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    video_viewCount = models.IntegerField()
    likeCount = models.IntegerField()
    trainer = models.CharField(max_length=255)

    class Meta:
        db_table = "Workout_Video_Trainer"

class Workout_Video_Type(models.Model):
    video_id = models.CharField(max_length=11, primary_key=True)
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE)
    publish_date = models.CharField(max_length=20)
    video_title = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    video_viewCount = models.IntegerField()
    likeCount = models.IntegerField()
    workout_type = models.CharField(max_length=255)

    class Meta:
        db_table = "Workout_Video_Type"

class Recipe_Video(models.Model):
    video_id = models.CharField(max_length=11, primary_key=True)
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE)
    publish_date = models.CharField(max_length=20)
    video_title = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    video_viewCount = models.IntegerField()
    likeCount = models.IntegerField()

    class Meta:
        db_table = "Recipe_Video"

class User_Information(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = "User_Information"

class Forum(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User_Information, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=255)
    post_content = models.CharField(max_length=255)

    class Meta:
        db_table = "Forum"