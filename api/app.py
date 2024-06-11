from flask import Flask, jsonify, request
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

app = Flask(__name__)

# InfluxDB configuration
INFLUXDB_URL = "http://influxdb:8086"
INFLUXDB_TOKEN = "your_influxdb_token"
INFLUXDB_ORG = "your_influxdb_organization"
INFLUXDB_BUCKET = "your_influxdb_bucket"

# Initialize InfluxDB client
client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

@app.route('/api/data', methods=['POST'])
def write_to_influxdb():
    # Parse data from request
    data = request.json

    # Prepare data point for InfluxDB
    point = Point("your_measurement").tag("tag_key", "tag_value").field("field_key", data["field_value"])

    # Write data point to InfluxDB
    write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
