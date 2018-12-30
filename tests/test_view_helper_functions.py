import pytest
from taxmybrain.main.views import (
    allowed_file, buildheaders, buildurl, create_user, periodkey_valid, number_valid,
    int_nodp_valid,
    )


def test_buildurl_allowed_file(app):
    with app.app_context():
        assert allowed_file('spreadsheet.csv') is True
        assert allowed_file('spreadsheet.xls') is True
        assert allowed_file('spreadsheet.xlsx') is True
        assert allowed_file('spreadsheet.exe') is False
        assert allowed_file('spreadsheet.') is False
        assert allowed_file('spreadsheet') is False

        
def test_buildheaders(app):
    with app.app_context():
        assert buildheaders(authcode='', govtest='') == {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'application/vnd.hmrc.1.0+json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ',
            'Gov-Test-Scenario': '', 
        }
        assert buildheaders(authcode='123456', govtest='') == {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'application/vnd.hmrc.1.0+json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 123456',
            'Gov-Test-Scenario': '', 
        }
        assert buildheaders(authcode='', govtest='SOMETHING') == {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'application/vnd.hmrc.1.0+json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ',
            'Gov-Test-Scenario': 'SOMETHING', 
        }
        assert buildheaders(authcode='6523411', govtest='OTHERTHING') == {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'application/vnd.hmrc.1.0+json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 6523411',
            'Gov-Test-Scenario': 'OTHERTHING', 
        }


def test_buildurl_create_test_user(app):
    with app.app_context():
        assert buildurl(endpoint='URL_CREATE_TEST_USER',
            vrn='', period='', parameters=[],
            api='test-api') == 'https://test-api.service.hmrc.gov.uk/create-test-user/organisations'
        assert buildurl(endpoint='URL_CREATE_TEST_USER',
            vrn='', period='', parameters=[],
            api='api') == 'https://api.service.hmrc.gov.uk/create-test-user/organisations'


def test_buildurl_get_obligations(app):
    with app.app_context():
        # note below that parameters is a list of tuples, not a dict. This is to ensure order of parameters is consistant for testing.
        assert buildurl(endpoint='URL_GET_OBLIGATIONS',
            vrn='666544036', period='', parameters=[('from', '2017-01-01'), ('to', '2017-12-01')],
            api='test-api') == 'https://test-api.service.hmrc.gov.uk/organisations/vat/666544036/obligations?from=2017-01-01&to=2017-12-01'
        assert buildurl(endpoint='URL_GET_OBLIGATIONS',
            vrn='666544036', period='', parameters=[('from', '2017-01-01'), ('to', '2017-12-01'), ('status', 'O')],
            api='test-api') == 'https://test-api.service.hmrc.gov.uk/organisations/vat/666544036/obligations?from=2017-01-01&to=2017-12-01&status=O'


def test_buildurl_submit_vat(app):
    with app.app_context():
        assert buildurl(endpoint='URL_SUBMIT_VAT',
            vrn='666544036', period='', parameters=[],
            api='test-api') == 'https://test-api.service.hmrc.gov.uk/organisations/vat/666544036/returns'


def test_buildurl_get_returns(app):
    with app.app_context():
        assert buildurl(endpoint='URL_GET_RETURNS',
            vrn='666544036', period='18A2', parameters=[],
            api='test-api') == 'https://test-api.service.hmrc.gov.uk/organisations/vat/666544036/returns/18A2'


def test_buildurl_get_liabilities(app):
    with app.app_context():
        assert buildurl(endpoint='URL_GET_LIABILITIES',
            vrn='666544036', period='', parameters=[],
            api='test-api') == 'https://test-api.service.hmrc.gov.uk/organisations/vat/666544036/liabilities'


def test_buildurl_get_payments(app):
    with app.app_context():
        assert buildurl(endpoint='URL_GET_PAYMENTS',
            vrn='666544036', period='', parameters=[],
            api='test-api') == 'https://test-api.service.hmrc.gov.uk/organisations/vat/666544036/payments'


def test_create_user(app):
    with app.app_context():
        r = create_user()
        assert r.status_code == 201


def test_periodkey_valid(app):
    # periodkey must be 4 alphanumeric characters and occasionally a # symbol
    assert periodkey_valid('18AD')
    assert periodkey_valid('18A1')
    assert periodkey_valid('#001')
    assert not periodkey_valid('24T ')
    assert not periodkey_valid('24T@')
    assert not periodkey_valid('1234A')
    assert not periodkey_valid(1234)


def test_number_valid(app):
    # value is passed as a string
    assert number_valid('999.00')
    assert number_valid('999.99')
    assert not number_valid('999.9')
    assert number_valid('999.01')
    assert number_valid('-9999999999999.99')
    assert number_valid('9999999999999.99')
    assert not number_valid('99999999999999.99')
    assert not number_valid('999')
    assert not number_valid('999.999')
    assert number_valid('9999999999999.99', lowerbound='0.00')
    assert not number_valid('-9999999999999.99', lowerbound='0.00')
    assert number_valid('999', dec_places=-1)
    assert number_valid('-999', dec_places=-1)
    assert number_valid('-9999999999999', dec_places=-1)
    assert number_valid('9999999999999', dec_places=-1)
    assert not number_valid('999.99', dec_places=-1)


def test_int_nodp_valid(app):
    # value is passed as a string
    # Must represent an integer between -9999999999999 and 9999999999999
    assert int_nodp_valid('999')
    assert int_nodp_valid('-999')
    assert int_nodp_valid('-9999999999999')
    assert int_nodp_valid('9999999999999')
    assert not int_nodp_valid('999.99')
    