from rest_framework import serializers

from .models import EntryModel

class EntryModelSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=500)
    tu = serializers.CharField(max_length=100)
    length = serializers.CharField(max_length=100)
    res = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    adress = serializers.CharField(max_length=100)

    status = serializers.CharField(max_length=100)
    notes = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return EntryModel.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.tu = validated_data.get('tu', instance.tu)
        instance.length = validated_data.get('length', instance.length)
        instance.res = validated_data.get('res', instance.res)
        instance.type = validated_data.get('type', instance.type)
        instance.adress = validated_data.get('adress', instance.adress)

        instance.status = validated_data.get('status', instance.status)
        instance.notes = validated_data.get('notes', instance.notes)

        instance.save()
        return instance
