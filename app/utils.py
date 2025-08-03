import string
import random
import re

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def is_valid_url(url: str) -> bool:
    # Simple regex-based URL validation
    regex = re.compile(
        r'^(https?://)?'                  # optional scheme
        r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,6})'   # domain...
        r'(:\d+)?'                       # optional port
        r'(/[A-Za-z0-9._~:/?#[\]@!$&\'()*+,;=-]*)?$'  # path, query etc
    )
    return bool(regex.match(url))
