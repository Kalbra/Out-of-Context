import functools
import random
import string

from flask import request, make_response, redirect

from api.models.models import Instance

from api.models.base import db


def check_cookie(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if 'ooc_auth' in request.cookies:
            auth_token = request.cookies.get('ooc_auth')

            instance = Instance.query.first()
            if instance:
                kwargs['instance_id'] = instance.id
            else:
                # Delete and reload page without fake cookie
                response = make_response(redirect('/'))
                response.set_cookie('ooc_auth', '', expires=0)
                return response

        else:
            auth_token = ''.join(random.choice(string.ascii_letters + "!#$%&'*+-.^_`|~") for i in range(100))
            new_instance = Instance(auth_token=auth_token)

            db.session.add(new_instance)
            db.session.commit()

            kwargs['instance_id'] = new_instance.id

        response = func(*args, **kwargs)
        response.set_cookie('ooc_auth', auth_token)

        return response

    return wrapper
