import data, csv, json

def max_value(data, key):
    largest = ''
    for dict in data:
        if dict[key] > largest:
            largest = dict[key]
    return largest


def init_dictionary(data, key):
    new_dict = {}
    for dict in data:
        if key in dict:
            v = dict[key]
            new_dict[v] = 0
    return new_dict


def sum_matches(lod, k, v, tgt):
    acc = 0
    for dict in lod:
        if dict[k] == v:
            acc += dict[tgt]
    return acc


def copy_matching(lod, k, v):
    l = []
    for dict in lod:
        if k in dict:
            if dict[k] == v:
                l.append(dict)
    return l

def bar_graph():
    ld = get_data('saved_data.csv')
    m = max_value(ld, 'date')
    upToDate = list(filter(lambda x: x['date'] == m, ld))
    locations = [x['location'] for x in upToDate]
    series_complete = [x['series_complete_pop_pct'] for x in upToDate]
    return [locations, series_complete]


def pie_chart():
    ld = get_data('saved_data.csv')
    m = max_value(ld, 'date')
    upToDate = list(filter(lambda x: x['date'] == m, ld))
    vaccines = data.make_lists(['administered_janssen', 'administered_moderna', 
    'administered_pfizer', 'administered_unk_manuf'], upToDate)
    vaccine_sums = [sum(int(row[i]) for row in vaccines) for i in range(len(vaccines[0]))]
    return vaccine_sums


def line_graph(location):
    location = json.loads(location)
    location = location.upper()
    ld = get_data('saved_data.csv')
    location_data = list(filter(lambda x: x['location'] == location, ld))
    series_complete = [x['series_complete_pop_pct'] for x in location_data]
    dates = [x['date'] for x in location_data]
    return [series_complete, dates]


def get_data(file):
    l = data.read_values('saved_data.csv')
    with open(file) as f:
        reader = csv.reader(f)
        header = next(reader)
    return data.dic_list_gen(header, l)

