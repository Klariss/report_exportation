from json import JSONDecodeError

from flask import send_file, Response, Blueprint
import json

from model.reportData import ReportData
from use_case.html_to_pdf import HTML2PDF
from repository.request_report import request_report

blueprint = Blueprint('report_pdf', __name__)


@blueprint.route("/report/<report_id>", methods=['GET'])
def report(report_id):
    if not (str.isdecimal(report_id)):
        return Response("{\"error\":\"proved a valid report id\"}", status=400, mimetype='application/json')

    response = request_report(report_id)

    if len(response) == 0:
        return Response("{\"error\":\"report could not be found\"}", status=404, mimetype='application/json')

    data = response[0][1]
    report_id = response[0][0]

    try:
        json_dict = json.loads(data)
    except JSONDecodeError:
        return Response("{\"error\":\"corrupted data\"}", status=400, mimetype='application/json')

    report_data = ReportData(report_id, json_dict)

    HTML2PDF().html_to_pdf(report_data, f'html2pdf{report_id}.pdf')
    return send_file(f'html2pdf{report_id}.pdf')
