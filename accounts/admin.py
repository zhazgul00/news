from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "username", "age", "is_staff", "is_active")
    
    # Поля для отображения на страницах редактирования и добавления
    fieldsets = (
        *UserAdmin.fieldsets,  # Наследуем стандартные поля
        (None, {"fields": ("age",)}),  # Добавляем свои
    )
    add_fieldsets = (
        *UserAdmin.add_fieldsets,  # Наследуем поля для добавления
        (None, {"fields": ("age",)}),  # Добавляем свои
    )
