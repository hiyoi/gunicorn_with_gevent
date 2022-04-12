import sys
import gevent
import time
import urllib.request
from gevent import monkey
monkey.patch_all()


def fetch_url(url):
    t0 = time.time()
    try:
        resp = urllib.request.urlopen(url)
        resp_code = resp.code
    except Exception:
        raise

    t1 = time.time()
    print("\t@ %5.2fs got response [%d]" % (t1 - t0, resp_code))
    return t1 - t0


def time_fetch_urls(url, num_jobs):
    print("Sending %d requests for %s..." % (num_jobs, url))
    t0 = time.time()
    jobs = [gevent.spawn(fetch_url, url) for i in range(num_jobs)]
    gevent.joinall(jobs)
    t1 = time.time()
    print("\t= %5.2fs TOTAL" % (t1 - t0))
    return t1 - t0


if __name__ == '__main__':

    try:
        num_requests = int(sys.argv[1])
    except IndexError:
        num_requests = 5

    t = time_fetch_urls("http://localhost:5500/db", num_requests)

    print("------------------------------------------")
    print("SUM TOTAL = %.2fs" % (t))
    print("RPS = {} /seconds".format(num_requests / t))
