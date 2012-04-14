import os
import memcache
import yaml
from fabric.api import *

LOCAL_ROOT = os.path.dirname(os.path.abspath(__file__))
#
#
#---------------------- CONFIG --------------------------
stream = open('%s/fabfile.yaml' % LOCAL_ROOT, 'r')
configfile = yaml.load(stream)
stream.close()
for key, value in configfile.items():
    setattr(env, key, value)
#
#
# ------------------- DEVLOPMENT--------------------------

def test(apps=""):
    """Clears the screen and runs the tests om the test project"""
    local('clear')
    local('%s/manage.py test %s --setting=jamiecurle.settings.test'\
                 % ( LOCAL_ROOT, apps))

def kill_cache_dev(key=None):
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    if key is None:
        mc.flush_all()
    else:
        mc.delete(key)

#
#
# -------------------- OMBLOG
@with_settings(warn_only=True)
def install_production_omblog():
    """installs cccheckout using the version in the requirements file"""
    req = local('cat requirements.txt | grep obscuremetaphor-blog',
                capture=True)
    remove_omblog()
    local('pip install %s' % req)


@with_settings(warn_only=True)
def remove_omblog():
    """removees cccheckout completly"""
    #with hide('stderr', 'warnings', 'stdout'):
    local('pip uninstall obscuremetaphor-blog')
    local('rm -rf %(site_packages)s/omblog' % env)

def edit_dev_omblog():
    """opens cccheckout in TextMate"""
    local('mate %(omblog_project)s' % env)


@with_settings(warn_only=True)
def install_dev_omblog():
    """Installs the development copy of cccheckout"""
    remove_omblog()
    local('ln -s %(omblog_src)s %(site_packages)s/omblog' % env )




#
#
# ---------------------- OLDSTUFF ------------------------
"""
#import datetime
#import memcache

@with_settings(warn_only=True):
def install_dev_omblog():

    local('rm -rf %s/omblog %s/obscuremetaphor_blog-0.0.3-py2.7.egg-info' % 
                (om_settings.SITE_PACKAGES, om_settings.SITE_PACKAGES))
    local('ln -s  %s %somblog' % 
                (om_settings.DEV_OMBLOG_PATH, om_settings.SITE_PACKAGES))




def compress_css():
    with lcd('/Users/jcurle/Sites/jamiecurle/jamiecurle/static/css/'):
        local('cssprefixer global.css about.css syntax.css devices.css  --minify > production.css')

def mem():
    run('ps -u curle -o pid,rss,command')

def restart_nginx():
    run('nginx -s reload')

"""