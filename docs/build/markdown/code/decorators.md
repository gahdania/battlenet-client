# Decorators


### battlenet_client.decorators.verify_region(func)
Verifies the function’s first parameter is a valid region abbreviation


* **Raises**

    **BNetRegionNotFoundError** – when the region (arg[0]) is not a valid region tag
