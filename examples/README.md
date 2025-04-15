# Square legacy compatiblity

While the new SDK has a lot of improvements, we at Square understand that
it takes time to upgrade when there are breaking changes. To make the
migration easier, the new SDK can be used alongisde legacy SDK, which is
now published as `squareup_legacy`. 

This example demonstrates how you can use the legacy SDK alongside the new
SDK inside a single file.

```python
from square import Square
from square_legacy.client import Client as LegacySquare


def main():
    client = Square(token="<YOUR_API_KEY>")
    legacy_client = LegacySquare(access_token="<YOUR_API_KEY>")

    ...
```

You can run the example with the following:

```sh
cd example
poetry install
poetry run run-example
```