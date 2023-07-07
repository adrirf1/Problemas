def relation_to_luke(name):
    dic = {
        "Darth Vader": "father.",
        "Leia": "sister.",
        "Han": "brother in law.",
        "R2D2": "droid."
    }
    if name == "Darth Vader":
        return "Luke, I am your " + dic["Darth Vader"]
    elif name == "Leia":
        return "Luke, I am your " + dic["Leia"]
    elif name == "Han":
        return "Luke, I am your " + dic["Han"]
    elif name == "R2D2":
        return "Luke, I am your " +  dic["R2D2"]