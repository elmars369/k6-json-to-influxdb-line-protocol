# k6 JSON output conversion to InfluxDB line protocol
Contains Python scripts for converting the JSON output from k6 tests to InfluxDB's line protocol.

k6 test results can be sent directly to an InfluxDB database when running a test, for example:
>`k6 run --out influxdb=http://localhost:8086/k6 script.js`

But if you only have the results in JSON and want to send the data to an InfluxDB database after the fact, these scripts can be used for that.

## Required modules
InfluxDB-Python:
>`pip install influxdb`

## Examples:
1. Convert from JSON and write to InfluxDB database
```bash
python convert_and_write_to_db.py ../path/to/json/file
```
2. Convert from JSON and write to InfluxDB database, with parameters for the database
```bash
python convert_and_write_to_db.py ../path/to/json/file --host=example.com --port=8088 --username=admin --password=secret --db=k6_results
```
3. Convert from JSON and write result to file
```bash
python convert_and_write_to_file.py ../path/to/json/file ../path/to/output/file
```

## Tested with
Python 3.7.4

k6 v0.26.0 (dev build, go1.13.4, darwin/amd64)

InfluxDB 1.7.9

InfluxDB-Python 5.2.3
