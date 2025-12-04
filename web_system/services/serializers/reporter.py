from rest_framework import serializers
from relacionamentos.models.reporter import Reporter
#from services.serializers import PersonDetailSerializer

class ReporterMinimaSerlializer(serializers.ModelSerializer):
    '''
    url = serializers.HyperlinkedIdentityField(
        view_name='services:reporter_list',
        lookup_field = 'pk',
        read_only = True,
    )
    '''

    class Meta:
        model = Reporter
        fields = [ 'name'] # 'url',

    def create(self, validated_data):
        return Reporter.objects.create(**validated_data)