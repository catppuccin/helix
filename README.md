<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/dev/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/dev/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for Helix
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/dev/assets/misc/transparent.png" height="30" width="0px"/>
</h3>
<p align="center"><a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=302d41&colorB=c9cbff"/></a></p>


<p align="center">
    <a href="https://github.com/catppuccin/helix/stargazers"><img src="https://img.shields.io/github/stars/catppuccin/dunst?colorA=1e1e28&colorB=c9cbff&style=for-the-badge&logo=starship style=for-the-badge"></a>
    <a href="https://github.com/catppuccin/helix/issues"><img src="https://img.shields.io/github/issues/catppuccin/dunst?colorA=1e1e28&colorB=f7be95&style=for-the-badge"></a>
    <a href="https://github.com/catppuccin/helix/contributors"><img src="https://img.shields.io/github/contributors/catppuccin/dunst?colorA=1e1e28&colorB=b1e1a6&style=for-the-badge"></a>
</p>

![helix preview](assets/helix_preview.png)

## Usage

1. Copy the contents of the `italics` or `no_italics` folder into `$HOME/.config/helix/themes/catppuccin.toml`.
2. Choose a palette (latte, frappe, macchiato, mocha) and add `theme = "catppuccin_(palette)"` to your config.toml
3. Add cursor mode indicator to your config.toml:
	```toml
	[editor.cursor-shape]
	insert = "bar"
	normal = "block"
	select = "underline"
	```
