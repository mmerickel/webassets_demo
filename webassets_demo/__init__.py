from pyramid.config import Configurator
from webassets import Bundle

def static_assets(config):
    config.include('pyramid_webassets')
    config.add_jinja2_extension('webassets.ext.jinja2.AssetsExtension')

    webassets_env = config.get_webassets_env()
    webassets_env.config['LESS_RUN_IN_DEBUG'] = False

    jinja2_env = config.get_jinja2_environment()
    jinja2_env.assets_environment = webassets_env

    def setup_bootstrap(env):
        js = Bundle(
            'bootstrap/js/bootstrap-*.js',
            filters='jsmin',
            output='gen/bootstrap.js',
        )

        if env.debug:
            js.contents += (
                'http://lesscss.googlecode.com/files/less-1.3.0.min.js',
            )
        config.add_webasset('bootstrap_js', js)

        css = Bundle(
            'bootstrap/less/bootstrap.less',
            filters='less',
            extra={'rel': 'stylesheet/less' if env.debug else 'stylesheet'},
            output='gen/bootstrap.css',
        )
        config.add_webasset('bootstrap_css', css)

    setup_bootstrap(webassets_env)

    config.add_static_view('static', 'static')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')

    config.include(static_assets)

    config.add_route('home', '/')
    config.scan('.views')
    return config.make_wsgi_app()
