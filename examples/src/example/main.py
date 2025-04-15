"""
Example script demonstrating how to use both square and square_legacy packages together.
"""

from square_legacy.client import Client as LegacySquare  # type: ignore

from square import Square


def main():
    print("Using both square and square_legacy packages together")

    # Initialize clients from both packages
    client = Square(token="<YOUR_API_KEY>")
    legacy_client = LegacySquare(access_token="<YOUR_API_KEY>")

    # Use functionality from new client
    print("\nUsing new square client:")
    try:
        response = client.payments.list()
        print(f"New client payment results: {response.items}")
    except Exception as e:
        print(f"Example new client call failed: {e}")

    # Use functionality from legacy client
    print("\nUsing legacy square client:")
    try:
        legacy_response = legacy_client.payments.list_payments()
        print(f"Legacy client payment results: {legacy_response}")
    except Exception as e:
        print(f"Example legacy client call failed: {e}")


if __name__ == "__main__":
    main()
