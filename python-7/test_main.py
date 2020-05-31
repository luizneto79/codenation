from unittest import mock
from unittest.mock import patch

import pytest
from main import (get_temperature, calculate_temperature,
                  _api_on)


@mock.patch('main.requests.head')
def test_api_online(mocked_head):
    # HTTP Response: OK
    mocked_head.return_value.status_code = 200
    assert _api_on(lat=-14.235004, lng=-51.92528) is True


@mock.patch('main.requests.head')
def test_api_offline(mocked_head):
    # HTTP Response: Not Found
    mocked_head.return_value.status_code = 404
    assert _api_on(lat=-14.235004, lng=-51.92528) is False


@pytest.mark.parametrize("temperature, expected", ((62, 16), (107, 41),
                                                   (32, 0)))
def test_calculate_temperature(temperature, expected):
    assert calculate_temperature(temperature) == expected


@pytest.mark.parametrize("lat, lng, temperature, expected",
                         ((-14.235004, -51.92528, 67, 19),
                          (-30.0277, -51.2287, 70, 21),
                          (-30.0277, -51.2287, 33, 0)))
def test_get_temperature_lat_lng(lat, lng, temperature, expected):

    mock_patcher = patch('main.requests.get')

    temperature = {
        'currently': {
            'temperature': temperature
        }
    }

    mocker = mock_patcher.start()
    mocker.return_value.json.return_value = temperature
    resp = get_temperature(lat, lng)
    mock_patcher.stop()

    assert resp == expected
