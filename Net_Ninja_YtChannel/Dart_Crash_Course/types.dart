void main() {
  String name = "mario";
  name = "luigi";
  print(name);

  int age = 25;
  age = 30;
  print(age);

  bool isOpen = true;
  isOpen = false;
  print(isOpen);

  double averageRating = 7;
  averageRating = 7.9;
  print(averageRating);

  // // NOTE: Error: Non-nullable variable 'points' must be assigned before it can be used.
  // int points;
  // print(points);

  int? points;
  print(points);
}
