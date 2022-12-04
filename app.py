from flask import Flask, render_template, jsonify, request
from util import get_1_data, get_2_data, get_3_data, find_years, find_types, find_table

app = Flask(__name__)


# main page
@app.route('/')
def hello_world():
    years = find_years()
    types, c = find_types('')
    return render_template("index.html", years=years, types=types)


#Histogram
@app.route('/echarts1', methods=['GET', 'POST'])
def echarts1():
    form = request.form.to_dict()
    data = get_1_data(form)
    if data:
        return jsonify({"data": data, "msg": True})
    return jsonify({"data": 'Can not find any information', "msg": False})

