# report_exportation

Generating report PDF documents for given report id.


- URL  
```/report/{report_id}```

- Method:
GET 

- URL Params
Required:
report_id=[integer]

- Data Params
None

- Success Response:
```
Code: 200 
Content-type:application/pdf
Content-Disposition:attachment;filename=report{report_id}.pdf'
Content: PDF
```

- Error Response:
```
Code: 404 Report ID Not Found 
mimtype: 'application/json'
response: “{ 'error': 'report could not be found' }”
```
```
Code: 400 invalid report id
mimtype: 'application/json'
response: “{ 'error': 'proved a valid report id' }”
```
```
Code: 400 data is corrupted in the database
mimtype: 'application/json'
response: “{ 'error': 'corrupted data' }”
```

- Sample Call:
```python
import requests

if __name__ == '__main__':
    response = requests.get('http://127.0.0.1:5000/report/3')
    data = response.json()
    print(data)
```


