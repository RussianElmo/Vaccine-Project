import csv, urllib.request as r, json

def dic_list_gen(ls, ll):
    result = []
    for l in ll:    # loops through lists in list of lists
        dict = {}
        for i in range(len(ls)):  # loops through strings in list of strings
            dict[ls[i]] = l[i]
        result.append(dict)
    return result


def read_values(file):
    result = []
    with open(file) as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            result.append(row)
    return result


def make_lists(keys, ld):
    result = []
    for d in ld:
        temp = []
        for key in keys:
            temp.append(d[key])
        result.append(temp)
    return result


def write_values(file, ll):
    with open(file, 'a') as f:
        writer = csv.writer(f)
        for row in ll:
            writer.writerow(row)
        

def json_loader(url):
    return json.loads(r.urlopen(url).read().decode())


def make_values_numeric(keys, dict):
    for key in keys:
        dict[key] = float(dict[key])
    return dict


def save_data(keys, ld, file):
    ll = make_lists(keys, ld)
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(keys)
        for l in ll:
            writer.writerow(l)


def load_data(file):
    values = read_values(file)
    with open(file, 'r') as f:
        reader = csv.reader(f)
        return dic_list_gen(next(reader), values)


