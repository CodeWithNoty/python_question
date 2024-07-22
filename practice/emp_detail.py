class Emp:
    # count=1000
    def __init__(self,name,age,city,cmpny_name,id_card,slry):
        self.name=name
        self.age=age
        self.slry=slry
        self.cmpny_name=cmpny_name
        self.city=city
        self.id_card=id_card

    def get(self):
        print(f"enter your name :{self.name}")
        print(f"enter your age :{self.age}")
        print(f"enter your cite name :{self.city}")
        print(f"enter your companay name :{self.cmpny_name}")
        print(f"enter your id card :{self.id_card}")
        print(f"enter your salaray :{self.slry}")
        count=1000
        if self.slry >15000:
            count=count+2*5000
            print("your latest salary :",self.slry+count)
            # print(count)
        else:
            print("grow up")
e=Emp("neeraj",18,"chandigarrh","infotech",2211628,17000)
e.get()
