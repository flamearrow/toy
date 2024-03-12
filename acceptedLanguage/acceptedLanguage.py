# http reaquest could have headers like en-US, fr-CA, fr-FR,
# write a function to take server accepted languages and user requested languages, return the language header server
# supports
# part 1
# Examples:
# parse_accept_language(
#     "en-US, fr-CA, fr-FR", # client's request
#     ["fr-FR", "en-US"] # server supported
# )
# returns ["en-US", "fr-FR"]
# part 2
# often a language tag is not region specifc, e,g "en" means any variatn of englisth. Extend the function to do that
# Examples:
# parse_accept_language(
#     "en", # client's request
#     ["fr-FR", "en-US", "en-GB"] # server supported
# )
# returns ["en-US", "en-GB"]

# part 3
# support wildcard where * means all langs
# Part 4
# Support a q-factor, indicating the preference of the language returned, the higher the more preferred
# Examples:
# parse_accept_language(
#     "fr-FR;q=1, fr;q=0.5, fr-CA;q=0", # client's request
#     ["fr-FR", "fr-CA", "fr-BG"] # server supported
# )
# returns ["fr-FR", "fr-BG", 'fr-CA"]
import unittest
from unittest import TestCase


def parse_accept_language(header, supported_list):
    supported_set = set()
    for supported_lang in supported_list:
        supported_set.add(supported_lang)

    requested_headers = []

    for langQPair in list(map(lambda s: s.strip(), header.split(','))):
        if ";" in langQPair:
            lqArry = langQPair.split(";")
            lang = lqArry[0]
            q = float(lqArry[1].split("=")[1])
            requested_headers.append((lang, q))
        else:
            requested_headers.append((langQPair, 1.0))  # if there's no q, append 1.0

    requested_headers.sort(key=lambda pair: pair[1], reverse=True)  # sort by q

    # iterate through the entire list from highest,

    ret = []
    for i in range(len(requested_headers)):
        # requested_header is a pair of (requested_lang, p)
        requested_header = requested_headers[i]
        requested_lang = requested_header[0]
        #   if there is a exact match, append to result
        if requested_lang in supported_set:
            ret.append(requested_lang)
        #   if there's a langId match, the all the matches entires, to remove any entry appearing after this
        elif requested_lang == "*":
            # append all supported headers that are not added to ret yet
            ret.extend(list(filter(lambda x: x not in ret, supported_set)))
            break
        elif "-" not in requested_lang:  # en/fr
            matched_headers = list(filter(lambda x: requested_lang in x, supported_set))
            # anything that's added before, has already been added
            # anything that's added after, will be processed in next round
            for j in range(i + 1, len(requested_headers)):
                header_appeared_later = requested_headers[j][0]
                matched_headers.remove(header_appeared_later)

            ret.extend(filter(lambda x: x not in ret, matched_headers))

    return ret


def headers_in_language(header, supported_headers):
    if "-" in header:  # not wildcard
        return []
    else:  # if header is "en", find all langId with "en" in it
        return list(filter(lambda x: header in x, supported_headers))


class HeaderTestCase(TestCase):
    def test_blah(self):
        self.assertEqual(['fr-FR', 'fr-BG', 'fr-CA'],
                          parse_accept_language("fr-FR;q=1, fr;q=0.5, fr-CA;q=0", ["fr-FR", "fr-CA", "fr-BG"]))

    def test_empty(self):
        self.assertEqual([],
                          parse_accept_language("fr-FR", ["en-Us", "en-GB"]))


if __name__ == '__main__':
    unittest.main()
