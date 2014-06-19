use std::io::println;

#[test]
fn test_is_three_div_three() {
  if !div_three(3) {
    fail!("should be div 3");
  }
}

fn div_three(num: int) -> bool {
  return false;
}

fn main() {
  println("fizzbuzz starting...");

}
