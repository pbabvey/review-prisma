from flask import Flask, render_template, request

from plot import plot_wells, query_db

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/plot', methods=['POST'])
def plot():
    depth_min = request.form['depth_min']
    grad_min = request.form['grad_min']

    chart_json = plot()
    
    return render_template('plot.html', chart=chart_json)


if __name__ == '__main__':
    app.run(debug=True)
