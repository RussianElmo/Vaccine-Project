import os.path, data, bottle, processing, json

def load_data():
    csv_file = 'saved_data.csv'
    if not os.path.isfile(csv_file):
        url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
        info = data.json_loader(url)
        heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer',\
                        'administered_unk_manuf','series_complete_pop_pct']
        data.save_data(heads, info, 'saved_data.csv')

@bottle.route('/')
def index():
    return bottle.static_file('index.html', root='.')


@bottle.route('/graphs.js')
def script():
    return bottle.static_file('graphs.js', root='.')



@bottle.route('/bar')
def bar():
    return json.dumps(processing.bar_graph())


@bottle.route('/pie')
def pie():
    return json.dumps(processing.pie_chart())


@bottle.post('/vacByDate')
def line():
    content = bottle.request.body.read().decode()
    return json.dumps(processing.line_graph(content))



load_data()
bottle.run(host='localhost', port=8080)