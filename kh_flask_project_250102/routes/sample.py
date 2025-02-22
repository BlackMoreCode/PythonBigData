from flask import Response
import json


def root_print():
    return "안녕하세요. Flask Main입니다."

def subway_info():
    data = {
        "station": ["강남역", "역삼역", "서울역"],
        "ridership": [19000, 9800, 22000]
    }

    response = Response(json.dumps(data, ensure_ascii=False),
                                   mimetype='application/json; charset=utf-8')
    return response