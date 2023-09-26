import os
import re


def process_files(function):
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk("./src/lib/pug/articles"):
        path = root.split(os.sep)
        for file in files:
            if file.endswith(".pug"):
                print(root + "/" + file)
                with open(root + "/" + file, "r") as f:
                    text = "".join(f.readlines())
                text = function(text)
                with open(root + "/" + file, "w") as f:
                    f.write(text)


# If you not sure not CHANGE!! DANGER
def function(text):
    test(text)
    return text


def test(input):
    if input:
        text = input
    else:
        text = r"""p As an example, consider the inverse cosine of #[+m i]. We shall find only one of its many values, by using the plus sign in the formula. We get: #[+m \cos^{-1} i = -i\ln\left[i+i\sqrt{1-i^2}\right\] = -i\ln\left[(1+\sqrt{2})i\right\]]. Then we use the logarithm formula to continue: #[+m -i\ln\left[(1+\sqrt{2})i\right] = -i\ln\left[(1+\sqrt{2})e^{\frac{i\pi}{2}}\right] = -i\left[\ln(1+\sqrt{2}) +\frac{\pi}{2}i \right]]. This can be simplified, and we get #[+m -i\left[\ln(1+\sqrt{2}) +\frac{\pi}{2}i \right] = \frac{\pi}{2} -i\ln(1+\sqrt{2}) \approx 1.57-0.88i]."""
    for entry in re.finditer(r"#\[\+m", text):
        was_open = False
        pos = entry.end()
        result = None
        while result == None:
            if text[pos] == "[":
                was_open = True
            elif text[pos] == "]":
                if was_open:
                    was_open = False
                else:
                    buff = text[entry.end() : pos].strip()
                    if "]" in buff:
                        buff = "String.raw`%s`" % buff
                    result = entry[0] + " " + buff + text[pos]
            pos += 1
        text.replace(text[entry.start() : pos + 1], result)
        print(result)

    # print(text)


process_files(function)
