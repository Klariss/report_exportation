

class ReportData:
    def __init__(self, report_id, data_dict):
        self.report_id = report_id
        self.org_name = data_dict['organization']
        self.report_date = data_dict['reported_at']
        self.created_at = data_dict['created_at']
        self.inventory = [(item['name'], item['price']) for item in data_dict['inventory']]
