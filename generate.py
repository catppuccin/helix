from pathlib import Path
import json
from data.colors import color_is_bright, blend_colors

DIRNAME = Path(__file__).parent
PALETTES_DIR = DIRNAME / "data" / "palettes"
CONFIGS_DIR = DIRNAME / "data" / "configs"
TARGET_DIR = Path("themes/")


def load_styles(config_name):
    with (CONFIGS_DIR / "default.json").open("r") as f:
        default_config = json.load(f)

    with (CONFIGS_DIR / (config_name + ".json")).open("r") as f:
        json_config = json.load(f)

    merged_styles = default_config["styles"] | json_config["styles"]

    return {
        k: (
            ", modifiers = [{}]".format(", ".join(f'"{mod}"' for mod in v)) if v else ""
        )
        for (k, v) in merged_styles.items()
    }


def generate_derived_colors(palette):
    theme_is_light = color_is_bright(palette["base"])
    derived_colors = {}

    derived_colors["secondary_cursor"] = blend_colors(
        palette["base"], palette["rosewater"], 0.7
    )

    derived_colors["secondary_cursor_normal"] = blend_colors(
        palette["base"], palette["lavender"], 0.7
    )

    derived_colors["secondary_cursor_insert"] = blend_colors(
        palette["base"], palette["green"], 0.7
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

    for config_file in CONFIGS_DIR.glob("*.json"):
        config_name = config_file.stem

        styles = load_styles(config_name)

        (TARGET_DIR / config_name).mkdir(parents=True, exist_ok=True)

        for palette_file in PALETTES_DIR.glob("*.json"):
            palette_name = palette_file.stem

            with palette_file.open("r") as f:
                palette = json.load(f)

            derived_colors = generate_derived_colors(palette)

            with (TARGET_DIR / config_name / (palette_name + ".toml")).open("w") as f:
                f.write(
                    template.format(
                        **{
                            "palette": palette,
                            "styles": styles,
                            "derived_colors": derived_colors,
                        }
                    )
                )


if __name__ == "__main__":
    generate_themes()
