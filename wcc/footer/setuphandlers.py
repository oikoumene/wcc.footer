from collective.grok import gs
from wcc.footer import MessageFactory as _

@gs.importstep(
    name=u'wcc.footer', 
    title=_('wcc.footer import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.footer.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
