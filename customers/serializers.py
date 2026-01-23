from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'created_at']

    def validate_phone(self, value):
        if not value:
            raise serializers.ValidationError("Phone number is required.")
        digits = ''.join(filter(str.isdigit, value))
        if len(digits) < 10:
            raise serializers.ValidationError("Phone number must be at least 10 digits")
        if digits.startswith('-'):
            raise serializers.ValidationError("Phone number cannot be negative.")
        if Customer.objects.filter(phone=digits).exists():
            raise serializers.ValidationError("Phone number is already in use.")
        return digits
    
    
    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError({"name": "Name field is required"})
        if not data.get('email'):
            raise serializers.ValidationError({"email": "Email field is required"})
        if not data.get('phone'):
            raise serializers.ValidationError({"phone": "Phone field is required"})
        return data