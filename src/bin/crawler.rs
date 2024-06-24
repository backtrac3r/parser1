use spider::configuration::Configuration;
use spider::tokio;
use spider::website::Website;

#[tokio::main]
async fn main() {
    let config = Configuration::new()
        .with_user_agent(Some("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"))
        .with_depth(30)
        .with_redirect_limit(3)
        .with_respect_robots_txt(true)
        .build();

    let mut website = Website::new("https://spider-rs.github.io/spider-py/")
        .with_config(config.clone())
        .build()
        .unwrap();

    let mut rx = website.subscribe(16).unwrap();

    tokio::spawn(async move {
        while let Ok(res) = rx.recv().await {
            println!("{:?}", res.get_url());
        }
    });

    website.crawl_smart().await;
    website.unsubscribe();
}
