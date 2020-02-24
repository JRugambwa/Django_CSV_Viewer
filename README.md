# Django_CSV_Viewer
project for processing file.csv

## Code example

```python
def parse_csv(content):
    reader = csv.reader(io.StringIO(content), delimiter=";")
    content = []

    for row in reader:
        content.append(row)

    columns_number = len(content[0])

    for row in content:

        if len(row) > columns_number:

            row[columns_number - 1] = ' '.join(row[columns_number - 1:])
            del row[columns_number:]

    return content
    
```
##Project pages
### start page
![START](https://sun9-19.userapi.com/c204820/v204820640/7ec5e/YrRP89xTZdE.jpg)
### page with file.csv
![END](https://sun9-61.userapi.com/c857628/v857628640/187846/4PFo2muKtQU.jpg)