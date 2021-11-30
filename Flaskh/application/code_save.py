from application.models import Savedcode


def code_save(user_id=None):
    savedCode = list(Savedcode.objects.aggregate(*[
    {
        '$match': {
            'user_id': user_id
        }
    }
]))
    return savedCode