use std::io::{self, Write};

fn main() {
    loop {
        let bill_amount = get_bill_amount();
        let tip_percent = get_tip_percent();
        let tip_amount = calculate_tip(&bill_amount, &tip_percent);
        println!("You should leave a {tip_amount} tip");
    }
}

fn get_something(prompt: String) -> f64 {
    let something: f64 = loop {
        print!("{prompt}");
        let _ = std::io::stdout().flush();
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read line");
        match input.trim().parse() {
            Ok(input) => break input,
            Err(_) => continue,
        };
    };
    something
}

fn get_bill_amount() -> f64 {
    return get_something(String::from("Please enter the bill total: "));
}

fn get_tip_percent() -> f64 {
    return get_something(String::from("Please enter the tip percent: "));
}

fn calculate_tip(bill_amount: &f64, tip_percent: &f64) -> f64 {
    // The divide by 100 serves two purposes:
    // 1. The tip_percent is `15` to represent 15%, or 0.15, so we need to divide by 100 anyway.
    // 2. When we round() the product of bill_amount and tip_percent, we get an integer, then
    //    dividing by 100 gives us a number with 100ths-place accuracy.
    (bill_amount * tip_percent).round() / 100.0
}

#[test]
fn test_calculate_tip() {
    assert_eq!(calculate_tip(&50.00, &15.00), 7.50);
}
