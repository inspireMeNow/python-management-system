from pojo.part import Part
from service import part_service
from datetime import datetime
import json
import requests


if __name__ == "__main__":
    data = {'p_code': 'pj00000002'}
    # url = 'http://127.0.0.1:8088/part'
    # headers = {'Content-Type': 'application/json'}
    # r = requests.post(url, data=json.dumps(part.to_json()), headers=headers)
    # print(r.json())

    # print(part_service.find_all())

    # # test search part
    # response = requests.get('http://localhost:8088/search_part', params=data)
    # response.encoding = 'utf-8'
    # new_data = json.dumps(response.text)
    # print(json.loads(new_data))

    # # test update part
    # data = {'p_code': 'pj00000001', 'p_name': 'i7-13700k', 'p_type': 'cpu', 'manufacture': 'intel',
    #         'protime': '2022-12-07 18:18:00', 'warranty_time': 2, 'info': '散片', 'size': 40}
    # response = requests.get('http://localhost:8088/update_part', params=data)
    # response.encoding = 'utf-8'
    # new_data = json.dumps(response.text)
    # print(new_data)

    # # test delete part
    # data = {'p_code': 'pj00000002'}
    # response = requests.get('http://localhost:8088/delete_part', params=data)
    # response.encoding = 'utf-8'
    # new_data = json.dumps(response.text)
    # print(new_data)

    # test insert part
    data = {'p_code': 'pj00000002', 'p_name': 'i7-13700k', 'p_type': 'cpu', 'manufacture': 'intel',
            'protime': '2022-12-07 18:18:00', 'warranty_time': 2, 'info': '散片', 'size': 40}
    response = requests.get('http://localhost:8088/insert_part', params=data)
    response.encoding = 'utf-8'
    new_data = json.dumps(response.text)
    print(new_data)