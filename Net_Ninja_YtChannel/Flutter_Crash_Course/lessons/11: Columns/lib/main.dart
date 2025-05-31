import 'package:coffee_card/home.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: Home()));
}

class Sandbox extends StatelessWidget {
  const Sandbox({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Sandbox"),
        backgroundColor: Colors.grey,
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Container(width: 100, color: Colors.red, child: const Text("one")),
          Container(width: 200, color: Colors.green, child: const Text("two")),
          Container(width: 300, color: Colors.blue, child: const Text("three")),
        ],
      ),
    );
  }
}
