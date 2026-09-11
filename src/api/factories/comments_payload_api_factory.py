from src.api.models.comments_api_models import CommentPayload
from src.api.utils.api_util import _current_utc_timestamp
from src.factories.comment_payload_factory import prepare_random_comment


def prepare_comment_payload(article_id: int) -> CommentPayload:
    random_comment = prepare_random_comment()
    return CommentPayload(
        article_id=article_id,
        body=random_comment.body,
        date=_current_utc_timestamp(),
    )
    
    # return {
    #     "article_id": article_id,
    #     "body": random_comment.body,
    #     "date": _current_utc_timestamp(),
    # }
