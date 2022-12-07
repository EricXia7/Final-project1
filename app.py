from flask import Flask, render_template, jsonify, request
from util import get_1_data, get_2_data, get_3_data, find_years, find_types, find_table

app = Flask(__name__)

'''main page'''
@app.route('/')
def hello_world():
    years = find_years()
    types, c = find_types('')
    return render_template("index.html", years=years, types=types)


'''Histogram'''
@app.route('/echarts1', methods=['GET', 'POST'])
def echarts1():
    form = request.form.to_dict()
    data = get_1_data(form)
    if data:
        return jsonify({"data": data, "msg": True})
    return jsonify({"data": 'Can not find any information', "msg": False})

'''line chart'''
@app.route('/echarts2', methods=['GET', 'POST'])
def echarts2():
    form = request.form.to_dict()
    data = get_2_data(form)
    data = [i for i in data if i]
    if data:
        data1, data2, data3, data4,data5, years = data
        return jsonify({"data1": data1, "data2": data2, "data3": data3, "data4": data4,"data5": data5,"years": years, "msg": True})
    return jsonify({"data": 'Can not find any information', "msg": False})


'''pie chart'''
@app.route('/echarts3', methods=['GET', 'POST'])
def echarts3():
    form = request.form.to_dict()
    print(form)
    data = get_3_data(form)
    data = [i for i in data if i]
    if data:
        types, data = data
        return jsonify({"types": types, "data": data, "msg": True})
    return jsonify({"data": "can not find the data", "msg": False})


'''connect to the table'''
@app.route('/info/all', methods=['GET', 'POST'])
def info_search():
    data = find_table()
    return jsonify({"msg": True, "data": data})


if __name__ == '__main__':
    app.run()