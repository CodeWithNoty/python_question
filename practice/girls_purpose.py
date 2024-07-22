girl=["gori","chimkandi","baby","nathu"]

for girls in girl:
    try:
        response=input(f"prem purpose to {girl}.do you accept? (yes/no):")
        if response.lower()=="yes":
            print(girl,"lets have a dear")
            break
        else:
            raise Exception("its her a loss ,lets try another girl")
    except Exception as e:
        print(e)
