from rest_framework import serializers
from .models import *

class Channels_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = ('channel_id', 'channel_title', 'subscriberCount', 'channel_viewCount', 'videoCount')

class Workout_Video_TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout_Video_Trainer
        fields = ('video_id', 'channel_id', 'publish_date', 'video_title', 'duration', 'video_viewCount', 'likeCount', 'trainer')

class User_Information_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Information
        fields = ('user_id', 'email', 'phone_number', 'password')