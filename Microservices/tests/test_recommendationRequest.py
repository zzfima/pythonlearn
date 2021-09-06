import pytest

from src.recommendations.recommendations_pb2 import BookCategory, RecommendationRequest


def test_recommendation_request_1():
    request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
    assert request.category == 1, "Should be 61"


def test_recommendation_request_2():
    with pytest.raises(TypeError) as excinfo:
        request = RecommendationRequest(user_id="oops", category=BookCategory.SCIENCE_FICTION, max_results=3)
    assert "'oops' has type str, but expected one of: int, long" in str(excinfo.value)
