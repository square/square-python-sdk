import time
import uuid

import pytest

from square.types.dispute import Dispute
from square.types.dispute_evidence import DisputeEvidence
from square.types.get_dispute_evidence_response import GetDisputeEvidenceResponse

from . import helpers


def create_dispute() -> str:
    client = helpers.test_client()

    # Create a payment that will generate a dispute
    client.payments.create(
        source_id="cnon:card-nonce-ok",
        idempotency_key=str(uuid.uuid4()),
        amount_money={"amount": 8803, "currency": "USD"},
    )

    # Poll for dispute to be created
    for _ in range(100):
        dispute_response = client.disputes.list(states="EVIDENCE_REQUIRED")
        if dispute_response.items is not None and len(dispute_response.items) > 0:
            assert dispute_response.items[0].id is not None
            return dispute_response.items[0].id

        # Wait for 2 seconds before polling again
        time.sleep(2)

    raise Exception("Could not create dispute")


def create_evidence_text(dispute_id: str) -> str:
    client = helpers.test_client()
    evidence_response = client.disputes.create_evidence_text(
        dispute_id=dispute_id,
        idempotency_key=str(uuid.uuid4()),
        evidence_text="This is not a duplicate",
        evidence_type="GENERIC_EVIDENCE",
    )
    evidence = evidence_response.evidence
    assert evidence is not None
    assert isinstance(evidence, DisputeEvidence)
    assert evidence.id is not None
    return evidence.id


def delete_dispute_evidence(*, dispute_id: str, text_evidence_id: str):
    client = helpers.test_client()
    # Clean up evidence if it exists
    try:
        client.disputes.evidence.delete(
            dispute_id=dispute_id, evidence_id=text_evidence_id
        )
    except Exception as e:
        # Evidence might already be deleted by test
        pass


def test_list_disputes():
    client = helpers.test_client()
    dispute_id = create_dispute()
    text_evidence_id = create_evidence_text(dispute_id)

    response = client.disputes.list(states="EVIDENCE_REQUIRED")
    assert response.items is not None
    assert len(response.items) > 0
    assert isinstance(response.items[0], Dispute)
    assert "DUPLICATE" == response.items[0].reason
    assert "EVIDENCE_REQUIRED" == response.items[0].state
    assert "VISA" == response.items[0].card_brand

    delete_dispute_evidence(dispute_id=dispute_id, text_evidence_id=text_evidence_id)


def test_retrieve_dispute():
    client = helpers.test_client()
    dispute_id = create_dispute()
    text_evidence_id = create_evidence_text(dispute_id)
    response = client.disputes.get(dispute_id=dispute_id)
    assert response.dispute is not None
    assert isinstance(response.dispute, Dispute)
    assert response.dispute.id

    delete_dispute_evidence(dispute_id=dispute_id, text_evidence_id=text_evidence_id)


def test_create_dispute_evidence_text():
    client = helpers.test_client()
    dispute_id = create_dispute()
    text_evidence_id = create_evidence_text(dispute_id)
    response = client.disputes.create_evidence_text(
        dispute_id=dispute_id,
        idempotency_key=str(uuid.uuid4()),
        evidence_text="This is not a duplicate",
        evidence_type="GENERIC_EVIDENCE",
    )
    assert response.evidence is not None

    delete_dispute_evidence(dispute_id=dispute_id, text_evidence_id=text_evidence_id)


def test_retrieve_dispute_evidence():
    client = helpers.test_client()
    dispute_id = create_dispute()
    text_evidence_id = create_evidence_text(dispute_id)
    response = client.disputes.evidence.get(
        dispute_id=dispute_id, evidence_id=text_evidence_id
    )
    assert response.evidence is not None
    assert isinstance(response, GetDisputeEvidenceResponse)
    assert text_evidence_id == response.evidence.id

    delete_dispute_evidence(dispute_id=dispute_id, text_evidence_id=text_evidence_id)


def test_list_dispute_evidence():
    client = helpers.test_client()
    dispute_id = create_dispute()
    text_evidence_id = create_evidence_text(dispute_id)
    response = client.disputes.evidence.delete(
        dispute_id=dispute_id, evidence_id=text_evidence_id
    )
    assert response is not None

    delete_dispute_evidence(dispute_id=dispute_id, text_evidence_id=text_evidence_id)


@pytest.mark.skip(
    reason="Temporarily skipping test_create_dispute_evidence_file; 'Evidence"
)
def test_create_dispute_evidence_file():
    client = helpers.test_client()
    dispute_id = create_dispute()
    text_evidence_id = create_evidence_text(dispute_id)

    response = client.disputes.create_evidence_file(
        dispute_id=dispute_id,
        image_file=helpers.get_test_file(),
        request={
            "idempotency_key": str(uuid.uuid4()),
            "content_type": "image/jpeg",
            "evidence_type": "GENERIC_EVIDENCE",
        },
    )

    assert response.evidence is not None
    assert isinstance(response.evidence, DisputeEvidence)
    assert dispute_id == response.evidence.id

    delete_dispute_evidence(dispute_id=dispute_id, text_evidence_id=text_evidence_id)


def test_submit_evidence():
    client = helpers.test_client()
    dispute_id = create_dispute()
    text_evidence_id = create_evidence_text(dispute_id)

    response = client.disputes.submit_evidence(dispute_id=dispute_id)
    assert response is not None

    delete_dispute_evidence(dispute_id=dispute_id, text_evidence_id=text_evidence_id)


def test_accept_dispute():
    client = helpers.test_client()
    dispute_id = create_dispute()
    text_evidence_id = create_evidence_text(dispute_id)

    response = client.disputes.accept(dispute_id=dispute_id)
    assert response is not None

    delete_dispute_evidence(dispute_id=dispute_id, text_evidence_id=text_evidence_id)
