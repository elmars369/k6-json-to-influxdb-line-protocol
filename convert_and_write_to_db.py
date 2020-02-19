import argparse
import json

from influxdb import InfluxDBClient
from convert_json_line_to_point import convert_json_line_to_point


def main(k6json_location, host, port, username, password, database):
    with open(k6json_location, 'r') as f:
        lines = f.readlines()

    client = InfluxDBClient(host, port, username, password, database)

    points = []
    for line in lines:
        point = convert_json_line_to_point(line)
        if point:
            points.append(point)

    if points:
        client.write_points(points, batch_size=5000)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'json', help='Location of the k6 JSON results file')
    parser.add_argument(
        '--host', nargs='?', default='localhost', help='Host for connecting to InfluxDB instance')
    parser.add_argument(
        '--port', nargs='?', default=8086, type=int, help='Port on which InfluxDB is running on the host')
    parser.add_argument(
        '--username', nargs='?', default='', help='Username for accessing InfluxDB database')
    parser.add_argument(
        '--password', nargs='?', default='', help='Password for accessing InfluxDB database')
    parser.add_argument(
        '--db', nargs='?', default='k6', help='InfluxDB database name')
    args = parser.parse_args()
    main(args.json, args.host, args.port, args.username, args.password, args.db)
