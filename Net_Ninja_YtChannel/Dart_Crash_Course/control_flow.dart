void main() {
  List<int> scores = [50, 75, 20, 99, 100, 30];

  // for (int i = 0; i < 5; i++) {
  //   print("the current value of i is $i");
  // }

  // for (int score in scores) {
  //   print("the score is $score");
  // }

  // for (int score in scores) {
  //   if (score > 50) {
  //     print("the score is $score");
  //   } else {
  //     print("score not high enough");
  //   }
  // }

  for (int score in scores.where((s) => s > 50)) {
    print("the score is $score");
  }
}
