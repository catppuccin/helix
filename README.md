<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://github.com/helix-editor/helix">Helix</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
    <a href="https://github.com/catppuccin/helix/stargazers"><img src="https://img.shields.io/github/stars/catppuccin/dunst?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
    <a href="https://github.com/catppuccin/helix/issues"><img src="https://img.shields.io/github/issues/catppuccin/dunst?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
    <a href="https://github.com/catppuccin/helix/contributors"><img src="https://img.shields.io/github/contributors/catppuccin/dunst?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

![helix preview](assets/helix_preview.png)

## Usage

1. Copy the contents of the `themes/default` or `themes/no_italics` folder into `$HOME/.config/helix/themes/`.
2. Choose a palette (latte, frappe, macchiato, mocha) and add `theme = "catppuccin_(palette)"` to your config.toml
3. (Optional) modify your `$HOME/.config/helix/config.toml` to activate features (might require Helix build from master):
	```toml
	[editor]
	line-number = "relative"
	cursorline = true
	color-modes = true

	[editor.cursor-shape]
	insert = "bar"
	normal = "block"
	select = "underline"

	[editor.indent-guides]
	render = true
	```
	
## Modify themes
Modfiy the themes by editing the template (`data/template.tmpl`), the palettes (`/data/palettes`) or the configs (`/data/configs`).
To generate all the themes execute `python generate.py`.

## 💝 Thanks to

- [Spaxly](https://github.com/Spaxly)

&nbsp;

<p align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

<p align="center">
	Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
</p>

<p align="center">
	<a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
