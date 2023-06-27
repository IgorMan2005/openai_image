
# pip install openai

try:
    import openai
except ImportError:
    print('You must install openai first: pip install openai\nDo it and try again')
    exit()

import os
import json
from base64 import b64decode

# You can use this function or https://pypi.org/project/screen-cls/
def cls():
    '''
    Python script for clearing screen for any OS's: Windows, MAC, Linux created by IgorMan
    cls()
    https://pypi.org/project/screen-cls/
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

def get_image(
        API_KEY='your-secret-openai-api-key', 
        PIC_SIZE='256x256',
        IMAGES = '',
        TARGET_TEXT = ''):
    '''
    Python script for generating image from text by Open AI created by IgorMan
    https://pypi.org/project/openai-image/
    
    pip install openai-image
    
    import openai_image

    openai_image.get_image(
        API_KEY='your-secret-openai-api-key', PIC_SIZE='256x256', IMAGES = '', TARGET_TEXT = ''
        )

    homepage: https://github.com/IgorMan2005/openai_image/
    '''

    cls()

    if TARGET_TEXT == '':
        TARGET_TEXT = input('Prompt target text: ')

    openai.api_key = API_KEY

    print('Just waiting...')

    try:
        response = openai.Image.create(
            prompt=TARGET_TEXT,
            n=1,
            size=PIC_SIZE,
            response_format='b64_json'
        )

        with open('openai_data.json', 'w') as file:
            json.dump(response, file, indent=4, ensure_ascii=False)

        image_data = b64decode(response['data'][0]['b64_json'])
        file_name = '_'.join(TARGET_TEXT.split(' '))

        path = os.getcwd()
        sep = os.sep

        if IMAGES == '':

            with open(f'{path}{sep}{file_name}.png', 'wb') as file:
                file.write(image_data)

            print(f'Your image file ready: {path}{sep}images{sep}{file_name}.png')

        else: 
            try:
                with open(f'{IMAGES}{sep}{file_name}.png', 'wb') as file:
                    file.write(image_data)
                    print(f'Your image file ready: {IMAGES}{sep}{file_name}.png')

            except:
                print(f'Save file error! Check you images folder: {IMAGES}')

        
    except:
        print('Receiving data error! Try once again...')



if __name__ == '__main__':
    print('You can install and use openai-image:')
    print('https://pypi.org/project/openai-image/')

