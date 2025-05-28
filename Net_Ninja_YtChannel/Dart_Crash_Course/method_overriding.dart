void main() {
  var noodles = MenuItem("veg noodles", 9.99);
  var pizza = Pizza(["mushrooms", "peppers"], "veg volcano", 15.99);

  print(noodles.format());
  print(pizza.format());

  print(noodles);
  print(pizza);
}

// title, price, format() -> String
class MenuItem {
  String title;
  double price;

  MenuItem(this.title, this.price);

  String format() {
    return "$title --> $price";
  }

  @override
  String toString() {
    return format();
  }
}

class Pizza extends MenuItem {
  List<String> toppings;

  Pizza(this.toppings, super.title, super.price);

  @override
  String format() {
    var formattedToppings = "Contains:";

    for (final topping in toppings) {
      formattedToppings = "$formattedToppings $topping";
    }

    return "$title --> €$price \n$formattedToppings";
  }

  @override
  String toString() {
    return "Instance of Pizza: $title, $price, $toppings";
  }
}
