import random,requests
from swiper import config
from django.core.cache import cache

from worker import call_by_worker


def gen_verify_code(length = 6):
    '''产生验证码'''

    min_value = 10 ** (length-1)
    max_value = 10 ** length

    number = random.randrange(min_value, max_value)
    return number


import time
@call_by_worker
def send_verify_code(phonenum):
    '''发送验证码'''

    vcode = gen_verify_code()
    params = config.HY_SMS_PARAMS.copy()
    params['mobile'] = phonenum
    params['content'] = params['content'] % vcode
    #response = requests.post(config.HY_SMS_URL, data=params)
    cache.__setattr__('VCode-%s' % phonenum, vcode)
    print(f'VCode-{phonenum} ：{vcode}')
    time.sleep(30)
    print('async task finished')
    return cache.__getattr__('VCode-%s' % phonenum)


#send_verify_code = celery_app.task(send_verify_code)
#send_verify_code = send_verify_code.__add__()


def check_vcode(phonenum, vcode):
    vcode_cache = cache.__getattr__('VCode-%s' % phonenum)

    return vcode_cache == vcode



