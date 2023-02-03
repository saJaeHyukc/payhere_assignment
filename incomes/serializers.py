# rest_framework
from rest_framework import serializers

# django
from django.utils.dateformat import DateFormat

# incomes
from .models import Income


class IncomeSerializer(serializers.ModelSerializer):
    money = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Income
        fields = ("id", "money", "income_detail", "payment_method", "memo",  "updated_at", "created_at",)
    
    def get_updated_at(self, obj):
        return DateFormat(obj.updated_at).format("Y-m-d H:i")
    
    def get_created_at(self, obj):
        return DateFormat(obj.created_at).format("Y-m-d H:i")
    
    def get_money(self, obj):
        return format(obj.money, ",")