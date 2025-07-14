import pytest
from PIL import Image

def test_image_creation():
    # Create a simple image using Pillow
    img = Image.new('RGB', (100, 100), color='red')
    assert img.size == (100, 100)
    assert img.mode == 'RGB'
