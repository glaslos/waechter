import json
import requests

from pprint import pprint


def report_data(data_points, name, columns, influx_host='localhost', debug=False, dry_run=False):
    data = {
        'name': name,
        'columns': columns,
        'points': data_points
    }
    if debug:
        print('Inserting into: "{0}" with columns: "{1}"'.format(name, ', '.join(columns)))
        pprint(data)
    if not dry_run:
        requests.post(influx_host, data=json.dumps([data, ]))
