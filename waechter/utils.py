import json
import requests

from pprint import pprint


def report_data(data_points, name, columns, influx_host='localhost', debug=False):
    stats = list()
    for key, value in data_points.items():
        stats.append([key, value])
    data = {
        'name': name,
        'columns': columns,
        'points': stats
    }
    if debug:
        print('|Inserting into "{0}" with columns"{1}"'.format(name, ' '.join(columns)))
        pprint(data)
    requests.post(influx_host, data=json.dumps([data, ]))
