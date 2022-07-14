import json
from pathlib import Path

from erddapy.url_handling import check_url_response

data_sources = {
    "glider": "https://gliders.ioos.us/erddap/info/allDatasets/index.json",
    "ioos": "http://erddap.ioos.us/erddap/info/allDatasets/index.json",
}


def is_src_connected(src="glider"):
    url = data_sources[src]
    if url == check_url_response(url):
        return True
    else:
        return False


def check_server(colors, src):
    label = f"Data source {src}"
    status = "down"
    if is_src_connected(src=src):
        status = "up"

    # Create json file with full results for badge:
    color = colors[status]
    message = status
    data = {}
    data["schemaVersion"] = 1
    data["label"] = label
    data["message"] = message
    data["color"] = color
    fname = Path(f"status_{src}.json")
    fname.write_text(json.dumps(data))

    # Create text file with status:
    fname = Path(f"{src.upper()}.txt")
    fname.write_text(status.upper())


def save_status():
    colors = {"up": "green", "down": "red", "unknown": "black"}
    erddap_server_list = ["glider", "ioos"]
    for erddap in erddap_server_list:
        check_server(colors, src=erddap)


if __name__ == "__main__":
    save_status()
