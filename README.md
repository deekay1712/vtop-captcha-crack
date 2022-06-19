# VTOP Captcha Crack

This is a simple pip package to crack VTOP captchas. It is kept simple and fast. To use it, you have to simply download the captcha image and pass it's path to the package.

## Instructions

1. Install:

```
pip install capthca-crack
```

2. Get the captcha:

```python
from captcha_crack import vtop

# initialise the load object
load = vtop.Load()
# you can use the relative path too
captchaPath = 'C:/Users/Alien/Desktop/Test/Captcha.png'
# the fucntion get_captcha_text(captchaPath) will return the text of the captcha
captchaText = load.get_captcha_text(captchaPath)

print(captchaText)
```

3. You're good to go! :rocket: