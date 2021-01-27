import json
import re


def main() -> None:
    with open("developers.json") as json_file:
        sections = json.load(json_file)

    toc = "\n## Contents\n"
    text = ""

    for section in sections:
        name = section["name"]
        description = section["description"]

        text += f"## { name }\n{ description }\n\n"
        toc += f"- [{ name }](#{ name.lower().replace(' ', '-') })\n"

        developers = section.get("developers", [])
        developers = sorted(developers, key=lambda developer: developer["name"])
        for developer in developers:
            name = developer["name"]
            profile = developer["profile"]
            avatar = developer["avatar"]

            languages = [f"`{ language }`" for language in developer["languages"]]
            featured = [f"[{ featured['name'] }]( { featured['link'] })" for featured in developer["featured"]]
            
            badges = []

            ghstar = developer.get("ghstar")
            if ghstar: 
                badges.append(f"[:star:]({ ghstar })")

            ghreadme = developer.get("ghreadme")
            if ghreadme:
                badges.append(f"[:page_facing_up:]({ ghreadme })")

            text += (
                f"[<img align=\"left\" height=\"94px\" width=\"94px\" alt=\"{ name } avatar\" src=\"{ avatar }\"/>]({ profile })\n\n"
                f"[**{ name }**]({ profile}) { ' '.join(badges) }\\\n"
                f"Languages: { ', '.join(languages) }\\\n"
                f"Featured Projects: { ', '.join(featured) }\n"
                "<br/><br/>\n\n"
            )

        text += "[:arrow_up_small: Back to the top](#contents)\n\n"

    replacement = toc + "\n" + text

    with open("README.md", encoding='utf-8') as readme_file:
        readme = readme_file.read()

    updated_readme = re.sub(
        f'(?<=<!-- REPLACEMENT_START -->).*?(?=<!-- REPLACEMENT_END -->)',
        replacement,
        readme,
        flags=re.DOTALL
    )

    with open("README.md", "w", encoding='utf-8') as readme_file:
        readme_file.write(updated_readme)


if __name__ == "__main__":
    main()
