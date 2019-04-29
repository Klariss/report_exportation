from flask import render_template, app
from fpdf import FPDF, HTMLMixin

from model.reportData import ReportData


class HTML2PDF(FPDF, HTMLMixin):

    def html_to_pdf(self, data: ReportData, file_name):
        template = render_template("pdf_template.html",
                                   org_name=data.org_name,
                                   report_date=data.report_date,
                                   render_timestamp=data.created_at,
                                   inventory=data.inventory)
        self.add_page()
        self.write_html(template)
        self.output(file_name)
