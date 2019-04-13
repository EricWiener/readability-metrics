# import readability
from collections import defaultdict
from metrics.metrics import Readability


def test_readability():
    readability_dic = defaultdict(lambda: Readability())
    readability_dic["Test"].analyze_text("Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this.")
    readability_dic["Test"].analyze_text(
        "If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.")
    readability_res = readability_dic["Test"].get_results()
    correct_dic = {'ARI': 12.163787878787879, 'FleschReadingEase': 58.2319, 'FleschKincaidGradeLevel': 11.2857,
                   'GunningFogIndex': 14.5465, 'SMOGIndex': 12.287087810503355, 'ColemanLiauIndex': 9.5226, 'LIX': 46.467171717171716, 'RIX': 5.375}
    assert correct_dic == readability_res
