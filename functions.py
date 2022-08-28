import json
import os


def search(path, primary_key):
    y = False
    for r, d, f in os.walk(path):
        if primary_key in f:
            y = True
            break
    return y


def creates_dir(schema):
    x = json.load(open(schema, 'r'))
    p = os.path.join(os.getcwd(), x['database_name'])
    os.mkdir(p)
    for i in x['Tables']:
        d = os.path.join(p, i['name'])
        os.mkdir(d)


def creates(schema, table, primary_key):
    x = json.load(open(schema, 'r'))
    path = os.getcwd() + '\\' + x['database_name'] + '\\' + table + '\\' + primary_key
    f = open(path, 'w')
    f.write("{\n")
    i = 0
    for k in x['Tables']:
        if k['name'] != table:
            i = i + 1
        else:
            break
    x = x['Tables'][i]
    i = len(x['columns'])
    j = 0
    for t in x['columns']:
        f.write("\t\"" + t + "\" : \"0\"")
        j = j + 1
        if j < i:
            f.write(",\n")
    f.write("\n}\n")
    f.close()


def sets(database, table, primary_key, parameter, value):
    path = os.getcwd() + '\\' + database + '\\' + table + '\\' + primary_key
    x = gets(database, table, primary_key)
    if not x:
        creates('Check-in-schema.json', table, primary_key)
        f = open(x, 'r')
        x = json.load(f)
        f.close()
    i = 0
    k = 0
    for k in x:
        if k != parameter:
            i = i + 1
        else:
            break
    x[k] = value
    f = open(path, 'w')
    json.dump(x, f)
    f.close()


def gets(database, table, primary_key):
    path = os.getcwd() + '\\' + database + '\\' + table
    if search(path, primary_key):
        f = open(path + '\\' + primary_key, 'r')
        e = json.load(f)
        f.close()
        return e
    else:
        return False


def deletes(database, table, primary_key):
    path = os.getcwd() + '\\' + database + '\\' + table
    if search(path, primary_key):
        os.remove(path + '\\' + primary_key)
        return True
    else:
        return False