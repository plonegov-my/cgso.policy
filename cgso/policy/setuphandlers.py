from collective.grok import gs
from cgso.policy import MessageFactory as _

@gs.importstep(
    name=u'cgso.policy', 
    title=_('cgso.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('cgso.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
