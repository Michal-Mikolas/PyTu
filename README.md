# PyTu
My personal Python Tuuls :-) 

## Install & init
```
> pip install pytu
```

```py
from pytu.tools import Tools  # general python tools
from pytu.Matt import Matt    # GUI automation tool based on PyAutoGUI
```

## Logging
```py
Tools.log('Hello world')  # prints "[2022-02-07 16:31:14] Hello world"

Tools.log_path = "log/{year}-{month}-{day}_{hour}.log"  # from now log messages are also saved in text file
```

## Type conversions
```py
Tools.str(datetime.now())                      # "2022-02-07 16:31:14"
Tools.str("5.1234000")                         # "5.1234"
Tools.str(ValueError('something went wrong'))  # "ValueError: something went wrong"

Tools.datetime('7.2.2022')    # datetime(2022, 2, 7)
Tools.datetime('2/7/2022')    # datetime(2022, 2, 7)
Tools.datetime('2022-07-02')  # datetime(2022, 2, 7)
```

## Automation 
```py
# Init
matt = Matt(
	cache_file = 'temp/cache/matt.json',
	logger = Tools,
)
matt.set_ui({                     # recommended, but not mandatory
	'btn_ok' => 'ui/btn_ok.png',
	'btn_home' => 'ui/btn_home.png',
	'msg_ok' => 'ui/msg_ok.png',
	'msg_error' => 'ui/msg_error.png',
	'homescreen' => 'ui/homescreen.png',
})

# Automate
matt.click('btn_ok')

found = matt.which(['msg_ok', 'msg_error'])  # waits for one of the messages to show up
if found == 'msg_error':
	print('Error message found')
elif found == 'msg_ok':
	matt.click('btn_home')
	matt.wait('homepage')
```
