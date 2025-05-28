void main() {
  var name = "mario";
  print(name);

  // // NOTE:  Error: A value of type 'int' can't be assigned to a variable of type 'String'.
  // name = 15;
  // print(name);

  // name = "luigi";
  // print(name);

  // final age = 25;
  // // NOTE: Error: Can't assign to the final variable 'age'.
  // age = 26;

  // const isOpen = true;
  // // NOTE: Error: Can't assign to the const variable 'isOpen'.
  // isOpen = false;

  const age = 25;
  print(age);

  // print(age + 10);
  // print(age - 10);
  // print(age * 10);
  // print(age / 5);
  // print(age % 10);

  print("my name is " + name);
  print("my name is $name and my age is $age");
  print("my name is ${name}");
}
