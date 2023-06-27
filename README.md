# openai_image
Python script for generating image from text by Open AI

**1. Install openai & openai-image**


```
pip install openai


pip install openai-image
```


**2. Recieve your OpenAI API KEY**

https://platform.openai.com/account/api-keys

create file settings.py in your folder/

put this key to settings.py file

```
API_KEY = 'your-secret-openai-api-key'
```

**3. Set image size**

settings.py:

```
PIC_SIZE = '256x256'
```

(options :'256x256', '512x512', '1024x1024')


**4. Mkdir images**

Create folder 'images' (foder for ready images)

**5. Use openai_image**

```
import openai_image
```

*Example1:*

```
import openai_image

openai_image.get_image()

```
Prompt target text: **helicopter**

Your image file ready: /images/helicopter.jpg



*Example2:*

```
import openai_image

openai_image.get_image('helicopter')

```
Your image file ready: /images/helicopter.jpg


That's All, Folks! 
;)