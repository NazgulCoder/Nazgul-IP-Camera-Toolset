# Nazgul IP Camera Toolset
Nazgul IP Camera Toolset borns as an All-In-One collection of tools and scripts to be used universally for IP Cameras that support the standard protocols such as RTSP and ONVIF.

# FTP-Backup
Many IP Cameras (e.g. Reolink, Ctronics) have the possibility to save Pictures and Videos when Movement is detected to FTP Servers.

This is a very easy way to securely backup your footages in case your camera gets stolen or broken.

The only issue I encountered it was the fact I had to manually delete the old footages from the FTP server since I was using a free webhosting service.

So I decided to create this little PHP Script and use a cronjob (you can use this free service https://console.cron-job.org/) to run the script every night.

The PHP Script is designed to work with Folders, it will erase all the subfolders inside that are older than a specified day threshold.

![image](https://github.com/NazgulCoder/Nazgul-IP-Camera-Toolset/assets/85739956/2055022c-1f6d-4250-9094-73350890105c)

![image](https://github.com/NazgulCoder/Nazgul-IP-Camera-Toolset/assets/85739956/742c106f-f540-4f6c-8a8d-c596e6107258)

This is what the folders structure looks like, just edit the PHP Script according to your needs.

![image](https://github.com/NazgulCoder/Nazgul-IP-Camera-Toolset/assets/85739956/ce7db8c2-a5d0-4c3d-a9ec-b782a395d2ce)

# IPCamera-Scanner
This is a simple IPCamera Scanner that can be customized and used to detect IPCameras in your network (just change the PORT in the python script, default is 554 for RTSP, but you can definitely use it for ONVIF at ports 80, 8080, 443).

Make sure to change in the `subnet.txt` the IP Address and the subnet mask according to your subnet. If you need help with subnetting refer to this online service https://www.calculator.net/ip-subnet-calculator.html

![image](https://github.com/NazgulCoder/Nazgul-IP-Camera-Toolset/assets/85739956/2a6959f1-1b75-429a-8c7d-b147cccfe752)

# RTSP Streams
This project was made since all the RTSP Stream tools we find online don't really work, or require too much work/settings (e.g. ffmpeg, mpv, VLC), or are not open source.

With this toolset written in Python (so you can run them almost anywhere) all you have to do is just replace `rtsp_urls.txt` file the RTSP URLs.

In the OLD Folder you can find some previous sketches and tests, but they are not meant to be used since are highly unstable.

Motiondetect project works quite nicely, it uses OpenCV and can be used constantly, it doesn't drain computer resources like other tools

![image](https://github.com/NazgulCoder/Nazgul-IP-Camera-Toolset/assets/85739956/9ed80309-c6d3-48fd-a914-eda1395c29a3)

![image](https://github.com/NazgulCoder/Nazgul-IP-Camera-Toolset/assets/85739956/f7c3dd7f-dc49-424b-8a9d-ec4dcd4aa25b)

To use *RTSP Streams* you can either run the version with the motiondetect (which apparently looks a bit more stable since few tweaks has been made and an autorefresh timer of 30 seconds has been added). However, the viewertxtadaptive2 is stable too, and has error recovery function that if the RTSP stream crashes, after few seconds it recovers automatically.

I highly recommend you to launch it via CMD, so you can see eventually all the error logs.

The `settings.txt` file must be configured only if you are using the motiondetect version.

The first value can be `0` or `1` which means `Off` or `On` for the motion detect feature.

The second value is the sensitivity of the OpenCV motion detect feature, I recommend to leave it `500000`. The lower this value is, the higher it is the sensitivity.

# phpIPCameraViewer
This simple project doesn't do any magic trick at all, and can be used only with the cameras that support the jpg preview via HTTP (I recommend you to check on iSpy whether your IPCamera supports that).

For this project you need an HTTP Server such as Apache or Nginx, I recommend https://www.uwamp.com/en/ since is very robust, light and portable.

Copy all the content into the `www` folder in uWamp and then run the webserver. Make sure to change the HTTP urls in `image_urls.txt`.

It then uses Javascript to refresh the image every 1 second, and a proxy.php API to bypass the CORS policy and Google security measure that blocks credentials inside iframes and img source.

I personally don't recommend this method because you are going to flood too much your IPCamera and it might reboot many times


## LICENSE



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

MIT License

Copyright (c) [2023] [NazgulCoder]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
