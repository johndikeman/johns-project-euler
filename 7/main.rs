

fn main() {
    let mut num_of_primes: u64 = 2;
    let mut progress: u64 = 3;

    while(num_of_primes < 10001) {
        if test_if_prime(progress){
            num_of_primes += 1;
        }
        progress += 1
    }
}

fn test_if_prime(num: u64) -> bool{
    for a in 2..num {
        if num % a == 0 {
            return false;
        }
    }
    return true;
}
