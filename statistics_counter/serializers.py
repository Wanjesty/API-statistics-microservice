from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import statictics_data
from datetime import date


class ShowStaticticSerializers(serializers.ModelSerializer):
    """Отображение всех данных"""

    class Meta:
        model = statictics_data
        fields = "__all__"


class AddStaticticSerializers(serializers.ModelSerializer):
    """Добавление статистики"""

    date = serializers.DateField(default=date.today(), read_only=True)
    
    class Meta:
        model = statictics_data
        fields = "__all__"