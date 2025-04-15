from datetime import datetime, timedelta

from . import helpers


def test_list_cash_drawer_shifts():
    client = helpers.test_client()
    begin_time = (datetime.now() - timedelta(seconds=1)).isoformat()
    end_time = datetime.now().isoformat()
    location_id = helpers.get_default_location_id(client)

    response = client.cash_drawers.shifts.list(
        location_id=location_id, begin_time=begin_time, end_time=end_time
    )

    assert response is not None
