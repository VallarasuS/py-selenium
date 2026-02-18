##  Web Driver

- Firefox
- Chrome
- Edge
- Safari
- Ie

```python
from selenium import webdriver

driver = webdriver.Firefox()    # Firefox
driver = webdriver.Chrome()     # Chrome
driver = webdriver.Edge()       # Edge
driver = webdriver.Safari()     # Safari
driver = webdriver.Ie()         # Internet Explorer
```

### Web Driver Methods

- close
- get
- quit
- refresh

``` python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("www.selenium.dev")  # load URL
driver.close()                  # close current tab
driver.quit()                   # quit browser
```

### X-Path

XPath Priority Ladder 2025
1. //*[@data-testid='login-button']
2. //button[@id='submit' or @name='submit']
3. //button[text()='Sign in']
4. //button[contains(text(),'Sign')]
5. //button[contains(@class,'btn-primary')]
6. //div[contains(@class,'modal')]//button[1]
7. //label[text()='Email']/following-sibling::input
8. //tr[td='John']//button[contains(text(),'Edit')]

Avoid if possible:
- /html/body/…
- //*[1]
- //div[5]
- long chains without attributes