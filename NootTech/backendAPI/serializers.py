from rest_framework import serializers
from .models import User, ErrorVideo, File, FavouritedFile, ReportedFile
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


class ListUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'colour', 'is_admin')


class ListFilesSerializer(serializers.ModelSerializer):

    uploader_id = serializers.CharField(source='user.id')
    uploader = serializers.CharField(source='user.username')

    class Meta:
        model = File
        fields = '__all__'


class FavouriteFiles(serializers.ModelSerializer):
    '''
    Serializer for favourite files
    '''
    generated_filename = serializers.CharField(source='file.generated_filename')
    original_filename = serializers.CharField(source='file.original_filename')
    file_url = serializers.CharField(source='file.file_content')
    uploader = serializers.CharField(source='file.user.username')
    icon = serializers.CharField(source='file.icon')
    thumbnail = serializers.CharField(source='file.thumbnail')

    class Meta:
        model = FavouritedFile
        fields = ('id', 'generated_filename', 'original_filename', 'icon', 'thumbnail', 'file_url', 'uploader')


class DeleteFavourite(serializers.ModelSerializer):
    '''
    API for deleting Files
    '''
    class Meta:
        model = FavouritedFile
        fields = ('file','user')


class CreateUserSerializer(serializers.ModelSerializer):

    email = serializers.CharField(write_only= True)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    colour = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username','email','colour','password')

    def create(self, validated_data):
        password = validated_data['password']

        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            colour=validated_data['colour'],
        )

        try:
            validate_password(password=validated_data['password'], user=user)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})

        user.set_password(password)
        user.save()
        return validated_data


class ErrorVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorVideo
        fields = '__all__'


class SettingsSerializer(serializers.ModelSerializer):
    gen_upload_key = serializers.BooleanField(default=False)
    email = serializers.CharField(allow_null=True)

    class Meta:
        model = User
        fields = ('colour', 'email', 'warnings', 'upload_key', 'gen_upload_key')


class ReportList(serializers.ModelSerializer):
    class Mete:
        model = ReportedFile
        fields = '__all__'


class ReportAdd(serializers.ModelSerializer):
    class Mete:
        model = ReportedFile
        fields = '__all__'



