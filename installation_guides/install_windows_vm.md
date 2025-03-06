# Install Windows 10 VM and MS Office (with a ETH license)

## Use existing VM (qemu + virt-manager)

### Download the VM disk image

Here is the [Google drive
link](https://drive.google.com/file/d/1-SWQf73rt9lKHe6oxyINBS0scdc5Tz57/view?usp=sharing)
(this link is accessible only with an ETH Google account). The VM has already
the office suite installed.

### Configure QEMU and Virt-manager

Install QEMU and Virt-manager

```sh
sudo apt-get install -y qemu virt-manager
```

Enable `libvirtd`

```sh
sudo systemctl enable --now libvirtd
```

Check if libvirtd daemon is enabled by running:

```sh
systemctl status libvirtd
```

Now you need to make your user part of the libvirtd group. You can do that by running:

```sh
sudo usermod -G libvirtd -a  your_user
```

### Add the new virtual machine:

Go File -> Create a new virtual machine -> Import existing disk image, click `forward`.

Providing existing storge path, then click `Browse Local`, select the `win10-box.qcow2` disk image.

Then allocate the resources for the VM, it is recommended to give at least 4 cores and 8092 MB of memory.


## Creating Your Own VM:

### Order a license in ETH IT shop

Service Catalog -> Software and Business Applications -> Software & Licenses -> Order Software Product

### Mount the ETH Network Drive for the Windows 10 ISO

Open your file manager, and choose "Other Locations"

Use the location: 
`smb://software.ethz.ch/<your_account>$`

You will be prompted for your credential, use the following

user: YOUR USERNAME
domain: d
password: YOUR PASSWORD

(domain has only one letter "d")

And the ISO will be there in `<your_account>$ on software.ethz.ch/<the_version_you_ordered>`

### Install the ISO

This part should be easy

### Activate the product key

Follow the instructions on the IT shop

### Fix the scaling

Install "Spice Guest Tools"

`https://www.spice-space.org/download.html` Under "Windows Binaries", first clickable link.

After installation the scaling should be automatically fixed.

### Mount the drive inside the Windows VM for the MS Office installer

Open files, rightclick "this PC", click add network location, use `\\software.ethz.ch\<your_account>$`.

You will be prompted with username and password. The username should be prefixed with `d\`, and the password is the same as your email, for example:

username: d\\<your_account>
password: YOUR PASSWORD

Go to `Microsoft_Office_2019_Win_EN`, and double click the installer exe (64-bit).

### Activate the product key

Follow the instructions on the IT shop
