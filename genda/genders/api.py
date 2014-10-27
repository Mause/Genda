import logging
import json as simplejson

from django.core.serializers import json
from django.http import HttpResponse, Http404
from django.core import serializers

from .models import UserToPronoun

serialize = lambda data: simplejson.loads(
    serializers.serialize("json", [data])
)[0]['fields']


def resolve_mapping(request, email_hash):
    mapping = UserToPronoun.objects.filter(email_hash=email_hash)
    if not mapping:
        error = 'No user for {}'.format(email_hash)
        logging.info(error)
        raise Http404(error)
    else:
        mapping = mapping[0]

    data = {
        'pronouns': serialize(mapping.default_pronoun),
        'gender': serialize(
            mapping.default_gender
        ) if mapping.default_gender else None
    }

    return HttpResponse(simplejson.dumps(
        data,
        cls=json.DjangoJSONEncoder,
        sort_keys=True,
        ensure_ascii=False,
        indent=4
    ), content_type='application/json')
