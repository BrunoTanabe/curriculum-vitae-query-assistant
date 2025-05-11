from mongoengine import DateTimeField, Document, StringField, UUIDField

"""
The Model curriculum.py.
O modelo curriculum.py representa os logs das operações realizadas em currículos no sistema.

@Author Bruno Tanabe
@CreatedAt 2025-05-07
"""


class Curriculum(Document):
    request_id = UUIDField(
        db_field="request_id", required=True, unique=True, primary_key=True
    )

    user_id = UUIDField(
        db_field="user_id",
        required=True,
        # unique_with="request_id",
    )

    timestamp = DateTimeField(db_field="timestamp", required=True)

    query = StringField(
        db_field="query",
        required=False,
        max_length=256,
    )

    result = StringField(
        db_field="result",
        required=False,
    )

    meta = {
        "collection": "curriculum",
        "timeseries": {
            "timeField": "timestamp",
            "metaField": "metadata",
            "granularity": "seconds",
        },
        "ordering": ["-timestamp"],
    }
