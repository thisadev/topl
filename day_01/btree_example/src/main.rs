use std::collections::BTreeMap;

fn main() {
    let mut scores = BTreeMap::new();
    scores.insert("Thisara", 85);
    scores.insert("Gihan", 92);
    scores.insert("Kamal", 78);

    // Keys are automatically sorted
    for (name, score) in &scores {
        println!("{}: {}", name, score);
    }

    // Efficient range query
    let range = scores.range("A".."P");
    for (name, score) in range {
        println!("In range: {}: {}", name, score);
    }
}
