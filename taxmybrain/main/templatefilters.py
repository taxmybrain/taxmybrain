import datetime
import decimal
from flask import Blueprint, Markup

blueprint = Blueprint('filters', __name__)


@blueprint.app_template_filter()
def datetimefilter(value, frmt='%d/%m/%Y'):
    """convert a date to a different format."""
    if value is None:
        return ''
    else:
        dt = datetime.datetime.strptime(value, '%Y-%m-%d')
        return dt.strftime(frmt)


@blueprint.app_template_filter()
def todecimal(value):
    """convert a number to a decimal"""
    if value is None:
        return ''
    else:
        return decimal.Decimal(str(value))

