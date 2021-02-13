from rest_framework import serializers
from .models import bulletJournal

class JournallSerializer(serializers.ModelSerializer):
	class Meta:
		model = bulletJournal
		fields ='__all__'