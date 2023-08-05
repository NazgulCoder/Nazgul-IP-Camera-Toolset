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

# RTSP Streams
This project was made since all the RTSP Stream tools we find online don't really work, or require too much work/settings (e.g. ffmpeg, mpv, VLC), or are not open source.

With this toolset written in Python (so you can run them almost anywhere) all you have to do is just replace in the .txt file the RTSP URLs.

In the OLD Folder you can find some previous sketches and tests, but they are not meant to be used since are highly unstable.

Motiondetect project works quite nicely, it uses OpenCV and can be used constantly, it doesn't drain computer resources like other tools

![image](https://github.com/NazgulCoder/Nazgul-IP-Camera-Toolset/assets/85739956/9ed80309-c6d3-48fd-a914-eda1395c29a3)

![image](https://github.com/NazgulCoder/Nazgul-IP-Camera-Toolset/assets/85739956/f7c3dd7f-dc49-424b-8a9d-ec4dcd4aa25b)
