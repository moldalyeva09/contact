from rest_framework import serializers
from .models import Contacts

class ContactsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_blank=True)
    class Meta:
        model = Contacts
        fields = '__all__'

    def validate_name(self, value):
        if value.strip() == '':
            raise serializers.ValidationError('Атынызды жазыныз!')
        elif len(value) >20:
            raise serializers.ValidationError('Атыныз 20 символдон коп ')
        return value

    def validate_phone_number(self, value):
        if len(value)<10:
            raise serializers.ValidationError('Телефон номер 10 символдон аз!')
        elif len(value) > 15:
            raise serializers.ValidationError('Телефон номер 14 символдон аз турушу керек!')
        return value


