import requests
import logging
import json

def get_all(current_url):
    urls=[current_url]
    finished=False
    result_objects=[]
    for url in urls:
        logging.debug("Making request to URL: " + url)
        print("Making request to URL: " + url)
        response = requests.get(url=url)
        if response.status_code != 200:
            raise Exception(f"Received status code of {response.status_code}!")
        else:
            response_obj = json.loads(response.content)
            if response_obj.get('next'):
                urls.append(response_obj['next'])
            if response_obj.get('results'):
                for result in response_obj['results']:
                    result_objects.append(result)
    return result_objects

def get_one(current_url): #assume json
    response = requests.get(url=current_url)
    if response.status_code != 200:
        raise Exception(f"Received status code of {response.status_code}!")
    return json.loads(response.content)