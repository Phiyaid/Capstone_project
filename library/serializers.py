from rest_framework import serializers
from .models import Book, LibraryUser, Transaction


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# class LibraryUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LibraryUser
#         fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        
        
        
class LibraryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryUser
        fields = ['id', 'username', 'email', 'password', 'is_active']

    def create(self, validated_data):
        user = LibraryUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
