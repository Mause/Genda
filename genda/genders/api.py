import logging
import json as simplejson

from django.core.serializers import json

from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from .models import UserToPronoun, Pronoun


class MySerializer(Serializer):
    json_indent = 2

    def to_json(self, data, options=None):
        """ Pretty-print JSON """
        options = options or {}
        data = self.to_simple(data, options)
        return simplejson.dumps(
            data,
            cls=json.DjangoJSONEncoder,
            sort_keys=True,
            ensure_ascii=False,
            indent=self.json_indent
        )


class NoListsAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        raise Unauthorized("Sorry, no list reads.")

    def read_detail(self, object_list, bundle):
        # Is the requested object the user?
        return bundle.obj == bundle.request.user

    def create_list(self, object_list, bundle):
        raise Unauthorized("Sorry, no creates.")

    def create_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no creates.")

    def update_list(self, object_list, bundle):
        raise Unauthorized("Sorry, no updates.")

    def update_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no updates.")

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")


class AllPronounsResource(ModelResource):
    class Meta:
        resource_name = 'pronoun'
        queryset = Pronoun.objects.filter()
        max_limit = 0
        serializer = MySerializer()
        authorization = NoListsAuthorization()

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = super().detail_uri_kwargs(bundle_or_obj)

        from pprint import pprint
        pprint(kwargs)

        return kwargs

    def get_resource_uri(self, bundle_or_obj):
        uri = super().get_resource_uri(bundle_or_obj)

        uri, _ = uri.rsplit('/', 1)

        return uri

    def dehydrate(self, bundle):
        del bundle.data['id']
        return bundle

    @classmethod
    def should_skip_field(cls, field):
        if field.name == 'id':
            return False
        else:
            return ModelResource.should_skip_field(field)

    def obj_get(self, bundle, **kwargs):
        email_hash = kwargs.pop('pk')

        mapping = UserToPronoun.objects.filter(email_hash=email_hash)
        if not mapping:
            logging.info('No user for {}'.format(email_hash))
            return None
        else:
            mapping = mapping[0]

        return mapping.default_pronoun
