# AI-deck examples repository

Check out the [documentation](https://www.bitcraze.io/documentation/repository/aideck-gap8-examples/master/)
for starting guides. 

## Installing the WiFi video streaming example
First, install docker as instructed here: https://docs.docker.com/engine/install/ubuntu/

Then follow the instructions for setting up the AI deck and its development environment, except for 'Flash WiFi example': https://www.bitcraze.io/documentation/tutorials/getting-started-with-aideck/. A JTAG programmer is needed for setting up the AI deck for the first time.

```
sudo apt-get git
git clone https://github.com/BNoordam/aideck-gap8-examples.git
cd aideck-gap8-examples
sudo docker run --rm -v ${PWD}:/module aideck-with-autotiler tools/build/make-example examples/other/wifi-img-streamer image
cfloader flash examples/other/wifi-img-streamer/BUILD/GAP8_V2/GCC_RISCV_FREERTOS/target.board.devices.flash.img deck-bcAI:gap8-fw -w radio://0/1/2M
pip install opencv-python==4.5.5.64
```

The video streamer can be tested by connecting to the WiFi access point of the AI deck and running the following commands:

```
cd aideck-gap8-examples/examples/other/wifi-img-streamer
python opencv-viewer.py
```

Images are saved in the same folder as opencv-viewer.py in /stream_out/raw/

One error that appears when running the WiFi video streamer could not be solved in this research: qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in "/home/Bjorn/.local/lib/python3.11/site-packages/cv2/qt/plugins". Bitcraze states that this should not make a difference in framerate
