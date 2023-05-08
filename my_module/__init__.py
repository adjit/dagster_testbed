from dagster import (
    Definitions,
    load_assets_from_modules,
    BindResourcesToJobs
)

from .assets.my_asset import asset_1_file
from .my_jobs import my_job

defs = Definitions(
    assets=[
        *load_assets_from_modules([asset_1_file], group_name='test_group_name')
    ],
    # jobs=BindResourcesToJobs([
    #     my_job.my_job
    # ])
)