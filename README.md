# USB SuperDrive Automount

This is a simple udev rule for Linux computer to automount an [Apple USB SuperDrive](https://www.apple.com/hk/shop/product/MD564ZM/A/apple-usb-superdrive) when plugged-in.


## Why?

Although Linux can detect a SuperDrive being plugged in, the hardware won't do anything until receiving a specific set of [Command Descriptor Block](https://en.wikipedia.org/wiki/SCSI_CDB) (CDB) through USB.

If not, you cannot put disc in or take disc out even when the drive was connected correctly.

To use SuperDrive on Linux you can use Linux's [SCSI Utilities](https://sg.danny.cz/sg/sg3_utils.html) (sg3_utils) to manually send the CDBs like this:

```
/usr/bin/sg_raw /dev/sr0 EA 00 00 00 00 00 01
```

But to do this manually everytime is simply a stupid task not to automate.


## What does it do?

When installed properly into `/etc/udev/rules.d`, the udev rule file (90-mac-superdrive.rules) will be triggered everytime the drive is plugged. The previously mentioned series of CDBs will be sent to the SuperDrive to make it useable.

The udev rule will even detect the correct device number if multiples are plugged.

Reference:
* [Beginners Guide to Udev in Linux](https://www.thegeekdiary.com/beginners-guide-to-udev-in-linux/), the Geek Dairy
* [Dynamic Kernel Device Management with udev](https://documentation.suse.com/sles/12-SP4/html/SLES-all/cha-udev.html), SUSE Documentation
* [Use Apple’s USB SuperDrive with Linux](https://cmos.blog/use-apples-usb-superdrive-with-linux/comment-page-1/), techtalk – Christian Moser


## Prerequsities

* Ubuntu / Debian: [sg3-utils](https://tracker.debian.org/pkg/sg3-utils)
* Fedora / RHEL / Rocky Linux: [sg3_utils](https://src.fedoraproject.org/rpms/sg3_utils)


## License

This is licensed under the MIT-License. Please read the details in [LICENSE](LICENSE) file in this repository.