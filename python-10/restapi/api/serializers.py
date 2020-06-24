from rest_framework import serializers


class QuestionSerializer(serializers.Serializer):

    question = serializers.ListField(
        child=serializers.IntegerField(),
        required=True)

    class Meta:
        fields = ('question',)
