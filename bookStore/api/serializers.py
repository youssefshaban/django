from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import bookStore


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookStore
        fields = "__all__"

    def delete(self):
        id = self.data.get('id')
        book = bookStore.objects.get(pk=id)
        book.delete()




class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def save(self):
        user = User(
            email=self.validated_data.get('email'),
            username=self.validated_data.get('username')
        )
        if self.validated_data.get('password') != self.validated_data.get('password2'):
            raise serializers.ValidationError({
                'password': "pass not matched"
            })
        else:
            user.set_password(self.validated_data.get('password'))
            user.save()
