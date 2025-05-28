void main() {
  // // NOTE: creating map same as a Set but its map
  // var planets = {"first": "mercury"};
  // print(planets);

  Map<String, String> planets = {
    "first": "mercury",
    "second": "venus",
    "third": "earth",
    "fourht": "mars",
    "fifth": "jupiter",
  };
  print(planets);

  // print(planets["third"]);

  // planets["third"] = "my planet";
  // print(planets["third"]);

  planets["sixth"] = "uranus";
  print(planets);

  print(planets.containsKey("third"));
  print(planets.containsKey("seventh"));
  print(planets.containsValue("earth"));

  print(planets.remove("earth"));
  print(planets.remove("third"));
  print(planets);

  print(planets.keys);
  print(planets.values);
}
