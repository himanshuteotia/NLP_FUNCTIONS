import re

# Sample code to remove noisy words from a text

noise_list = ["is","a","this",".","..."]

def _remove_noise(input_text):
    words = input_text.split()
    noise_free_words = [word for word in words if word not in noise_list]
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text


print(_remove_noise("This is a company."))


# Sample code to remove a regex patter

def _remove_regex(input_text,regex_pattern):
    urls = re.finditer(regex_pattern,input_text)
    for i in urls:
        input_text = re.sub(i.group().strip(),'',input_text)
    return input_text


regex_pattern = r"#[\w]*"

print(_remove_regex("remove this #hashtag from analytics", regex_pattern))
