import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("My Coffee Id"),
        centerTitle: true,
        backgroundColor: Colors.brown[700],
      ),
      body: const Text("Hello world!"),
    );
  }
}
