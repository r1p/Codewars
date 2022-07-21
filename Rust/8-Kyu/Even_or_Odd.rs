/*
Description:
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

Categories:
#Mathematics #Fundamentals
Solve date:

26 Jun 2022
*/

fn even_or_odd(i: i32) -> &'static str {
    if i % 2 == 0 {
        return "Even";
    } else {
        return  "Odd";
    }
}
