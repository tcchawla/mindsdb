from mindsdb.integrations.libs.const import HANDLER_TYPE
from mindsdb.integrations.handlers.ray_serve_handler.__about__ import __version__ as version, __description__ as description
try:
    from mindsdb.integrations.handlers.ray_serve_handler.ray_serve_handler import RayServeHandler as Handler
    import_error = None
except Exception as e:
    Handler = None
    import_error = e

title = 'RayServe'
name = 'ray_serve'
type = HANDLER_TYPE.ML
icon_path = 'icon.svg'
permanent = True

__all__ = [
    'Handler', 'version', 'name', 'type', 'title', 'description', 'import_error', 'icon_path'
]
