<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://github.com/helix-editor/helix">Helix</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>
<p align="center"><a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=302d41&colorB=b7bdf8"/></a></p>


<p align="center">
    <a href="https://github.com/catppuccin/helix/stargazers"><img src="https://img.shields.io/github/stars/catppuccin/dunst?colorA=363a4f&colorB=b7bdf8&style=for-the-badge&logo=starship style=for-the-badge"></a>
    <a href="https://github.com/catppuccin/helix/issues"><img src="https://img.shields.io/github/issues/catppuccin/dunst?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
    <a href="https://github.com/catppuccin/helix/contributors"><img src="https://img.shields.io/github/contributors/catppuccin/dunst?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
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
