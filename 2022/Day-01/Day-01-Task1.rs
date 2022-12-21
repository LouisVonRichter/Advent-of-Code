use std::fs;
use std::io;

use std::io::BufRead;

fn main() -> io::Result<()> {
    let input = fs::File::open("Day-01.txt")?;
    let reader = io::BufReader::new(input);

    let mut current = 0;
    let mut max = 0;

    let mut numbers = [1, 2, 3];

    for line in reader.lines() {
        let line = line?;
        if line.is_empty() {
            if current > max {
                max = current;
            }
            current = 0;
            continue;
        }

        match line.parse::<i32>() {
            Ok(n) => {
                current += n;
            },
            Err(e) => {
                println!("Error: {}", e);
                continue;
            }
        };
    }

    println!("Max: {}", max);

    Ok(())
}