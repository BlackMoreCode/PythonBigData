# app.py
from flask import Flask, jsonify
from data_analysis import get_gender_data
from flask_cors import CORS  # React와의 크로스 오리진 문제를 해결하기 위해 사용

app = Flask(__name__)
CORS(app)  # CORS 설정 (필요에 따라 옵션 조정 가능)

@app.route('/api/gender/<region>', methods=['GET'])
def gender_data(region):
    """
    URL의 지역(region)을 기반으로 CSV 파일에서 남녀 인구 데이터를 읽어 JSON 형태로 반환합니다.
    """
    data = get_gender_data(region)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
