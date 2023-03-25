# -*- coding: utf-8 -*-

def etl_compilation_async():
    import celery
    celery  # load celery configuration
    from adltrack import tasks

    return tasks.etl_compilation.apply_async()
