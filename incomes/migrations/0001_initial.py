# Generated by Django 4.1.5 on 2023-02-03 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("account_books", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Income",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일")),
                ("money", models.IntegerField(verbose_name="금액")),
                (
                    "income_detail",
                    models.CharField(max_length=15, null=True, verbose_name="수입 내역"),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("현금", "현금")],
                        max_length=2,
                        null=True,
                        verbose_name="결제 수단",
                    ),
                ),
                (
                    "memo",
                    models.CharField(max_length=255, null=True, verbose_name="메모"),
                ),
                (
                    "account_book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="incomes",
                        to="account_books.accountbook",
                        verbose_name="가계부",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="incomes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="유저",
                    ),
                ),
            ],
            options={
                "db_table": "Income",
            },
        ),
        migrations.CreateModel(
            name="IncomeURL",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("shared_url", models.URLField(verbose_name="공유 링크")),
                ("expired_at", models.DateTimeField(verbose_name="만료일")),
                (
                    "expense",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="income_urls",
                        to="incomes.income",
                        verbose_name="수익",
                    ),
                ),
            ],
            options={
                "db_table": "IncomeURL",
            },
        ),
    ]
