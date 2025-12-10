# Question 2 
# Write a program that finds all prime numbers up to a given limit (maximum 100), and 
# display: 
# • the total count of prime numbers found 
# • the smallest and largest prime number in the range 
# • the sum of all prime numbers found 
 
# Example: 
# Input: 20 
# Output: 
# Prime numbers found: 2 3 5 7 11 13 17 19 
# Total primes found: 8 
# Largest prime: 19 
# Smallest prime: 2 
# Sum of all primes: 77

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes
def main():
    limit = int(input("Enter a limit (maximum 100): "))
    if limit > 100:
        print("Limit exceeds maximum of 100.")
        return
    primes = find_primes_up_to(limit)
    if primes:
        print("Prime numbers found:", ' '.join(map(str, primes)))
        print("Total primes found:", len(primes))
        print("Largest prime:", max(primes))
        print("Smallest prime:", min(primes))
        print("Sum of all primes:", sum(primes))
    else:
        print("No prime numbers found up to", limit)
if __name__ == "__main__":
    main()