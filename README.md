# PyConst

## The problem

Everbody in Python need create a little constants in your project. I had been working with
Django Project and is a good pratices create constants for `permission` or any others
values that could be `global` in your project. And could be good for `translation`,
your IDE can help you ... and other things

Ok, everybody that use `constants` in your project is a good pratices :D


## But why this project ?

When I created one `cont.py` this file could be big and I need one right way to aggroup the values
with the constants.

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

You must check is the value is not duplicated, because you can overrind other values.

## The problem to use this


In my module, now I'll need only one value from my `constant`


```

from .const import USER_PERMISSIONS, ADD_USER

@has_perm(ADD_USER)
def my_example():
    ....

```

And think that you USER_PERMISSIONS could be bigger, with 30 permissions or more ...
Import all the `constants` could be more hard that you through.


# The Solution (Morning Sum)

Yes, we working with Python.

And now we can set the contants as one PyConst

```
from pyconst import PyConst

USER_PERMISSIONS = PyConst(
    'Add User',
    'Update User'
)

```

![Enable Auto Complate](https://github.com/valdergallo/pyconst/screen_auto_complete.png "Enable Auto Complate")

And `USER_PERMISSION` will have one new attribute by `permission`

```
In [5]: USER_PERMISSIONS.add_user
Out[5]: 'add_user'

In [6]: USER_PERMISSIONS.add_user.label
Out[6]: u'Add User'
```

