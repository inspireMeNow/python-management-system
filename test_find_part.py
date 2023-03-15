from pojo.part import Part
from service import part_service
from datetime import datetime
import json
import requests


if __name__ == "__main__":
    part = Part()
    part = part_service.find_by_code('pj00000002')
    print(part.to_json())
    print(json.dumps(part.to_json()))
    url = 'http://127.0.0.1:8088/part'
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=json.dumps(part.to_json()), headers=headers)
    print(r.json())

    # part_service.delete_by_code('pj00000001')
    # part.set_args('i7-13700k', 'cpu', 'intel', datetime.strptime(
    # '2022-12-07 18:18:49', '%Y-%m-%d %H:%M:%S'), 2, '散片', 40)
    # part.set_p_code('pj00000001')
    # part_service.update_by_code(part)
    # print(part_service.find_by_code('pj00000001').to_json())
    # for i in part_service.find_all():
    #     print(i)
