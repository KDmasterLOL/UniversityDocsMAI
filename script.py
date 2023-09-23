import os
import re

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("./src/lib/pug/articles"):
    path = root.split(os.sep)

    # print((len(path) - 1) * "---", os.path.basename(root))
    for file in files:
        if file.endswith(".pug"):
            print(root + "/" + file)
            with open(root + "/" + file, "r") as f:
                text = "".join(f.readlines())
            for math_exp in re.finditer(
                r"\${1,2}\s*(([^$])*)\s*\${1,2}", text, flags=re.M
            ):
                if "\n" in math_exp[0]:
                    new_text = re.sub(r"\s{2,}", " ", math_exp[1].replace("\n", " "))
                else:
                    new_text = math_exp[1]
                text = text.replace(math_exp[0], "#[+m %s]" % new_text)
            with open(root + "/" + file, "w") as f:
                f.write(text)
