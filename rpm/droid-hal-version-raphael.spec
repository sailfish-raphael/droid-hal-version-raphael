%define rpm_device raphael
# rpm_vendor is used in the rpm space
%define rpm_vendor xiaomi
# Manufacturer and device name to be shown in UI
%define vendor_pretty Xiaomi
%define device_pretty Mi 9T Pro
# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator_native 1
%define have_led 1
%define makefstab_skip_entries / /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl
%include droid-hal-version/droid-hal-version.inc
