import csv
import io
from . import models


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


def insert_to_db(content):

    models.CSVRecord.objects.all().delete()

    for row in content[1:]:

        models.CSVRecord(

            code=row[0],
            name=row[1],
            level_one=row[2],
            level_two=row[3],
            level_three=row[4],
            price=row[5],
            bid_price=row[6],
            number=row[7],
            property_fields=row[8],
            joint_purchase=row[9],
            unit=row[10],
            picture=row[11],
            display_onscreen=row[12],
            description=row[13],

        ).save()


def get_content():

    content = []

    for item in models.CSVRecord.objects.all():

        content.append([

            item.code,
            item.name,
            item.level_one,
            item.level_two,
            item.level_three,
            item.price,
            item.bid_price,
            item.number,
            item.property_fields,
            item.joint_purchase,
            item.unit,
            item.picture,
            item.display_onscreen,
            item.description
        ])

    return content
