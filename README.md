## Parser

## Install
- **update** update: `sudo apt update`
- **python** install: `sudo apt install python3`
- **pip** install: `sudo apt install python3-pip`

## App
- `cd  smart-cart-charging`
- `pip3 install flask`
- `pip3 install waitress`
- `sudo chmod 777 ./autosetup.sh`
- `./autosetup.sh`
- `sudo systemctl status smcart.service` To check status
- `sudo systemctl stop smcart.service` To stop
- `sudo systemctl start smcart.service` To start
- `sudo systemctl restart smcart.service` To restart

## Note

flask version : 1.0.2
waitress version : 1.4.4