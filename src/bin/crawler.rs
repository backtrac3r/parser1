use clap::{arg, command};
use scraper::{Html, Selector};
use spider::configuration::Configuration;
use spider::tokio;
use spider::website::Website;

#[tokio::main]
async fn main() {
    let matches = command!()
        .arg(arg!(-u --url <URL> "Sets a start url").required(true))
        // .arg(arg!(-w --word <WORD> "Sets word").required(true))
        .get_matches();

    let url = matches.get_one::<String>("url").unwrap();
    // let word = matches.get_one::<String>("word").unwrap().clone();

    let config = Configuration::new()
        .with_redirect_limit(111)
        .with_caching(true)
        // .with_respect_robots_txt(true)
        // .with_user_agent(Some("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"))
        // .with_chrome_intercept(cfg!(feature = "chrome_intercept"), true)
        .build();

    let mut website = Website::new(url)
        .with_config(config.clone())
        .build()
        .unwrap();

    let mut rx = website.subscribe(128).unwrap();

    tokio::spawn(async move {
        while let Ok(res) = rx.recv().await {
            let html = res.get_html();
            let url = res.get_url();

            let fragment = Html::parse_fragment(&html);

            let selector = Selector::parse(r#"h1[data-qa="vacancy-title"]"#).unwrap();

            for e in fragment.select(&selector) {
                let vacancy_title = e.inner_html();

                println!("{vacancy_title}");
                println!("url: {url}");
                println!();
            }
        }
    });

    website.crawl_smart().await;
    website.unsubscribe();
}

fn word_count(s: &str, word: &str) -> usize {
    s.to_lowercase().matches(word).count()
}

fn word_is_present(s: &str, word: &str) -> bool {
    word_count(s, word) > 0
}
