from django.shortcuts import render
from lib.http import render_json
from lib.sms import send_verify_code, check_vcode
from common import errors
from user.models import User


def get_verify_code(request):
    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum=phonenum)
    return render_json(None,)



def login(request):
    phonenum = request.Post.get('phonenum')
    vcode = request.Post.get('vcode')

    if check_vcode(phonenum=phonenum, vcode=vcode):
        user = User.objects.get_or_create(phonenum = phonenum)
        return render_json(user.to_dict())

    else:
        return render_json(None)

def show_profile(request):
    return render()


def modify_profile(request):
    return render()


def upload_avatar(request):
    return render()
