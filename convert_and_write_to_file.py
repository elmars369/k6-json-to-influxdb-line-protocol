import argparse
import json
import datetime

from convert_json_line_to_point import convert_json_line_to_point
from influxdb.line_protocol import make_lines


def main(k6json_location, output_location):
    with open(k6json_location, 'r') as f:
        lines = f.readlines()

    output_file = open(output_location, 'w+')

    for line in lines:
        point = convert_json_line_to_point(line)
        if point:
            output_file.write(to_line_protocol(point))

    output_file.close()


def to_line_protocol(point):
    data = {
        'points': [point]
    }
    return make_lines(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'json', help='Location of the k6 JSON results file')
    parser.add_argument(
        'output', help='File where to save the converted result')
    args = parser.parse_args()
    main(args.json, args.output)
