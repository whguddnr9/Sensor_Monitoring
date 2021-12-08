import json
from flask import Flask, request, jsonify, render_template, make_response
import os
from view import send_json
# from module import parshingData

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


@app.route('/')
def hello():
    return 'helloworld'


@app.route('/chart')
def chart():
    return render_template('test_chart.html')


@app.route('/chart2')
def chart2():
    return render_template('test_chart2.html')

@app.route('/chart3')
def chart3():
    return render_template('test_chart3.html')
@app.route('/chart4')
def chart4():
    return render_template('test_chart4.html')
@app.route('/table')
def table_show():
    return render_template('test_table.html')



@app.route('/live-table')
def table():
    response = make_response(send_json.send_5_test())
    print("전부 보냈다.")
    response.content_type = 'application/json'
    # print("DATA:", data)
    return response


@app.route('/live-table-all')
def table_all():
    response = make_response(send_json.send_all_test())
    print("전부 보냈다.")
    response.content_type = 'application/json'
    # print("DATA:", data)
    return response


@app.route('/live-data')
def live_data():
    response = make_response(send_json.send_temp())
    print("temp보냈다")
    response.content_type = 'application/json'
    # print("DATA:", data)
    return response


@app.route('/live-data2')
def live_data2():
    response = make_response(send_json.send_humi())
    print("humi보냈다")
    response.content_type = 'application/json'
    # print("DATA:", data)
    return response

@app.route('/live-data3')
def live_data3():
    response = make_response(send_json.send_temp())
    print("temp보냈다")
    response.content_type = 'application/json'
    # print("DATA:", data)
    return response

@app.route('/live-data4')
def live_data4():
    response = make_response(send_json.send_temp_test())
    print("temp보냈다")
    response.content_type = 'application/json'
    # print("DATA:", data)
    return response

#############################


# @app.route('/graph')
# def graph():
#     return render_template('test_chart2.html', chartInfo=parshingData.get_Data())


if __name__ == '__main__' :
    app.run(debug=True, port=5000, host='0.0.0.0')
