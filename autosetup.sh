sudo cp /home/pi/smart-charging-cart/smcart.service /lib/systemd/system/smcart.service

sudo systemctl enable smcart.service

sudo systemctl start smcart.service
