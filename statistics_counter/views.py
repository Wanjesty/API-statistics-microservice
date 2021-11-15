from rest_framework.response import Response
from rest_framework.views import APIView


from .models import statictics_data
from .serializers import ShowStaticticSerializers, AddStaticticSerializers
from django.forms.models import model_to_dict


def sort_list_of_dict_by_field(list_of_dicts, field="date"):
        sorted_list_of_dict = []
        copy_list_of_dicts = list_of_dicts
        value_list = [one_dict[field] for one_dict in list_of_dicts]
        value_list.sort()
        for value in value_list:
            for index, one_dict in enumerate(copy_list_of_dicts):
                if one_dict[field] == value:
                    sorted_list_of_dict.append(copy_list_of_dicts.pop(index))
                    break
        return sorted_list_of_dict



class ShowStatisticView(APIView):
    """Список всех данных"""
    
    def post(self, request):
        statistic = statictics_data.objects.filter(date__gte=request.data["from"], date__lte=request.data["to"])
        if "sorted_by" in request.data:
            list_statistic = list(map(lambda x: x.__dict__, statistic))
            sorted_statistic = sort_list_of_dict_by_field(list_statistic, field=request.data["sorted_by"])
            serializer = ShowStaticticSerializers(sorted_statistic, many=True)
            return Response(serializer.data)
        serializer = ShowStaticticSerializers(statistic, many=True)
        return Response(serializer.data)


class AddStatisticView(APIView):
    """Добавление статистики"""

    def post(self, request):
        entered = AddStaticticSerializers(data=request.data)
        added = {}
        if entered.is_valid():     
            filter_data_queryset = statictics_data.objects.filter(date=entered.data["date"])
            if len(filter_data_queryset) == 0:
                if "views" in entered.data:
                    added["views"] = entered.data["views"]
                if "clicks" in entered.data:
                    added["clicks"] = entered.data["clicks"]
                if "cost" in entered.data:
                    added["cost"] = entered.data["cost"]
                if "cost" in entered.data and "clicks" in entered.data:
                    added["cpc"] = entered.data["cost"] / entered.data["clicks"]
                if "cost" in entered.data and "views" in entered.data:
                    added["cpm"] = entered.data["cost"] / entered.data["views"] * 1000
                add_statistic = AddStaticticSerializers(data=added)
                if add_statistic.is_valid():
                    add_statistic.save()
            else:
                if "views" in entered.data:
                    added["views"] = filter_data_queryset[0].views + entered.data["views"]
                else:
                    added["views"] = filter_data_queryset[0].views
                if "clicks" in entered.data:
                    added["clicks"] = filter_data_queryset[0].clicks + entered.data["clicks"]
                else:
                    added["clicks"] = filter_data_queryset[0].clicks
                if "cost" in entered.data:
                    added["cost"] = filter_data_queryset[0].cost + entered.data["cost"]
                else:
                    added["cost"] = filter_data_queryset[0].cost
                added["cpc"] = added["cost"] / added["clicks"]
                added["cpm"] = added["cost"] / added["views"] * 1000
                update_statistic = AddStaticticSerializers(filter_data_queryset[0], data=added)
                if update_statistic.is_valid():
                    update_statistic.save()
        return Response(status=201)

class DeleteStatisticView(APIView):
    """Удаление статистики"""
    def get(self, request):
        statictics_data.objects.all().delete()
        return Response(status=200)