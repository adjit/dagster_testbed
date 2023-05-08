from dagster import (
    asset
)

@asset
def asset_1(context):
    return 123