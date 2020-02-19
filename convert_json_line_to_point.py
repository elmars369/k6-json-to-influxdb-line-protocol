import json


def convert_json_line_to_point(k6json_line):
    k6json = json.loads(k6json_line)
    if k6json["type"] == "Point":
        point = {
            "measurement": k6json["metric"],
            "tags": k6json["data"]["tags"],
            "time": k6json["data"]["time"],
            "fields": {
                "value": float(k6json["data"]["value"]),
            }
        }

        return point
