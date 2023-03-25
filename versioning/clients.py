# -*- coding: utf-8 -*-

def etl_elasticsearch_async():
    import celery
    celery  # load celery configuration
    from versioning import tasks

    return tasks.etl_elasticsearch.apply_async()
