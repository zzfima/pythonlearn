import pytest
import grpc

from src.recommendations.recommendations_pb2 import BookCategory, RecommendationRequest
from src.recommendations.recommendations_pb2_grpc import RecommendationsStub


def test_recommendation_request_1():
    request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
    assert request.category == 1, "Should be 1"


def test_recommendation_request_2():
    with pytest.raises(TypeError) as excinfo:
        request = RecommendationRequest(user_id="oops", category=BookCategory.SCIENCE_FICTION, max_results=3)
    assert "'oops' has type str, but expected one of: int, long" in str(excinfo.value)


def test_recommendation_request_3():
    request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION)
    assert request.max_results == 0, "Should be 0"


def test_recommendation_request_4():
    channel = grpc.insecure_channel("localhost:50051")
    client = RecommendationsStub(channel)
    request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
    client.Recommend(request)
