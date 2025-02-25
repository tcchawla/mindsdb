from .__about__ import (
    __description__ as description,
    __version__ as version,
)
from mindsdb.integrations.libs.const import HANDLER_TYPE

try:
    from .popularity_recommender_handler import PopularityRecommenderHandler as Handler

    import_error = None
except Exception as e:
    Handler = None
    import_error = e

title = "Popularity_Recommender"
name = "popularity_recommender"
type = HANDLER_TYPE.ML
icon_path = "icon.svg"
permanent = True

__all__ = ["Handler", "version", "name", "type", "title", "description", "import_error", "icon_path"]
