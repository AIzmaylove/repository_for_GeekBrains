from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField
from .models import Author


class AuthorSerializer(Serializer):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    birthday_year = IntegerField()

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
        instance.save()
        return instance

    def create(self, validated_data):
        author = Author(**validated_data)
        author.save()
        return author

    def validate_birthday_year(selfs, value):
        if value > 2004:
            raise ValidationError('18+')
        return value

class AutorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

