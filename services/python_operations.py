import json


async def convert_mongo_result_to_dict(data):
    """ 
    convert mongo result to from string json to dict json 
    """
    converted_data = json.loads(data.to_json())

    if converted_data["created_at"]:
        # created_at = converted_data.pop("created_at")
        converted_data["created_at"] = await format_mongodate(data.created_at)

    if converted_data["updated_at"]:
        # updated_at = converted_data.pop("updated_at")
        converted_data["updated_at"] = await format_mongodate(data.updated_at)

    return converted_data


async def loop_through_queryset(queryset):
    """ 
    Handle formating for querysets
    """

    converted_data = json.loads(queryset.to_json())

    i = 0
    while i < queryset.count():
        converted_data[i] = await convert_mongo_result_to_dict(queryset[i])
        i += 1

    return converted_data


async def format_mongodate(date_data):
    """
    convert mongodate to readable format
    """
    # print(date_data.isoformat())
    # print(date_data.strftime("%d-%m-%Y, %H:%M:%S"))

    return date_data.isoformat()
