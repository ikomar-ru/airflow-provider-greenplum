__version__ = "1.0.0"

## This is needed to allow Airflow to pick up specific metadata fields it needs for certain features.
def get_provider_info():
    return {
        "package-name": "airflow-provider-greenplum",  # Required
        "name": "Greenplum",  # Required
        "description": "Greenplum provider for Apache Airflow.",  # Required
        "connection-types": [
            {
                "connection-type": "greenplum",
                "hook-class-name": "greenplum_provider.hooks.greenplum_hook.GreenplumHook"
            }
        ],
        "versions": [__version__],  # Required
    }
