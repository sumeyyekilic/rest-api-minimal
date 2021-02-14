from rest_framework import serializers
from .models import BulletJournal

class JournallSerializer(serializers.ModelSerializer):
	class Meta:
		model = BulletJournal
		fields ='__all__'