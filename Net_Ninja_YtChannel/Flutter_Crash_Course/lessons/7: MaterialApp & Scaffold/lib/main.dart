import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text("My Coffee Id"),
          centerTitle: true,
          backgroundColor: Colors.brown[700],
        ),
        body: const Text("Hello Ninjas!"),
      ),
    ),
  );
}
