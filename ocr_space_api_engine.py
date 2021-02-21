import requests


def get_text_file(filename):
    api_key = 'e18f7b258888957'
    post_api = 'https://api.ocr.space/parse/image'
    OCREngine = 2

    payload = {'apikey': api_key,
               'ocrengine': OCREngine}

    with open(filename, 'rb') as file:
        req = requests.post(post_api,
                            files={filename: file},
                            data=payload)
    response = req.json()

    try:
        text_value = response['ParsedResults'][0]['ParsedText']
        return text_value
    except Exception as err:
        print(f'Could not find in {err} JSON Payload')
        print('Check POST Request')
        return None
