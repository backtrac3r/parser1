use reqwest::header;
use reqwest::Client;
use scraper::{Html, Selector};
use std::collections::HashMap;
use std::fs;

#[tokio::main]
async fn main() {
    let mut headers = header::HeaderMap::new();

    headers.insert("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36".parse().unwrap());

    let client = Client::new();
    let response = client
        .get("https://hh.ru/vacancy/101946855?hhtmFrom=vacancy_search_list")
        .headers(headers)
        .send()
        .await
        .unwrap();

    assert!(response.status().is_success());

    let fragment = Html::parse_fragment(&response.text().await.unwrap());

    let selector = Selector::parse(r#"h1[data-qa="vacancy-title"]"#).unwrap();
    println!(
        "{}",
        fragment.select(&selector).next().unwrap().inner_html()
    );
}
