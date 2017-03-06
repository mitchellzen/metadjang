from _socket import gaierror
from rest_framework import serializers

#this is the non-model used by the serializer
class LogEntry(object):
    def __init__(self, pk, payload, label):
        self.pk = pk
        self.payload = payload
        self.label = label

    def save(self, *args, **kwargs):
        from .tasks import add_to_queue
        try:
            add_to_queue.delay(self.__dict__)
        except gaierror as e:
            print("CELERY IS NOT RUNNING")
        add_to_queue.delay(self.__dict__)

#this is a serializer for a non-model
class LogSerializer(serializers.Serializer):
    pk = serializers.CharField()
    payload = serializers.CharField()
    label = serializers.CharField()

    class Meta:
        fields = ['pk', 'payload', 'label']


    def create(self, validated_data):
        instance = LogEntry(**validated_data)
        instance.save()
        return instance