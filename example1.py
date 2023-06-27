# Example1 to use OpenAIimage
import openai_image

# https://platform.openai.com/account/api-keys
API_KEY = 'your-secret-openai-api-key'

# PIC_SIZE = '256x256' or '512x512' or '1024x1024'
PIC_SIZE = '256x256'

IMAGES = ''
TARGET_TEXT = ''

# Use function:
openai_image.get_image(API_KEY, PIC_SIZE, IMAGES, TARGET_TEXT)

