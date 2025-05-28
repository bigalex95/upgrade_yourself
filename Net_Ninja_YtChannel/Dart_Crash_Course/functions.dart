void main() {
  final greeting = greet(name: "mario", age: 25);
  print(greeting);
}

// // NOTE: positional arguments
// String greet(String name, int age) {
//   return "Hi, my name is $name and I am $age";
// }

// // NOTE: in this function String can be nullable but age need to be called
// // NOTE: name parameters
// String greet({String? name, required int age}) {
//   return "Hi, my name is $name and I am $age";
// }

// NOTE: both need to be called
// NOTE: name parameters
String greet({required String name, required int age}) {
  return "Hi, my name is $name and I am $age";
}
