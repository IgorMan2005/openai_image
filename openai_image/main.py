# pip install openai

try:
    import openai
except ImportError:
    print('You must install openai first: pip install openai\nDo it and try again')
    exit()

try:
    import settings
except ImportError:
    print('You must have the settings.py file.\nCheck it and try again')
    exit()


import os
import json
from base64 import b64decode

def get_image(target_text=''):

    if target_text == '':
        target_text = input('Prompt target text: ')

    openai.api_key = settings.API_KEY


    try:
        response = openai.Image.create(
            prompt=target_text,
            n=1,
            size=settings.PIC_SIZE,
            response_format='b64_json'
        )

        with open('openai_data.json', 'w') as file:
            json.dump(response, file, indent=4, ensure_ascii=False)

        image_data = b64decode(response['data'][0]['b64_json'])
        file_name = '_'.join(target_text.split(' '))

        path = os.getcwd()
        sep = os.sep

        with open(f'{path}{sep}images{sep}{file_name}.jpg', 'wb') as file:
            file.write(image_data)

        print(f'Your image file ready: {path}{sep}images{sep}{file_name}.jpg')

    except:
        print('Receiving data error! Try once again...')




if __name__ == '__main__':
    get_image()


