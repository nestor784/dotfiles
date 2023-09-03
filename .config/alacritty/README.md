# dots-alacritty
#### Temas

Descargar temas  
```sh
mkdir -p ~/.config/alacritty/themes
git clone https://github.com/alacritty/alacritty-theme ~/.config/alacritty/themes
```
Importar temas a configuración  
```yaml
import:
 - ~/.config/alacritty/themes/themes/{theme}.yaml
```
#### Oh My Bash
Descargar Oh My Bash  

```sh
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"
```

Descargar lsDeluxe
```sh
pacman -Syu
pacman -S lsd
```
Descargar los archivos de configuración de alacritty, .bashrc y .ls_config
