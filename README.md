# dots

Personal config for linux and more.  
- [ ] Desktop Environment Window Manager   
- [ ] Development Apps
- [ ] Office Apps
- [ ] System Apps
- [ ] Graphics Apps
- [x] Internet Apps
- [ ] Audio Apps
- [ ] Video Apps
- [x] GitHub ssh authentication
- [x] Fonts
- [x] Basic Setup

## Basic Setup

1. Actualizar paquete
```bash
pacman -Syu
```
2. Instalar paquetes del sistema
```bash
pacman -S base base-devel systemd-sysvcompat neovim man-dv man-pages texinfo elinks sudo git go libmtp gvfs-mtp
```
3. Instalar YAY
```bash
git clone https://aur.archlinux.org/yay.git
chown nestor /home/nestor/yay/
makepkg -si
```
4. Firmwares
```bash
yay -S amd-ucode ast-firmware linux-firmware-qlogic upd72020x-fw wd719x-firmware aic94xx-firmware 
```
5. Paquetes básicos
```bash
pacman -S bash-completion pkgstats bc mlocate neofetch htop zip unzip p7zip jq wget
```
6. Sonido
```bash
pacman -S alsa-utils alsa-plugins pulseaudio pulseaudio-alsa rhythmbox gst-plugins-base gst-plugins-base-libs gst-plugins-good gst-plugins-ugly gst-plugins-bad gst-libav alsa-oss
alsactl init
alsactl store
```
7. Fuentes
```bash
sudo pacman -S --asdeps --needed cairo fontconfig freetype2
yay -S ttf-fira-code ttf-hack nerd-fonts-complete
```
8. Video (Solo AMD)
```bash
pacman -S vlc libdvdnav cdrdao cdrtools ffmpeg ffmpegthumbnailer ffmpegthumbs xf86-video-amdgpu vulkan-radeon mesa-libgl mesa-vdpau libvdpau-va-gl xf86-video-vesa
``` 
9. Bluetooth
```bash
pacman -S bluez bluez-utils
systemctl enable bluetooth.service
```
10. Aplicaciones
```bash
pacman -S thunar zathura leafpad nitrogen viewnior tumbler alacritty
yay -S epdfview
```
11. Xorg packages
```bash
pacman -S xorg-server weston xorg-server-xwayland libx11 libxft libxinerama libxrandr libxss xorg-apps xorg-xinit xorg-xmessage pkgconf xorg-tmw xorg-setxkbmap
```
## Internet apps
```sh
yay -S networkmanager-dmenu-git
pacman -S qutebrowser
```
Configurar el tema de qutebrowser
```sh
git clone https://github.com/catppuccin/qutebrowser.git ~/.config/qutebrowser/catppuccin
```


## Development Apps

* Configuración de alacritty :link: [dots/alacritty](https://github.com/nestor784/dots-alacritty.git)
* Configuración de neovim :link: [dots/nvim](https://github.com/nestor784/dots-neovim.git)

## GitHub SSH Auth

Run
```sh
ssh-keygen -t ed25519 -C "nestorjari784@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```
Copiar la salida a ssh key generation en GitHub

## Fonts

Descargar las siguientes fuentes desde [fonts](https://www.nerdfonts.com/font-downloads)  
* Hack
* Iosevka
* JetBrains Mono
```sh
mkdir ~/.fonts
unzip '*.zip' -d ~/.fonts
fc-cache -f -v
```
Descargar figlet fonts desde :link: [figlet-fonts](https://github.com/xero/figlet-fonts/tree/master) y copiar
a */usr/share/figlet/fonts*
 ```sh
pacman -S figlet lolcat
yay -S toilet
showfigfonts
```
```sh
pacman -S noto-fonts-emoji
```

## Window Manager

##### Instalar Qtile
```bash
pacman -S qtile
cp -fv /etc/X11/xinit/xinitrc /home/nestor/.xinitrc
echo -e "exec awesome" >> /home/nestor/.xinitrc 
chown -R nestor:users /home/nestor/.xinitrc 
chown -R nestor:users /home/nestor/.config/
```
##### Configurar teclado de Xorg
```bash
nvim /etc/X11/xorg.conf.d/00-keyboard.conf
```
Escribir y guardar  
```text
Section "InputClass"
	Identifier "system-keyboard"
	MatchIsKeyboard "on"
	Option "XkbLayout" "latam"
	Option "XkbVariant" ",winkeys"
EndSection
```
##### Configurar .xinitrc y alacritty como terminal

Eliminar  
```
twm &
xclock -geometry 50x50-1+1 &
xterm -geometry 80x50+494+51 &
xterm -geometry 80x20+494-0 &
exec xterm -geometry 80x66+0+0 -name login
```
Añadir al final  
```sh
exec qtile start
```
Para añadir alacritty se debe cambiar la siguiente linea  
```python
#~/.config/qtile/config.py 
terminal = "alacritty" #(Antes) terminal = guess_terminal()
```
##### Configurar Xorg para AMD

Crear el archivo  
```bash
nvim /etc/X11/xorg.conf.d/20-amdgpu.conf
```
Pegar  
```
Section "OutputClass"
	Identifier "AMD"
	MatchDriver "amdgpu"
	Driver "amdgpu"
EndSection
```
##### Compositor picom


Añadir a .config/qtile/config.py
```sh
os.system("exec picom --config $HOME/.config/qtile/picom.conf &"
```
##### Lanzador de aplicaciones

Install rofi

```sh
pacman -S rofi
rofi-theme-selector
```
##### sddm

Install and create config file

```sh
pacman -S sddm
yay -S sddm-sugar-dark
systemctl enable sddm
sddm --example-config > /etc/sddm.conf.d/sddm.conf
```

Config `/etc/sddm.conf.d/sddm.conf`

```conf
[Theme]
# Current theme name
Current=sugar-dark
```
Config `/usr/share/sddm/themes/sugar-dark/theme.conf`
```conf
[General]

Background="*path-background-image.png"
...
MainColor="deepskyblue"
```


## MATH books
##### Algebra
* David S. Dummit, Richard M. Foote - Abstract Algebra, 3rd Edition Wiley 2003
* Serge Lang - Algebra, Springer 2002
* Serge Lang - Introduction to Linear Algebra, Springer 1985
* Serge Lang - Linear Algebra, Springer 2004
* William C. Brown - A Second Course in Linear Algebra, Wiley 1988
##### Real Analysis
* Apostol, T. M. - Análisis matemático, Reverté 2006
* Michael Spivak - Calculo En Variedades Spanish, Reverté 2008
* Elon Lages Lima - Análise no Espaço Rn, IMPA 2004
* Elon Lages Lima - Curso de Análise. 2, IMPA 1999
* Elon Lages Lima - Espaços Métrico, IMPA 2014
##### Complex Analysis
* Serge Lang - Complex Analysis, Springer 2003
* Serge Lang - Real and Functional Analysis, Springer 1993
* Walter Rudin - Real and Complex Analysis, McGraw-Hill 1986
##### Set Theory
* Jech Hrbacek - Introduction to Set Theory, Dekker 1999

## Programming Books
* Ben Shaw, Chris Guest - Web Development with Django
* G. Lim, D. Correa - Django 4 for the impatient
