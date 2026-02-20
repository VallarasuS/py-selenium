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
---

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
---

#### FORMAT

- `// tag-name [ @attribute-name = 'attribute-value' ]`
- `// tag-name [contains ( @attribute-name, 'partial' )]`

### Examples

- //*[@data-testid='login-button']
- //button[@id='submit' or @name='submit']
- //button[text()='Sign in']
- //button[contains(text(),'Sign')]
- //button[contains(@class,'btn-primary')]
- //div[contains(@class,'modal')]//button[1]
- //label[text()='Email']/following-sibling::input
- //tr[td='John']//button[contains(text(),'Edit')]


### CSS

#### Format

| type     | syntax    | example                                            |
|----------|-----------|----------------------------------------------------|
| tag-name | only name | `a`, `button`, `input`, `select`, `div`            |
| id       | #id       | `#search-input`, `#email-input`, `#password-field` |
| class    | .class    | `.btn`, `.button-primary`, `.side-bar`             |


