import requests
import logging
import json

def get_all(current_url):
    urls=[current_url]
    finished=False
    result_objects=[]
    for url in urls:
        logging.debug("Making request to URL: " + url)
        response = requests.get(url=url)
        if response.status_code != 200:
            logging.error(f"Received HTTP status code of {response.status_code}!\nResponse: {str(response)}")
            raise Exception()
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
        logging.error(f"Received HTTP status code of {response.status_code}!\nResponse: {str(response)}")
        raise Exception()
    return json.loads(response.content)
    
    
def send_file_to_url(url, file_name):
    with open(file_name, "r") as csvfile:
        response = requests.post(url, files={file_name: csvfile})
        if response.status_code != 200:
            logging.error(f"Received HTTP status code of {response.status_code}!\nResponse: {str(response)}")
            raise Exception()