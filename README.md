# PyTu

## Logging
```py
from pytu.tools import Tools

Tools.log('Hello world')  # prints "[2022-02-07 16:31:14] Hello world"

Tools.log_path = "log/{year}-{month}-{day}_{hour}.log"  # from now log messages are also saved in text file
```

## Type conversions
```py
Tools.str(datetime.now())                      # "2022-02-07 16:31:14"
Tools.str("5.1234000")                         # "5.123"
Tools.str(ValueError('something went wrong'))  # "ValueError: something went wrong"

Tools.datetime('7.2.2022')    # datetime(2022, 2, 7)
Tools.datetime('2/7/2022')    # datetime(2022, 2, 7)
Tools.datetime('2022-07-02')  # datetime(2022, 2, 7)
```

## Automation 
TODO: finish the docs
