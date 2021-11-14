{
"views":  10,
"clicks":10,
"cost": 100
}

{
"from": "2021-11-01",
"to": "2021-11-02"
}

a = [
 {'date': "2021-11-01", "key2": 15, "key3": 7},
 {'date': "2021-11-04", "key2": 14, "key3": 8},
 {'date': "2021-11-02", "key2": 13, "key3": 8}
 ]


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

    


print(sort_list_of_dict_by_field(a))
