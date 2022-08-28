from rest_framework import serializers
from .models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'theme', 'the_quote', 'created_at', 'updated_at')
        model = Quote