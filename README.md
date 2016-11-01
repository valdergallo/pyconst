# PyConst

[![Build Status](https://travis-ci.org/valdergallo/pyconst.svg?branch=master)](https://travis-ci.org/valdergallo/pyconst)
[![Coverage Status](https://coveralls.io/repos/github/valdergallo/pyconst/badge.svg?branch=master)](https://coveralls.io/github/valdergallo/pyconst?branch=master)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
[![Latest Version](http://img.shields.io/pypi/v/pyconst.svg)](https://pypi.python.org/pypi/pyconst)

## The problem

Everbody in Python need create a little constants in your project. I had been working with
Django Project and is a good pratices create constants for `permission` or any others
values that could be `global` in your project. And could be good for `translation`,
your IDE can help you with `autocomplete` and other things

Ok, everybody that use `constants` in your project is a good pratices :D

## Why I need this ?

Think that you need create one `const.py` with a lot `constants` and aggroup the values

```
ADD_USER = 'add_user'
UPDATE_USER = 'add_user'

USER_PERMISSIONS = (
    (ADD_USER, 'Add User'),
    (UPDATE_USER, 'Update User'),
)
```

Ok, this is simple, but think in a case that you have more than 100 values in your file.
Or think that you need create one constant with a similar name.

```
ADD_USER_PRIVATE = 'add_user_private'
```

You must check the value if is not duplicated, because you can overrind other values.

## The problem

In my module, now I'll need only one value from my `constant`

```
from company.const import (
    ADD_PERSON,
    EXCLUDE_PERSON,
    PERSON_STATE_START,
    PERSON_STATE_END,
    PERSON_STATE_WAITING,
    ...
    )
from .const import (
    USER_PERMISSIONS, 
    ADD_USER
    )

@has_perm(ADD_USER)
def my_example():
    choices = USER_PERMISSIONS
    ....

```

And think that you `USER_PERMISSIONS` could be bigger, with 30 permissions or more ...
`ADD_USER` no have any connection with `USER_PERMISSION`, I could have `ADD_USER` in a different
`constants` without connection with `USER_PERMISSION`, something like `ADMIN_DEFAULT_ACTIONS` or 
`MANAGER_CONSTANT`.

## The Solution (Morning Sun)

Yes, we working with Python. And now we can set the contants as one `Const`

```
from pyconst import Const

USER_PERMISSIONS = Const(
    'Add User',
    'Update User'
)

```

![Enable Auto Complate](https://github.com/valdergallo/pyconst/blob/master/screen_auto_complete.png "Enable Auto Complate")

And `USER_PERMISSION` will have one new attribute by `permission`

```
In [5]: USER_PERMISSIONS.add_user
Out[5]: 'add_user'

In [6]: USER_PERMISSIONS.add_user.label
Out[6]: u'Add User'
```

Check that is more easy undestand the constants and organize the values, and no need use
multiple imports to get values. Because the values are in `constants`

```
from company.const import COMPANY_PERMISSIONS
from company.const import COMPANY_WORKFLOW
from user.const import USER_PERMISSIONS

```

Example in `django model`

```
from pyconst import Const

USER_PERMISSIONS = Const(
    'Add User',
    'Update User'
)

class CustomUser(AbstractUser):
    
    class Meta:
        permissions = USER_PERMISSIONS

```

Add value in constants

```
>>> from pyconst import Const
>>> const = Const()
>>> cont.add(label='My Label Name', attr='my_attribute_name')
```

or

```
>>> from pyconst import Const
>>> const = Const('My Label Name')
```

or

```
>>> from pyconst import Const
>>> const = Const(('My Label Name', 'my_attribute_name'))
```

or

```
>>> c = Cont()
>>> c.add('First Item', 1)
>>> c._1 
'1'
```

or 

```
>>> c = Cont()
>>> c.add(label='First Item',attr="my_attr", value=1)
>>> c.my_attr 
'1'
```
