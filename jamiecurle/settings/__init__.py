from default import *

try:
    from local import *
except ImportError:
    pass

#
#
#  add in the dev stuff

#try:
#    INSTALLED_APPS += DEV_APPS
#except NameError:
#    pass


#try:
#    MIDDLEWARE_CLASSES += DEV_MIDDLEWARE
#except NameError:
#    pass
