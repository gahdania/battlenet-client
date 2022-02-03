import pytest

from battlenet_client.bnet import exceptions


def test_get_not_found(client):
    with pytest.raises(exceptions.BNetDataNotFoundError):
        client.api_get(
            f"{client.api_host}/data/wow/playable-class/-1",
            "en_US",
            headers={"Battlenet-Namespace": "static-us"},
        )


def test_get_found(client):
    data = client.api_get(
        f"{client.api_host}/data/wow/playable-class/1",
        "enus",
        headers={"Battlenet-Namespace": "static-us"},
    )
    assert type(data) == dict


def test_post_not_found(client):
    with pytest.raises(exceptions.BNetDataNotFoundError):
        client.api_post(
            f"{client.api_host}/data/wow/playable-class/-1",
            "en_US",
            headers={"Battlenet-Namespace": "static-us"},
        )


def test_post_invalid(client):
    with pytest.raises(exceptions.BNetDataNotFoundError):
        client.api_post(
            f"{client.api_host}/data/wow/playable-class/1",
            "enus",
            headers={"Battlenet-Namespace": "static-us"},
        )
