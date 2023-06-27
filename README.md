# openai_image
Python script for generating image from text by Open AI


<img src="https://igorman2005.github.io/images/openai-image.jpg" alt="openai_image">


**1. Install openai & openai-image**


```
pip install openai


pip install openai-image
```


**2. Recieve your OpenAI API KEY**

https://platform.openai.com/account/api-keys



**3. Settings**

```
API_KEY = 'your-secret-openai-api-key'

PIC_SIZE = '256x256'

IMAGES = ''

TARGET_TEXT = ''
```

PIC_SIZE options :'256x256', '512x512', '1024x1024'

IMAGES options: if IMAGES = '', script will use current folder. But you can set your own dir, for example: IMAGES = 'D:\Pictures'

TARGET_TEXT options: TARGET_TEXT = '', you will input your target text from keyboard. And you can set it in code, for example TARGET_TEXT = 'Alice in Wonderland'

**4. Use openai_image**

```
import openai_image
```

*Example1:*

```
import openai_image

API_KEY = 'your-secret-openai-api-key'

PIC_SIZE = '256x256'

IMAGES = ''

TARGET_TEXT = ''

openai_image.get_image(API_KEY, PIC_SIZE, IMAGES, TARGET_TEXT)

```
Prompt target text: **blue bird**

<img src="https://igorman2005.github.io/images/blue_bird.jpg" alt="openai_image blue bird">

Your image file ready: **blue_bird.png**



*Example2:*

```
from openai_image import *

API_KEY = 'your-secret-openai-api-key'

PIC_SIZE = '256x256'

IMAGES = 'D:\Pictures\'

TARGET_TEXT = 'Alice in Wonderland'

get_image(API_KEY, PIC_SIZE, IMAGES, TARGET_TEXT)


```

<img src="https://igorman2005.github.io/images/Alice_in_Wonderland.jpg" alt="openai image Alice in Wonderland">

Your image file ready: **D:\Pictures\Alice_in_Wonderland.png**


### Documentation

https://best-itpro.ru/news/openai_image/


That's All, Folks! 
;)