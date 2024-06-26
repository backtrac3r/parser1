use clap::{arg, command};
use spider::configuration::Configuration;
use spider::tokio;
use spider::website::Website;

#[tokio::main]
async fn main() {
    let matches = command!()
        .arg(arg!(-u --url <URL> "Sets a start url").required(true))
        .get_matches();

    let url = matches.get_one::<String>("url").unwrap();

    let config = Configuration::new()
        // .with_user_agent(Some("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"))
        // .with_chrome_intercept(cfg!(feature = "chrome_intercept"), true)
        // .with_depth(0)
        // .with_redirect_limit(10000)
        // .with_caching(true)
        // .with_respect_robots_txt(true)
        .build();

    let mut website = Website::new(url)
        .with_config(config.clone())
        .build()
        .unwrap();

    let mut rx = website.subscribe(128).unwrap();

    tokio::spawn(async move {
        while let Ok(res) = rx.recv().await {
            println!("{:?}", res.get_url());
        }
    });

    website.crawl_smart().await;
    website.unsubscribe();
}
