from fpdf import FPDF, HTMLMixin


class HTML2PDF(FPDF, HTMLMixin):
    pass


html = '''<h1 align="center">PyFPDF HTML Demo</h1>
    <p>This is regular text</p>
    <p>You can also <b>bold</b>, <i>italicize</i> or <u>underline</ '''

pdf = HTML2PDF()
# First page
pdf.add_page()
pdf.write_html(html)
pdf.output('html.pdf', 'F')