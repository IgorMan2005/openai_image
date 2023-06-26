# openai_image
Python script for generating image from text by Open AI

### Install openai

**pip install openai**

### Install openai-image

**pip install openai-image**


### Recieve your OpenAI API KEY

https://platform.openai.com/account/api-keys

create settings.py:

put this key to settings.py file

**API_KEY = 'your-secret-openai-api-key'**

### Set image size

settings.py:

PIC_SIZE = '256x256'

('256x256', '512x512', '1024x1024')


### Mkdir images

Create folder 'images'

### Use openai_image

**import openai_image**

#### Example1:

openai_image.get_image()

Prompt target text: helicopter

Your image file ready: /images/helicopter.jpg

#### Example2:

openai_image.get_image('helicopter')

Your image file ready: /images/helicopter.jpg


