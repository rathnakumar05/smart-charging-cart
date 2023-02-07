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

<p align="center"><img src="https://user-images.githubusercontent.com/60918147/217249828-035bad85-a2ab-4a32-b713-4cddd4db5211.png" alt="smcart" width="500" align="center"/></p>