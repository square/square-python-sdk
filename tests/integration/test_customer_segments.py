from square.types.customer_segment import CustomerSegment

from . import helpers


def test_list_customer_segments():
    client = helpers.test_client()
    response = client.customers.segments.list()
    assert response.items is not None
    assert len(response.items) > 0


def test_retrieve_customer_segment():
    client = helpers.test_client()
    list_response = client.customers.segments.list()
    segments = list_response.items
    assert segments is not None
    assert len(segments) > 0
    segment = segments[0]
    segment_id = segment.id
    assert segment_id is not None
    response = client.customers.segments.get(segment_id=segment_id)
    assert response.segment is not None
    assert isinstance(response.segment, CustomerSegment)
    assert response.segment.name is not None
