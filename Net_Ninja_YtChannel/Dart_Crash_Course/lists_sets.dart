void main() {
  // // NOTE: List<int>
  // var scores = [50, 75, 20, 99];
  // print(scores);

  // // NOTE: List<Object>
  // var scores = [50, 75, 20, 99, "mario"];
  // print(scores);

  List<int> scores = [50, 75, 20, 99];
  print(scores);

  // // NOTE: Error: A value of type 'String' can't be assigned to a variable of type 'int'.
  // scores[0] = "hello";
  // print(scores[0]);

  scores.add(20);
  print(scores);

  scores.remove(20);
  print(scores);

  scores.removeLast();
  print(scores);

  scores.shuffle();
  print(scores);

  print(scores.indexOf(99));

  print(scores.length);

  // // NOTE: Set<String>
  // var names = {"mario", "luigi", "peache"};
  // print(names);

  Set<String> names = {"mario", "luigi", "peache"};
  print(names);

  //   // NOTE: same values(duplicates) cannot be in Set
  //   Set<String> names = {"mario", "luigi", "peache", "mario"};
  //   print(names);

  // NOTE: we can add same values in Set but dart not use it, and we see only one duplicate
  names.add("mario");
  print(names);

  names.add("bower");
  print(names);

  names.remove("luigi");
  print(names);

  print(names.length);
}
