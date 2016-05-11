

fn main() {
    assert_eq!(test_if_prime(7),true);
    assert_eq!(test_if_prime(35),false);

    let mut num_of_primes: u64 = 2;
    let mut progress: u64 = 3;

    while num_of_primes < 10001 {
        progress += 2;
        if test_if_prime(progress){
            num_of_primes += 1;
        }
    }
    println!("{}", progress);
}

fn test_if_prime(num: u64) -> bool{
    for a in 2..num {
        if num % a == 0 {
            return false;
        }
    }
    return true;
}
