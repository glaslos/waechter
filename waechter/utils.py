import json
import requests

from pprint import pprint


def report_data(data_points, influx_host):
    stats = list()
    for key, value in data_points.items():
        stats.append([key, value])
    data = {
        "name": "asgard.queue.gauges",
        "columns": ["queue_name", "value"],
        "points": stats
    }
    pprint(data)
    requests.post(influx_host, data=json.dumps([data, ]))
