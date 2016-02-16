# RbxAPI
Provides an API in Python that handles various interactions with the ROBLOX website, including:

* Logging in/out
* Handle multipul different accounts and configuration information for them.
* Get various ROBLOX validation tokens required to do various actions on the site
* Provide access to various methods and actions of the Trade Currency

This API is considered an ALPHA and is subject to change at any moment without prior notice, and break backwards 
compatibility between releases


Example Usage:
```python
from RbxAPI import login, LoggedInUser

login("Username", "Password")
print(LoggedInUser)
> Username
```


Read the source code for docs
