import json

cannot_find_response = {
    'error': 'report could not be found'
}

invalid_id_response = {
    'error': 'proved a valid report id'
}

corrupted_response = {
    'error': 'corrupted data'
}


def test_missing_id(client):
    http_response = client.get('/report/3')

    assert json.loads(http_response.data.decode('UTF-8')) == cannot_find_response
    assert http_response.status_code == 404
    assert http_response.mimetype == 'application/json'


def test_invalid_request(client):
    http_response = client.get('/report/asd')

    assert json.loads(http_response.data.decode('UTF-8')) == invalid_id_response
    assert http_response.status_code == 400
    assert http_response.mimetype == cannot_find_response


def test_get_pdf(client):
    http_response = client.get('/report/1')

    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/pdf'


def test_corrupted_data(client):
    http_response = client.get('/report/5')

    assert json.loads(http_response.data.decode('UTF-8')) == corrupted_response
    assert http_response.status_code == 400
    assert http_response.mimetype == 'application/json'
