# rest_framework
from rest_framework import serializers

# django
from django.utils.dateformat import DateFormat

# expenses
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    money = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Expense
        fields = ("id", "money", "expense_detail", "payment_method", "memo",  "updated_at", "created_at",)
    
    def get_updated_at(self, obj):
        return DateFormat(obj.updated_at).format("Y-m-d H:i")
    
    def get_created_at(self, obj):
        return DateFormat(obj.created_at).format("Y-m-d H:i")
    
    def get_money(self, obj):
        return format(obj.money, ",")


class ExpenseCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = ("money", "expense_detail", "payment_method", "memo", )
        extra_kwargs = {
            "money": {
                "error_messages": {
                    "required": "금액을 입력해주세요.",
                    "blank": "금액을 입력해주세요.",
                    "invalid": "숫자만 입력해주세요.",
                }
            },
        }