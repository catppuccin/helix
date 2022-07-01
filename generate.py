from pathlib import Path
import json
from data.colors import color_is_bright, blend_colors

DIRNAME = Path(__file__).parent
PALETTES_DIR = DIRNAME / "data" / "palettes"
STYLES_DIR = DIRNAME / "data" / "styles"
TARGET_DIR = Path("themes/")


def load_style(style_name):
    with (STYLES_DIR / "default.json").open("r") as f:
        default_style = json.load(f)

    with (STYLES_DIR / (style_name + ".json")).open("r") as f:
        json_style = json.load(f)

    merged_style = default_style | json_style

    return {
        k: (
            ", modifiers = [{}]".format(", ".join(f'"{mod}"' for mod in v)) if v else ""
        )
        for (k, v) in merged_style.items()
    }


def generate_derived_colors(palette):
    theme_is_light = color_is_bright(palette["base"])
    derived_colors = {}

    derived_colors["secondary_cursor"] = blend_colors(
        palette["base"], palette["rosewater"], 0.7
    )

    if theme_is_light:
        derived_colors["cursorline"] = blend_colors(
            palette["base"], palette["mantle"], 0.7
        )
    else:
        derived_colors["cursorline"] = blend_colors(
            palette["base"], palette["surface0"], 0.64
        )

    return derived_colors


def generate_themes():
    with (DIRNAME / "data" / "template.tmpl").open("r") as f:
        template = f.read()

    for style_file in STYLES_DIR.glob("*.json"):
        style_name = style_file.stem

        style = load_style(style_name)

        (TARGET_DIR / style_name).mkdir(parents=True, exist_ok=True)

        for palette_file in PALETTES_DIR.glob("*.json"):
            palette_name = palette_file.stem

            with palette_file.open("r") as f:
                palette = json.load(f)

            derived_colors = generate_derived_colors(palette)

            with (TARGET_DIR / style_name / (palette_name + ".toml")).open("w") as f:
                f.write(
                    template.format(
                        **{
                            "palette": palette,
                            "style": style,
                            "derived_colors": derived_colors,
                        }
                    )
                )


if __name__ == "__main__":
    generate_themes()
