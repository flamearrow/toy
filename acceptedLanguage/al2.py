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

class Parser:
    def __init__(self):
        pass

    # parse_accept_language(
    #     "en-US, fr-CA, fr-FR", # client's request
    #     ["fr-FR", "en-US"] # server supported
    # )
    # request can be "en, fr-CA" etc.
    # returns ["en-US", "fr-FR"]

    # Support a q-factor, indicating the preference of the language returned, the higher the more preferred
    # Examples:
    # parse_accept_language(
    #     "fr-FR;q=1, fr;q=0.5, fr-CA;q=0", # client's request
    #     ["fr-FR", "fr-CA", "fr-BG"] # server supported
    # )
    # returns ["fr-FR", "fr-BG", 'fr-CA"]
    def parse_accept_language(self, request, supported):
        requestList = request.split(", ")
        # [lang, q]
        mappedRequestList = []

        for request in requestList:
            # if has q, add as [req, q]
            if ";" in request:
                reqList = request.split(";")
                qList = reqList[1].split("=")
                mappedRequestList.append([reqList[0], float(qList[1])])
            # otherwise request is lang itself, add as [lang, 0] loest priority
            else:
                mappedRequestList.append([request, 0])
        sortedRequest = sorted(mappedRequestList, key=lambda x: -x[1])
        ret = []
        for lang, _ in sortedRequest:
            results = self.parse_internal(lang, supported)
            for result in results:
                if result not in ret:
                    ret.append(result)
        return ret

    def parse_internal(self, requestedLang, supported):
        if requestedLang == "*":
            return supported
        return [lang for lang in supported if (lang == requestedLang or lang.startswith(requestedLang))]


if __name__ == "__main__":
    p = Parser()
    # print(p.parse_accept_language("en-US, fr-CA, fr-FR", ["fr-FR", "en-US"]))

    # print(p.parse_accept_language("en, fr-CA, fr-FR", ["fr-FR", "en-US", "en-GB"]))
    # print(p.parse_accept_language("en, fr-CA, fr-FR, *", ["fr-FR", "en-US", "en-GB", "es-mx"]))

    print(p.parse_accept_language(
        "fr-FR;q=0, fr;q=0.5, fr-CA;q=4, en-US;q=5",  # client's request
        ["fr-FR", "fr-CA", "fr-BG", "en-US"]  # server supported
    ))