/// Demonstrates HTTP requests in Dart using the http package
/// Shows how to fetch data from an API and parse JSON responses
import "package:http/http.dart" as http;
import "dart:convert" as convert;

void main() async {
  final post = await fetchPost();
  print(post.title);
  print(post.userId);
}

/// Fetches a post from JSONPlaceholder API
/// Returns a Post object with title and userId
Future<Post> fetchPost() async {
  var uri = Uri.https('jsonplaceholder.typicode.com', 'posts/2');
  final headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'};

  try {
    final response = await http.get(uri, headers: headers);

    if (response.statusCode == 200) {
      Map<String, dynamic> data = convert.jsonDecode(response.body);
      return Post(data["title"], data["userId"]);
    } else {
      throw Exception('Failed to load post: ${response.statusCode}');
    }
  } catch (e) {
    throw Exception('Failed to load post: $e');
  }
}

/// Simple model class for Post data
class Post {
  String title;
  int userId;

  Post(this.title, this.userId);
}
