from pyramid.view import view_config

@view_config(
    route_name='home',
    renderer='webassets_demo:templates/home.jinja2',
)
def home_view(request):
    return {'project': 'webassets_demo'}
