# Dynamic IP to Discord

Monitor WAN IP address of your machine circumventing CGNAT and send an update to a specified Discord channel whenever it changes. This is particularly useful if you're running a machine connected to a router with dynamic IP address.

Implemented Routers:

* AX3

## Table of Contents

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [License](#license)

## Installation

This application requires Python 3 and either [Microsoft Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) or [GeckoDriver](https://github.com/mozilla/geckodriver/releases) in your system's PATH.

## Dependencies

Install the necessary Python packages with the following command:

```bash
$ pip install -r requirements.txt
```

## Usage

To use this application, you need to configure the `.env` file with your specific settings. Here's a breakdown of what each setting does:

- `ROUTER_TYPE`: This should be one of the supported routers, for example `AX3`.
- `WEBDRIVER`: This should be either `edge` or `firefox`, depending on which webdriver you want Selenium to use.
- `ROUTER_HOST`, `ROUTER_USER`, `ROUTER_PASSWORD`: These should be the IP address, username, and password for your router, respectively. Note that the username isn't always supported by your routers.
- `WEBHOOK_URL`: This should be the URL of the Discord webhook you want to send notifications to.

Once you've configured your `.env` file, you can run the program with the following command:

```bash
python main.py
```

## License

This project is licensed under the terms of the MIT license. See [LICENSE](./LICENSE).