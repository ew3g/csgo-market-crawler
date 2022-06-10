<!-- markdownlint-configure-file {
  "MD013": {
    "code_blocks": false,
    "tables": false
  },
  "MD033": false,
  "MD041": false
} -->

<div align="center">

# CSGO Market Crawler

[![GitHub license](https://img.shields.io/github/license/ew3g/csgo-market-crawler.svg)](https://github.com/ew3g/csgo-market-crawler/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/ew3g/csgo-market-crawler.svg)](https://github.com/ew3g/csgo-market-crawler/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/ew3g/csgo-market-crawler.svg)](https://github.com/ew3g/csgo-market-crawler/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/ew3g/csgo-market-crawler.svg)](https://gitHub.com/ew3g/csgo-market-crawler/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/ew3g/csgo-market-crawler.svg?style=social&label=Watch)](https://github.com/ew3g/csgo-market-crawler/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/ew3g/csgo-market-crawler.svg?style=social&label=Fork)](https://gitHub.com/ew3g/csgo-market-crawler/network/)
[![GitHub stars](https://img.shields.io/github/stars/ew3g/csgo-market-crawler.svg?style=social&label=Star)](https://gitHub.com/ew3g/csgo-market-crawler/stargazers/)

![Counter Strike Logo](https://github.com/ew3g/csgo-market-crawler/blob/main/csgo-icon.png?raw=true "Sample inline image")

This project is a web crawler that retrieves items from CSGO Steam Market and store them in a Mongo Database

Items available: Knives • Pistols • Rifles • Shotguns • Snipers • Machineguns • Smgs • Gloves

[Installation](#installation) •
[Configuration](#configuration) •
[Integrations](#third-party-integrations)
</div>

## Installation
- Get a Steam Api Key, following these [instructions](https://cran.r-project.org/web/packages/CSGo/vignettes/auth.html).
- Use package manager [pip](https://pip.pypa.io/en/stable/) to install all needed libs
```bash pip install -r requirements.txt```
- Create the file .env in the project root folder with the following content:
```
STEAM_API_KEY='PLACE YOU STEAM API KEY HERE'
LAST_PROCESSED_PAGE_KNIFE='-1'
LAST_PROCESSED_PAGE_PISTOL='-1'
LAST_PROCESSED_PAGE_RIFLE='-1'
LAST_PROCESSED_PAGE_SHOTGUN='-1'
LAST_PROCESSED_PAGE_SNIPER='-1'
LAST_PROCESSED_PAGE_MACHINEGUN='-1'
LAST_PROCESSED_PAGE_SMG='-1'
LAST_PROCESSED_PAGE_GLOVE='-1'
BATCH_SIZE=50
LAST_PROCESSED_PAGE='1'
DATABASE_PASSWORD='PLACE YOUR DATABASE PASSWORD HERE'
DATABASE_USER='PLACE YOUR DATABASE PASSWORD HERE'
DATABASE_URL='mongodb+srv://USER:PASSWORD@HOST/DATABASE?retryWrites=true&w=majority'
LOG_LEVEL='INFO'
```  

## Usage
```
python crawler.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[The MIT License (MIT)](https://mit-license.org/)

## Thanking

CSGO png image for the project icon [csgo-icon](https://www.freeiconspng.com/img/42849). Credits to Ahkâm.

Crawler png image for the project icon [crawler-icon](https://pypi.org/project/schedule/) lib. Credits to [Dan Bader](https://github.com/dbader).