# Integry

Access [Integry REST API](https://docs.integry.ai/apis-and-sdks/api-reference) from JS/TS or Python programs.

# Get Started with Python

## 1. Installation

```bash
# install from PyPI
pip install integry
```

## 2. Usage
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
