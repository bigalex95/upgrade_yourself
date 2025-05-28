void main() {
  var noodles = MenuItem("veg noodles", 9.99);
  var pizza = Pizza(["mushrooms", "peppers"], "veg volcano", 15.99);
  var roast = MenuItem("veggie roast dinner", 12.49);
  var kebab = MenuItem("plant kebab", 7.49);

  var foods = Collection<MenuItem>("Menu", [noodles, pizza, roast, kebab]);

  var random = foods.randomItem();
  print(random);
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

// NOTE: we create generic class with T - type, so we can define anytype what we need when call this class somewhere
class Collection<T> {
  String name;
  List<T> data;

  Collection(this.name, this.data);

  T randomItem() {
    data.shuffle();

    return data[0];
  }
}
