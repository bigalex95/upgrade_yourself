// NOTE: pub.dev package manager for dart
// NOTE: we need http package for this unit
import "package:http/http.dart" as http;

import "dart:convert" as convert;

void main() async {
  final post = await fetchPost();
  print(post.title);
  print(post.userId);
}

Future<Post> fetchPost() async {
  var uri = Uri.https('jsonplaceholder.typicode.com', 'posts/2');

  // Add headers to mimic a browser request
  final headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'};

  try {
    final response = await http.get(uri, headers: headers);

    if (response.statusCode == 200) {
      // Parse JSON response
      Map<String, dynamic> data = convert.jsonDecode(response.body);
      return Post(data["title"], data["userId"]);
    } else {
      print('Failed with status code: ${response.statusCode}');
      print('Response headers: ${response.headers}');
      print('Response body: ${response.body}');
      throw Exception('Failed to load post: ${response.statusCode}');
    }
  } catch (e) {
    print('Error occurred during fetch: $e');
    throw Exception('Failed to load post: $e');
  }
}

class Post {
  String title;
  int userId;

  Post(this.title, this.userId);
}
