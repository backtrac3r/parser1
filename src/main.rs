use reqwest::header;
use reqwest::Client;
use scraper::{Html, Selector};
use std::collections::HashMap;

#[tokio::main]
async fn main() {
    let mut headers = header::HeaderMap::new();

    headers.insert("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36".parse().unwrap());

    let params = {
        let mut params = HashMap::new();
        params.insert("v", "KmzvSo90Zj4".to_string());
        params
    };

    let client = Client::new();
    let response = client
        .get("https://www.youtube.com/watch")
        .headers(headers)
        .query(&params)
        .send()
        .await
        .unwrap();

    assert!(response.status().is_success());

    // println!("{}", response.text().await.unwrap());

    let html = Html::parse_fragment(&response.text().await.unwrap());

    let selector = Selector::parse("title").unwrap();

    let h1 = html.select(&selector).next().unwrap();

    println!("{}", h1.html());
}
