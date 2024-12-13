# Integry Python API Library

[![PyPI version](https://img.shields.io/pypi/v/integry.svg)](https://pypi.org/project/integry/)

The Python API library allows access to [Integry REST API](https://docs.integry.ai/apis-and-sdks/api-reference) from Python programs.

# Installation

```bash
# install from PyPI
pip install integry
```

# Usage

```python
import os
from integry import Integry

user_id = "your user's ID"

# Initialize the client
integry = Integry(
    app_secret=os.environ.get("INTEGRY_APP_KEY"),
    app_key=os.environ.get("INTEGRY_APP_SECRET"),
)

# Get the most relevant function
predictions = await integry.functions.predict(
    prompt="say hello to my team on Slack", user_id=user_id, predict_arguments=True
)

if predictions:
    function = predictions[0]
    # Call the function
    await function(user_id, function.arguments)
```

# Pagination
List methods are paginated and allow you to iterate over data without handling pagination manually.
```python
from integry import Integry

user_id = "your user's ID"

integry = Integry(
    app_secret=os.environ.get("INTEGRY_APP_KEY"),
    app_key=os.environ.get("INTEGRY_APP_SECRET"),
)

async for function in integry.functions.list(user_id):
    # do something with function
    print(function.name)
```

If you want to control pagination, you can fetch individual pages by using the `cursor` returned by the previous page.
```python
from integry import Integry

user_id = "your user's ID"

integry = Integry(
    app_secret=os.environ.get("INTEGRY_APP_KEY"),
    app_key=os.environ.get("INTEGRY_APP_SECRET"),
)

first_page = await integry.apps.list(user_id)

second_page = await integry.apps.list(user_id, cursor=first_page.cursor)
```
