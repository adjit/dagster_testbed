from setuptools import find_packages, setup

setup(
    name="data_pipeline",
    packages=find_packages(exclude=["data_pipeline_dagster_tests"]),
    install_requires=[
        "dagster >= 1.3.1",
        "dagster-aws",
        "dagster-docker",
        "dagster-postgres",
        "dagster-k8s",
        "kafka-python",
        "pandas",
        "asyncio",
        "aiohttp",
        "pyodbc",
    ],
    extras_require={"dev": ["dagit", "pytest", "pytest-dotenv"]},
)
