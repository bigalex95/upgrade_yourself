void main() {
  var noodles = MenuItem("veg noodles", 9.99);
  var pizza = Pizza(["mushrooms", "peppers"], "veg volcano", 15.99);

  print(noodles.format());
  print(pizza.format());
}

// title, price, format() -> String
class MenuItem {
  String title;
  double price;

  MenuItem(this.title, this.price);

  String format() {
    return "$title --> $price";
  }
}

class Pizza extends MenuItem {
  List<String> toppings;

  // // NOTE: first way how to setup Parent class arguments
  // Pizza(this.toppings, String title, double price) : super(title, price);

  // NOTE: second way how to setup Parent class arguments
  Pizza(this.toppings, super.title, super.price);
}
