import csv
import io


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
