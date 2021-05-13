#![allow(unused_imports)]

#[tokio::main]
async fn main() {
    tokio::spawn(async {
        println!("{:?}", tracing_exponential::gen::f0().await.unwrap());
    });
}
