import requests
import json

from flask import jsonify


def auth(data: dict):
    url = "http://172.16.0.5:8000/auth/"  # todo: Перенести в .env
    return requests.request("POST", url, data=json.dumps(data))


def insert_sample(access_token: str, data: dict):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    url = "http://172.16.0.5:8000/samples/"

    return requests.request("POST", url, headers=headers, data=json.dumps(data))


def stats_sample_min(access_token: str, data: dict):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    url = "http://172.16.0.5:8000/samples/min/" + data['month']

    return requests.request("GET", url, headers=headers, data=json.dumps(data))


def stats_sample_avg(access_token: str, data: dict):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    url = "http://172.16.0.5:8000/samples/avg/" + data['month']

    return requests.request("GET", url, headers=headers, data=json.dumps(data))


def stats_sample_max(access_token: str, data: dict):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    url = "http://172.16.0.5:8000/samples/max/" + data['month']

    return requests.request("GET", url, headers=headers, data=json.dumps(data))