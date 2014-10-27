import hashlib

from django.shortcuts import render_to_response, redirect
from django import forms
from django.template import RequestContext

from .models import Pronoun, UserToPronoun, Gender


def index(request):
    if request.user.is_authenticated():
        return redirect('/profile')

    return render_to_response('index.html')


class PronounChoiceForm(forms.Form):
    selected_pronoun = forms.ModelChoiceField(
        queryset=Pronoun.objects.all(),
    )
    selected_gender = forms.ModelChoiceField(
        queryset=Gender.objects.all(),
    )


def profile(request):
    if not request.user.is_authenticated():
        return redirect('/')

    try:
        mapping = UserToPronoun.objects.get(user=request.user)
    except UserToPronoun.does_not_exist:
        mapping = UserToPronoun()
        mapping.email_hash = hashlib.md5(request.user.email)

    if request.method == 'POST':
        form = PronounChoiceForm(request.POST)
    else:
        form = PronounChoiceForm(initial={
            'selected_pronoun': mapping.default_pronoun,
            'selected_gender': mapping.default_gender
        })
    if form.is_valid() and form.has_changed():
        mapping.default_pronoun = form.clean()['selected_pronoun']
        mapping.default_gender = form.clean()['selected_gender']
        mapping.save()

    return render_to_response(
        'profile.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


def demo(request):
    return render_to_response(
        'demo.html',
        context_instance=RequestContext(request)
    )
