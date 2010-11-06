from pyramid.configuration import Configurator
from imhotep.models import get_root

def app(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """
    config = Configurator(root_factory=get_root, settings=settings)
    config.begin()
    config.add_view('imhotep.views.my_view',
                    context='imhotep.models.MyModel',
                    renderer='imhotep:templates/mytemplate.pt')
    config.add_static_view('static', 'imhotep:static')
    config.end()
    return config.make_wsgi_app()

