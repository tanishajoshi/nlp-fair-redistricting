import os
import io
from flask_cors import CORS
import seaborn as sns
import pandas as pd
from flask import send_file,  Flask, render_template, request, jsonify, abort
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from machine_learning.data import StoreData
import main
import printcode
plt.switch_backend('Agg')


store_data_obj = StoreData()
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static'
app.config['UPLOAD_EXTENSIONS'] = ['.csv']
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/graph')
def graph():
    return render_template('graph.html')


@app.route('/graph2')
def graph2():
    return render_template('graph2.html')


@app.route('/upload_static_file', methods=['POST'])
def upload_static_file():
    f = request.files['static_file']
    if f != '':
        file_ext = os.path.splitext(f.filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
    f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        app.config['UPLOAD_FOLDER'], f.filename))
    resp = {"success": True, "response": "file saved!", 'filename': f.filename}
    with open('code.txt', 'a', encoding='utf-8') as fle:
        fle.truncate(0)
    printcode.printcode_readcsv(f.filename)
    return jsonify(resp), 200


@app.route('/showdata', methods=['GET', 'POST'])
def show_data():
    filename = request.form['filename']
    df = pd.read_csv(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], filename))
    store_data_obj.setData(df)
    return jsonify({'df': df.to_html()})

@app.route('/clustering',methods = ['GET', 'POST'])
def clustering():
    
    sim_thresh = request.form.get("sim_thresh", False)
    num_clusters = request.form.get("clusters_size", False)
    df = store_data_obj.getData()
    res = main.cluster(df, sim_thresh, num_clusters)
    
    return jsonify(results = res)

@app.route('/preprocessing', methods=['GET', 'POST'])
def pre_process():
    selected_preprocess = request.form['preprocess']
    df = store_data_obj.getData()
    df = main.select_preprocess_feature(selected_preprocess, df)
    store_data_obj.setData(df)
    return jsonify({'df': df.to_html()})


@app.route('/train', methods=['GET', 'POST'])
def train_algo():
    output = request.form['output'].strip()
    independent = request.form['input'].strip()
    selected_model = request.form['selected_model']
    test_size = request.form['test_size']
    df = store_data_obj.getData()
    metric = main.train(df, output, independent, selected_model, test_size)
    return jsonify({'metric': metric})


@app.route('/datainfo', methods=['GET', 'POST'])
def info():
    selected_info = request.form['info']
    df = store_data_obj.getData()
    info = main.information(selected_info, df)
    return jsonify({'info': info.to_html()})


@app.route('/heatmap', methods=['GET'])
def heatmapGraph():
    df = store_data_obj.getData()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df.corr(), cmap='magma', annot=True)
    canvas = FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    plt.switch_backend('agg')
    print(ax, canvas)
    return send_file(img, mimetype='img/png')

########


@app.route('/isnull', methods=['GET'])
def innullGraph():
    df = store_data_obj.getData()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df.isnull(), cmap='magma', annot=True)
    canvas = FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    plt.switch_backend('agg')
    print(ax, canvas)
    return send_file(img, mimetype='img/png')
#######


@app.route('/printdata', methods=['GET', 'POST'])
def printdata():
    df = store_data_obj.getData()
    return jsonify({'df': df.to_html()})


@app.route('/printcode', methods=['GET', 'POST'])
def showcode():

    code = ""
    with open('code.txt', 'r', encoding='utf-8') as file:
        for line in file:
            code += line+'<br>'
        return jsonify({'code': code})

@app.route('/columns', methods=['GET', 'POST'])
def column():
    df = store_data_obj.getData()
    columns = df.columns.values.tolist()
    return jsonify({'columns': columns})


if __name__ == '__main__':
    app.run(debug=True)
