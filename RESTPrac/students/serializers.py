from rest_framework import serializers
from students.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'first_name', 'last_name', 'email_id')

    def create(self, validated_data):
        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_mame', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email_id = validated_data.get('email_id', instance.email_id)
        instance.save()
        return instance
