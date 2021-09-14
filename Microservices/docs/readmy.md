https://realpython.com/python-microservices-grpc/

1. pip install requirements.txt
2. cd src\recommendations
3. recommendations.proto file:
- Line 1 specifies that the file uses the proto3 syntax instead of the older proto2 version.
- Lines 3 to 7 define your book categories, and each category is also assigned a numeric ID.
- Lines 9 to 13 define your API request. A message contains fields, each of a specific type. You’re using int32, which is a 32-bit integer, for the user_ID and max_results fields. You’re also using the BookCategory enum you defined above as the category type. In addition to each field having a name, it’s also assigned a numeric field ID. You can ignore this for now.
- Lines 15 to 18 define a new type that you can use for a book recommendation. It has a 32-bit integer ID and a string-based title.
- Lines 20 to 22 define your Recommendations microservice response. Note the repeated keyword, which indicates that the response actually has a list of BookRecommendation objects.
- Lines 24 to 26 define the method of the API. You can think of this like a function or a method on a class. It takes a RecommendationRequest and returns a RecommendationResponse.
4. python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto
5. 