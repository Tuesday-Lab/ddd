from rest_framework import serializers


# TODO: 프로젝트 구성원이 모두 알아들을 수 있는 표현은 어디서부터 적용해야 할까?
# 유저가 회원가입을 합니다
class SignupParameters(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=30)
