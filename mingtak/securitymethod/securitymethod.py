from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder


from mingtak.securitymethod import MessageFactory as _


class ISecurityMethod(form.Schema, IImageScaleTraversable):
    """
    Define security method, use dexterity content type
    """
    leadImage = NamedBlobImage(
        title=_(u"Lead image"),
        required=True,
    )


class SecurityMethod(Container):
    grok.implements(ISecurityMethod)


class SampleView(grok.View):
    """ sample view class """

    grok.context(ISecurityMethod)
    grok.require('zope2.View')
    grok.name('view')
