# Example2 to use OpenAIimage
from openai_image import *

# https://platform.openai.com/account/api-keys
API_KEY = 'your-secret-openai-api-key'

# PIC_SIZE = '256x256' or '512x512' or '1024x1024'
PIC_SIZE = '256x256'

IMAGES = 'D:\Pictures'
TARGET_TEXT = 'Alice in Wonderland'

# Use function:
get_image(API_KEY, PIC_SIZE, IMAGES, TARGET_TEXT)


