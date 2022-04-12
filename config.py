import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'


def when_ready(server):
    import psycogreen.gevent
    psycogreen.gevent.patch_psycopg()
    server.log.info("psycopg2 is patched")
