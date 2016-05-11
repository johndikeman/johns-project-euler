

fn main() {
    let mut sum: u64 = 3;

    for num in 4..2000001 {
        if test_if_prime(num) {
            sum += num;
        }
    }
    println!("{}",sum)
}

fn test_if_prime(num: u64) -> bool{
    for a in 2..num {
        if num % a == 0 {
            return false;
        }
    }
    return true;
}
