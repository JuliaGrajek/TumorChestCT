from PIL import Image
from io import BytesIO

def read_imagefile(file) -> Image.Image:
    '''
    read image from file upload
    '''
    image = Image.open(BytesIO(file))
    return image

